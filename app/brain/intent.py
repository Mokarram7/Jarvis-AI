def detect_intent(command: str):

    command = command.lower()

    if "youtube" in command:
        return "youtube"

    elif "google" in command:
        return "google"

    elif "chrome" in command:
        return "chrome"

    elif "notepad" in command or "notebook" in command:
        return "notepad"

    elif "calculator" in command:
        return "calculator"

    elif "time" in command:
        return "time"

    elif "date" in command:
        return "date"

    return "chat"