#!/usr/bin/python3
"""
Esta función verifica si obj es una instancia
de a_class, o si heredó una instancia de una clase
"""


def is_kind_of_class(obj, a_class):
    """Esta función toma  argumentos y
    verifica si obj es una instancia o subclase de ella

    Args:
        obj (objeto) este es el objeto que deseas verificar

    Return:
        Devuelve (booleano) si obj es una instancia, o instancia
        de la clase que heredó de a_class de lo contrario False
    """
    return isinstance(obj, a_class)
