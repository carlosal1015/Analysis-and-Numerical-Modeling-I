#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary2decimal(cadena: str):
    for x in range(len(cadena)):
        if x == 0:
            b = int(cadena[x])
        else:
            b = int(cadena[x]) + 2 * b
    return b


# Verificación
def binary2decimal_(binary: str):
    return int(binary, base=2)


binarios = ["10111000", "01010101", "11111111", "00011011"]


if __name__ == "__main__":
    for binario in binarios:
        print(f"({binario})_(2) = {binary2decimal(binario)}.")
        print("Verificación:")
        print(f"({binario})_(2) = {binary2decimal_(binario)}.\n")
