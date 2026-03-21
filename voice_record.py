import matplotlib.pyplot as plt 
import sounddevice as sd # type: ignore
import soundfile as sf # type: ignore
import os

def voice_rec():
    fs = 48000
    duration = 5

    record = sd.rec(int(duration * fs), samplerate=fs, channels=2)

    sd.wait()

    sf.write("Audio_file.flac", record, fs)

    data, fs = sf.read("Audio_file.flac")
    sd.play(data, fs)
    sd.wait()

    os.unlink("Audio_file.flac")
    print(record.shape)
    plt.plot(record[:, 0], label="Right")
    plt.plot(record[:, 1], label="Left")
    plt.legend()
    plt.show()


voice_rec()
