from sympy import symbols, ForAll, Exists, And

# Definición de variables
x, y = symbols('x y')

# Definición de un conjunto (dominio)
domain = [1, 2, 3, 4, 5]

# Proposición universal: Para todo x en el dominio, x es un número par.
even_proposition = ForAll(x, x % 2 == 0, domain=domain)

# Proposición existencial: Existe un y en el dominio tal que y es un número impar.
odd_proposition = Exists(y, y % 2 == 1, domain=domain)

# Combinación de proposiciones: Para todo x en el dominio, existe un y en el dominio tal que y es mayor que x.
combined_proposition = ForAll(x, Exists(y, y > x, domain=domain), domain=domain)

# Evaluación de las proposiciones
is_even = even_proposition.doit()
is_odd = odd_proposition.doit()
combined_result = combined_proposition.doit()

print("Para todo x, x es un número par:", is_even)
print("Existe un y, y es un número impar:", is_odd)
print("Para todo x, existe un y tal que y > x:", combined_result)
