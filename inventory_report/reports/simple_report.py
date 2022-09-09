from collections import Counter


class SimpleReport:

    def generate(data):
        sort_old = sorted(
           data, key=lambda item: item["data_de_fabricacao"]
        )
        old = sort_old[0]["data_de_fabricacao"]
        sort_close = sorted(
            data, key=lambda item: item["data_de_validade"]
        )
        close = sort_close[0]["data_de_validade"]

        company_counter = [item["nome_da_empresa"] for item in data]
        company = Counter(company_counter).most_common()

        return (
            f"Data de fabricação mais antiga: {old}\n"
            f"Data de validade mais próxima: {close}\n"
            f"Empresa com mais produtos: {company[0][0]}"
        )
