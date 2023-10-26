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

    def to_json(self):
        """
        Esta función regrea un diccionario con los atributos
        de nuestra instancia

        Return:
            dict: regresa un diccionario con los atributos de la instancia
        """
        return self.__dict__
