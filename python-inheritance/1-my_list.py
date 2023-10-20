#!/usr/bin/python3
"""
Definimos una clase llamada MyList
que hereda de la clase list
"""


class MyList(list):
    """
    Esta clase toma funcionalidad heredando de list
    """
    def print_sorted(self):
        """
        Este método crea e imprime una copia de la
        lista original
        """
        print(sorted(self))

    def __repr__(self):
        """
        Este metodo regresa como string y representa
        de manera oficial de lista

        Return:
            list (list): regresa la representacion de una lista
        """
        return f"{list(self)}"
