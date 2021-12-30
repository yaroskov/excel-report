from classes.data.Data import Data
from classes.tools.Tools import Tools
from classes.clear_msg.ClearMsg import ClearMsg


class AddTasks(Data):
    def __init__(self, config):
        super(AddTasks, self).__init__(config)

    def load_tasks(self):
        return Tools.json_load(self.config.paths["tasks"]["list"])

    def run(self, search_data):
        if search_data:
            tasks_list = self.load_tasks()

            found_tasks = []
            found_for_word = {
                "message": search_data,
                "tasks": []
            }
            for task in tasks_list:
                if search_data in ClearMsg.make_search_data(task["description"]):
                    word_found_in_task = {
                        "key": task["key"],
                        "summary": task["summary"]
                    }
                    found_for_word["tasks"].append(word_found_in_task)

            found_tasks.append(found_for_word)

            return found_tasks
        else:
            return None
