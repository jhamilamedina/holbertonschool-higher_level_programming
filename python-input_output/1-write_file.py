#!/usr/bin/python3
"""
se define la función write_file y
toma 2 parametros
"""


def write_file(filename="", text=""):
    """
    Esta función sobreescribe el contenido
    dle archivo y si no existe lo crea

    Args:
        filename(string): contine el nombre
        o ruta del archivo
        text(string): texto a escribir

    Return:
        int: nro de bytes escritos.
    """
    with open(filename, "w") as f:
        f.write(text)
        return f.tell()
