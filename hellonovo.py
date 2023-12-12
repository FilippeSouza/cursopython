#!/usr/bin/python/env python
"""Hello world mult linguas.
teste
Desta forma vira documentação do programa.
boas praticas colocar em ingles fica compartivel com o mercado e etc.
How to use:

Have the varavel lang previsiou config exempla:

    export LANG=pt_BR

Execution

    python3 hello.py
    or
    ./hello.py
"""

__version__ = "0.1.2"
__author__ = "Filipe"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalide Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, mondo",
    "es_ES": "Hola, Mundo",
    "fr_FR": "bonjou, monde",
}

print(
    msg[current_language] * int(arguments["count"])
)
