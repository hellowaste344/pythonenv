import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf


def voice_rec():
    fs = 48000
    duration = 5

    record = sd.rec(int(duration * fs), samplerate=fs, channels=2)

    sd.wait()

    sf.write("Audio_file.flac", record, fs)

    data, fs = sf.read("Audio_file.flac")
    sd.play(data, fs)
    sd.wait()

    print(record.shape)
    plt.plot(record[:, 0], label="Right")
    plt.plot(record[:, 1], label="Left")
    plt.legend()
    plt.show()


voice_rec()
