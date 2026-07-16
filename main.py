from app.voice.speaker import speak
from app.voice.listener import listen
from app.brain.router import process_command


def main():
    speak("Jarvis Activated")

    while True:
        print("\nListening...")

        command = listen()

        if not command:
            continue

        if "exit" in command:
            speak("Goodbye")
            break

        response = process_command(command)
        speak(response)


if __name__ == "__main__":
    main()