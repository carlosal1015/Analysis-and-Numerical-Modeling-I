#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculadora import (
    decimal2binary,
    verificacion,
    complemento2,
    completarceros,
    complementoa2_a_decimal,
    decimal_a_hexadecimal,
    hexadecimal_a_decimal,
    binario_a_hexadecimal,
)

# Casos de prueba
numbers = [-41298, 0, 41298, 412312, -412312]

for numero in numbers:
    print(f"{numero} en base 2 es\t {decimal2binary(numero)}")

# TODO: Detectar el error en el caso calculadora decimal binario para el numero de muestra 412312.

verificaciones = [
    "-1010000101010010",
    "0",
    "1010000101010010",
    "1100100101010011000",
    "-1100100101010011000",
]

print("----------------------------------")

for v in verificaciones:
    print(verificacion(v))


numeros = [20, 34, 1, 50, -50]  # 0 considerar valores naturales.

for numero in numeros:
    print(f"{numero} en complemento a 2 es\t{complemento2(numero)}")


numeros_completar = [56, 0, -10]  # 00000000000

for numero in numeros_completar:
    print(f"{numero}\t{decimal2binary(numero)}\t{completarceros(numero)}")


numeros_complementoa2_a_decimal = [
    "11111111",
    "000000001",
    "11110000",
]  # "-11110000" "111.10000"
# verificar que ocurre cuando se coloca punto o coma decimal en base 2

for numero in numeros_complementoa2_a_decimal:
    print(f"{numero}\t{complementoa2_a_decimal(numero)}")

# https://madformath.com/calculators/basic-math/base-converters/decimal-to-hexadecimal-converter-with-steps/decimal-to-hexadecimal-converter-with-steps
numeros_decimal2hexa = [0, 1, -1, 10, -10, 31, 31.1, 21, 21.4, 45, 45.1]

for numero in numeros_decimal2hexa:
    print(f"{numero}\t{decimal_a_hexadecimal(numero)}")


numeros_hexa2deci = [
    "AAAAAAAA",
    "-AAAAAAAA",
    "ABCDEF",
    "FEDCBA",
    "999999",
    "A1B2C3D4E5F6",
    "0",
]  # "0.5"

for numero in numeros_hexa2deci:
    print(f"{numero}\t{hexadecimal_a_decimal(numero)}")

# TODO: Considerar el caso con puntos decimales
numeros_binarios2hexa = ["10101010", "010101", "0", "1000", "-1000"]  # "1.01" "1.1"
# https://www.rapidtables.com/convert/number/binary-to-hex.html?x=1.01
#
# el resultado 10101010 es AA, pero la pagina binario.org lo muestra como A.

for numero in numeros_binarios2hexa:
    print(f"{numero}\t{binario_a_hexadecimal(numero)}")
