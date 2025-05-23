from pathlib import Path
from src.open_api_client import get_openai_client
import os

client = get_openai_client()

def speak_out(text:str):
    # Set the path for the output speech file
    speech_file_path = Path(__file__).parent / "speech.mp3"

    with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="coral",
            input=text,
            instructions="Speak in a cheerful and positive tone.",
    ) as response:
        response.stream_to_file(speech_file_path)
    return speech_file_path

def main():
    # Example usage
    text = "Today is a wonderful day to build something people love!"
    speech_file_path = speak_out(text)



if __name__ == "__main__":
    main()