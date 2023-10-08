#!/usr/bin/python3
def safe_print_integer(value):

    try:
        print("{:d}".format(value))  # si imprime un valor entero
        return True  # Devulve tru si la impresión se realiza correctamente

    except (ValueError, TypeError):
        return False  # falso cunado hay un error o el valor no es un entero
