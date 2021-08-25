from classes.data.Data import Data
from classes.tools.Tools import Tools
from bs4 import BeautifulSoup


class MakeTasks(Data):
    def __init__(self, config):
        super(MakeTasks, self).__init__(config)
        self.tasks = []

    def make_tasks(self):
        html_doc = Tools.text_file_load(self.config.paths["tasks"]["source"])
        html_data = BeautifulSoup(html_doc, 'html.parser')
        tbody = html_data.tbody
        rows = tbody.find_all("tr", {"class": "issuerow"})

        tasks = []
        for row in rows:
            task = {"key": row.find("a", {"class": "issue-link"}).text}
            summary = row.find("td", {"class": "summary"}).text
            task["summary"] = " ".join(summary.split())
            task["description"] = row.find("td", {"class": "description"}).text
            tasks.append(task)

        tasks = Tools.json_view(tasks)
        self.tasks = tasks

    def print(self):
        print(self.tasks)

    def write(self):
        Tools.write_data_to_file(data=self.tasks,
                                 path=self.config.paths["tasks"]["results"],
                                 prefix="tasks",
                                 extension="json")
