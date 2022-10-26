import math

# Binario a Decimal
def binario_a_decimal(binario):
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


# Decimal a Binario
def decimal_a_binario(decimal):
    binario = ""
    if decimal == 0:
        return 0
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


# Decimal a Complemento 1
def decimal_a_complementoa1(decimal):
    if decimal < 0:
        decimal = -decimal
    elif decimal == 0:
        return "00000000"
    if decimal < 127:
        n = 8  # numero de bits
    else:
        if decimal < 32768:
            n = 16
        else:
            n = 32
    # transformando de decimal a binario
    c = decimal_a_binario(decimal)
    m = len(c)
    for i in range(n - int(m)):
        c = "0" + c

    # cambia los 1 por 0 y los 0 por 1
    c = c.replace("1", "a")
    c = c.replace("0", "1")
    c = c.replace("a", "0")
    return c


# Complemento a 1 a decimal
def complementoa1_a_decimal(c1):

    n = len(c1)
    # cambia los 1 por 0 y los 0 por 1

    c1 = c1.replace("1", "a")
    c1 = c1.replace("0", "1")
    c1 = c1.replace("a", "0")
    # transformando de binario a decimal
    numero = binario_a_decimal(c1)
    return numero


# Decimal a Complemento 2
def decimal_a_complementoa2(decimal):
    if decimal < 0:
        decimal = -decimal
    elif decimal == 0:
        return "00000000"
    if decimal < 127:
        n = 8  # numero de bits
    else:
        if decimal < 32768:
            n = 16
        else:
            n = 32
    c = decimal_binario(decimal)
    m = len(c)
    for i in range(n - int(m)):
        c = "0" + c
    # invertimos la cadena para ver donde esta el primer 1
    c_inv = c[::-1]

    # cambia los 1 por 0 y los 0 por 1 desde que encuentra el primer 1
    for i in range(n):
        if c_inv[i] == "1":
            aux = c_inv[i + 1 : n]
            aux2 = c_inv[0 : i + 1]
            aux = aux.replace("1", "a")
            aux = aux.replace("0", "1")
            aux = aux.replace("a", "0")
            c_inv = aux2 + aux
            break
    # reinvertimos la cadena para ver el resultado final
    c = c_inv[::-1]
    return c


# Complemento a 2 a decimal
def complementoa2_a_decimal(c2):

    n = len(c2)
    if c2[0] == "1":
        c_inv = c2[::-1]
        # cambia los 1 por 0 y los 0 por 1 desde que encuentra el primer 1
        for i in range(n):
            if c_inv[i] == "1":
                aux = c_inv[i + 1 : n]
                aux2 = c_inv[0 : i + 1]
                aux = aux.replace("1", "a")
                aux = aux.replace("0", "1")
                aux = aux.replace("a", "0")
                c_inv = aux2 + aux
                break
        c2 = c_inv[::-1]
        numero = -binario_a_decimal(c2)
    else:
        numero = binario_a_decimal(c2)
    return numero


# Decimal a octal
def decimal_a_octal(decimal):
    if decimal == 0:
        return 0
    elif decimal < 0:
        decimal = -decimal
        aux = 1  # indicador que tratamos con un numero negativo
    else:
        aux = 0  # indicador que tratamos con un numero positivo

    parte_fraccionaria, parte_entera = math.modf(decimal)
    parte_entera = int(parte_entera)
    if parte_fraccionaria == 0:
        coma = 0
    else:
        coma = 1
    cadena_parte_fraccionaria = ""
    sobrante = None
    while True:
        resultado = parte_fraccionaria * 8
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = str(int(sobrante))
        cadena_parte_fraccionaria += digito
        if parte_fraccionaria == 0:
            break

    octal = ""
    while decimal > 0:
        residuo = int(decimal) % 8
        verdadero_caracter = str(residuo)
        octal = verdadero_caracter + octal
        decimal = int(decimal / 8)
    if aux == 1:
        if coma == 0:
            return "-" + octal
        else:
            return "-" + octal + "." + cadena_parte_fraccionaria
    else:
        if coma == 0:
            return octal
        else:
            return octal + "." + cadena_parte_fraccionaria


# Octal a Decimal
def octal_a_decimal(octal):
    if octal[0] == "-":
        octal = octal[1 : len(octal)]
        aux = 1  # verificador que estamos tratando con un numero negativo
    else:
        aux = 0  # verificador que estamos tratando con un numero positivo

    for i in range(len(octal)):
        if octal[i] == ".":
            parte_fraccionaria = octal[i + 1 : len(octal)]
            parte_entera = octal[0:i]
            break
        else:
            parte_fraccionaria = "0"
            parte_entera = octal
    frac_decimal = 0
    posicion2 = 0
    if parte_fraccionaria != "0":
        for digito in parte_fraccionaria:
            valor = int(digito)
            elevado = 8 ** (-posicion2 - 1)
            equivalencia = elevado * valor
            frac_decimal += equivalencia
            posicion2 += 1
    # La debemos recorrer del final al principio, así que la invertimos
    parte_entera = parte_entera[::-1]
    decimal = 0
    posicion = 0
    for digito in parte_entera:
        valor = int(digito)
        elevado = 8**posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    if aux == 1:
        return -decimal - frac_decimal
    else:
        return decimal + frac_decimal


def binario_a_octal(binario):
    return decimal_a_octal(binariofrac_a_decimal(binario))


def octal_a_binario(octal):
    return decimalfrac_a_binario(octal_a_decimal(octal))


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


def decimal_a_hexadecimal(decimal):
    if decimal == 0:
        return 0
    elif decimal < 0:
        decimal = -decimal
        aux = 1  # indicador que tratamos con un numero negativo
    else:
        aux = 0  # indicador que tratamos con un numero positivo

    parte_fraccionaria, parte_entera = math.modf(decimal)
    parte_entera = int(parte_entera)
    if parte_fraccionaria == 0:
        coma = 0
    else:
        coma = 1
    cadena_parte_fraccionaria = ""
    sobrante = None
    while True:
        resultado = parte_fraccionaria * 16
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = obtener_caracter_hexadecimal(int(sobrante))
        cadena_parte_fraccionaria += digito
        if parte_fraccionaria == 0:
            break

    hexadecimal = ""
    while decimal > 0:
        residuo = int(decimal) % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    if aux == 1:
        if coma == 0:
            return "-" + hexadecimal
        else:
            return "-" + hexadecimal + "." + cadena_parte_fraccionaria
    else:
        if coma == 0:
            return hexadecimal
        else:
            return hexadecimal + "." + cadena_parte_fraccionaria


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
    # Convertir a minúsculas para hacer las cosas más simples
    hexadecimal = hexadecimal.lower()
    if hexadecimal[0] == "-":
        hexadecimal = hexadecimal[1 : len(hexadecimal)]
        aux = 1  # verificador que estamos tratando con un numero negativo
    else:
        aux = 0  # verificador que estamos tratando con un numero positivo

    for i in range(len(hexadecimal)):
        if hexadecimal[i] == ".":
            parte_fraccionaria = hexadecimal[i + 1 : len(hexadecimal)]
            parte_entera = hexadecimal[0:i]
            break
        else:
            parte_fraccionaria = "0"
            parte_entera = hexadecimal
    frac_decimal = 0
    posicion2 = 0
    if parte_fraccionaria != "0":

        for digito in parte_fraccionaria:
            valor = obtener_valor_real(digito)
            elevado = 16 ** (-posicion2 - 1)
            equivalencia = elevado * valor
            frac_decimal += equivalencia
            posicion2 += 1
    # La debemos recorrer del final al principio, así que la invertimos
    parte_entera = parte_entera[::-1]
    decimal = 0
    posicion = 0
    for digito in parte_entera:
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = obtener_valor_real(digito)
        elevado = 16**posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    if aux == 1:
        return -decimal - frac_decimal
    else:
        return decimal + frac_decimal


print(hexadecimal_a_decimal("A31"))

# Binario a Hexadecimal
def binario_a_hexadecimal(binario):
    return decimal_a_hexadecimal(binariofrac_a_decimal(binario))


# Hexadecimal a Binario
def hexadecimal_a_binario(hexadecimal):
    return decimalfrac_a_binario(hexadecimal_a_decimal(hexadecimal))


# Binario fraccionario a decimal
def binariofrac_a_decimal(binario):
    if binario[0] == "-":
        binario = binario[1 : len(binario)]
        aux = 1  # verificador que estamos tratando con un numero negativo
    else:
        aux = 0  # verificador que estamos tratando con un numero positivo

    for i in range(len(binario)):
        if binario[i] == ".":
            parte_fraccionaria = binario[i + 1 : len(binario)]
            parte_entera = binario[0:i]
            break
        else:
            parte_fraccionaria = "0"
            parte_entera = binario
    frac_decimal = 0
    posicion2 = 0
    if parte_fraccionaria != "0":
        for digito in parte_fraccionaria:
            valor = int(digito)
            elevado = 2 ** (-posicion2 - 1)
            equivalencia = elevado * valor
            frac_decimal += equivalencia
            posicion2 += 1
    # La debemos recorrer del final al principio, así que la invertimos
    parte_entera = parte_entera[::-1]
    decimal = 0
    posicion = 0
    for digito in parte_entera:
        # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
        valor = int(digito)
        elevado = 2**posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    if aux == 1:
        return -decimal - frac_decimal
    else:
        return decimal + frac_decimal


# Decimal fraccionario a binario
def decimalfrac_a_binario(decimal):
    if decimal == 0:
        return 0
    elif decimal < 0:
        decimal = -decimal
        aux = 1  # indicador que tratamos con un numero negativo
    else:
        aux = 0  # indicador que tratamos con un numero positivo

    parte_fraccionaria, parte_entera = math.modf(decimal)
    parte_entera = int(parte_entera)
    if parte_fraccionaria == 0:
        coma = 0
    else:
        coma = 1
    cadena_parte_fraccionaria = ""
    sobrante = None
    while True:
        resultado = parte_fraccionaria * 2
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = str(int(sobrante))
        cadena_parte_fraccionaria += digito
        if parte_fraccionaria == 0:
            break

    binario = ""
    while decimal > 0:
        residuo = int(decimal) % 2
        verdadero_caracter = str(residuo)
        binario = verdadero_caracter + binario
        decimal = int(decimal / 2)
    if aux == 1:
        if coma == 0:
            return "-" + binario
        else:
            return "-" + binario + "." + cadena_parte_fraccionaria
    else:
        if coma == 0:
            return binario
        else:
            return binario + "." + cadena_parte_fraccionaria


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
