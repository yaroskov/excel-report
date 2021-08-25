from classes.data.Data import Data
from classes.tools.Tools import Tools
from lxml import etree


class SourceHandler(Data):
    def __init__(self, config):
        super(SourceHandler, self).__init__(config)

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
        html_doc = Tools.text_file_load(self.config.paths["source"])
        doc = etree.HTML(html_doc)

        for br in doc.xpath("*//br"):
            br.tail = "\n" + br.tail if br.tail else "\n"

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
