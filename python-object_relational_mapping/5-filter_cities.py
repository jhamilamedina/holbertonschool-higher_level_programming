#!/usr/bin/python3
"""
Este modulo sirve para con BD MySQL
Muestre todos los valores en la tabla de estados en la BD hbtn_0e_0_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Estableciendo la coneccion con MySQL
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306,
            db=sys.argv[3],
    )
    cu = db.cursor()
    # Consulta para ordenar estados que empiecen con N ordenados por id
    cu.execute("""SELECT cities.name FROM cities INNER JOIN states
               ON states.id=cities.state_id
               WHERE states.name = %s""", (sys.argv[4],))

    # Recupera todas las filas(rows)
    rows = cu.fetchall()

    # Mustra el resultado
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    # Cerrar el cursor y la coneccion
    cu.close()
    db.close()
