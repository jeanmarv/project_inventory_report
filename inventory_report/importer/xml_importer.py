import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    def import_data(path_file):
        if ".xml" not in path_file:
            raise ValueError("Arquivo inválido")

        with open(path_file, 'r') as file:
            read_file = file.read()
            file_to_json = xmltodict.parse(read_file)
            data = file_to_json['dataset']['record']

        return data
