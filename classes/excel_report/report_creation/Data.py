from classes.tools.Tools import Tools
from lxml import etree


class Data:
    def __init__(self):
        self.settings = Tools.json_load("settings.json")
        #self.results = []
        #self.results_lite = []

    def set_path(self, source):
        return self.settings["paths"][source]["path"]

    def set_file(self, source):
        return self.settings["paths"][source]["source"]
