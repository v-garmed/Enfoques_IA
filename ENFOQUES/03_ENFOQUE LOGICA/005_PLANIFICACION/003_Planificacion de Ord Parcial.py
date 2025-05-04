# Representación de acciones con dependencias
acciones = {
    "cortar_verduras": [],
    "calentar_sarten": [],
    "freir_verduras": ["cortar_verduras", "calentar_sarten"]
}

# Determinar orden de ejecución
def planificar(acciones):
    plan = []
    while acciones:
        ejecutables = [accion for accion, deps in acciones.items() if all(dep in plan for dep in deps)]
        if not ejecutables:
            raise Exception("No se puede planificar debido a dependencias cíclicas.")
        for accion in ejecutables:
            plan.append(accion)
            del acciones[accion]
    return plan

# Ejecución del planificador
plan = planificar(acciones.copy())
print("Plan de acciones:", plan)
