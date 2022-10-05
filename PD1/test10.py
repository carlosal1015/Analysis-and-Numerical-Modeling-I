#!/usr/bin/env python

from sympy import var, simplify, sqrt, cbrt


def InductionFormula(x):
    return cbrt(4 + x * x)


# a = var("a")
a = 1
Sequence = [a]
print(f"u_0 = {a}")

for i in range(1, 11):
    Sequence.append(simplify(InductionFormula(Sequence[-1])))
    print("u_" + str(i) + " = " + str(Sequence[-1]))

# print((3- sqrt(5).evalf(10)) / 2)