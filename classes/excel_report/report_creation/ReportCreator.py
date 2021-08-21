from classes.excel_report.report_creation.Data import Data
from classes.tools.Tools import Tools
from lxml import etree


class ReportCreator(Data):
    def __init__(self):
        super(ReportCreator, self).__init__()

    def build_report(self):
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

            task_complete = Data.beauty_formatting(task)
            tasks.append(task_complete)

        tasks.pop(len(tasks) - 1)
        tasks.pop(0)

        tasks = Tools.json_view(tasks)
        self.results = tasks

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(data=self.results, path=self.set_path("results"), prefix="results", extension="json")
