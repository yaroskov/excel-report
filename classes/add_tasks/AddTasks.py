from classes.data.Data import Data
from classes.tools.Tools import Tools


class AddTasks(Data):
    def __init__(self, config):
        super(AddTasks, self).__init__(config)

    def load_tasks(self):
        return Tools.json_load(self.config.paths["tasks"]["list"])

    def run(self, search_data):
        if search_data:
            tasks_list = self.load_tasks()

            found_tasks = []
            for word in search_data:
                found_for_word = {
                    "message": word,
                    "tasks": []
                }
                for task in tasks_list:
                    if word in task["description"]:
                        word_found_in_task = {
                            "key": task["key"],
                            "summary": task["summary"]
                        }
                        found_for_word["tasks"].append(word_found_in_task)

                found_tasks.append(found_for_word)

            return found_tasks
        else:
            return None
