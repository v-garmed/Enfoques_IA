# Simulamos una red bayesiana simple con relaciones entre variables
# Variables: A → X ← B → C

# A y B son padres de X
# X y B son padres de C

# Manto de Markov de X = {A, B, C}

# Definimos un conjunto de relaciones
red = {
    "A": {"hijos": ["X"]},
    "B": {"hijos": ["X", "C"]},
    "X": {"padres": ["A", "B"], "hijos": ["C"]},
    "C": {"padres": ["X", "B"]}
}

# Función para obtener el manto de Markov de una variable
def obtener_manto_markov(variable, red):
    padres = set(red[variable].get("padres", []))
    hijos = set(red[variable].get("hijos", []))
    co_padres = set()

    for hijo in hijos:
        co_padres.update(red[hijo].get("padres", []))
    
    manto = padres.union(hijos).union(co_padres)
    manto.discard(variable)  # Quitamos la variable misma
    return manto

# Manto de Markov de X
manto_x = obtener_manto_markov("X", red)
print("Manto de Markov de X:", manto_x)
