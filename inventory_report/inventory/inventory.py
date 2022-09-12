from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def read(file_path):
        if "csv" in file_path:
            return CsvImporter.import_data(file_path)
        if "json" in file_path:
            return JsonImporter.import_data(file_path)
        if "xml" in file_path:
            return XmlImporter.import_data(file_path)

    def import_data(file_path, simp_compl):
        data = Inventory.read(file_path)

        if simp_compl == "simples":
            return SimpleReport.generate(data)
        if simp_compl == "completo":
            return CompleteReport.generate(data)
