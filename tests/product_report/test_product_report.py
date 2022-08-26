from inventory_report.inventory.product import Product


def test_relatorio_produto():
    data = Product(
        1,
        'Leite',
        'LongaVida',
        '2022-01-01',
        '2022-06-01',
        '123789',
        'Ambiente refrigerado'
    )

    data_repr = data.__repr__()

    expected = (
        "O produto Leite"
        " fabricado em 2022-01-01"
        " por LongaVida com validade"
        " até 2022-06-01"
        " precisa ser armazenado Ambiente refrigerado."
    )

    assert data_repr == expected
