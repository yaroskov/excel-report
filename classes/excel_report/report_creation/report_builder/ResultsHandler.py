from classes.excel_report.report_creation.report_builder.data.Data import Data
from classes.tools.Tools import Tools
import copy


class ResultsHandler(Data):
    def __init__(self, config, data):
        super(ResultsHandler, self).__init__(config=config)
        self.results = data.results
        self.results_light = data.results_light
        self.errors_total_number = data.errors_total_number
        self.affected_services_number = data.affected_services_number

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(data=self.results,
                                 path=self.config.paths["results_full"],
                                 prefix="results_full")

    def write_light(self):
        Tools.write_data_to_file(data=self.results_light,
                                 path=self.config.paths["results_light"],
                                 prefix="results_light")

    def make_light_version(self):
        self.results_light = copy.deepcopy(self.results)
        for item in self.results_light["errorsData"]:
            item.pop("errors", None)

    def complete_info(self):
        print("\nReport done with: " + str(self.errors_total_number) +
              " Incidents in " + str(self.affected_services_number) + " services.")
