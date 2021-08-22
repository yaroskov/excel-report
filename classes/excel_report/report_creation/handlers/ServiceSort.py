from classes.excel_report.report_creation.data.Data import Data


class ServiceSort(Data):
    def __init__(self):
        super(ServiceSort, self).__init__()

    @staticmethod
    def run(source):
        results = []

        curr_service = ""
        for block in source:
            if curr_service != block["service"]:
                curr_service = block["service"]
                new_block = {
                    "service": curr_service,
                    "data": [block]
                }
                results.append(new_block)
            else:
                target_block = results[-1]
                target_block["data"].append(block)

        return results
