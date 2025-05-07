import asyncio
from concurrent import futures
import grpc
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tts import generate_bark_audio_async
from app.proto import story_pb2
from app.proto import story_pb2_grpc
from app.load_models import preload_all

import asyncio
import platform

import warnings
warnings.filterwarnings("ignore")


class StoryToAudioService(story_pb2_grpc.StoryToAudioServicer):
    async def Generate(self, request, context):
        audio_path, status, text = await generate_bark_audio_async(request.text, request.voice)
        if not audio_path:
            return story_pb2.AudioResponse(success=False, status=status)

        with open(audio_path, "rb") as f:
            audio_data = f.read()

        return story_pb2.AudioResponse(
            success=True,
            status=status,
            text=text,
            audio=audio_data
        )

async def serve_async():
    server = grpc.aio.server()
    story_pb2_grpc.add_StoryToAudioServicer_to_server(StoryToAudioService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server running on port 50051...")
    await server.start()
    await server.wait_for_termination()

def serve():
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(serve_async())

if __name__ == '__main__':
    serve()