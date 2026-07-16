import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()