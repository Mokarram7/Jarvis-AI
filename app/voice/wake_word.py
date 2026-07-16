from app.voice.speaker import speak


WAKE_WORDS = [
    "jarvis",
    "hey jarvis",
    "hello jarvis"
]


def detect_wake_word(command):

    command = command.lower()

    for word in WAKE_WORDS:
        if word in command:
            speak("Yes Sir")
            return True

    return False