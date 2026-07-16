import webbrowser


def browser_command(command):

    command = command.lower()

    if "youtube" in command:

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube"

    elif "google" in command:

        webbrowser.open("https://www.google.com")

        return "Opening Google"

    elif "search" in command:

        query = command.replace("search", "").strip()

        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)

        return f"Searching {query}"

    return "Browser command not found."