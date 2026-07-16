import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
    source,
    timeout=5,
    phrase_time_limit=6
)

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text.lower()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Internet connection required.")
        return ""