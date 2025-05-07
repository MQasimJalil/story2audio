import grpc
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.proto import story_pb2
from app.proto import story_pb2_grpc
import unittest

class TestAPI(unittest.TestCase):
    def test_grpc_call(self):
        channel = grpc.insecure_channel('localhost:50051')
        stub = story_pb2_grpc.StoryToAudioStub(channel)
        request = story_pb2.AudioRequest(text="Hello, World!", voice="English - Voice 1")
        response = stub.Generate(request)

        self.assertTrue(response.success)
        self.assertIn("Success", response.status)
        self.assertGreater(len(response.audio), 0)

if __name__ == '__main__':
    unittest.main()
