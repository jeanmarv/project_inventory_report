import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(path_file):
        if ".csv" not in path_file:
            raise ValueError("Arquivo inválido")
        with open(path_file, "r") as file:
            data = list(csv.DictReader(file, delimiter=",", quotechar='"'))

        return data
