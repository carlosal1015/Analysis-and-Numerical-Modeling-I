from sympy import Function, symbols, simplify, rsolve, latex, Rational

u = Function("u")  # declares the name of the sequence
n = symbols("n", integer=True)  # declares the variable
f = 2 * u(n - 1) - u(n - 2)  # the expression which is to be zero
ExplicitFormula = simplify(rsolve(f, u(n), {u(1): 1, u(2): 1}))
Formula2 = latex(simplify(ExplicitFormula))
print("The formula for u(n) is " + str(Formula2) + "")


Value = ExplicitFormula.subs(n, 10)
print("10th Fibonacci number = " + str(Value))
print("After simplification : " + str(simplify(Value)))
