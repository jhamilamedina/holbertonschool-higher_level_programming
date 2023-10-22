#!/usr/bin/python3
"""
Definimos una clase Square que herede
de la clase Rectangle
"""


"""Importa la clase Rectangle del modulo 9-rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsentación de la clase"""
    def __init__(self, size):
        """Define el metodo init e inicializa
        sus atributos

        Args:
            size(int): tamaño del Square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Esta función calcula el area del cuadrado
        Return:
            int: size ** 2
        """
        return self.__size ** 2

    def __str__(self):
        """Este metodo dvuelve una cadena de texo de la clase

        Return:
            string: Representación informal del rectangulo
        """
        return f"[Square] {self.__size}/{self.__size}"
