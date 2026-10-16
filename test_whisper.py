
import whisper

audio_path = r"D:\Ai Meeting Assisstant System\Voice Message.mp4"

print("Loading Whisper model...")
model = whisper.load_model("base")

print("Transcribing audio...")
result = model.transcribe(audio_path)

print("\n--- TRANSCRIPTION RESULT ---")
print(result["text"])
