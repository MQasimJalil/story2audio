import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from bark import preload_models

import warnings
warnings.filterwarnings("ignore")

def download_bark_models():
    print("🔄 Downloading Bark models...")
    preload_models()
    print("✅ Bark models downloaded.")

def download_emotion_model():
    print("🔄 Downloading emotion detection model...")
    model_name = "j-hartmann/emotion-english-roberta-large"
    AutoTokenizer.from_pretrained(model_name)
    AutoModelForSequenceClassification.from_pretrained(model_name)
    print("✅ Emotion model downloaded.")

def preload_all():
    download_bark_models()
    download_emotion_model()

if __name__ == "__main__":
    preload_all()
