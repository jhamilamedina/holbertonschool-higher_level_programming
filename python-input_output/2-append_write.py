#!/usr/bin/python3
"""
Definimos una función append_write
y toma 2 parametros
"""


def append_write(filename="", text=""):
    """
    Esta función agrega una cadena y devuelve
    la cantidad de caracteres agregados

    Args:
        filename(string): contiene el nombre
        o ruta del archivo
        text(string): texto a escribir o agregar

        Return:
            int: cantidad de caracteres escritos
    """
    with open(filename, 'a', encoding='utf-8') as al:
        return al.write(text)
