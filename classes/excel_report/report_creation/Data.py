#from datetime import datetime
from classes.tools.Tools import Tools


class Data:
    def __init__(self):
        self.settings = Tools.json_load("settings.json")
        self.results = []
        self.results_lite = []

    """def curr_item(self, item):
        curr_item = {'name': item['name']}
        int_unix_time = int(item['startTime']) / 1000
        curr_item['startTime'] = datetime.fromtimestamp(int_unix_time).strftime('%Y-%m-%d %H:%M:%S')
        curr_item["URI"] = self.set_path_relative("dynotraceURI") + item["callURI"] + ";gf=all"
        curr_item["errorsData"] = item["errorsData"]
        curr_item["requestAttributeData"] = item["requestAttributeData"]

        return curr_item"""

    def set_path(self, source):
        return self.settings["paths"][source]["path"]

    #def set_path_relative(self, source):
    #    return self.settings["sources"][source]["path"]

    def set_file(self, source):
        return self.settings["paths"][source]["source"]

    #def print_results(self, data):
    #    if self.settings["options"]["printData"]:
    #        print(data)

    #def write_results(self, data, path, prefix, extension):
    #    if self.settings["options"]["writeData"]:
    #        Tools.write_data_to_file(data=data, path=path, prefix=prefix, extension=extension)
