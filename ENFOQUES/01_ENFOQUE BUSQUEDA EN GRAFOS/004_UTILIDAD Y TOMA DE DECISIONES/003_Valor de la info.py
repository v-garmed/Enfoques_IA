# Probabilidad de que llueva
P_lluvia = 0.3

# Utilidades según acción y clima
utilidad = {
    ("llevar_paraguas", True): 7,
    ("llevar_paraguas", False): 5,
    ("no_llevar_paraguas", True): 0,
    ("no_llevar_paraguas", False): 10
}

acciones = ["llevar_paraguas", "no_llevar_paraguas"]

def utilidad_esperada_sin_info():
    return max(
        sum(utilidad[(a, clima)] * (P_lluvia if clima else 1 - P_lluvia)
            for clima in [True, False])
        for a in acciones
    )

def utilidad_esperada_con_info():
    # Si supiéramos con certeza el clima, elegiríamos la mejor acción en cada caso
    utilidad_si_llueve = max(utilidad[(a, True)] for a in acciones)
    utilidad_si_no_llueve = max(utilidad[(a, False)] for a in acciones)
    return utilidad_si_llueve * P_lluvia + utilidad_si_no_llueve * (1 - P_lluvia)

# Cálculo del Valor Esperado de Información Perfecta
VEIP = utilidad_esperada_con_info() - utilidad_esperada_sin_info()

print("Utilidad esperada SIN información:", utilidad_esperada_sin_info())
print("Utilidad esperada CON información perfecta:", utilidad_esperada_con_info())
print("Valor Esperado de la Información Perfecta:", VEIP)
