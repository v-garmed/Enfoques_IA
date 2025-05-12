# Definimos una base de conocimiento inicial como un diccionario.
# En este caso, se indica que "es_pajaro" es True (es un pájaro) y "vuela" es True (puede volar).
base_conocimiento = {
    "es_pajaro": True,
    "vuela": True
}

# Definimos una nueva información que se añadirá a la base de conocimiento.
# Aquí se indica que "es_pinguino" es True (es un pingüino).
nueva_info = {
    "es_pinguino": True
}

# Definimos una función que implementa razonamiento no monótonico.
# Este tipo de razonamiento permite que las conclusiones cambien al incorporar nueva información.
def razonamiento_no_monotonico(base, nueva_info):
    # Si en la base de conocimiento se indica que es un pájaro y no se indica que es un pingüino,
    # entonces concluimos que el ave vuela.
    if base.get("es_pajaro") and not nueva_info.get("es_pinguino"):
        return "El ave vuela"
    else:
        # En caso contrario, concluimos que el ave no vuela.
        return "El ave no vuela"

# Llamamos a la función de razonamiento no monótonico con la base de conocimiento y la nueva información.
# Imprimimos la conclusión obtenida.
print("Conclusión:", razonamiento_no_monotonico(base_conocimiento, nueva_info))
