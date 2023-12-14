#!/usr/bin/python3
"""
Este modulo sirve para 
conectar con MySQL
"""


import MySQLdb
import sys


def main():
    """
    Esta función consulta la
    tabla states en BD hbtn_0e_0_usa
    """
    
    # Estableciendo la coneccion con MySQL
    connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            port=3306,
            database=sys.argv[3],
    )
    cursor = connection.cursor()
    # Consulta para ordenar eatados ordenados por id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Recupera todas las filas(rows)
    states = cursor.fetchall()
    
    # Mustra el resultado
    for state in states:
        print(states)

    # Cerrar el cursor y la coneccion
    cursor.close()
    connection.close()


if __name__ == "__main__":
    """
    Esta validacion evitara que se ejecute este archivo
    """
    main()
