from app.commands.apps import open_app
from app.commands.browser import browser_command
from app.commands.system import system_command


class TaskExecutor:

    def execute(self, tasks):

        responses = []

        for task in tasks:

            action = task["action"]

            if action == "open_app":
                responses.append(open_app(task["app"]))

            elif action == "youtube":
                responses.append(browser_command("youtube"))

            elif action == "google_search":
                responses.append(
                    browser_command(
                        f"search {task['query']}"
                    )
                )

            elif action == "time":
                responses.append(system_command("time"))

            elif action == "date":
                responses.append(system_command("date"))

        return responses