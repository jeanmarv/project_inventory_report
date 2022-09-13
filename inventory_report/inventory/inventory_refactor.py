from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path_file, type):
        self.data.extend(self.importer.import_data(path_file))
        if type == 'simples':
            return SimpleReport.generate(self.data)

        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
