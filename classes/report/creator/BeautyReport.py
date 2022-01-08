from classes.tools.Tools import Tools
from classes.data.Data import Data


class BeautyReport(Data):
    def __init__(self, config):
        super(BeautyReport, self).__init__(config)
        self.results = ""
        self.raw = {}

    def load_raw_report(self):
        self.raw = Tools.json_load(self.config.paths["results"]["ready"])

    def make(self):
        self.load_raw_report()

        results = '\n<!DOCTYPE html>'
        results += '\n<html lang="en">'
        results += '\n<head>'
        results += '\n<meta charset="UTF-8">'
        results += '\n<title>Excel Report</title>'
        results += '\n</head>'
        results += '\n<body>'
        results += '\n<div id="header"></div>'
        results += '\n<div id="content">'
        results += '\n'
        results += f'\n<h3>Отчёт за {Tools.time_now("%d.%m.%Y")} составлен на основании трёх отчётов:</h3>'
        results += '\n<ul>'
        results += '\n<li>Ошибки в услугах;</li>'
        results += '\n<li>Отчёт по статусам “отказ”;</li>'
        results += '\n<li>Анализ Dynatrace.</li>'
        results += '\n</ul>'
        results += '\n'
        results += f'\n<p>Статистика выведена за {Tools.now_minus_days("%d.%m.%Y")}.</p>'
        results += '\n'
        results += '\n<ol type="I">'
        results += '\n<li>'
        results += '\nОшибки по новым услугам:'

        for service in self.raw["errorsData"]:
            results += '\n<ol>'
            results += '\n<li>'
            results += f'\n{service["service"]}:'
            results += '\n<ul>'

            for error in service["light"]:
                task_msg = ''
                if error["foundTasks"] and len(error["foundTasks"]) > 0 \
                        and error['foundTasks'][0]['tasks'] and len(error['foundTasks'][0]['tasks']) > 0:
                    task_key = error["foundTasks"][0]["tasks"][0]["key"]
                    task_msg = f' - <a href="https://jira.egovdev.ru/browse/{task_key}">{task_key}</a>'

                results += '\n<li style="margin-bottom: 10px">'

                if error["state"] == 666:
                    state = ""
                else:
                    state = f'ID {error["state"]} - '

                results += f'\n{state}<span style="font-style:italic">{error["message"]}</span> - {error["incidentsNumber"]} шт.{task_msg};'
                results += '\n</li>'

            results += '\n</ul>'
            results += '\n</li>'
            results += '\n</ol>'

        results += '\n</li>'
        results += '\n</ol>'
        results += '\n'
        results += '\n</div>'
        results += '\n<div id="bottom"></div>'
        results += '\n</body>'
        results += '\n</html>'
        results += '\n'

        self.results = results

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(self.results, self.config.paths["report"], "report", "html")
