import openai
import os
from pydub import AudioSegment

# Initialize OpenAI client (replace with your actual API key)
client = openai.OpenAI(api_key="replace-with-your-api-key")

def transcribe_audio(file_path):
    """Transcribes a single audio file using OpenAI's Whisper API."""
    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file, 
                response_format="text"
            )
            return transcript
    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")
        return None

def split_large_audio(file_path, max_size_mb=25):
    """Splits a large audio file into smaller chunks to meet API file size limits."""
    audio = AudioSegment.from_file(file_path)
    chunk_size = max_size_mb * 1024 * 1024  # Convert MB to bytes

    chunks = []
    start = 0

    while start < len(audio):
        # Determine the end of the chunk (time is in milliseconds)
        end = min(len(audio), start + chunk_size)
        chunk = audio[start:end]
        chunks.append(chunk)
        start += chunk_size

    return chunks

def process_large_audio(file_path):
    """Processes large audio files by splitting them into smaller chunks and transcribing each chunk."""
    chunks = split_large_audio(file_path)

    transcription = []
    for i, chunk in enumerate(chunks):
        # Export each chunk to a temporary file
        chunk_file = f"{os.path.splitext(file_path)[0]}_part{i}.mp3"
        chunk.export(chunk_file, format="mp3")

        # Transcribe the chunk
        chunk_transcription = transcribe_audio(chunk_file)

        if chunk_transcription:
            transcription.append(chunk_transcription)

        # Clean up temporary file
        os.remove(chunk_file)

    # Join all transcriptions
    return " ".join(transcription)

def save_transcription_to_file(transcription, output_file):
    """Saves the transcription text to a file."""
    with open(output_file, "w") as f:
        f.write(transcription)

def transcribe_multiple_files(directory_path):
    """Transcribes all mp3 files in the specified directory and saves their transcription."""
    
    # Ensure 'text_files' directory exists
    output_directory = "text_files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing {file_path}...")

            # Check file size (in MB)
            file_size = os.path.getsize(file_path) / (1024 * 1024)

            if file_size > 25:
                # Process large files
                print(f"File {filename} is larger than 25MB, processing in chunks...")
                transcription = process_large_audio(file_path)
            else:
                # Process regular files
                transcription = transcribe_audio(file_path)

            if transcription:
                # Save transcription to the 'text_files' directory
                output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".txt")
                save_transcription_to_file(transcription, output_file)
                print(f"Saved transcription to {output_file}")
            else:
                print(f"Failed to transcribe {file_path}")

if __name__ == "__main__":
    # Set the path to the directory containing your mp3 files
    directory_path = "voice_files"
    transcribe_multiple_files(directory_path)
