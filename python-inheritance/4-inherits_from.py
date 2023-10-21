#!/usr/bin/python3
"""
Esta funció verifica si el obj es una
instancia de una clase a_class
"""


def inherits_from(obj, a_class):
    """Define una función que toma 2 argumentos
    y verifica si obj es una instancia o subclase
    de a_class
    Args:
        obj (objeto) es el objeto que deseas verificar

    Return:
        Devuelver(bool) True si obj es una instancia de
        la clase a_class de lo contrario False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
