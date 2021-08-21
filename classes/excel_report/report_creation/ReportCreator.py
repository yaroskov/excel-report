from classes.excel_report.report_creation.Data import Data
from classes.tools.Tools import Tools
from classes.excel_report.report_creation.SourceHandler import SourceHandler


class ReportCreator(Data):
    def __init__(self):
        super(ReportCreator, self).__init__()
        self.results = []

    def build_report(self):
        source_handler = SourceHandler()
        self.results = source_handler.source_handler()

        self.results = Tools.json_view(self.results)

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(data=self.results, path=self.set_path("results"), prefix="results", extension="json")

    @staticmethod
    def complete_info():
        print("\ndone")
