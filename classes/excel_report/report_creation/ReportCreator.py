from classes.excel_report.report_creation.data.Data import Data
from classes.tools.Tools import Tools
from classes.excel_report.report_creation.handlers.SourceHandler import SourceHandler
from classes.excel_report.report_creation.handlers.ServiceSort import ServiceSort
from classes.excel_report.report_creation.handlers.MessageSort import MessageSort
import copy


class ReportCreator(Data):
    def __init__(self, config):
        super(ReportCreator, self).__init__(config)
        self.results = {}
        self.results_light = {}
        self.errors_total_number = 0
        self.affected_services_number = 0

    def build_report(self):
        source_handler = SourceHandler(self.config)
        self.results = source_handler.source_handler()
        self.results = ServiceSort.run(self.results)
        message_sort = MessageSort(self.config)
        self.results["errorsData"] = message_sort.sorter(self.results["errorsData"])
        self.make_light_version()
        self.prepare_info()

        self.results = Tools.json_view(self.results)
        self.results_light = Tools.json_view(self.results_light)

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(data=self.results, path=self.set_path("results"), prefix="results", extension="json")

    def write_light(self):
        Tools.write_data_to_file(data=self.results_light, path=self.set_path("results"), prefix="results_light",
                                 extension="json")

    def make_light_version(self):
        self.results_light = copy.deepcopy(self.results)
        for item in self.results_light["errorsData"]:
            item.pop("errors", None)

    def prepare_info(self):
        self.errors_total_number = self.results["errorsTotalNumber"]
        self.affected_services_number = self.results["affectedServicesNumber"]

    def complete_info(self):
        print("\nReport done with: " + str(self.errors_total_number) +
              " Incidents in " + str(self.affected_services_number) + " services.")
