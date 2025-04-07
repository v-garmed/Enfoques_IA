# Definimos la función de utilidad para cada posible acción
utilidad = {
    "limpiar_todo": 10,
    "limpiar_parcialmente": 6,
    "no_hacer_nada": 0
}

# El agente simplemente elige la acción con mayor utilidad
def elegir_mejor_accion(utilidad):
    mejor_accion = max(utilidad, key=utilidad.get)
    return mejor_accion

accion_elegida = elegir_mejor_accion(utilidad)
print("El agente elige hacer:", accion_elegida)

# Este enfoque se basa en un enfoque numerico en el que se asigna un valor a cada acción posible y se elige la que maximiza la utilidad esperada.
# En este caso, el agente elige limpiar todo, ya que tiene la mayor utilidad (10).