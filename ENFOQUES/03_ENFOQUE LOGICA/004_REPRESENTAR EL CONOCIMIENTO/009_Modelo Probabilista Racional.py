# Diccionario que contiene las acciones posibles con sus respectivas probabilidades y utilidades
acciones = {
    "buscar_sombra": {"probabilidad": 0.9, "utilidad": 7},  # Acción 1: Buscar sombra
    "caminar_bajo_el_sol": {"probabilidad": 0.3, "utilidad": 3}  # Acción 2: Caminar bajo el sol
}

# Función para seleccionar la mejor acción basada en el valor esperado
def seleccionar_mejor_accion(acciones):
    mejor = None  # Variable para almacenar la mejor acción
    max_utilidad = -1  # Inicializa la utilidad máxima como un valor bajo
    # Itera sobre las acciones y sus datos
    for accion, datos in acciones.items():
        # Calcula el valor esperado como probabilidad * utilidad
        valor_esperado = datos["probabilidad"] * datos["utilidad"]
        # Imprime el valor esperado de la acción actual
        print(f"{accion}: Valor esperado = {valor_esperado}")
        # Si el valor esperado es mayor que la utilidad máxima actual, actualiza los valores
        if valor_esperado > max_utilidad:
            max_utilidad = valor_esperado  # Actualiza la utilidad máxima
            mejor = accion  # Actualiza la mejor acción
    return mejor  # Devuelve la mejor acción encontrada

# Imprime la acción racional seleccionada basada en el valor esperado
print("Acción racional:", seleccionar_mejor_accion(acciones))
