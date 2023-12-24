#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Inicialza el contador con los elementos impresos
    for i in range(x):  # covierte el elemento a un entero
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return  # Retora un numero real o entero
