class Data:
    def __init__(self, config):
        self.config = config

        self.results = {}
        self.results_light = {}
        self.errors_total_number = 0
        self.affected_services_number = 0
