#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10


Tabuada do 1
1
2
3
...
_------


"""
__version__ = "0.1.0"
__author__ = "Filippe"


#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(0, 11))


#iterable (percorriveis)
#print(base)
# para
#para cada numero em numeros:
for numero in numeros:
    print("Tabuadada do 1 ao 10 :", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
#repeticao
