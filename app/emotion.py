from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

EMOTION_TAGS = {
    "neutral": "",
    "joy": "[laughs] ",
    "sadness": "[sighs] ",
    "fear": "[gasps] ",
    "anger": "[anger] ",
    "disgust": "[disgust] ",
    "surprise": "[excited] ",
}

def load_emotion_model():
    model_name = "j-hartmann/emotion-english-roberta-large"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return TextClassificationPipeline(model=model, tokenizer=tokenizer, return_all_scores=False)

emotion_model = load_emotion_model()

def detect_emotion(text):
    result = emotion_model(text)[0]
    return result['label'], result['score']
