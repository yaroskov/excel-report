from classes.data.Data import Data


class AddTasks(Data):
    def __init__(self, config):
        super(AddTasks, self).__init__(config)

    @staticmethod
    def run(error, tasks_list):
        for task in tasks_list:
            if "like" in error:
                check_key = error["like"]
            else:
                check_key = error["exceptionMessage"]

            if check_key in task["description"]:
                error["taskName"] = task["summary"]
                error["taskNumber"] = task["key"]
                break

        return error
