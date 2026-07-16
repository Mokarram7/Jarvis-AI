from app.voice.speaker import speak
from app.voice.listener import listen
from app.ai.memory import Memory
from app.ai.router import process

memory = Memory()

speak("AI Jarvis Started")

while True:

    command = listen()

    if not command:
        continue

    command = command.lower().strip()

    # Exit
    if command == "exit":
        speak("Goodbye!")
        break

    # -----------------------
    # Save Name
    # -----------------------
    if command.startswith("my name is"):

        name = command.replace("my name is", "").strip()

        memory.save("name", name)

        speak(f"Okay {name}, I will remember your name.")

        continue

    # -----------------------
    # Recall Name
    # -----------------------
    if "what is my name" in command:

        name = memory.recall("name")

        if name:
            speak(f"Your name is {name}")
        else:
            speak("I don't know your name yet.")

        continue

    # -----------------------
    # AI + Automation
    # -----------------------
    reply = process(command)

    print(f"Jarvis: {reply}")

    speak(reply)