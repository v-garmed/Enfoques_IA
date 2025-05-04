# Representación de una acción en STRIPS
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

# Estado inicial
estado = {"en(casa)", "tiene(llaves)"}

# Definición de acciones
acciones = [
    Accion("salir_de_casa", {"en(casa)", "tiene(llaves)"}, {"en(calle)"}),
    Accion("entrar_a_casa", {"en(calle)", "tiene(llaves)"}, {"en(casa)"})
]

# Aplicación de una acción
def aplicar_accion(estado, accion):
    if accion.precondiciones.issubset(estado):
        nuevo_estado = estado.union(accion.efectos)
        return nuevo_estado
    else:
        return estado

# Ejemplo de uso
estado = aplicar_accion(estado, acciones[0])
print("Estado después de la acción:", estado)
