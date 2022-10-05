#!/usr/bin/env python

from sympy import var, simplify, solve, Function, symbols, rsolve, latex

n = var("n", integer=True)
alpha, a, b, c = var("alpha a b c")


def v(n, alpha, a, b, c):
    return alpha * 2**n + a * n**2 + b * n + c


def u(n):
    if n == 0:
        return 1
    else:
        return u(n - 1) * 2 + 3 * n * n


Solutions = solve(
    # Quantities which are to be zero:
    [
        v(0, alpha, a, b, c) - u(0),  # initial condition
        v(1, alpha, a, b, c) - u(1),
        v(2, alpha, a, b, c) - u(2),
        v(3, alpha, a, b, c) - u(3),
    ],
    # Unknowns:
    [alpha, a, b, c],
)
print(Solutions)


# -------------- Question 2 ----------------
# We fix parameters according to Question 1:
c_s = -18
alpha_s = 19
b_s = -12
a_s = -3
var("n")
print(
    "With these coefficients the simplification of v(n)-2v(n-1) gives : "
    + str(simplify(v(n, alpha_s, a_s, b_s, c_s) - 2 * v(n - 1, alpha_s, a_s, b_s, c_s)))
)
# We can check that u and v coincide for the first values:
# print([u(n) for n in range(10)])
# print([v(n,alpha_s,a_s,b_s,c_s) for n in range(10)])

# First example: a geometric sequence
print("----------------------------------")
print("Example 1 (order one): u(n)=3*u(n-1), u(0)=5")
u = Function("u")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = u(n) - 3 * u(n - 1)  # the expression which is to be zero
ExplicitFormula = rsolve(
    f, u(n), {u(0): 5}
)  # solves f=0 with a given initial condition
print("The formula for u(n) is " + str(ExplicitFormula) + "")
# Second example with a non-constant term
print("----------------------------------")
print("Example 2 (order one): 2v(n)=v(n-1)+2**n, v(0)=1")
v = Function("v")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = 2 * v(n) - v(n - 1) - 2**n  # the expression which is to be zero
ExplicitFormula2 = rsolve(f, v(n), {v(0): 1})
print("The formula for v(n) is " + str(ExplicitFormula2) + "")
# Third example: order two
print("----------------------------------")
print("Example 3 (order two): w(n)=2*w(n-1)+w(n-2)-1, w(0)=1,w(1)=1")
w = Function("w")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = w(n) - 2 * w(n - 1) - w(n - 2) + 1  # the expression which is to be zero
ExplicitFormula3 = rsolve(f, w(n), {w(0): 1, w(1): 1})
print("The formula for w(n) is " + str(ExplicitFormula3) + "")


u = Function("u")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = u(n) - u(n - 1) - u(n - 2)  # the expression which is to be zero
ExplicitFormula = simplify(rsolve(f, u(n), {u(1): 1, u(2): 1}))
Formula2 = latex(simplify(ExplicitFormula))
print("The formula for u(n) is " + str(Formula2) + "")


Value = ExplicitFormula.subs(n, 10)
print("10th Fibonacci number = " + str(Value))
print("After simplification : " + str(simplify(Value)))


J = Function("J")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = J(n) - 2 * J(n - 2) - 5  # the expression which is to be zero
ExplicitFormula = rsolve(f, J(n), {J(0): 1, J(1): 2})
Formula = simplify(ExplicitFormula)
print("Sympy says the formula for J(n) is " + str(Formula) + "")
print(latex(simplify(Formula)))
