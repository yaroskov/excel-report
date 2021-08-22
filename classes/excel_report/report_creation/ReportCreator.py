from classes.excel_report.report_creation.data.Data import Data
from classes.tools.Tools import Tools
from classes.excel_report.report_creation.handlers.SourceHandler import SourceHandler
from classes.excel_report.report_creation.handlers.ServiceSort import ServiceSort


class ReportCreator(Data):
    def __init__(self):
        super(ReportCreator, self).__init__()
        self.results = []

    def build_report(self):
        source_handler = SourceHandler()
        self.results = source_handler.source_handler()
        self.results = ServiceSort.run(self.results)

        self.results = Tools.json_view(self.results)

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(data=self.results, path=self.set_path("results"), prefix="results", extension="json")

    @staticmethod
    def complete_info():
        print("\ndone")
