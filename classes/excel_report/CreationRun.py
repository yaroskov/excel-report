from classes.excel_report.report_creation.ReportCreator import ReportCreator


class CreationRun(ReportCreator):
    def __init__(self):
        super(CreationRun, self).__init__()
        self.results_info = ""

    def run_with_print_and_write(self):
        self.build_report()
        self.print()
        self.write()

    def results_interface(self):
        self.results_info = "report done with: errors: " + str(self.results_lite["errorsNumber"])
        self.results_info += "; incidents: " + str(self.results_lite["incidentsTotalNumber"])
