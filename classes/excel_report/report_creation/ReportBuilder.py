from classes.excel_report.report_creation.report_builder.ReportCreator import ReportCreator
from classes.excel_report.report_creation.report_builder.ResultsHandler import ResultsHandler


class ReportBuilder(ReportCreator):
    def __init__(self, config):
        super(ReportBuilder, self).__init__(config)
        self.results_handler = None
        self.results_lite_file_name = ""

    def run(self):
        self.handle_source_data()
        self.sort_by_service()
        self.sort_by_message()
        self.make_light_version()
        self.prepare_info()
        self.json_convert()

    def handle_results(self):
        self.results_handler = ResultsHandler(self.config, self)

        self.results_handler.print()
        self.results_handler.write()
        self.results_lite_file_name = self.results_handler.write_light()
        self.results_handler.complete_info()
