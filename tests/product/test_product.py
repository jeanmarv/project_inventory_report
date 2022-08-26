from inventory_report.inventory.product import Product


def test_cria_produto():

    data = Product(
        1,
        'Leite',
        'LongaVida',
        '2022-01-01',
        '2022-06-01',
        '123789',
        'Ambiente refrigerado'
    )

    assert data.id == 1
    assert type(data.id) == int
    assert data.nome_do_produto == 'Leite'
    assert type(data.nome_do_produto) == str
    assert data.nome_da_empresa == 'LongaVida'
    assert type(data.nome_da_empresa) == str
    assert data.data_de_fabricacao == '2022-01-01'
    assert type(data.data_de_fabricacao) == str
    assert data.data_de_validade == '2022-06-01'
    assert type(data.data_de_validade) == str
    assert data.numero_de_serie == '123789'
    assert type(data.numero_de_serie) == str
    assert data.instrucoes_de_armazenamento == 'Ambiente refrigerado'
    assert type(data.instrucoes_de_armazenamento) == str
