# --- RAG utility functions for rag_router.py ---
import json
from fastapi import HTTPException
from lightrag.llm.ollama import ollama_model_complete, ollama_embed
from lightrag import LightRAG, QueryParam
from lightrag.utils import EmbeddingFunc
from lightrag.kg.shared_storage import initialize_pipeline_status

from clickup_utils import fetch_clickup_task, update_clickup_task
from schemas import RagRequest, TextRequest
from settings import LocalSettings
from utils import flatten_dict_to_string, upload_file_from_bytes


async def initialize_rag(
    chat_model: str = "gemma3:1b", embed_model: str = "nomic-embed-text:latest"
) -> LightRAG:
    # detect embedding dimension from the embedding model to avoid mismatches
    try:
        sample = await ollama_embed(
            [""], embed_model=embed_model, host="http://localhost:11434"
        )
        # sample is a numpy array like (1, dim)
        try:
            detected_dim = int(sample.shape[1])
        except Exception:
            detected_dim = (
                len(sample[0])
                if len(sample) and hasattr(sample[0], "__len__")
                else 1024
            )
    except Exception:
        # fall back to 1024 if detection fails
        detected_dim = 1024

    print(
        f"Chosen models: chat_model={chat_model}, embed_model={embed_model} with dim={detected_dim}"
    )

    rag = LightRAG(
        working_dir=LocalSettings().research_output_dir,
        llm_model_func=ollama_model_complete,
        llm_model_name=chat_model,
        summary_max_tokens=20000,
        llm_model_kwargs={
            "host": "http://localhost:11434",
            "options": {"num_ctx": 20000},
            "timeout": 300,
        },
        embedding_func=EmbeddingFunc(
            embedding_dim=detected_dim,
            max_token_size=20000,
            func=lambda texts: ollama_embed(
                texts,
                embed_model=embed_model,
                host="http://localhost:11434",
            ),
        ),
    )

    await rag.initialize_storages()
    await initialize_pipeline_status()

    return rag


async def query_rag_and_update_outputs(
    request: RagRequest,
    prompt_task_id: str,
    output_dir: str,
    clickup_task_status: str,
):
    """Query the RAG system and update ClickUp task and save output file."""
    try:
        task = fetch_clickup_task(task_id=prompt_task_id)
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch ClickUp task {request.task_id}: {e}")

    try:
        system_prompt_dict = json.loads(system_prompt) if system_prompt else {}
    except Exception as e:
        system_prompt_dict = None
        print(f"Warning: Failed to parse system prompt JSON: {e}")

    # it seems like lightrag struggles with json, so if system_prompt_dict, then we need to unpack it
    # and save it as markdown
    if system_prompt_dict:
        system_prompt = flatten_dict_to_string(system_prompt_dict)

    try:
        rag = await initialize_rag(
            chat_model=request.chat_model or "gemma3:1b",
            embed_model=request.embedding_model or "nomic-embed-text:latest",
        )
        print(f"system prompt length: {len(system_prompt)}, text length: {len(request.text)}")

        response = await rag.aquery(
            query=request.text,
            param=QueryParam(mode=request.mode or "hybrid", top_k=request.top_k or 5),
            system_prompt=system_prompt,
        )
        print("RAG response length:", len(response))
    except Exception as e:
        print(f"Error during RAG query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    try:
        filename = f"{request.task_id or 'unknown_task'}.txt"
        upload_file_from_bytes(
            filename=filename,
            data=response.encode("utf-8"),
            output_dir=output_dir,
        )
        if request.task_id:
            updated_text = request.text + "\n\n" + response
            update_clickup_task(
                task_id=request.task_id,
                status=clickup_task_status,
                description=updated_text,
            )
    except Exception as e:
        print(f"Error during RAG query or ClickUp update: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"detail": f"Question generated and saved for task {request.task_id}"}
