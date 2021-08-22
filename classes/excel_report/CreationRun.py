from classes.excel_report.report_creation.ReportCreator import ReportCreator


class CreationRun(ReportCreator):
    def __init__(self):
        super(CreationRun, self).__init__()

    def run_with_print_and_write(self):
        self.build_report()
        self.print()
        self.write()
        self.write_light()
        self.complete_info()
