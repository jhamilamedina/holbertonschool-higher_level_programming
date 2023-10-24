#!/usr/bin/python3
"""
Define este modulo una función
load_from_json_file para serializar
"""
import json


def load_from_json_file(filename):
    """
    Esta funcion desserializa el contenido del
    archivo en un objeto de python

    Args:
        filename(str): Nombre del fichero donde se
        encuentra los datos a deserializar.
    Return:
        obj: Regresa un objeto de python
    """
    with open(filename, 'r') as fr:
        return json.load(fr)
