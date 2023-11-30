#!/usr/bin/env python3
"""Exibe relatorio de crianças por atividade.
Algoritmo para tratar dados, separar dados é utilizado

"""

__version__ = "0.1.0"


sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Isolda", "Maria", "Carlos", "Antonio", "Joao"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aula_sala1 = []
aula_sala2 = []


atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca),
]


for nome_atividade, atividade in atividades:

    print(f"Alunos da ativdade {nome_atividade}\n")
    print("-" * 48)

    

    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("Atividade sala1 ", atividade_sala1)
    print("Atividade sala2 ", atividade_sala2)

    print()
    print("#" * 40)
