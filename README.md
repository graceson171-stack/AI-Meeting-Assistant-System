# AI Meeting Assistant

An AI-powered web application that processes meeting transcripts and recordings to generate structured meeting notes, including a meeting summary, action items, and open questions.

## Features

- Upload a meeting recording or paste a transcript.
- Transcribe supported audio/video files locally using OpenAI Whisper.
- Extract text from PDF and PowerPoint (`.pptx`) files.
- Generate meeting summaries, action items, and open questions using the Google Gemini API.
- Save meetings in a local SQLite database.
- View saved meetings and reopen their results.
- Retry selected temporary Gemini API errors.
- Navigate back to meeting history or start processing another meeting.

## Technology Stack

- Python
- Flask
- SQLite
- Google Gemini API (`google-genai`)
- OpenAI Whisper
- PyMuPDF
- `python-pptx`
- FFmpeg

## Requirements

- Python 3.10 or a compatible Python version supported by the dependencies
- FFmpeg installed and available on your system `PATH`
- A Google Gemini API key
- Internet access for Gemini API requests

Whisper runs locally, so audio transcription speed depends on your computer. CPU transcription can be slower than GPU transcription.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-meeting-assistant.git
cd ai-meeting-assistant
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the virtual environment's Python executable directly or follow your system's approved PowerShell execution policy.

### 3. Install FFmpeg

Install FFmpeg using a trusted distribution for your operating system and make sure the folder containing `ffmpeg.exe` is included in `PATH`.

Verify the installation:

```powershell
ffmpeg -version
```

Restart your terminal after changing `PATH`.

### 4. Install Python dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Whisper may download its model the first time an audio/video file is processed.

### 5. Configure the Gemini API key

Create a file named `.env` in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own key. **Do not commit or share your `.env` file.**

### 6. Run the application

```powershell
python app.py
```

Open the local address shown in the terminal, normally:

http://127.0.0.1:5000

## Using the Application

1. Enter a meeting title.
2. Either upload one supported file or paste a transcript. Do not submit both at once.
3. Select **Generate Meeting Notes**.
4. Review the summary, action items, open questions, and original transcript.
5. Use **View Saved Meetings** to browse previously saved meetings.

Supported upload extensions in the application include PDF, PPTX, MP3, WAV, M4A, MP4, MPEG, MPGA, WEBM, OGG, FLAC, and AAC. The configured upload limit is 20 MB.

PDF files need extractable text; scanned PDFs may require OCR, which is not currently included.

## Project Structure

```text
ai-meeting-assistant/
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
├── .env                 # Create locally; do not commit
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
└── static/
    └── style.css
```

The exact files in your repository may differ as the project evolves.

## Privacy and Security

- Keep API keys in environment variables and never commit them.
- Uploaded media is temporarily written to a local temporary file for Whisper transcription and is removed after processing.
- Meeting transcripts and generated notes are stored in the local SQLite database.
- Do not upload confidential meeting recordings or transcripts unless you have permission and understand the applicable data-handling requirements.
- Gemini API requests send the meeting text to the configured Google service for analysis.

## Current Limitations

- Whisper transcription may be slow on CPU-only computers.
- Gemini requests require network access and may temporarily fail due to service availability or API limits.
- The application is configured for local development using Flask's development server. It is not configured for production deployment.

## Future Improvements

Potential improvements include PDF export, OCR for scanned PDFs, user authentication, configurable meeting retention, background processing for long recordings, and automated tests.

## License

No license is specified yet. Add a license file if you decide to make the project open source.
