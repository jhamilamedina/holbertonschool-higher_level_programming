#!/usr/bin/python3
"""Definición de una clase"""


class Rectangle:
    """Representación de la clase"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Inicializa el metodo constructor, tiene 2 parametros

        Args:
            width(int)es el ancho del rectangulo
            height(int) es el alto del rectangulo
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
            str_repr = ''.join(
                [f"{str(self.print_symbol) * b}\n" for i in range(a) if i])
            return str_repr[:len(str_repr) - 1]

    def __repr__(self):
        """
        Este metodo regresa la resentación del rectangulo
        Return:
            string: cadena que representa al rectangulo
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Este metodo imprime un mensaje al eliminar la instancia del rectangulo
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Este metodo estatico compara el área  de 2 rectangulos.
        Anos deben pertenecer a la misma clase

        Args:
            rect_1 (Rectangle):Instancia de la clase rectangle
            rect_2 (Rectangle):Instancia de la clase rectangle

        Raise:
            TypeError: Si no son instancias del rectangulo

        Returns:
            rect_1: Retorna la instancia con mayor área
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
