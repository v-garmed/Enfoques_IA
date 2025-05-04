reglas = {
    "tos": "resfriado",
    "dolor_cabeza": "migraña",
    "fiebre": "infección"
}

sintomas_usuario = ["fiebre", "tos"]

def sistema_experto(sintomas):
    diagnosticos = []
    for sintoma in sintomas:
        if sintoma in reglas:
            diagnosticos.append(reglas[sintoma])
    return set(diagnosticos)

print("Diagnóstico:", sistema_experto(sintomas_usuario))
