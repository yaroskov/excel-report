from classes.tools.func.WriteToFile import WriteToFile
from classes.tools.func.Text import Text


class Tools:
    @staticmethod
    def json_view(results):
        return Text.json_view(results)

    @staticmethod
    def json_load(source, path=""):
        return Text.json_load(source, path)

    @staticmethod
    def text_file_load(source):
        return Text.text_file_load(source)

    @staticmethod
    def write_data_to_file(data, path="", prefix="", extension="json"):
        WriteToFile.run(data, path, prefix, extension)
