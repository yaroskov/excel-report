from datetime import datetime


class Time:
    @staticmethod
    def now():
        return datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
