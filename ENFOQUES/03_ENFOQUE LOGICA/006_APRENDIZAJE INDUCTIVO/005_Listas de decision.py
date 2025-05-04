class KDecisionList:
    def __init__(self, rules, default):
        self.rules = rules  # lista de tuplas (condicion, resultado)
        self.default = default  # valor por defecto si ninguna regla se cumple

    def predict(self, features):
        for condition, result in self.rules:
            if condition(features):
                return result
        return self.default


# Reglas simples tipo K-DL
rules = [
    (lambda x: x['edad'] > 60, 'Adulto Mayor'),
    (lambda x: x['edad'] > 18, 'Adulto'),
    (lambda x: x['edad'] > 12, 'Adolescente'),
]

modelo = KDecisionList(rules, default='Niño')

datos_prueba = [
    {'nombre': 'Juan', 'edad': 10},
    {'nombre': 'Ana', 'edad': 20},
    {'nombre': 'Pedro', 'edad': 65},
]

for persona in datos_prueba:
    print(f"{persona['nombre']} es clasificado como: {modelo.predict(persona)}")
