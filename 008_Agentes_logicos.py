class AgenteLogico:
    def __init__(self):
        # Base de conocimiento (reglas lógicas)
        self.base_de_conocimiento = {
            "Regla 1": {"antecedentes": {"edad": 18, "examen_aprobado": True}, "consecuente": "Puede obtener la licencia"},
            "Regla 2": {"antecedentes": {"edad": 16, "examen_aprobado": True}, "consecuente": "No puede obtener la licencia"},
            "Regla 3": {"antecedentes": {"examen_aprobado": False}, "consecuente": "No puede obtener la licencia"}
        }

    def tomar_decision(self, edad, examen_aprobado):
        for regla, datos in self.base_de_conocimiento.items():
            antecedentes = datos["antecedentes"]
            consecuente = datos["consecuente"]
            if all(antecedentes[condicion] == valor for condicion, valor in antecedentes.items()):
                return consecuente
        return "No se puede determinar la decisión"

# Crear un agente lógico
agente = AgenteLogico()

# Tomar decisiones basadas en reglas lógicas
edad = 18
examen_aprobado = True
decision = agente.tomar_decision(edad, examen_aprobado)
print(f"Para una persona de {edad} años con examen aprobado: {decision}")

edad = 16
examen_aprobado = True
decision = agente.tomar_decision(edad, examen_aprobado)
print(f"Para una persona de {edad} años con examen aprobado: {decision}")

examen_aprobado = False
decision = agente.tomar_decision(edad, examen_aprobado)
print(f"Para una persona de {edad} años sin examen aprobado: {decision}")
