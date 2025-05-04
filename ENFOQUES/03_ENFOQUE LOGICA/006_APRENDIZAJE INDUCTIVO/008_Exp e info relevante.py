def clasificar_estudiante(estudiante):
    if estudiante['nota_final'] >= 90:
        return "Excelente (por nota >= 90)"
    elif estudiante['asistencia'] < 70:
        return "Reprobado (por baja asistencia)"
    elif estudiante['nota_final'] >= 60:
        return "Aprobado (por nota >= 60)"
    else:
        return "Reprobado (por nota < 60)"

# Ejemplo de estudiantes
estudiantes = [
    {'nombre': 'Lucía', 'nota_final': 95, 'asistencia': 85},
    {'nombre': 'Carlos', 'nota_final': 65, 'asistencia': 50},
    {'nombre': 'Elena', 'nota_final': 58, 'asistencia': 80},
]

# Mostrar explicaciones
for e in estudiantes:
    resultado = clasificar_estudiante(e)
    print(f"{e['nombre']}: {resultado}")
