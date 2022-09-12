import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(path_file):
        if ".json" not in path_file:
            raise ValueError("Arquivo inválido")
        with open(path_file, "r") as file:
            data = json.load(file)

        return data
