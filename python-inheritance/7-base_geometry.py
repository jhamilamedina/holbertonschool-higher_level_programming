#!/usr/bin/python3
"""
Se define una clase llamada BaseGeometry
"""


class BaseGeometry:
    """Representación de la clase"""
    def area(self):  # Definimos un metodo area, argumento self
        """
        Esta función lanza una excepción
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Definimos un metodo y sus argmentos

        Args:
            value(int): valida el valor
            name(str): nombre del parametro value

        Return:
            None
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
