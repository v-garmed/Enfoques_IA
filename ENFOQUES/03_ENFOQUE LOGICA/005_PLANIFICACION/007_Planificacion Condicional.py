# Planificación con condiciones
def planificar(estado):
    if estado == "lluvioso":
        return ["llevar_paraguas", "caminar"]
    else:
        return ["caminar"]

# Ejecución del planificador
estado_actual = "lluvioso"
plan = planificar(estado_actual)
print("Plan para el estado actual:", plan)
