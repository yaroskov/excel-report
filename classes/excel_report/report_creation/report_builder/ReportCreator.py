from classes.excel_report.report_creation.report_builder.data.Data import Data
from classes.tools.Tools import Tools
from classes.excel_report.report_creation.report_builder.handlers.SourceHandler import SourceHandler
from classes.excel_report.report_creation.report_builder.handlers.ServiceSort import ServiceSort
from classes.excel_report.report_creation.report_builder.handlers.MessageSort import MessageSort
import copy


class ReportCreator(Data):
    def __init__(self, config):
        super(ReportCreator, self).__init__(config)

    def handle_source_data(self):
        source_handler = SourceHandler(self.config)
        self.results = source_handler.source_handler()

    def sort_by_service(self):
        self.results = ServiceSort.run(self.results)

    def sort_by_message(self):
        message_sort = MessageSort(self.config)
        self.results["errorsData"] = message_sort.sorter(self.results["errorsData"])

    def make_light_version(self):
        self.results_light = copy.deepcopy(self.results)
        for item in self.results_light["errorsData"]:
            item.pop("errors", None)

    def prepare_info(self):
        self.errors_total_number = self.results["errorsTotalNumber"]
        self.affected_services_number = self.results["affectedServicesNumber"]

    def json_convert(self):
        self.results = Tools.json_view(self.results)
        self.results_light = Tools.json_view(self.results_light)
