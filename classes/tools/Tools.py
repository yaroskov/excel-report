import json
import os
from datetime import datetime


class Tools:
    @staticmethod
    def json_view(results):
        results = json.dumps(results, sort_keys=False, indent=4, ensure_ascii=False)
        return results

    @staticmethod
    def json_load(source, path=""):
        with open(path + source, "r", encoding='utf-8') as txtData:
            jsonData = json.load(txtData)
        return jsonData

    @staticmethod
    def text_file_load(source):
        with open(source, "r", encoding="windows-1251") as data:
            text = data.read()
        return text

    @staticmethod
    def write_data_to_file(data, path="", prefix="", extension="json"):
        Tools.make_folders_by_path(path)
        encoded_unicode = data.encode("utf8")
        currDateTime = datetime.now().strftime("%d-%m-%Y_%H.%M.%S")
        a_file = open(path + prefix + "_" + currDateTime + "." + extension, "wb")
        a_file.write(encoded_unicode)

    @staticmethod
    def make_folders_by_path(path):
        folders = path.split("/")
        if len(folders[-1]) < 1:
            del folders[-1]

        new_folders = []
        i = 0
        while i < len(folders):
            new_path = ""
            j = 0
            while j <= i:
                new_path += folders[j]
                new_path += "/"
                j += 1
            new_folders.append(new_path)
            if not os.path.exists(new_path):
                os.mkdir(new_path)
            i += 1
