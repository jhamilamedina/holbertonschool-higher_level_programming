#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_element = 0  # Inicialza el contador con los elementos impresos

    for e in range(x):  # covierte el elemento a un entero
        try:
            print("{:d}".format(my_list[i]), end="")
            n_element += 1
        except (ValueError, TypeError):
            continue
    print()  # Imprime una nueva linea
    return n_element  # Retora un numero real o entero
