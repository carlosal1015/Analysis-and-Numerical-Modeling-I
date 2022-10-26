#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from math import *


def g(x):
    return cos(1 / x)


def p_sombrero(x0, x1, x2):
    return x0 - pow(x1 - x0, 2) / (x2 - 2 * x1 + x0)


def metodo_Aitken(x_n, p, n):
    """x_n : sucesion

    Args:
        x_n (_type_): _description_
        p (_type_): _description_
        n (_type_): _description_
    """
    init_values = [0] * (n + 2)

    for i in range(n + 2):
        init_values[i] = x_n(p)
        p += 1

    for i in range(n + 2):
        print(f"X{i}:\t{init_values[i]:.5f}")
    print("-------------------")
    for i in range(n):
        resultado_aitken = p_sombrero(
            init_values[i], init_values[i + 1], init_values[i + 2]
        )
        print(f"P^{i}:\t{resultado_aitken:.5f}")


def x_n(n):
    return g(n)


if __name__ == "__main__":
    metodo_Aitken(x_n, 1, 5)
