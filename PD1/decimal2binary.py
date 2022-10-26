#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decimal2binary(decimal: str):
    """Creamos la funcion para convertir de decimal a binario con 8 bits

    Args:
        Num (_type_): _description_
    """
    N0 = decimal
    N = str()
    while N0 != 0:
        if N0 % 2 != 0:
            ak = 1
        else:
            ak = 0

        N0 = (N0 - ak) / 2
        N = N + str(ak)  # concateno el ak que obtengo en cada iteracion
    while len(N) < 8:  # concateno los 0 restantes para completar la longitud de 8 bits
        N += str(0)
    N = N[::-1]  # como empiezo del ultimo al primero, invierto la cadena
    return N


decimales = [56, 85, 127, 27]

if __name__ == "__main__":
    for decimal in decimales:
        print(f"({decimal})_(10) = {decimal2binary(decimal)}.")
