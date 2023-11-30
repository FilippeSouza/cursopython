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


atividades = [aula_ingles, aula_musica,aula_danca]


for atividade in atividades:

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Atividade sala1 ", atividade_sala1)
    print("Atividade sala2 ", atividade_sala2)


