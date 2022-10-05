#!/usr/bin/env python

from sympy import var, simplify, sqrt


def InductionFormula(x):
    return sqrt(3 * x)


# a = var("a")
a = sqrt(3)
Sequence = [a]
print(f"u_0 = {a}")

for i in range(1, 101):
    Sequence.append(simplify(InductionFormula(Sequence[-1])))
    print("u_" + str(i) + " = " + str(Sequence[-1]))

# print((3- sqrt(5).evalf(10)) / 2)
