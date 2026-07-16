from app.brain.brain import think
from app.brain.executor import TaskExecutor

executor = TaskExecutor()


def process_command(command):

    tasks = think(command)

    responses = executor.execute(tasks)

    if responses:
        return ". ".join(responses)

    return "Sorry, I couldn't execute the command."