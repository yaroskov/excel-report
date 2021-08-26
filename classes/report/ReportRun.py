from classes.report.creator.Report import Report


class ReportRun(Report):
    def __init__(self, config):
        super(ReportRun, self).__init__(config)

    def run(self):
        self.make()
        self.print()
        self.write()
