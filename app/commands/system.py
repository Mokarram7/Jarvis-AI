from datetime import datetime


def system_command(command):

    if "time" in command:

        now = datetime.now().strftime("%I:%M %p")

        return f"The time is {now}"

    elif "date" in command:

        today = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {today}"

    return "System command not found."