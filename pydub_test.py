from pydub import AudioSegment  # type: ignore
from pydub.playback import play  # type: ignore

wav_file = AudioSegment.from_file(file="test.wav", format="wav")

play(wav_file)
print(type(wav_file))
print(wav_file.frame_rate)
print(wav_file.channels)
print(wav_file.sample_width)
print(wav_file.max)
print(len(wav_file))

# increasing db
higher_volume_wav = wav_file + 10

lower_volume_wav = wav_file - 5

play(higher_volume_wav)
play(lower_volume_wav)

wav_file_new = wav_file + lower_volume_wav
play(wav_file_new)

louder_wav_file = wav_file + 10
louder_wav_file.export(out_f="louder_test.wav", format="wav")
play(louder_wav_file)
