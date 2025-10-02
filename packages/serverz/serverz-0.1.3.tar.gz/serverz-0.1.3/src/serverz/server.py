from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from serverz.core import ChatBox
from serverz.models import *
from serverz.log import Log
import argparse
import uvicorn
import time
import uuid
import asyncio


logger = Log.logger
coding_log = logger.info

default=8008

app = FastAPI(
    title="LLM Service",
    description="Provides an OpenAI-compatible API for custom large language models.",
    version="1.0.1",
)

# --- Configure CORS ---
origins = [
    "*", # Allows all origins (convenient for development, insecure for production)
    # Add the specific origin of your "别的调度" tool/frontend if known
    # e.g., "http://localhost:5173" for a typical Vite frontend dev server
    # e.g., "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the allowed origins
    allow_credentials=True, # Allows cookies/authorization headers
    allow_methods=["*"],    # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],    # Allows all headers (Content-Type, Authorization, etc.)
)
# --- End CORS Configuration ---

# Router
from serverz.reader_router import router
app.include_router(router,prefix="/reader")

chatbox = ChatBox()

# --- (Optional) Authentication Dependency ---
async def verify_api_key(authorization: Optional[str] = Header(None)):
    """
    Placeholder for API key verification.
    In a real application, you'd compare this to a stored list of valid keys.
    """
    if not authorization:
        # Allow requests without Authorization for local testing/simplicity
        # OR raise HTTPException for stricter enforcement
        # raise HTTPException(status_code=401, detail="Authorization header missing")
        logger.warning("Warning: Authorization header missing.")
        return None # Or a default principal/user if needed

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization scheme")

    token = authorization.split(" ")[1]
    # --- Replace this with your actual key validation logic ---
    # Example:
    # valid_keys = {"your-secret-key-1", "your-secret-key-2"}
    # if token not in valid_keys:
    #     raise HTTPException(status_code=401, detail="Invalid API Key")
    # print(f"Received valid API Key (last 4 chars): ...{token[-4:]}")
    # --- End Replace ---
    logger.info(f"Received API Key (placeholder validation): ...{token[-4:]}")
    return token # Return the token or an identifier associated with it

# --- Mock LLM Call ---
async def generate_llm_response(prompt: str, stream: bool, model: str):
    """
    Replace this with your actual LLM call logic.
    This mock function simulates generating text.
    """
    response_id = f"chatcmpl-{uuid.uuid4().hex}"
    created_time = int(time.time())
    if not stream:
        full_response = chatbox.product(prompt_with_history = prompt,model=model)
        # full_response = " ".join(words)
        words = full_response.split(' ')
        choice = Choice(
            index=0,
            message=ChatCompletionMessage(role="assistant", content=full_response),
            finish_reason="stop"
        )
        # Simulate token counts (highly inaccurate)
        usage = UsageInfo(prompt_tokens=len(prompt.split()),
                          completion_tokens=len(words),
                          total_tokens=len(prompt.split()) + len(words))
        return ChatCompletionResponse(
            id=response_id,
            model=model,
            choices=[choice],
            usage=usage,
            created=created_time
        )
    else:
        async def stream_generator():
            # First chunk: Send role
            first_chunk_choice = ChunkChoice(index=0, delta=DeltaMessage(role="assistant"),
                                                                finish_reason=None)
            yield ChatCompletionChunkResponse(
                id=response_id, model=model, choices=[first_chunk_choice], created=created_time
            ).model_dump_json() # Use model_dump_json() for Pydantic v2

            # Subsequent chunks: Send content word by word

            async for word in chatbox.astream_product(prompt_with_history = prompt,
                                                            model=model):
                chunk_choice = ChunkChoice(index=0,
                                           delta=DeltaMessage(content=f"{word}"),
                                                                finish_reason=None)
                yield ChatCompletionChunkResponse(
                    id=response_id, model=model, choices=[chunk_choice], created=created_time
                ).model_dump_json()
                await asyncio.sleep(0.001) # Simulate token generation time


            # Final chunk: Send finish reason
            final_chunk_choice = ChunkChoice(index=0, delta=DeltaMessage(), finish_reason="stop")
            yield ChatCompletionChunkResponse(
                id=response_id, model=model, choices=[final_chunk_choice], created=created_time
            ).model_dump_json()

            # End of stream marker (specific to SSE)
            yield "[DONE]"

        # Need to wrap the generator for EventSourceResponse
        async def event_publisher():
            try:
                async for chunk in stream_generator():
                    yield {"data": chunk}
                    await asyncio.sleep(0.01) # Short delay between sending chunks is good practice
            except asyncio.CancelledError as e:
                logger.error("Streaming connection closed by client.")
                raise e

        return EventSourceResponse(event_publisher())



@app.get("/")
async def root():
    """ x """
    return {"message": "LLM Service is running."}

@app.get("/v1/models", response_model=ModelList,  tags=["Models"])
async def list_models():
    """ x """
    # Replace with your actual list of models

    available_models = [ModelCard(id=ModelCardName) for ModelCardName in chatbox.custom]
    return ModelList(data=available_models)


@app.post(
    "/v1/chat/completions",
    response_model=None, # Response model needs dynamic handling (stream vs non-stream)
    summary="Chat Completions",
    description="Creates a model response for the given chat conversation.",
    tags=["Chat"],
)
async def create_chat_completion(
    request: ChatCompletionRequest,
    # token: str = Depends(verify_api_key) # Uncomment to enable authentication
):
    """ use """
    # --- 1. Prepare Prompt for your LLM ---
    # This is highly dependent on your specific model.
    # You might concatenate messages, add special tokens, etc.
    # Example simplistic prompt concatenation:

    prompt_for_llm_list = []
    for msgs in request.messages:
        if msgs.content:
            msgs_content = ""
            for msg in msgs.content:
                if msg.type == 'text':
                    msgs_content += f"{msg.text}\n"
                else:
                    pass
                           
        prompt_for_llm_list.append(f"{msgs.role}: {msgs_content}")

    prompt_for_llm = "\n".join(prompt_for_llm_list)
    # prompt_for_llm = "\n".join([f"{msg.role}: {msg.content}"
    #                             for msg in request.messages if msg.content])


    logger.debug(f"Received Request for model: {request.model}")
    logger.debug(f"Streaming: {request.stream}")
    logger.debug(f"Prompt for LLM:\n{prompt_for_llm}") # Be careful logging prompts with sensitive data


    # --- 2. Call your LLM Backend ---
    # Pass necessary parameters like temperature, max_tokens etc. from the request
    try:
        response_data = await generate_llm_response(
            prompt=prompt_for_llm,
            stream=request.stream,
            model=request.model # Echo back the requested model
        )
    except Exception as e:
        logger.error(f"Error calling LLM backend: {e}")
        raise HTTPException(status_code=500, detail=f"LLM backend error: {str(e)}") from e


    # --- 3. Format and Return Response ---
    if request.stream:
        if not isinstance(response_data, EventSourceResponse):
            raise HTTPException(status_code=500, detail=
                                 "Streaming response was not generated correctly.")
        return response_data # Return the SSE stream directly
    else:
        if not isinstance(response_data, ChatCompletionResponse):
            raise HTTPException(status_code=500,
                                 detail="Non-streaming response was not generated correctly.")
        return response_data # FastAPI automatically converts Pydantic model to JSON





if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Start a simple HTTP server similar to http.server."
    )
    parser.add_argument(
        'port',
        metavar='PORT',
        type=int,
        nargs='?', # 端口是可选的
        default=default,
        help=f'Specify alternate port [default: {default}]'
    )
    # 创建一个互斥组用于环境选择
    group = parser.add_mutually_exclusive_group()

    # 添加 --dev 选项
    group.add_argument(
        '--dev',
        action='store_true', # 当存在 --dev 时，该值为 True
        help='Run in development mode (default).'
    )

    # 添加 --prod 选项
    group.add_argument(
        '--prod',
        action='store_true', # 当存在 --prod 时，该值为 True
        help='Run in production mode.'
    )
    args = parser.parse_args()

    if args.prod:
        env = "prod"
    else:
        # 如果 --prod 不存在，默认就是 dev
        env = "dev"

    port = args.port
    if env == "dev":
        port += 100
        Log.reset_level('debug',env = env)
        reload = True
        app_import_string = f"{__package__}.server:app" # <--- 关键修改：传递导入字符串
    elif env == "prod":
        Log.reset_level('info',env = env)# ['debug', 'info', 'warning', 'error', 'critical']
        reload = False
        app_import_string = app
    else:
        reload = False
        app_import_string = app
    

    # 使用 uvicorn.run() 来启动服务器
    # 参数对应于命令行选项
    uvicorn.run(
        app_import_string,
        host="0.0.0.0",
        port=port,
        reload=reload  # 启用热重载
    )
