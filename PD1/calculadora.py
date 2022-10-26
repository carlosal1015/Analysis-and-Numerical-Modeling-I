#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decimal2binary(decimal):
    binario = str()
    if decimal == 0:
        return str(0)
    elif decimal < 0:
        decimal = -decimal

        while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return "-" + binario
    else:
        while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return binario


# de decimal a complemento a 2 (binario)
def complemento2(decimal):
    if decimal < 0:
        decimal = -decimal
    elif decimal == 0:
        return str(0) * 8
    if decimal < pow(2, 7) - 1:
        n = pow(2, 3)  # numero de bits
    elif decimal < pow(2, 15):
        n = pow(2, 4)
    elif decimal < pow(2, 31):
        n = pow(2, 5)
    c = decimal2binary(decimal)
    m = len(c)
    # Completando con ceros a la izquierda segun el numero de bits
    for i in range(n - int(m)):
        c = "0" + c
    # invertimos la cadena para ver donde esta el primer 1
    c_inv = c[::-1]

    # cambia los 1 por 0 y los 0 por 1 desde que encuentra el primer 1
    for i in range(n):
        if c_inv[i] == "1":
            # Obtiene el primer uno |1|<-111111111111111111111
            # y los terminos de la derecha los invierte, es decir 1 por 0 y 0 por 1.
            # y los de la izquierda los mantiene constante
            # la parte derecha
            aux = c_inv[i + 1 : n]
            # la parte izquierda
            aux2 = c_inv[0 : i + 1]

            # * representa la variable temporal
            aux = aux.replace("1", "*")
            aux = aux.replace("0", "1")
            aux = aux.replace("*", "0")
            c_inv = aux2 + aux
            break
    # reinvertimos la cadena para ver el resultado final
    c = c_inv[::-1]
    return c


def completarceros(decimal):
    if decimal < 127:
        n = 8  # numero de bits
    else:
        if decimal < 32768:
            n = 16
        else:
            n = 32
    c = decimal2binary(decimal)
    if c == str(0):
        return str(0) * 8
    else:
        # longitud del binario
        m = len(c)
        for i in range(n - int(m)):
            c = "0" + c
        return c


def verificacion(cadena_binario):
    return int(cadena_binario, base=2)


# calculadora de binario a decimal
def binary2decimal(binario):
    decimal = 0
    if binario[0] == "-":
        binario = binario[1 : len(binario)]
        for posicion, cadena in enumerate(binario[::-1]):  # para invertir los digitos
            decimal += int(cadena) * 2 ** (posicion)
        return -decimal
    else:
        for posicion, cadena in enumerate(binario[::-1]):  # para invertir los digitos
            decimal += int(cadena) * 2**posicion
        return decimal


# calculadora de complemento a 2 a decimal
def complementoa2_a_decimal(c2):
    n = len(c2)
    if c2[0] == "1":
        c_inv = c2[::-1]
        # cambia los 1 por 0 y los 0 por 1 desde que encuentra el primer 1
        for i in range(n):
            if c_inv[i] == "1":
                aux = c_inv[i + 1 : n]
                aux2 = c_inv[0 : i + 1]
                aux = aux.replace("1", "*")
                aux = aux.replace("0", "1")
                aux = aux.replace("*", "0")
                c_inv = aux2 + aux
                break
        c2 = c_inv[::-1]
        numero = -binary2decimal(c2)
    else:
        numero = binary2decimal(c2)
    return numero


# Decimal a Hexadecimal
# Función que regresa el verdadero valor hexadecimal.
# Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


# TODO: considerar con decimal, 1.1_(10) = xx_(16).
# CORRECCION DE DECIMAL A HEXADECIMAL (implementacion caso 0 y caso negativo):
def decimal_a_hexadecimal(decimal):
    if decimal == 0:
        return 0
    elif decimal < 0:
        decimal = -decimal
        aux = 1  # indicador que tratamos con un numero negativo
    else:
        aux = 0  # indicador que tratamos con un numero positivo
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    if aux == 1:
        return "-" + hexadecimal
    else:
        return hexadecimal


# decimal = int(input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
# hexadecimal = decimal_a_hexadecimal(decimal)
# print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")

# Hexadecimal a Decimal
def obtener_valor_real(caracter_hexadecimal):
    equivalencias = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10,
    }
    if caracter_hexadecimal in equivalencias:
        return equivalencias[caracter_hexadecimal]
    else:
        return int(caracter_hexadecimal)


def hexadecimal_a_decimal(hexadecimal):
    if hexadecimal[0] == "-":
        hexadecimal = hexadecimal[1 : len(hexadecimal)]
        aux = 1  # verificador que estamos tratando con un numero negativo
    else:
        aux = 0  # verificador que estamos tratando con un numero positivo
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        elevado = 16**posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    if aux == 1:
        return -decimal
    else:
        return decimal


# Decimal a IEEE754
def decimal_a_ieee754(decimal):
    if str(decimal)[0] == "-":
        signo = "1"
    else:
        signo = "0"
    for i in range(len(str(decimal))):
        if str(decimal)[i] == ".":
            n = 23
            break
        else:
            n = 22
    c = decimalfrac_a_binario(decimal)
    if len(c) > 32:
        c = c[0:23]
    m = len(c)
    # quitamos el punto fraccionario a la cadena binaria
    for i in range(m):
        if c[i] == ".":
            c2 = c[0:i] + c[i + 1 : m]
            break

    # cortamos la cadena 2 para la mantisa
    for i in range(m):
        if c2[i] == "1":
            mantisa = c2[i + 1 : len(c2)]
            break
    for i in range(n - len(mantisa)):
        mantisa = mantisa + "0"
    for i in range(len(c)):
        if str(c)[i] == ".":
            aux = i
            break

    exponente = decimalfrac_a_binario(126 + aux)
    if len(exponente) == 7:
        exponente = "0" + exponente

    return signo + " " + exponente + " " + mantisa


# if 8 == (8 or 16 or 32):
#     print("Bien")
# else:
#     print("Ingrese por teclado")
#     x = input("Valor")
#     print(x)


# Binario a Hexadecimal
def binario_a_hexadecimal(binario):
    return decimal_a_hexadecimal(binary2decimal(binario))


# Hexadecimal a Binario
def hexadecimal_a_binario(hexadecimal):
    return decimal2binary(hexadecimal_a_decimal(hexadecimal))


numeros = ["AAAAAAA", "0", "-AAAAAAA", "1234567890ABCDEF"]
# Esta fallando 1234567890ABCDEF pues debe ser 1001000110100010101100111100010010000101010111100110111101111

for numero in numeros:
    print(f"{numero}\t\t{hexadecimal_a_binario(numero)}")
