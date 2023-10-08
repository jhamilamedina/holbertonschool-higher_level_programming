#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Inicializa un conador para lo elementos impresos

    try:
        for i in range(x):
            print(my_list[i], end="")  # Imprime el elemento  con un espacio
            count += 1  # El contador se incrementa

    except IndexError:
        pass  # maneja la excepción cuando se agota la lista
    print()  # Imprime una nueva linea para finalizar la salida

    return count  # Devuelve el nro de elementos impresos
