from classes.tools.Tools import Tools


class Data:
    def __init__(self):
        self.settings = Tools.json_load("settings.json")
        self.results = []
        self.results_lite = []

    @staticmethod
    def beauty_formatting(task):
        columns = [
            "service",
            "context",
            "startDate",
            "statusDate",
            "orderId",
            "orderStatusId",
            "statusText",
            "action",
            "state",
            "body1",
            "body2",
            "body3",
            "body4",
            "errorMessage1",
            "errorMessage2",
            "errorMessage3"
        ]

        task_complete = {}
        i = 0
        for el in columns:
            if len(task) > i:
                task_complete[el] = task[i]
            i += 1

        return task_complete

    def set_path(self, source):
        return self.settings["paths"][source]["path"]

    def set_file(self, source):
        return self.settings["paths"][source]["source"]
