# Plan inicial
plan = ["ir_al_supermercado", "comprar_leche", "regresar_a_casa"]

# Simulación de ejecución con vigilancia
def ejecutar_plan(plan):
    for accion in plan:
        print(f"Ejecutando: {accion}")
        if accion == "comprar_leche":
            evento = "leche_no_disponible"
            if evento == "leche_no_disponible":
                print("Evento detectado: leche no disponible. Replanificando...")
                return ["comprar_jugo", "regresar_a_casa"]
    return plan

# Ejecución del plan con vigilancia
nuevo_plan = ejecutar_plan(plan)
print("Nuevo plan:", nuevo_plan)
