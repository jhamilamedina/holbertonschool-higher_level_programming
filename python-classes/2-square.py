#!/usr/bin/python3
"""Definición de ua clase Square"""


class Square:
    """Representa la clase Square"""
    def __init__(self, size=0):
        """Inicializa el new Square y verifica si size es numero int
        y si es mayor o igual a 0
        Args:
            size(int): y es el tamaño de Square es 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
