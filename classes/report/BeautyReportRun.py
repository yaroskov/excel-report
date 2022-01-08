from classes.report.creator.BeautyReport import BeautyReport


class ReportRun(BeautyReport):
    def __init__(self, config):
        super(ReportRun, self).__init__(config)

    def run(self):
        self.make()
        self.print()
        self.write()
