#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Inicialza el contador con los elementos impresos
    try:
        idx = 0
        while count < x:
            if type(my_list[idx]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            idx += 1
    except (ValueError, TypeError):
        pass
    print()
    return count  # Retora un numero real o entero
