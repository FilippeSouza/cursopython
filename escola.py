#!/usr/bin/env python3
"""Exibe relatorio de crianças por atividade.


"""

__version__ = "0.1.0"


sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Isolda", "Maria", "Carlos", "Antonio", "Joao"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aula_ingles_sala1 = []
aula_ingles_sala2 = []
aula_musica_sala1 = []
aula_musica_sala2 = []
aula_danca_sala1 = []
aula_danca_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
       aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
       aula_ingles_sala2.append(aluno)

print("Ingles sala1 ", aula_ingles_sala1)
print("Ingles sala2 ", aula_ingles_sala2)

for aluno in aula_musica:
    if aluno in sala1:
       aula_musica_sala1.append(aluno)
    elif aluno in sala2:
       aula_musica_sala2.append(aluno)

print("Musica sala1 ", aula_musica_sala1)
print("Musica sala2 ", aula_musica_sala2)

for aluno in aula_danca:
    if aluno in sala1:
       aula_danca_sala1.append(aluno)
    elif aluno in sala2:
       aula_danca_sala2.append(aluno)

print("Danca sala1 ", aula_musica_sala1)
print("Danca sala2 ", aula_musica_sala2)
