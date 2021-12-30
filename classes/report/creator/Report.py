from classes.tools.Tools import Tools
from classes.data.Data import Data


class Report(Data):
    def __init__(self, config):
        super(Report, self).__init__(config)
        self.results = ""
        self.raw = {}

    def load_raw_report(self):
        self.raw = Tools.json_load(self.config.paths["results"]["ready"])

    def make(self):
        self.load_raw_report()

        results = f"Отчет от {Tools.time_now('%d.%m.%Y')} г."
        results += "\n"
        results += "\nВ ходе анализа были получены следующие результаты:"
        results += f"\nВсего инцидентов {self.raw['errorsTotalNumber']} шт. обнаружено в {self.raw['affectedServicesNumber']} услугах."
        results += "\n"

        i = 0
        for service in self.raw["errorsData"]:
            i += 1
            results += f"\n{i}. {service['service']}"
            results += "\n"
            results += f"\n\tКОЛИЧЕСТВО ИНЦИДЕНТОВ В УСЛУГЕ: {service['incidentsNumber']}"
            results += "\n"
            j = 0
            for error in service["light"]:
                j += 1
                results += f"\n\t{j}) {error['message']}"
                results += f"\n\tКоличество: ~{error['incidentsNumber']} шт."

                if error["foundTasks"] and len(error["foundTasks"]) > 0:
                    if error['foundTasks'][0]['tasks'] and len(error['foundTasks'][0]['tasks']) > 0:
                        results += f"\n\tЗадача: {error['foundTasks'][0]['tasks'][0]['key']}"
                        results += f" {error['foundTasks'][0]['tasks'][0]['summary']}"

                    results += "\n"

                else:
                    results += "\n"

        self.results = results

    def print(self):
        print(self.results)

    def write(self):
        Tools.write_data_to_file(self.results, self.config.paths["report"], "report", "txt")

    def test(self):
        results = "Отчет от 33.07.2077 г."
        results += "\n"
        results += "\nОтчет составлен по данныим от 33.07.2077 г."
        results += "\nВ ходе анализа были выявлены следующие проблемы:"
        results += "\n"
        results += "\nУСЛУГИ:"
        results += "\n"
        results += "\n1. Супер мега услуга."
        results += "\n"
        results += "\n\tОШИБКИ:"
        results += "\n"
        results += "\n\t1) Ошибка 666."
        results += "\n\tКол-во: ~666 шт.; Задача: DEVIL-666"
        results += "\n"
        results += "\n\t\tBEGINNING OF TASKS LIST TO DELETE ----------------------------------------------"
        results += "\n\t\t\tMESSAGE: sdfsdfsdfdsgdfgdsfgdsffsdhfdhsdfhdsfhdfhsdfhfdhs"
        results += "\n\t\t\t\tTASK: DEVIL-613541"
        results += "\n\t\t\tMESSAGE: sdfsdfsdfdsgdfgdsfgdsffsdhfdhsdfhdsfhdfhsdfhfdhs"
        results += "\n\t\t\t\tTASK: DEVIL-613541"
        results += "\n\t\tENDING OF TASKS LIST TO DELETE -------------------------------------------------"
        results += "\n"
        results += "\n\t2) Ошибка супер мега черта Владимира и пророка его Вячеслава: ~13 шт."
        results += "\n\tКол-во: ~13 шт.; Задача: DEVIL-99"
        results += "\n"
        results += "\n\t\tBEGINNING OF TASKS LIST TO DELETE ----------------------------------------------"
        results += "\n\t\t\tMESSAGE: sdfsdfsdfdsgdfgdsfgdsffsdhfdhsdfhdsfhdfhsdfhfdhs"
        results += "\n\t\t\t\tTASK: DEVIL-613541"
        results += "\n\t\t\tMESSAGE: sdfsdfsdfdsgdfgdsfgdsffsdhfdhsdfhdsfhdfhsdfhfdhs"
        results += "\n\t\t\t\tTASK: DEVIL-613541"
        results += "\n\t\tENDING OF TASKS LIST TO DELETE -------------------------------------------------"

        self.results = results
