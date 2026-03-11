import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 300
r.pause_threshold = 1.5

with sr.Microphone() as source:
    print("Say sth\n")
    audio_text = r.listen(source)
    print("thanks")

    try:
        print("text: ", r.recognize_google(audio_text))
    except Exception as exc:
        print(f"Sorry, I did not get that {exc}")
        pass
