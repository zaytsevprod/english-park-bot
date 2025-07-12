import openai
from config import OPENAI_API_KEY, WHISPER_MODEL

openai.api_key = OPENAI_API_KEY

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(WHISPER_MODEL, audio_file)
    return transcript['text']
