from config import config
from classes.data.Data import Data
from classes.add_tasks.AddTasks import AddTasks
from classes.dictionaries.Dictionaries import Dictionaries


class MessageSort(Data):
    def __init__(self, config):
        super(MessageSort, self).__init__(config)

    def sorter(self, errors_source):
        whole_data = []
        for block in errors_source:

            if self.config.options["useServices"]:
                service = Dictionaries.service_search(block["service"], config.services)
            else:
                service = Dictionaries.clear_spaces(block["service"])

            results = {
                "service": service,
                "incidentsNumber": block["incidentsNumber"],
                "errors": [],
                "light": []
            }

            block["data"] = sorted(block["data"],
                                   key=lambda item: ("errorMessage1" not in item, item.get("errorMessage1", "")))

            results["errors"].append(MessageSort.new_block_light("Без сообщения", [], 666))
            results["errors"][0]["incidentsNumber"] = 0
            results["light"].append(MessageSort.new_block_light("Без сообщения", [], 666))
            results["light"][0]["incidentsNumber"] = 0

            clear_data = []
            for item in block["data"]:

                if "errorMessage1" in item:
                    source_msg = Dictionaries.remove_stack_trace(item["errorMessage1"])
                    source_msg = Dictionaries.clear_spaces(source_msg)

                    if source_msg is not None and len(source_msg) >= 10:
                        item["sourceMsg"] = source_msg

                        if self.config.options["useDict"]:
                            dict_results = Dictionaries.dictionary_check(source_msg, config.unique)
                        else:
                            dict_results = {}

                        item["dictResults"] = dict_results
                        clear_data.append(item)
                    else:
                        results["errors"][0]["incidentsNumber"] += 1
                        results["light"][0]["incidentsNumber"] += 1
                else:
                    results["errors"][0]["incidentsNumber"] += 1
                    results["light"][0]["incidentsNumber"] += 1

            clear_data = sorted(clear_data,
                                key=lambda element: ("pseudo" not in element["dictResults"],
                                                     element["dictResults"].get("pseudo", "")))

            results = self.counter(results, clear_data)

            whole_data.append(results)

        return whole_data

    def counter(self, results, clear_data):
        curr_msg = "0123456789asdfgesdsgdfgrgdfdsfgdsfhfsdhshsdghsh"

        for item in clear_data:
            if len(item["dictResults"]) > 0:
                compare_str = item["dictResults"]["pseudo"]
            else:
                compare_str = item["sourceMsg"]

            if curr_msg != compare_str:
                curr_msg = compare_str

                if self.config.options["useDict"] and item["dictResults"]:
                    add_tasks = AddTasks(self.config)
                    found_tasks = add_tasks.run(item["dictResults"])
                else:
                    found_tasks = []

                if len(item["dictResults"]) > 0:
                    report_msg = item["dictResults"]["pseudo"]
                else:
                    report_msg = "Уникальная ошибка: " + item["sourceMsg"]

                results["errors"].append(MessageSort.new_block_full(report_msg, found_tasks, item))
                results["light"].append(MessageSort.new_block_light(report_msg, found_tasks, item["orderStatusId"]))
            else:
                results["errors"][-1]["data"].append(item)
                results["errors"][-1]["incidentsNumber"] += 1
                results["light"][-1]["incidentsNumber"] += 1

        return results

    @staticmethod
    def new_block_light(cleared_msg, found_tasks, state):
        block = {
            "state": state,
            "message": cleared_msg,
            "incidentsNumber": 1,
            "foundTasks": found_tasks
        }
        return block

    @staticmethod
    def new_block_full(cleared_msg, found_tasks, item):
        block = MessageSort.new_block_light(cleared_msg, found_tasks, item["orderStatusId"])
        block["data"] = [item]
        return block
