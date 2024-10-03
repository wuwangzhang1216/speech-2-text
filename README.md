# Audio to Text Transcription Script

This Python script transcribes multiple `.mp3` audio files into text using the OpenAI Whisper API. The transcribed text files are saved in a separate `text_files` directory.

## Project Structure

The project is structured as follows:

```
.
├── text_files         # Directory where transcribed text files are saved
├── voice_files        # Directory where input .mp3 audio files are located
├── main.py            # The main Python script that performs the transcription
└── requirements.txt   # The list of required Python libraries
```

## Prerequisites

Before you run the script, ensure you have the following:

1. **Python 3.7+**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. **FFmpeg (optional)**: The script uses `pydub`, which requires FFmpeg to process audio files. Follow these steps to install FFmpeg:

   - Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
   - Add FFmpeg to your system's PATH:
     - **Windows**: Add the path to `ffmpeg.exe` to your system's environment variables under the `Path` section.
     - **macOS/Linux**: Add the FFmpeg path to your `.bashrc`, `.zshrc`, or equivalent shell configuration file.
3. **OpenAI API Key**: You need an API key to access OpenAI’s Whisper API. Get it from [OpenAI](https://platform.openai.com/).

## Installation

1. Clone or download the repository into a directory of your choice.
2. Navigate into the directory where the `main.py` script is located.
3. Install the required dependencies using `pip` by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the following dependencies:

   - `openai`
   - `pydub`

## Usage

1. **Prepare Your Audio Files**:

   - Place all your `.mp3` audio files inside the `voice_files` directory.
2. **Configure Your API Key**:

   - Open the `main.py` file and replace the `your-api-key` string with your actual OpenAI API key:

     ```python
     client = openai.OpenAI(api_key="your-api-key")
     ```
3. **Run the Script**:

   - Run the Python script using the following command in your terminal:

     ```bash
     python main.py
     ```
4. **Output**:

   - The script will process all `.mp3` files in the `voice_files` directory and save the transcription results as `.txt` files in the `text_files` directory.
   - Each text file will have the same name as its corresponding `.mp3` file but with a `.txt` extension.

## Example

For example, if you have an audio file `example.mp3` in the `voice_files` directory, after running the script, a file `example.txt` will be created in the `text_files` directory containing the transcription.

## Troubleshooting

- **Error: FFmpeg not found**: If you see an error message saying `Couldn't find ffmpeg`, ensure that FFmpeg is installed and properly added to your system’s PATH.
- **Transcription Errors**: If transcription fails, ensure the file is under 25MB. If the file is larger, the script will automatically split the file into smaller chunks for processing.
- **API Errors**: Ensure you are using a valid OpenAI API key and have sufficient quota available for API calls.
