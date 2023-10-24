#!/usr/bin/python3
"""
Define este modulo una función
save_to_json_file para serializar
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Esta funcion serializa o convierte un objeto de python
    a formato json y lo guarda en un fichero

    Args:
        my_obj(objeto): Objeto a serializar
        filename(str): ruta del proyecto
    """
    with open(filename, 'w') as fe:
        json.dump(my_obj, fe)
