# Definimos una base de conocimiento con valores de certeza para diferentes síntomas
base_conocimiento = {
    "síntoma_fiebre": 0.8,  # Grado de certeza de que el paciente tiene fiebre
    "síntoma_dolor_cabeza": 0.6  # Grado de certeza de que el paciente tiene dolor de cabeza
}

# Función que realiza un diagnóstico basado en la base de conocimiento
def diagnostico(base):
    # Calculamos el promedio de los valores de certeza de los síntomas
    cf_total = (base["síntoma_fiebre"] + base["síntoma_dolor_cabeza"]) / 2
    
    # Evaluamos el nivel de certeza basado en el promedio calculado
    if cf_total > 0.7:
        # Alta certeza si el promedio es mayor a 0.7
        return f"Alta certeza de enfermedad ({cf_total})"
    elif cf_total > 0.4:
        # Certeza moderada si el promedio está entre 0.4 y 0.7
        return f"Certeza moderada ({cf_total})"
    else:
        # Baja certeza si el promedio es menor o igual a 0.4
        return f"Baja certeza ({cf_total})"

# Llamamos a la función de diagnóstico y mostramos el resultado
print(diagnostico(base_conocimiento))
