#!/usr/bin/env python

from sympy import var, simplify


def InductionFormula(x):
    return (1 + x) / (1 - x)


a = var("a")
Sequence = [a]
print("u_0 = a")

for i in range(1, 12):
    Sequence.append(simplify(InductionFormula(Sequence[-1])))
    print("u_" + str(i) + " = " + str(Sequence[-1]))


x = var("x")
A = (x**6 + 45 * x**4 - 81 * x**2 + 27) / (3 * x * (x**2 + 3) ** 2)
B = (-(x**4) + 30 * x**2 - 9) / (3 * x * (x**2 + 3))
C = (-12 * x**3 + 36 * x) / ((x**2 + 3) ** 2)
print(simplify(A**3 + B**3 + C**3))
