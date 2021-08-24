from classes.tools.Tools import Tools


class Data:
    def __init__(self, config):
        self.settings = Tools.json_load("settings.json")
        self.config = config

    def set_path(self, source):
        return self.settings["paths"][source]["path"]

    def set_file(self, source):
        return self.settings["paths"][source]["source"]
