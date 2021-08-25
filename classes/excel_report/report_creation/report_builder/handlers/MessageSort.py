from classes.data.Data import Data
from classes.excel_report.report_creation.report_builder.handlers.LikeFinder import LikeFinder


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
                    cleared_msg = curr_message.replace("\n ", "")
                    new_block = {
                        "message": cleared_msg,
                        "incidentsNumber": 1,
                        "data": [item]
                    }
                    results["errors"].append(new_block)
                    new_light = {
                        "message": cleared_msg,
                        "incidentsNumber": 1
                    }
                    results["light"].append(new_light)
                else:
                    results["errors"][-1]["data"].append(item)
                    results["errors"][-1]["incidentsNumber"] += 1
                    results["light"][-1]["incidentsNumber"] += 1
            whole_data.append(results)

        return whole_data
