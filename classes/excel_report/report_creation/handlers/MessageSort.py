from classes.excel_report.report_creation.data.Data import Data


class MessageSort(Data):
    def __init__(self):
        super(MessageSort, self).__init__()

    @staticmethod
    def sorter(errors_source):
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
                if curr_message != item["body2"]:
                    curr_message = item["body2"]
                    new_block = {
                        "message": curr_message,
                        "incidentsNumber": 1,
                        "data": [item]
                    }
                    results["errors"].append(new_block)
                    new_light = {
                        "message": curr_message,
                        "incidentsNumber": 1
                    }
                    results["light"].append(new_light)
                else:
                    results["errors"][-1]["data"].append(item)
                    results["errors"][-1]["incidentsNumber"] += 1
                    results["light"][-1]["incidentsNumber"] += 1
            whole_data.append(results)

        return whole_data
