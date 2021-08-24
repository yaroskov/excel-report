from classes.excel_report.report_creation.data.Data import Data
from classes.excel_report.report_creation.handlers.LikeFinder import LikeFinder


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

                """likes = [
                    "ru.gosuslugi.pgu.core.processing.exception.NoResponseException: Couldn't\n  load response by link:\n  terrabyte:",
                    "ru.atc.carcass.common.exception.FaultException: Client error while calling\n  esia oss, orderId =",
                    "statusCode = 400, statusText = , body =\n  {\"reason\":\"ERROR: duplicate key value violates unique\n  constraint \\\"claim_oph_unq",
                    "QuSDQpNC10LTQtdGA0LDRhtC40LgwZjAfBggqhQMHAQEBATATBgcqhQMCAiQABggqhQMHAQECAgNDAARASUEeWLJAKYh4Pvb6LGw4Kask5cxFkwNQ25EOy6X9hOw0xeOouk09PN6MgsfE",
                    "ru.gosuslugi.pgu.core.processing.exception.ProcessingServiceException:\n  FAULTProcessing for messageId=ID:"
                ]"""

                likes = LikeFinder(self.config)
                like = likes.run(curr_message)

                if curr_message != item["body2"] and not like:
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
