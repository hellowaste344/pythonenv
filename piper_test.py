import wave

from piper.voice import PiperVoice

# load a voice model
voice = PiperVoice.load(
    "en_US-lessac-medium.onnx", config_path="en_US-lessac-medium.onnx.json"
)

with wave.open("output.wav", "wb") as f:
    # set audio paramaters
    f.setframerate(voice.config.sample_rate)
    f.setsampwidth(2)
    f.setnchannels(1)

    # synthesize the text
    for chunk in voice.synthesize("Hi, I'm Samantha"):
        f.writeframes(chunk.audio_int16_bytes)
