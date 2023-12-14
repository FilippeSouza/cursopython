#!/usr/bin/env python3

import os
import sys

# EAFP - easy to ask forgiveness than permission
#é mais facil perdir perdao do que permissao

try:
    names = open("names.txt").readlines()
    1 /   1 
    print(names.banana)
except FileNotFoundError:
    print("[Error] File names.txt not found.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!!")
    sys.exit(1)
except AttributeError:
    print("[Error] List doesn't banana")
    sys.exit(1)

    
try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
