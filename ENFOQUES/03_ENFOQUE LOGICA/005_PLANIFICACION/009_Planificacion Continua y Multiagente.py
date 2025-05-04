# Simulación de planificación multiagente
agentes = {
    "robot1": {"tarea": "limpiar", "estado": "disponible"},
    "robot2": {"tarea": "cargar", "estado": "ocupado"}
}

# Planificación continua
def planificar(agentes):
    for nombre, info in agentes.items():
        if info["estado"] == "disponible":
            print(f"{nombre} ejecuta la tarea: {info['tarea']}")
        else:
            print(f"{nombre} está ocupado. Replanificando...")
            info["tarea"] = "esperar"
    return agentes

# Ejecución de la planificación
agentes_actualizados = planificar(agentes)
print("Estado de los agentes:", agentes_actualizados)
