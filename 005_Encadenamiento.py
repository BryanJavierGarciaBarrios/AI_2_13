from pyke import knowledge_engine

# Crear la base de conocimientos
engine = knowledge_engine.engine(
    "animal_knowledge",
    my_module="animal_rules",
)

# Definir las reglas y hechos en un módulo separado (animal_rules.py)
engine.reset()
engine.activate('animal_rules')

# Hechos iniciales
engine.add_universal_fact('is_a', 'dog', 'animal')
engine.add_universal_fact('has_fur', 'dog', True)
engine.add_universal_fact('has_feathers', 'dog', False)

# Ejecutar el encadenamiento hacia adelante
engine.prove_1_goal('is_a($animal, $type)')

for vars, plan in engine.get_plan():
    print(f"{vars['animal']} es un {vars['type']}.")
