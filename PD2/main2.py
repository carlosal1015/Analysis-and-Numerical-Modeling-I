import numpy as np

import funcAuxiliares as aux
import ecuacLineales as el


def f(x):
    x = np.pi * x / 180
    return (
        0.43861 * np.sin(x) * np.cos(x)
        + 2.15583 * np.sin(x) * np.sin(x)
        - 0.23771 * np.cos(x)
        - 1.16838 * np.sin(x)
    )


def d(x):
    x = np.pi * x / 180
    return (
        0.43861 * np.cos(2 * x)
        + 2.15583 * np.sin(2 * x)
        + 0.23771 * np.sin(x)
        - 1.16838 * np.cos(x)
    )


def main():
    A, b = aux.readLinearEqSystem("A.txt", "b.txt")
    try:
        x = el.gaussJordan(A, b)
        print(x)
        # y=el.eliminaciónGaussiana(A,b)
        # print(y)

    except TypeError:
        pass


if __name__ == "__main__":
    main()
