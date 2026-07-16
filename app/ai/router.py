from app.commands.apps import open_app
from app.commands.browser import browser_command
from app.ai.llm import JarvisLLM

ai = JarvisLLM()


def process(command):

    cmd = command.lower()

    # Browser Commands
    if any(word in cmd for word in ["youtube", "google", "search"]):
        return browser_command(cmd)

    # Desktop Apps
    if any(word in cmd for word in ["chrome", "notepad", "calculator", "paint"]):
        return open_app(cmd)

    # AI Chat
    return ai.ask(command)