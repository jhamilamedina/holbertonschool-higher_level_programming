#!/usr/bin/python3
"""Definición de una clase"""


class Rectangle:
    """Representación de la clase"""
    def __init__(self, width=0, height=0):
        """
        Inicializa el metodo constructor, tiene 2 parametros

        Args:
            width(int)es el ancho del rectangulo
            height(int) es el alto del rectangulo
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Este atributo retorna el ancho del rectangle

        Return:
            int: retorna el ancho(height)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Definimos un metodo llamado width
        Args:
            value(int): este valor configura el ancho del rectangulo
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Este atributo retorna el alto del rectangle

        Return:
            int: Retorna el alto(hight)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Definimos un atributo configura el valor(height)

        Args:
            value(int): Este valor configura el alto del rectangulo
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Este metodo retorna el área de un rectangulo

        Return:
            int:alto * ancho
        """
        return self.__height * self.__width

    def perimeter(self):
        """Este metodo retorna el perimetro del rectangulo
        si el alto o el ancho == 0 retornará 0

        Return:
            int: alto * 2 + ancho * 2
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Este metodo representa un string de rectangulo
        Return:
            str: regresa el rectangulo con el #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            a = self.__height + 1
            b = self.__width
            str_repr = ''.join([f"{'#' * b}\n" for i in range(a) if i])
            return str_repr[:len(str_repr) - 1]

    def __repr__(self):
        """
        Este metodo regresa la resentación del rectangulo
        Return:
            string: cadena que representa al rectangulo
        """
        return f"Rectangle({self.__width}, {self.__height})"
