from classes.data.Data import Data
from classes.excel_report.report_creation.report_builder.handlers.LikeFinder import LikeFinder
import re


class MessageSort(Data):
    def __init__(self, config):
        super(MessageSort, self).__init__(config)

    def sorter(self, errors_source):
        whole_data = []
        for block in errors_source:
            results = {
                "service": block["service"],
                "incidentsNumber": block["incidentsNumber"],
                "errors": [],
                "light": []
            }
            block["data"] = sorted(block["data"], key=lambda item: item["body2"])
            curr_message = "666"
            for item in block["data"]:

                likes = LikeFinder(self.config)
                like = likes.run(curr_message)

                if curr_message != item["body2"] and not like:
                    curr_message = item["body2"]
                    cleared_msg = MessageSort.clear_msg(curr_message)
                    search_data = MessageSort.search_data(cleared_msg)
                    results["errors"].append(MessageSort.new_block_full(cleared_msg, search_data, item))
                    results["light"].append(MessageSort.new_block_light(cleared_msg, search_data))
                else:
                    results["errors"][-1]["data"].append(item)
                    results["errors"][-1]["incidentsNumber"] += 1
                    results["light"][-1]["incidentsNumber"] += 1
            whole_data.append(results)

        return whole_data

    @staticmethod
    def new_block_light(cleared_msg, search_data):
        block = {
            "message": cleared_msg,
            "incidentsNumber": 1,
            "searchData": search_data
        }
        return block

    @staticmethod
    def new_block_full(cleared_msg, search_data, item):
        block = MessageSort.new_block_light(cleared_msg, search_data)
        block["data"] = [item]
        return block

    @staticmethod
    def clear_msg(curr_message):
        return curr_message.replace("\n ", "")

    @staticmethod
    def search_data(cleared_msg):
        search_data = re.split(":|=", cleared_msg)
        search_data.append(cleared_msg)
        return search_data
