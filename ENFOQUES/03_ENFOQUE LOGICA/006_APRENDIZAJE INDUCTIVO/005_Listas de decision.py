# Definición de la clase KDecisionList para implementar una lista de decisión
class KDecisionList:
    def __init__(self, rules, default):
        # Inicializa la lista de reglas y el valor por defecto
        self.rules = rules  # Lista de tuplas (condición, resultado)
        self.default = default  # Valor por defecto si ninguna regla se cumple

    def predict(self, features):
        # Método para predecir el resultado basado en las reglas
        for condition, result in self.rules:
            # Evalúa cada condición con las características proporcionadas
            if condition(features):
                return result  # Retorna el resultado si la condición se cumple
        return self.default  # Retorna el valor por defecto si ninguna regla se cumple


# Definición de las reglas simples para la lista de decisión
rules = [
    (lambda x: x['edad'] > 60, 'Adulto Mayor'),  # Si la edad es mayor a 60, clasifica como 'Adulto Mayor'
    (lambda x: x['edad'] > 18, 'Adulto'),        # Si la edad es mayor a 18, clasifica como 'Adulto'
    (lambda x: x['edad'] > 12, 'Adolescente'),   # Si la edad es mayor a 12, clasifica como 'Adolescente'
]

# Creación de un modelo KDecisionList con las reglas definidas y un valor por defecto
modelo = KDecisionList(rules, default='Niño')  # Si ninguna regla se cumple, clasifica como 'Niño'

# Datos de prueba para evaluar el modelo
datos_prueba = [
    {'nombre': 'Juan', 'edad': 10},  # Niño
    {'nombre': 'Ana', 'edad': 20},  # Adulto
    {'nombre': 'Pedro', 'edad': 65},  # Adulto Mayor
]

# Itera sobre los datos de prueba y clasifica cada persona usando el modelo
for persona in datos_prueba:
    print(f"{persona['nombre']} es clasificado como: {modelo.predict(persona)}")
    # Imprime el nombre de la persona y su clasificación
