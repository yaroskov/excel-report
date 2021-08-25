from classes.excel_report.report_creation.ReportBuilder import ReportBuilder


class CreationRun(ReportBuilder):
    def __init__(self, config):
        super(CreationRun, self).__init__(config)

    def run_fully(self):
        self.run()
        self.handle_results()
