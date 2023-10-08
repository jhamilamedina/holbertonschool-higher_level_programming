#!/usr/bin/python3
"""Definición de una clase"""


class Square:
    """Represnta la clase Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el new square y si es entero, mayor
        o igual a 0
        Args:
            size(int): es el tamaño del square es igual a 0
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tupla) or len(value) != 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        x, y = self.__position
        for _ in range(y):
            print()

        for _ in range(self.size):
            print(" " * x + "#" * self.__size)
