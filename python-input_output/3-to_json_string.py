#!/usr/bin/python3
"""
Define este modulo una función
to_json_string para serializar un objeto
"""
import json


def to_json_string(my_obj):
    """
    Serializa o convierte un objeto de python
    a formato json

    Args:
        obj(objeto):Es el objeto a serializar

    Return:
        str: regresa un string a formato json
    """
    return json.dumps(my_obj)
