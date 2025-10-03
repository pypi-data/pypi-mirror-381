import json
from fastapi import APIRouter, HTTPException
from lightrag import QueryParam
import os

# local imports
from clickup_utils import fetch_clickup_task, update_clickup_task
from utils import flatten_dict_to_string, upload_file_from_bytes
from rag_utils import initialize_rag, query_rag_and_update_outputs
from schemas import InitializeRagRequest, RagRequest, TextRequest
from settings import LocalSettings

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/initialize")
async def initialize_rag_endpoint(request: InitializeRagRequest):
    try:
        rag = await initialize_rag(
            chat_model=request.chat_model, embed_model=request.embedding_model
        )
        return {"message": "RAG initialized successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/query")
async def query_rag_endpoint(request: RagRequest):
    """Query the RAG system with a question and return the answer."""
    try:
        rag = await initialize_rag(
            chat_model=request.chat_model or "gemma3:1b",
            embed_model=request.embedding_model or "nomic-embed-text:latest",
        )
        response = await rag.aquery(
            query=request.text,
            param=QueryParam(mode=request.mode, top_k=request.top_k),
        )
        print("RAG response:", response)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reload")
async def reload_rag_endpoint(request: InitializeRagRequest):
    """Scan the RAG working directory, enqueue new text files and process the pipeline."""
    try:
        # initialize RAG and storages
        rag = await initialize_rag(
            chat_model=request.chat_model, embed_model=request.embedding_model
        )

        # determine working dir
        working_dir = getattr(rag, "working_dir", LocalSettings().research_output_dir)

        docs = []
        paths = []
        for root, _, files in os.walk(working_dir):
            for fn in files:
                if fn.lower().endswith((".txt", ".md", ".html", ".htm")):
                    full = os.path.join(root, fn)
                    try:
                        with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                            content = fh.read()
                            if content and content.strip():
                                docs.append(content)
                                paths.append(full)
                    except Exception:
                        continue

        if not docs:
            return {
                "message": "RAG reloaded: no text files found in working_dir",
                "working_dir": working_dir,
            }

        track_id = await rag.apipeline_enqueue_documents(input=docs, file_paths=paths)
        await rag.apipeline_process_enqueue_documents()

        return {
            "message": "RAG reloaded and files enqueued/processed",
            "track_id": track_id,
            "files": len(docs),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/questions")
async def question_rag_endpoint(request: RagRequest):
    """Query the RAG system with a question and return the answer."""
    return await query_rag_and_update_outputs(
        request=request,
        prompt_task_id="869ak7hj3",
        output_dir=LocalSettings().question_output_dir,
        clickup_task_status="phase 4. interview",
    )


# /rag/transcript-cleanup
@router.post("/transcript-cleanup")
async def rag_cleanup_transcript(request: RagRequest):
    return await query_rag_and_update_outputs(
        request=request,
        prompt_task_id="869akcv3p",
        output_dir=LocalSettings().transcripts_output_dir,
        clickup_task_status="phase 6. transcript clean",
    )


# /rag/challenge-ideas
@router.post("/challenge-ideas")
async def rag_generate_challenge_ideas(request: RagRequest):
    return await query_rag_and_update_outputs(
        request=request,
        prompt_task_id="869akcv6d",
        output_dir=LocalSettings().challenge_output_dir,
        clickup_task_status="phase 7. challenge",
    )


# /rag/generate-content
@router.post("/generate-content")
async def rag_generate_content(request: RagRequest):
    content_type_clickup_map = {
        "blog": "869an89cp",
        "patreon": "869an89a6",
        "newsletter": "869an89cb",
        "discord": "869an89dn",
        "meta-ads": "869an89b1",
        "facebook-post": "869an89bj",
        "instagram-post": "869an89bw",
        "business-blog": "869an89d7",
        "freebie": "869an899t",
    }
    generated_content = ""
    for content_type, prompt_task_id in content_type_clickup_map.items():
        print(f"Generating content for type: {content_type} using prompt task ID: {prompt_task_id}")
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
                query=f"{content_type}: {request.text}",
                param=QueryParam(mode=request.mode or "hybrid", top_k=request.top_k or 5),
                system_prompt=system_prompt,
            )
            print("RAG response length:", len(response))
        except Exception as e:
            print(f"Error during RAG query: {e}")
            raise HTTPException(status_code=500, detail=str(e))
        
        generated_content += f"\n\n## {content_type.capitalize()}\n\n{response}"

    response = generated_content.strip()
    try:
        filename = f"{request.task_id or 'unknown_task'}.txt"
        upload_file_from_bytes(
            filename=filename,
            data=response.encode("utf-8"),
            output_dir=LocalSettings().content_generation_dir,
        )
        if request.task_id:
            updated_text = request.text + "\n\n" + response
            update_clickup_task(
                task_id=request.task_id,
                status="phase 8. draft channel",
                description=updated_text,
            )
    except Exception as e:
        print(f"Error during RAG query or ClickUp update: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"detail": f"Question generated and saved for task {request.task_id}"}


# /rag/review
@router.post("/review")
async def rag_review_content(request: RagRequest):
    return await query_rag_and_update_outputs(
        request=request,
        prompt_task_id="869ak6h10",
        output_dir=LocalSettings().review_output_dir,
        clickup_task_status="phase 9. review interlink",
    )
