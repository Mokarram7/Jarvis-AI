class TaskPlanner:

    def plan(self, command):

        command = command.lower()

        tasks = []

        if "chrome" in command:

            tasks.append({
                "action":"open_app",
                "app":"chrome"
            })

        if "youtube" in command:

            tasks.append({
                "action":"youtube"
            })

        if "search" in command:

            query = command

            query = query.replace("search","")

            query = query.replace("google","")

            query = query.replace("chrome","")

            query = query.strip()

            tasks.append({
                "action":"google_search",
                "query":query
            })

        return tasks