from classes.tools.func.Time import Time
from classes.tools.func.MakeFolders import MakeFolders


class WriteToFile:
    @staticmethod
    def run(data, path="", prefix="", extension="json"):
        MakeFolders.mkdir(path)
        encoded_unicode = data.encode("utf8")
        file_name = path + prefix + "_" + Time.now() + "." + extension
        a_file = open(file_name, "wb")
        a_file.write(encoded_unicode)

        return file_name

