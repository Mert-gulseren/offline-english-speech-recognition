# Offline English Speech Recognition

A small Python application that recognizes a short spoken English sentence from a microphone using the Vosk speech recognition toolkit. Audio recognition runs locally with a downloaded Vosk model; no cloud speech API is used.

## Features

- Records a five-second microphone sample
- Uses 16 kHz mono audio
- Recognizes English speech with Vosk
- Prints the recognized sentence in the terminal

## Requirements

- Python 3
- A working microphone
- A Vosk English model

Python packages are listed in [`requirements.txt`](requirements.txt).

## Setup

1. Clone or download this repository.
2. Create and activate a virtual environment (recommended):

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Download a Vosk model for English and extract it into a folder named `model` in the project root. The application expects this path:

   ```text
   project-root/
   ├── english_speech_to_text.py
   ├── requirements.txt
   └── model/
   ```

5. Run the application:

   ```powershell
   python english_speech_to_text.py
   ```

When prompted, speak an English sentence during the five-second recording window.

## Model and environment files

The virtual environment and Vosk model files are not included in this repository. Install the Python packages with `pip install -r requirements.txt` and place the downloaded model in the local `model/` folder before running the application.
