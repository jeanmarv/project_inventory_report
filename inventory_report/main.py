import sys
from inventory_report.inventory.inventory import Inventory


def main():
    if len(sys.argv) != 3:
        return sys.stderr.write('Verifique os argumentos\n')
    data = Inventory.import_data(sys.argv[1], sys.argv[2])
    return sys.stdout.write(data)
