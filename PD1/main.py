#!/usr/bin/env python


def suma_finita(N: int = 20, /, debug: bool = False):
    from random import randint

    numbers = [randint(0, 10) for i in range(N)]

    suma: int = 0

    if debug:
        print(f"Los primeros {len(numbers)} números.")
        print(numbers)

    for i in range(N):
        suma = suma + numbers[i]

    return f"{suma}"


def polinomio_taylor(
    x: float = 0, tolerancia: float = 1e-2, max_iteraciones: int = 100
):
    N: int = 1
    y: float = x - 1
    suma: float = 0
    potencia: float = y
    term: float = y
    signo: int = -1
    mensaje: bool = False

    while N <= max_iteraciones:
        signo = -signo
        suma = suma + signo * term
        potencia = potencia * y
        term = potencia / (N + 1)

        if abs(term) < tolerancia:
            mensaje = True
            return N
        N = N + 1

    assert mensaje


if __name__ == "__main__":
    print(suma_finita(debug=True))
    print(polinomio_taylor(x=1.5, tolerancia=1e-5, max_iteraciones=15))
