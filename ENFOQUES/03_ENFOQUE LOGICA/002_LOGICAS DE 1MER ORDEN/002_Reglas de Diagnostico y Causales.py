# Reglas causales
causas = {
    "fiebre": "infección",
    "tos": "resfriado",
    "dolor muscular": "gripe"
}

# Reglas de diagnóstico inversas
def diagnosticar(sintomas):
    posibles_causas = set()
    for sintoma in sintomas:
        if sintoma in causas:
            posibles_causas.add(causas[sintoma])
    return posibles_causas

sintomas_paciente = ["fiebre", "dolor muscular"]
print("Diagnóstico probable:", diagnosticar(sintomas_paciente))
