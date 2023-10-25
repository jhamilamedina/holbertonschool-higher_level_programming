#!/usr/bin/python3
"""
Este módulo define la función class_to_json,
obtiene un diccionario con los atributos del objeto pasado.
"""


def class_to_json(obj):
    """
    Esta función usa el atributo __dict__
    para retornar un diccionario con los atributos de la instancia.

    Args:
        obj (object):Un instancia de clase.
    Returns:
        dict: Regresa un diccionario con los atributos
        de la instancia de clase recibida.
    Nota:
        También se puede la función vars() para regresar un diccionario
        obj.__dict__
    """
    return vars(obj)
