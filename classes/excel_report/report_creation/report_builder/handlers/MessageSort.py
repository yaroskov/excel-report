from config import config
from classes.data.Data import Data
from classes.add_tasks.AddTasks import AddTasks
from classes.clear_msg.ClearMsg import ClearMsg


class MessageSort(Data):
    def __init__(self, config):
        super(MessageSort, self).__init__(config)

    def sorter(self, errors_source):
        whole_data = []
        for block in errors_source:

            if self.config.options["useServices"]:
                service = self.service_search(ClearMsg.clear_spaces(block["service"]))
            else:
                service = ClearMsg.clear_spaces(block["service"])

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

            curr_message = "0123456789asdfgesdsgdfgrgdfdsfgdsfhfsdhshsdghsh"
            for item in block["data"]:

                if "errorMessage1" in item:

                    search_data = ClearMsg.make_search_data(item["errorMessage1"], config.unique)
                    if search_data is not None and len(search_data) >= 10:

                        if curr_message != search_data:
                            curr_message = search_data
                            add_tasks = AddTasks(self.config)
                            found_tasks = add_tasks.run(curr_message)

                            cleared_msg = ClearMsg.clear_spaces(item["errorMessage1"])

                            if self.config.options["usePseudo"]:
                                cleared_msg = self.pseudo_search(cleared_msg)
                            else:
                                cleared_msg = "Уникальная ошибка: " + cleared_msg

                            results["errors"].append(MessageSort.new_block_full(cleared_msg, found_tasks, item))
                            results["light"].append(MessageSort.new_block_light(cleared_msg, found_tasks, item["orderStatusId"]))
                        else:
                            results["errors"][-1]["data"].append(item)
                            results["errors"][-1]["incidentsNumber"] += 1
                            results["light"][-1]["incidentsNumber"] += 1

                    else:
                        results["errors"][0]["incidentsNumber"] += 1
                        results["light"][0]["incidentsNumber"] += 1

            whole_data.append(results)

        return whole_data

    def pseudo_search(self, msg):
        target = ""
        for pseudo in self.config.pseudos:
            if pseudo["msg"] in msg:
                target = pseudo["pseudo"]
                break
            else:
                target = "Уникальная ошибка: " + msg

        return target

    def service_search(self, msg):
        target = ""
        for service in self.config.services:
            if service["msg"] in msg:
                target = f"{msg} ({service['service']})"
                break
            else:
                target = msg

        return target

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
