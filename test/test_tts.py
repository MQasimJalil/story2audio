# tests/test_tts.py
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.tts import generate_bark_audio

class TestTTS(unittest.TestCase):
    def test_generate_audio(self):
        text = "Hello, world!"
        voice = "English - Voice 1"
        output_path, status, used_text = generate_bark_audio(text, voice)

        self.assertTrue(output_path.endswith(".wav"))
        self.assertTrue("Success" in status)
        self.assertEqual(used_text, text)

if __name__ == '__main__':
    unittest.main()
