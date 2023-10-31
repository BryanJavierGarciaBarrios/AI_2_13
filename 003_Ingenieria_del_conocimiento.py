from pyke import knowledge_engine

# Definir el motor de conocimiento
engine = knowledge_engine.engine(__file__)

# Definir hechos sobre personas y sus relaciones
engine.prove_1('relacion', 'Juan', 'padre', 'María')
engine.prove_1('relacion', 'María', 'madre', 'Ana')
engine.prove_1('relacion', 'Juan', 'abuelo', 'Ana')

# Definir reglas de inferencia
engine.prove_1('hija', 'X', 'Y') <= (
    'relacion', 'Y', 'madre', 'X')
engine.prove_1('abuela', 'X', 'Z') <= (
    'relacion', 'X', 'madre', 'Y'),
    'relacion', 'Y', 'madre', 'Z')

# Realizar consultas
hijas = engine.prove_all('hija', 'X', 'Y')
abuelas = engine.prove_all('abuela', 'X', 'Z')

print("Hijas:")
for fact in hijas:
    print(f"{fact['X']} es hija de {fact['Y']}")

print("Abuelas:")
for fact in abuelas:
    print(f"{fact['X']} es abuela de {fact['Z']}")
