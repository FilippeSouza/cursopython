#!/sur/bin/env python3


import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("operacao")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Numero de argumentos invalidos")
    print("ex: 'sum 5 5'")
    sys.exit(1)#entrada de erro para o pront entender o erro

operation, *nums = arguments


valid_operations = ("sum", "sub", "mul", 'div')
if operation not in valid_operations:
    print("Operacao invalida")
    print(valid_operations)
    sys.exit(1)
