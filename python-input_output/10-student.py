#!/usr/bin/python3
"""Define una clase Student"""


class Student:
    """
    Esta clase define a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Inicializa el metodo y recibe 3 parametos
        Args:
            first_name (str): primer nombre
            last_name(str): apellido
            age(int): edad
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Esta función regrea un diccionario con los atributos
        de nuestra instancia

        Return:
            dict: regresa un diccionario con los atributos de la instancia
        """
        if isinstance(attrs, list) and all(isinstance(b, str) for b in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
