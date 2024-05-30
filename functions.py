from my_libraries import *


def product(a, b):
    return a*b


# swap two elements in a list
def redefine_order_col(list_col: list, to_switch: list) -> list:
    first = to_switch[0]
    second = to_switch[1]

    pos_1 = 0
    pso_2 = 0
    count = 0

    for el in list_col:
        if el == first:
            pos_1 = count
        elif el == second:
            pos_2 = count
        count += 1

    list_col[pos_1] = second
    list_col[pos_2] = first

    return list_col
# Titanic functions
