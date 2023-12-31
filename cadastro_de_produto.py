#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {#usamos dicionario
    "nome": "Caneta",
    "cores": ["azul", "branco"], #usamos listas
    "preco": 3.23,
    "dimensao": {#dentro de dicionarios
        "altura": 12.1,
        "largura": 0.8,
        #itens declarados com tipos diferentes
    },
    "em_estoque": True,
    "codigo": 4578,
    "codebar": None,
}

cliente = {
    "nome": "Bruno"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]#operacoes fora do print primeiro acessa o produto depois a chave


print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
