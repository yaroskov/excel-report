from classes.make_tasks.func.MakeTasks import MakeTasks


class MakeTasksRun(MakeTasks):
    def __init__(self, config):
        super(MakeTasks, self).__init__(config)

    def run(self):
        self.make_tasks()
        self.print()
        self.write()
