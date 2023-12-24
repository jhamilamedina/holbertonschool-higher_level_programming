#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_element = 0  # Inicialza el contador con los elementos impresos

    try:
        for i in range(x):  # covierte el elemento a un entero
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]),
                      end="\n" if i == x - 1 else " ")
                n_element += 1
    except (IndexError, TypeError):
        pass
    print()  # Imprime una nueva linea
    return n_element  # Retora un numero real o entero
