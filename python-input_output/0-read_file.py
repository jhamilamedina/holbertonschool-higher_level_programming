#!/usr/bin/python3
"""Definimos una función read_file"""


def read_file(filename=""):
    """Usamos el open para abrir el archivo"""
    with open(filename) as m:
        txt = m.read()
        print(txt)
