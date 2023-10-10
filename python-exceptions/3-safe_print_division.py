#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    # Intenta finalizar la división
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {0}".format(result))
        return result
