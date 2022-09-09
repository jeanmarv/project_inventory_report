from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(data):
        companies_stock = ''
        simpReport = SimpleReport.generate(data)
        company_counter = [item["nome_da_empresa"] for item in data]
        company = Counter(company_counter).most_common()
        for key, value in company:
            companies_stock += f"- {key}: {value}\n"

        return (
            f"{simpReport}\n"
            "Produtos estocados por empresa:\n"
            f"{companies_stock}"
        )
