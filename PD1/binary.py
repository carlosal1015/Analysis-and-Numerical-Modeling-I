#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binary2decimal(binary):
    return int(binary, base=2)


binarios = ["10111000", "01010101", "11111111", "00011011"]

for binario in binarios:
    print(f"{binario}_(2) = {binary2decimal(binario)}.")
