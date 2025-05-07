# app/tts.py
import numpy as np
import scipy.io.wavfile
from datetime import datetime
from nltk.tokenize import sent_tokenize
from bark import generate_audio, SAMPLE_RATE
from .emotion import detect_emotion, EMOTION_TAGS
from .voices import VOICE_PROFILES

import warnings
warnings.filterwarnings("ignore")

def generate_bark_audio(text, voice_name):
    if not text or not text.strip():
        return None, "❗ Error: Input text cannot be empty.", ""

    history_prompt = VOICE_PROFILES.get(voice_name)
    if not history_prompt:
        return None, "❗ Error: Invalid voice name provided.", ""

    sentences = sent_tokenize(text)
    full_audio = np.array([], dtype=np.float32)

    for i, sentence in enumerate(sentences):
        emotion_label, score = detect_emotion(sentence)
        emotion_tag = EMOTION_TAGS[emotion_label]
        prompt = f"{emotion_tag}{sentence}"

        try:
            print(f"[{i+1}/{len(sentences)}] Emotion: {emotion_label} | Score: {score:.2f}")
            audio_array = generate_audio(prompt, history_prompt=history_prompt)
            full_audio = np.concatenate((full_audio, audio_array))
        except Exception as e:
            print(f"Error generating audio for sentence {i+1}: {e}")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"bark_audio_{timestamp}.wav"
    scipy.io.wavfile.write(filename, rate=SAMPLE_RATE, data=full_audio)

    return filename, "✅ Success! Generated with automatic emotion detection.", text

# Async wrapper
import asyncio
async def generate_bark_audio_async(text, voice_name):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, generate_bark_audio, text, voice_name)
