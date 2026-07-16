import subprocess


def open_app(command: str):
    command = command.lower()

    if "chrome" in command:
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        return "Opening Chrome"

    elif "notepad" in command or "notebook" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad"

    elif "calculator" in command or "calc" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator"

    elif "paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint"

    return "Application not found."