import glob

from src.open_api_client import get_openai_client
import os
import math
from pydub import AudioSegment
from openai.types.audio import TranscriptionTextDeltaEvent, TranscriptionTextDoneEvent


client = get_openai_client()


# calling openAI transcriptions to transcribe a short file
def transcribe_short_file():
    with open("/Users/lila/Downloads/Shiur167.mp3", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
        print(f"Transcription: {transcript.text}")

# calling openAI transcriptions to transcribe a short file and pass the prompt with expected spellings
def transcribe_short_file_with_prompt():
    with open("/Users/lila/Downloads/Shiur167.mp3", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            prompt="This is a Torah lecture. Words like Torah, mitzvah, halacha, korban, esrog are common.")
        print(f"\nTranscription with Prompt: {transcript.text}")


# Function to split MP3 into chunks
def split_mp3(file_path, chunk_length_minutes=10, output_folder="chunks"):
    audio = AudioSegment.from_mp3(file_path)
    duration_ms = len(audio)
    chunk_length_ms = chunk_length_minutes * 60 * 1000
    os.makedirs(output_folder, exist_ok=True)
    num_chunks = math.ceil(duration_ms / chunk_length_ms)
    chunk_paths = []

    for i in range(num_chunks):
        start_ms = i * chunk_length_ms
        end_ms = min((i + 1) * chunk_length_ms, duration_ms)
        chunk = audio[start_ms:end_ms]
        chunk_filename = f"{output_folder}/chunk_{i + 1:03d}.mp3"
        chunk.export(chunk_filename, format="mp3")
        print(f"Saved: {chunk_filename}")
        chunk_paths.append(chunk_filename)

    return chunk_paths

def get_or_create_chunks(file_path, output_folder="chunks", chunk_length_minutes=10):
    # Look for existing chunk files
    chunk_paths = sorted(glob.glob(os.path.join(output_folder, "chunk_*.mp3")))

    if chunk_paths:
        print(f" Found {len(chunk_paths)} existing chunk(s).")
        return chunk_paths
    else:
        print("No existing chunks found. Splitting now...")
        return split_mp3(file_path, chunk_length_minutes, output_folder)

# split and transcribe - note that we are using the gpt-4o-transcribe model, not wisper-1
def transcribe_chunks(file_path):
    chunk_paths = get_or_create_chunks(file_path)
    event_counter = 0 # Initialize event counter. I want to show first two events and collect delta from others
    transcript_text = ""  # Initialize transcript text - we will add to it as we process events

    for i, chunk_path in enumerate(chunk_paths):  # Note how enumerate is used to get the index and iterate over the chunks
        if i < 2:  # only show for 2 chunks
            print(f"\n Transcribing chunk {i + 1}...")
            with open(chunk_path, "rb") as audio_file:
                stream = client.audio.transcriptions.create(
                    model="gpt-4o-transcribe",
                    file=audio_file,
                    response_format="text",
                    stream=True
                )
                for event in stream:
                    event_counter += 1
                    if event_counter < 3 or isinstance(event, TranscriptionTextDoneEvent):
                        print(event, end='\n', flush=True)
                    if isinstance(event, TranscriptionTextDeltaEvent):
                        # Collect the delta text
                        print(event.delta, end='', flush=True)
                        transcript_text += event.delta

    #show the transcript text
    print(transcript_text)

# Example usage
def main():
    # transcribe_short_file()
    # transcribe_short_file_with_prompt()
    transcribe_chunks("/Users/lila/Downloads/UncleMoishy.mp3")

if __name__ == "__main__":
    main()