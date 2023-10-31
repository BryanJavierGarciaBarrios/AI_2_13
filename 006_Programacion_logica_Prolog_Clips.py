from pyswip import Prolog

# Crear un objeto Prolog
prolog = Prolog()

# Definir relaciones lógicas
prolog.assertz("padre(juan, maria)")
prolog.assertz("padre(juan, pedro)")
prolog.assertz("padre(pedro, ana)")

# Consulta de relaciones lógicas
for resultado in prolog.query("padre(juan, X)"):
    print(f"Juan es padre de {resultado['X']}")

for resultado in prolog.query("padre(X, ana)"):
    print(f"{resultado['X']} es padre de Ana")


# CLIPS

pip install pyclips

import clips

# Crear un nuevo entorno CLIPS
env = clips.Environment()

# Cargar reglas y hechos en CLIPS
env.build('''
    (defrule regla1
        (hecho (valor 1))
        =>
        (assert (resultado "Regla 1 se cumple"))
    )

    (deffacts hechos-iniciales
        (hecho (valor 1))
    )
''')

# Ejecutar CLIPS
env.run()

# Obtener resultados
for fact in env.facts():
    if fact.template.name == "resultado":
        print(fact["resultado"])
