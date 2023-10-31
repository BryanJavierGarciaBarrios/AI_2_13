from collections import defaultdict

# Función para realizar la unificación
def unify(x, y, theta=None):
    if theta is None:
        theta = {}

    if x == y:
        return theta

    if isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if not x or not y:
            return None
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

# Función auxiliar para la unificación de variables
def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Ejemplo de unificación
theta = unify(['Father', 'x', 'y'], ['Father', 'John', 'Mary'])
if theta is not None:
    print("Unificación exitosa:")
    for key, value in theta.items():
        print(f"{key} = {value}")
else:
    print("No se pudo unificar los términos.")
