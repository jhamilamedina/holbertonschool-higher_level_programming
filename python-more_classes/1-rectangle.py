#!/usr/bin/python3
"""Definición de una clase"""


class Rectangle:
    """Representación de la clase"""
    def __init__(self, width=0, height=0):
        """Inicializa el metodo constructor, tiene 2 parametros

        Args:
            widh(int)es el ancho del rectangulo
            height(int) es el alto del rectangulo
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Este metodo retorna el ancho del rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Definimos un metodo llamado width
        Esta propiedad configura el ancho"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Este metodo retorna el alto del rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Definimos un metodo llamado height y configura el alto"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
