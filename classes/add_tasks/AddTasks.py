from config import config
from classes.data.Data import Data
from classes.tools.Tools import Tools
from classes.dictionaries.Dictionaries import Dictionaries


class AddTasks(Data):
    def __init__(self, config):
        super(AddTasks, self).__init__(config)

    def load_tasks(self):
        return Tools.json_load(self.config.paths["tasks"]["list"])

    def run(self, dict_results):
        if dict_results:
            tasks = []
            tasks_list = self.load_tasks()
            for task in tasks_list:
                cleared_task = Dictionaries.remove_stack_trace(task["description"])
                cleared_task = Dictionaries.clear_spaces(cleared_task)

                result = True
                for string in dict_results["target"]:
                    if string not in cleared_task:
                        result = False
                        break

                if result is True:
                    word_found_in_task = {
                        "key": task["key"],
                        "summary": task["summary"]
                    }
                    tasks.append(word_found_in_task)

            return tasks
        else:
            return False
