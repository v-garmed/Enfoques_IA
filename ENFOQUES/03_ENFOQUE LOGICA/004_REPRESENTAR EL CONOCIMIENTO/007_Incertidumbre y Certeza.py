base_conocimiento = {
    "síntoma_fiebre": 0.8,
    "síntoma_dolor_cabeza": 0.6
}

def diagnostico(base):
    cf_total = (base["síntoma_fiebre"] + base["síntoma_dolor_cabeza"]) / 2
    if cf_total > 0.7:
        return f"Alta certeza de enfermedad ({cf_total})"
    elif cf_total > 0.4:
        return f"Certeza moderada ({cf_total})"
    else:
        return f"Baja certeza ({cf_total})"

print(diagnostico(base_conocimiento))
