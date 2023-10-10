#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_element = 0  # Inicialza el contador con los elementos impresos

    try:
        for e in range(x):  # covierte el elemento a un entero
            e = my_list[e]
            if type(e) == int:
                print("{:d}".format(e), end="")  # Imprime los elemtos enteros
                n_element += 1
     
    except IndexError as e:
        print(e)  # maneja la excepción cuando la lista se agote
    print()  # Imprime una nueva linea
    return n_element  # Retora un numero real o entero

