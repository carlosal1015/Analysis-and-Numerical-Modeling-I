#!/usr/bin/env python
# -*- coding: utf-8 -*-


def binario_a_decimal(numero_binario):
    numero_decimal = 0
    for posicion, digito_string in enumerate(numero_binario[::-1]):
        numero_decimal += int(digito_string) * 2**posicion
    return numero_decimal


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario


def transformaComplemento(b):
    b = b[1:]
    numero_transformado = 32 - binario_a_decimal(b)
    numero_transformado = decimal_a_binario(numero_transformado)
    return numero_transformado


sigue = "si"
while sigue == "si":
    bin_1 = input("Ingrese el primer numero binario: ")
    bin_2 = input("Ingrese el segundo numero binario: ")
    isNegativo1 = bin_1.find("-")
    isNegativo2 = bin_2.find("-")
    if isNegativo1 != -1 and isNegativo2 != -1:
        print("El numero: ", bin_1)
        bin_1 = transformaComplemento(bin_1)
        bin_1 = bin_1[1:]
        print("En Complemento es: ", bin_1)
        print("El numero: ", bin_2)
        bin_2 = transformaComplemento(bin_2)
        bin_2 = bin_2[1:]
        print("En Complemento es: ", bin_2)
        sum = int(bin_1, 2) + int(bin_2, 2)
        sum = decimal_a_binario(sum)
        print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
    elif isNegativo1 == -1 and isNegativo2 == -1:
        sum = int(bin_1, 2) + int(bin_2, 2)
        sum = decimal_a_binario(sum)
        print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
    elif isNegativo1 == -1 and isNegativo2 != -1:
        print("El numero: ", bin_2)
        bin_2 = transformaComplemento(bin_2)
        bin_2 = bin_2[1:]
        print("En Complemento es: ", bin_2)
        if int(bin_2, 2) > int(bin_1, 2):
            sum = int(bin_1, 2) + int(bin_2, 2)
            sum = decimal_a_binario(sum)
            if len(sum) == 5:
                if sum[0] == "1":
                    sum = "0" + sum[1:]
            else:
                sum = "1" + sum
            print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
        else:
            sum = int(bin_1, 2) + int(bin_2, 2)
            sum = decimal_a_binario(sum)
            if len(sum) == 5:
                sum = "0" + sum[1:]
            else:
                sum = "0" + sum
            print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
    elif isNegativo1 != -1 and isNegativo2 == -1:
        print("El numero: ", bin_1)
        bin_1 = transformaComplemento(bin_1)
        bin_1 = bin_1[1:]
        print("En Complemento es: ", bin_1)
        if int(bin_1, 2) > int(bin_2, 2):
            sum = int(bin_1, 2) + int(bin_2, 2)
            sum = decimal_a_binario(sum)
            if len(sum) == 5:
                if sum[0] == "1":
                    sum = "0" + sum[1:]
            else:
                sum = "1" + sum
            print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
        else:
            sum = int(bin_1, 2) + int(bin_2, 2)
            sum = decimal_a_binario(sum)
            if len(sum) == 5:
                sum = "0" + sum[1:]
            else:
                sum = "0" + sum
            print("El resultado de la suma de ", bin_1, " + ", bin_2, " es: ", sum)
    sigue = input("Desea ingresar otra vez? (si|no): ")
