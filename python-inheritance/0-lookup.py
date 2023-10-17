#!/usr/bin/python3

"""Define un una función de busqueda de
    atributos de objeto"""


def lookup(obj):
    """
    Retorna una lista de objeto
    Args:obj
    Retun:list
    """
    return dir(obj)
