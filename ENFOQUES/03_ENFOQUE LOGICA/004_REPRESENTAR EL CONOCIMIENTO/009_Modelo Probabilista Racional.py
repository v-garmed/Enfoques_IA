# Probabilidad y utilidad de dos acciones
acciones = {
    "buscar_sombra": {"probabilidad": 0.9, "utilidad": 7},
    "caminar_bajo_el_sol": {"probabilidad": 0.3, "utilidad": 3}
}

def seleccionar_mejor_accion(acciones):
    mejor = None
    max_utilidad = -1
    for accion, datos in acciones.items():
        valor_esperado = datos["probabilidad"] * datos["utilidad"]
        print(f"{accion}: Valor esperado = {valor_esperado}")
        if valor_esperado > max_utilidad:
            max_utilidad = valor_esperado
            mejor = accion
    return mejor

print("Acción racional:", seleccionar_mejor_accion(acciones))
