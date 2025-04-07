# Coloreado de mapas con Salto Atrás Dirigido por Conflictos

# Variables: regiones
variables = ["A", "B", "C", "D"]
# Dominios: colores posibles
dominios = {v: ["Rojo", "Verde", "Azul"] for v in variables}
# Restricciones: regiones vecinas no pueden tener el mismo color
restricciones = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Almacena los conflictos
def conflicto(var, valor, asignacion):
    for vecina in restricciones[var]:
        if vecina in asignacion and asignacion[vecina] == valor:
            return vecina  # Se identifica el conflicto con esta variable
    return None

def cbj(asignacion, variables, dominios, nivel=0, conflictos={}):
    if len(asignacion) == len(variables):
        return asignacion

    var = variables[nivel]
    for valor in dominios[var]:
        conflicto_con = conflicto(var, valor, asignacion)
        if not conflicto_con:
            asignacion[var] = valor
            conflictos[var] = set()
            resultado = cbj(asignacion, variables, dominios, nivel+1, conflictos)
            if resultado:
                return resultado
            del asignacion[var]
        else:
            # Guardamos conflicto para salto dirigido
            if var not in conflictos:
                conflictos[var] = set()
            conflictos[var].add(conflicto_con)

    # Salto atrás dirigido por conflicto
    if var in conflictos and conflictos[var]:
        var_conflictiva = max(conflictos[var], key=lambda x: variables.index(x))
        return cbj(asignacion, variables, dominios, variables.index(var_conflictiva), conflictos)
    return None

solucion = cbj({}, variables, dominios)
print("Solución encontrada:", solucion)
