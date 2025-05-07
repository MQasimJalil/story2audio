import asyncio
import pytest
import grpc

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.proto import story_pb2, story_pb2_grpc

@pytest.mark.asyncio
async def test_async_fire_and_forget():
    async def send_request(i):
        try:
            channel = grpc.aio.insecure_channel('localhost:50051')
            stub = story_pb2_grpc.StoryToAudioStub(channel)
            request = story_pb2.AudioRequest(text=f"Test {i}", voice="English - Voice 1")
            # Fire and forget — don't await the result
            stub.Generate(request)
            return True
        except Exception as e:
            return e

    tasks = [send_request(i) for i in range(5)]
    results = await asyncio.gather(*tasks)

    for r in results:
        if isinstance(r, Exception):
            pytest.fail(f"Request raised an exception: {r}")