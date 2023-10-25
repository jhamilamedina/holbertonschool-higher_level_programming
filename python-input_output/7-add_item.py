#!/usr/bin/python3
"""
Este módulo recibe una serie de datso como argumentos,
los agreaga a una losta y los guarda en un fichero (add_item.json)
"""


from sys import argv
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

PATH_FILE_JSON = 'add_item.json'
obj = []

if path.exists(PATH_FILE_JSON):
    obj = load_from_json_file(PATH_FILE_JSON)
save_to_json_file(obj + argv[1:], PATH_FILE_JSON)
