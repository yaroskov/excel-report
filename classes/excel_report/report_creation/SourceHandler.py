from classes.excel_report.report_creation.Data import Data
from classes.tools.Tools import Tools
from lxml import etree


class SourceHandler(Data):
    def __init__(self):
        super(SourceHandler, self).__init__()
        #self.settings = Tools.json_load("settings.json")
        #self.results = []
        #self.results_lite = []

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

    def source_handler(self):
        html_doc = Tools.text_file_load(self.set_path("source") + self.set_file("source"))
        doc = etree.HTML(html_doc)

        tasks = []
        for tr in doc.xpath('//table/tr'):
            task = []
            for data in tr.xpath('./td'):
                td_text = data.xpath('./text()')
                star_text = data.xpath('.//*/text()')

                data_el = ""
                if len(td_text) > 0:
                    data_el += td_text[0]
                if len(star_text) > 0:
                    data_el += star_text[0]

                task.append(data_el)

            task_complete = SourceHandler.beauty_formatting(task)
            tasks.append(task_complete)

        tasks.pop(len(tasks) - 1)
        tasks.pop(0)

        return tasks