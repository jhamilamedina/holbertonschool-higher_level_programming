#!/usr/bin/python3
"""
Definimos una clase Rectangle que hereda
de la clase BaseGeometry
"""


"""Importa la clase BaseGeometry del modulo 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Representación de la clase"""
    def __init__(self, width, height):
        """Define el metodo init e inicializa
        sus atributos

        Args:
        width(int) ancho del rectangulo
        height(largo) del rectanglo
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
