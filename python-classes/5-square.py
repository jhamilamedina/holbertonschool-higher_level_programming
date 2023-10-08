#!/usr/bin/python3
"""Definiendo una clase Square"""


class Square:
    """Representa la clase square"""
    def __init__(self, size=0):
        """Inicializa el new square y verifica si es entero
        o si es mayor o igual a 0
        Args:
            size(int): es el tamaño del square es igual a 0
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
