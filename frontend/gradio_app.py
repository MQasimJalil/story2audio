import gradio as gr
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import warnings
warnings.filterwarnings("ignore")

from app.tts import generate_bark_audio
from app.voices import VOICE_PROFILES

import nltk
nltk.download("punkt_tab")

def serve_gradio():
    with gr.Blocks(title="Bark Text-to-Audio") as demo:
        gr.Markdown("<h1>Bark Text-to-Audio Generator</h1>")
        gr.Markdown("<h2>Enter text, choose voice & emotion, and generate speech!</h2>")

        with gr.Column():
            input_text = gr.Textbox(label="Input Text", lines=5, placeholder="Enter the text...")
            voice_dropdown = gr.Dropdown(choices=list(VOICE_PROFILES.keys()), label="Voice Type", value="English - Voice 1")
            generate_button = gr.Button("Generate Audio")
            audio_output = gr.Audio(label="Generated Audio")
            status_output = gr.Textbox(label="Status", interactive=False)
            transcript_output = gr.Textbox(label="Input Text Used", interactive=False)

        generate_button.click(
            fn=generate_bark_audio,
            inputs=[input_text, voice_dropdown],
            outputs=[audio_output, status_output, transcript_output],
            api_name="generate_bark_audio"
        )
    return demo

if __name__ == "__main__":
    interface = serve_gradio()
    interface.launch(debug=True)