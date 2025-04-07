# Probabilidad de que llueva
P_lluvia = 0.3

# Utilidades:
# (acción, lluvia) : utilidad
utilidad = {
    ("llevar_paraguas", True): 7,
    ("llevar_paraguas", False): 5,
    ("no_llevar_paraguas", True): 0,
    ("no_llevar_paraguas", False): 10
}

# Acciones posibles
acciones = ["llevar_paraguas", "no_llevar_paraguas"]

# Calcular utilidad esperada para cada acción
def utilidad_esperada(accion):
    u_lluvia = utilidad[(accion, True)] * P_lluvia
    u_no_lluvia = utilidad[(accion, False)] * (1 - P_lluvia)
    return u_lluvia + u_no_lluvia

# Elegir la mejor acción
mejor_accion = max(acciones, key=utilidad_esperada)

print("La mejor decisión es:", mejor_accion)
print("Utilidad esperada:", utilidad_esperada(mejor_accion))
#