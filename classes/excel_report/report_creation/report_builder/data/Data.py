from classes.tools.Tools import Tools


class Data:
    def __init__(self, config):
        self.settings = Tools.json_load("settings.json")
        self.config = config

        self.results = {}
        self.results_light = {}
        self.errors_total_number = 0
        self.affected_services_number = 0

    # def set_path(self, source):
    #    return self.settings["paths"][source]["path"]

    # def set_file(self, source):
    #    return self.settings["paths"][source]["source"]
