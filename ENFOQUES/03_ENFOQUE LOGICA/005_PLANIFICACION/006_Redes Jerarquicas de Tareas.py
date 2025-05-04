# Representación de una red jerárquica de tareas
tareas = {
    "preparar_comida": ["cocinar_arroz", "freir_pollo"],
    "cocinar_arroz": ["lavar_arroz", "hervir_arroz"],
    "freir_pollo": ["marinar_pollo", "freir"]
}

# Descomposición de tareas
def descomponer(tarea):
    if tarea not in tareas:
        return [tarea]
    subtareas = []
    for sub in tareas[tarea]:
        subtareas.extend(descomponer(sub))
    return subtareas

# Ejecución de la descomposición
plan = descomponer("preparar_comida")
print("Plan detallado de tareas:", plan)
