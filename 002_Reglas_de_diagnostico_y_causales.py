from problog.program import PrologString
from problog import get_evaluatable

# Definir reglas de diagnóstico y causales en lógica de primer orden
prolog_code = """
% Reglas de diagnóstico
diagnostico(X) :- sintoma(X), prueba_diagnostico(X).
diagnostico(Y) :- sintoma(Y), causa(X, Y), diagnostico(X).

% Relaciones causales
causa(resfrio, fiebre).
causa(gripe, fiebre).
causa(gripe, tos).

% Síntomas y pruebas de diagnóstico
sintoma(fiebre).
sintoma(tos).
prueba_diagnostico(resfrio).
prueba_diagnostico(gripe).
"""

# Crear un programa Prolog a partir del código
prolog_program = PrologString(prolog_code)

# Consultar el programa para obtener diagnósticos
query = "diagnostico(X)."

# Obtener resultados de diagnóstico
results = prolog_program.query(query)

for result in results:
    print(f"Diagnóstico: {result['X']}")

# Consultar el programa para obtener relaciones causales
query_causal = "causa(X, Y)."

# Obtener resultados de relaciones causales
results_causal = prolog_program.query(query_causal)

for result in results_causal:
    print(f"Causa: {result['X']} -> {result['Y']}")

# Consultar el programa para obtener síntomas
query_sintomas = "sintoma(X)."

# Obtener resultados de síntomas
results_sintomas = prolog_program.query(query_sintomas)

for result in results_sintomas:
    print(f"Síntoma: {result['X']}")
