#!/usr/bin/python3
"""
Esta función verifica si el obj
es una instancia de a_class
"""


def is_same_class(obj, a_class):
    """
    Se define esta función que toma 2 argumentos
    y verifica si el tipo de dato es concreto

    Args:
        obj (objeto): es el objeto que deseas verificar

    Return:
        Devuele True(booleano) si obj pertenece al
        tipo de dato a_class, caso contrario False
    """
    return type(obj) == a_class
