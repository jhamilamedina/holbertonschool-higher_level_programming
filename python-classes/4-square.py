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
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size
