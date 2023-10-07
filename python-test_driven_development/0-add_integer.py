#!/usr/bin/python3
def add_integer(a, b=98):
    """Verifica que a y b sean numeros enteros"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    """Convertir a y b a numeros enteros si son flotantes"""
    a = int(a)
    b = int(b)

    """Calcula y devuelve la suma de a + b"""
    return a + b
