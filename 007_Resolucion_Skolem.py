from sympy import symbols, ForAll, Exists, And, Or, Not, simplify_logic, ask, Q, Implies

# Definición de variables y símbolos
x, y, z = symbols('x y z')
f = symbols('f', cls='Function')
P = symbols('P', cls='Function')
Q = symbols('Q', cls='Function')

# Definición de cuantificadores existenciales y universales
exists_x = Exists(x)
exists_y = Exists(y)
for_all_x = ForAll(x)
for_all_y = ForAll(y)

# Fórmulas lógicas de ejemplo
formula1 = And(exists_x, Or(P(x), Q(y)))
formula2 = Implies(exists_x, for_all_x)
formula3 = And(for_all_x, Or(P(x), Q(f(x, y))))

# Realizar resolución Skolem
skolemized_formula1 = formula1.simplify()
skolemized_formula2 = formula2.simplify()
skolemized_formula3 = formula3.simplify()

# Verificar la satisfacción de una fórmula
is_satisfied = ask(skolemized_formula1, Q.exists(x))
print("Fórmula 1 satisfecha:", is_satisfied)

is_satisfied = ask(skolemized_formula2, Q.forall(x))
print("Fórmula 2 satisfecha:", is_satisfied)

is_satisfied = ask(skolemized_formula3, Q.forall(x), Q.exists(y))
print("Fórmula 3 satisfecha:", is_satisfied)

# Impresión de las fórmulas skolemizadas
print("Fórmula 1 skolemizada:", skolemized_formula1)
print("Fórmula 2 skolemizada:", skolemized_formula2)
print("Fórmula 3 skolemizada:", skolemized_formula3)
