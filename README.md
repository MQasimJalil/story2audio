
#  Story2Audio: Emotion-Aware Text-to-Speech Generator

Story2Audio is a powerful microservice that converts input text into expressive speech using [Bark](https://github.com/suno-ai/bark) and emotion detection via a fine-tuned RoBERTa model. The service supports asynchronous gRPC and RESTful communication, emotion-aware speech synthesis, concurrent request handling, and features a Gradio-based frontend for real-time demos.

---

##  Features

-  **Text-to-Audio Conversion** using Bark TTS
-  **Emotion Detection** via RoBERTa (`j-hartmann/emotion-english-roberta-large`)
-  **Dynamic Prompt Injection** with emotion tags like `[laughs]`, `[sighs]`, etc.
-  **gRPC Microservice** with asynchronous support
-  **Full Test Suite** (unit + integration + async tests)
-  **Performance Testing** with Locust
-  **gRPC + Postman** testing enabled
-  **Gradio Web Interface** for user-friendly interaction
-  **Dockerized Deployment** for reproducibility

---

##  Project Structure

```
.
├── app/
│   ├── main.py               # gRPC server
│   ├── tts.py                # Audio generation logic
│   ├── emotion.py            # Emotion detection
│   ├── voices.py             # Voice profiles
│   ├── loadmodels.py         # Preloading Bark and emotion models
│   └── proto/
│       └── story.proto       # gRPC protobuf definitions
├── gradioapp.py              # Gradio UI
├── Dockerfile                # Docker setup
├── Makefile                  # CLI task automation
├── requirements.txt          # Dependencies
├── tests/
│   ├── test_api.py           # gRPC integration test
│   ├── test_tts.py           # Unit test for TTS
│   └── test_async.py         # Async test
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MQasimJalil/story2audio.git
cd story2audio
```

### 2. Install Dependencies

```bash
make install
```

### 3. Download Required Models

```bash
make download-models
```

### 4. Build gRPC Protobuf

```bash
make build
```

### 5. Run the Server

```bash
make run-server
```

Or use Docker:

```bash
make docker-build
make docker-run
```

---

## 🎮 Using the Service

### gRPC Endpoint

- **Service**: `StoryToAudio`
- **Method**: `Generate`
- **Request**:  
  ```proto
  message AudioRequest {
    string text = 1;
    string voice = 2;
  }
  ```
- **Response**:  
  ```proto
  message AudioResponse {
    bool success = 1;
    string status = 2;
    string text = 3;
    bytes audio = 4;
  }
  ```

### Gradio Frontend

```bash
python frontend/gradio_app.py
```

- Input text and choose from 5 different English voices.
- Hear audio output directly in the browser.
- See auto-generated emotion tags and status updates.

---

##  Testing

```bash
make run-tests
```

Includes:

-  Unit Tests (`test_tts.py`)
-  gRPC Integration Tests (`test_api.py`)
-  Async Tests (`test_async.py`)
- Postman testing available for REST/JSON emulation

---

## Performance Testing

- Locust-based gRPC load testing simulates concurrent users
- Measures response times, throughput
- Identifies performance bottlenecks under load

---

##  Voice Options

```python
VOICE_PROFILES = {
    "English - Voice 1": "v2/en_speaker_0",
    "English - Voice 2": "v2/en_speaker_1",
    "English - Voice 3": "v2/en_speaker_2",
    "English - Voice 4": "v2/en_speaker_3",
    "English - Voice 5": "v2/en_speaker_6",
}
```

---

##  Emotion Tags

Based on detected emotion, the following tags are prepended to prompts for expressive synthesis:

| Emotion    | Tag        |
|------------|------------|
| Joy        | `[laughs]` |
| Sadness    | `[sighs]`  |
| Fear       | `[gasps]`  |
| Anger      | `[anger]`  |
| Disgust    | `[disgust]`|
| Surprise   | `[excited]`|
| Neutral    | *(none)*   |

---

##  Requirements

```txt
grpcio
grpcio-tools
numpy
scipy
transformers
torch
torchaudio
bark
librosa
scikit-learn
nltk
gtts
requests
gradio
pytest
```

---

##  Makefile Commands

| Command              | Description                          |
|----------------------|--------------------------------------|
| `make install`       | Install all Python dependencies      |
| `make run-server`    | Start the gRPC server                |
| `make run-tests`     | Run all tests                        |
| `make download-models` | Preload Bark & emotion models      |
| `make build`         | Compile protobuf definitions         |
| `make docker-build`  | Build Docker image                   |
| `make docker-run`    | Run Docker container                 |

---

## Audio Sample




https://github.com/user-attachments/assets/56d3f2a6-df6d-4b9e-8773-3edcb3f9427a

