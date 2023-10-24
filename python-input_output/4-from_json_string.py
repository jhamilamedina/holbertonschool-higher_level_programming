#!/usr/bin/python3
"""
Define este modulo una funcion
from_json_string para serializar un objeto
"""
import json


def from_json_string(my_str):
    """
    Serializa o convierte un objeto de python
    a formato json

    Args:
        my_str (str):Es el objeto a serializar

    Return:
        str: Regresa representado por una cadena(string)
        a formato json
    """
    return json.loads(my_str)
