from app.brain.task_planner import TaskPlanner


planner = TaskPlanner()


def think(command):

    return planner.plan(command)