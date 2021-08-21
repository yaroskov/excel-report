from classes.excel_report.report_creation.ReportCreator import ReportCreator


class CreationRun(ReportCreator):
    def __init__(self):
        super(CreationRun, self).__init__()
        self.results_info = ""

    def run_with_print_and_write(self):
        self.build_report()
        self.print()
        self.write()
        ReportCreator.complete_info()
