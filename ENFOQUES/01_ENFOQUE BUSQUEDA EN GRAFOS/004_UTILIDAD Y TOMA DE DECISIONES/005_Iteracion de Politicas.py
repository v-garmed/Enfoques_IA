# Definimos los estados posibles en el problema
states = ['A', 'B', 'C']

# Definimos las acciones posibles que se pueden tomar desde cada estado
actions = ['left', 'right']

# Modelo de transición y recompensa:
# T es un diccionario que define para cada estado y acción:
# - El siguiente estado al que se transita
# - La recompensa obtenida al tomar esa acción
T = {
    'A': {'left': ('A', 0), 'right': ('B', 5)},
    'B': {'left': ('A', 0), 'right': ('C', 10)},
    'C': {'left': ('B', 0), 'right': ('C', 0)},
}

# Factor de descuento (gamma) que pondera la importancia de las recompensas futuras
gamma = 0.9

# Inicializamos una política arbitraria (todas las acciones son 'left' inicialmente)
policy = {s: 'left' for s in states}

# Inicializamos los valores de los estados en 0
V = {s: 0 for s in states}

# Función para evaluar una política dada
# Actualiza los valores de los estados (V) en función de la política actual
def evaluar_politica(policy, V, iteraciones=10):
    for _ in range(iteraciones):  # Iteramos un número fijo de veces
        for s in states:  # Para cada estado
            a = policy[s]  # Obtenemos la acción definida por la política
            s_next, r = T[s][a]  # Obtenemos el siguiente estado y la recompensa
            V[s] = r + gamma * V[s_next]  # Actualizamos el valor del estado
    return V

# Función para mejorar la política basada en los valores actuales de los estados
# Busca la mejor acción para cada estado y actualiza la política
def mejorar_politica(V, policy):
    estable = True  # Indicador de si la política es estable
    for s in states:  # Para cada estado
        mejores_valores = {}  # Diccionario para almacenar los valores de cada acción
        for a in actions:  # Para cada acción posible
            s_next, r = T[s][a]  # Obtenemos el siguiente estado y la recompensa
            mejores_valores[a] = r + gamma * V[s_next]  # Calculamos el valor de la acción
        mejor_accion = max(mejores_valores, key=mejores_valores.get)  # Elegimos la mejor acción
        if mejor_accion != policy[s]:  # Si la mejor acción no coincide con la actual
            policy[s] = mejor_accion  # Actualizamos la política
            estable = False  # Marcamos que la política no es estable
    return policy, estable

# Proceso de iteración de políticas
# Alternamos entre evaluar la política y mejorarla hasta que sea estable
estable = False
while not estable:
    V = evaluar_politica(policy, V)  # Evaluamos la política actual
    policy, estable = mejorar_politica(V, policy)  # Mejoramos la política

# Imprimimos los valores finales de los estados y la política óptima encontrada
print("Valores finales:", V)
print("Política óptima:", policy)
