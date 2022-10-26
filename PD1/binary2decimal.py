#!/usr/bin/env -S python binary2decimal.py -v
# -*- coding: utf-8 -*-
"""
The example module supplies one function, factorial().  For example,

>>> binarios = ["10111000", "01010101", "11111111", "00011011"]
>>> for binario in binarios:
...     binary2decimal(binario)
...     assert(binary2decimal(binario) is int(binario, base=2))
184
85
255
27
"""


def binary2decimal(cadena: str):
    """Convierte un número desde base dos hacia base diez.

    Returns:
        int: número en base diez.
    >>> binary2decimal("10111000")
    184
    """
    for x in range(len(cadena)):
        """x varía entre 0, ..., longitud - 1."""
        if x == 0:
            """b_{j} = a_{j}"""
            b: int = int(cadena[x])
        else:
            """b_{j} = a_{j} + 2*b_{j+1} para k=0."""
            b: int = int(cadena[x]) + 2 * b
    return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
