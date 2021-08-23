from classes.excel_report.report_creation.data.Data import Data


class ServiceSort(Data):
    def __init__(self):
        super(ServiceSort, self).__init__()

    @staticmethod
    def run(source):
        report = {
            "errorsTotalNumber": len(source),
            "affectedServicesNumber": 0,
            "errorsData": []
        }

        curr_service = ""
        for block in source:
            if curr_service != block["service"]:
                report["affectedServicesNumber"] += 1
                curr_service = block["service"]
                report["errorsData"].append(ServiceSort.new_block_full(curr_service, block))
            else:
                report["errorsData"][-1]["data"].append(block)
                report["errorsData"][-1]["incidentsNumber"] += 1

        return report

    @staticmethod
    def new_block_full(curr_service, block):
        new_block = {
            "service": curr_service,
            "incidentsNumber": 1,
            "data": [block]
        }
        return new_block
