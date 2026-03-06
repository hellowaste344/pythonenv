import whisper

# tiny | base | small | medium
model = whisper.load_model("base")

transcription = model.transcribe("test.wav")

print(transcription["text"])
