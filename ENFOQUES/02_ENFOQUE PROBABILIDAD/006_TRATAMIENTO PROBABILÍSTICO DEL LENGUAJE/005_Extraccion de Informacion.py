import re

# Texto de entrada
texto = """
Elon Musk fundó SpaceX en 2002 en California. También es CEO de Tesla.
Mark Zuckerberg creó Facebook en 2004.
Bill Gates fue presidente de Microsoft hasta el año 2000.
"""

# Patrones básicos (muy simplificados)
patron_personas = r"(Elon Musk|Mark Zuckerberg|Bill Gates)"
patron_organizaciones = r"(SpaceX|Facebook|Tesla|Microsoft)"
patron_fechas = r"\b(19|20)\d{2}\b"

# Buscar coincidencias
personas = re.findall(patron_personas, texto)
organizaciones = re.findall(patron_organizaciones, texto)
fechas = re.findall(patron_fechas, texto)

# Mostrar resultados
print("Personas encontradas:", set(personas))
print("Organizaciones encontradas:", set(organizaciones))
print("Fechas encontradas:", set([f"{a}xx" for a in fechas]))
