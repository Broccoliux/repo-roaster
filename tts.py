from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

VOICE_ID = "UgBBYS2sOqTuMpoF3BR0"

def generate_speech(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print(response.status_code)
    print(response.text)

    return response.content
