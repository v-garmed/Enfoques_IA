# Importar librerías necesarias
import numpy as np
from hmmlearn import hmm

# Definir las semillas aleatorias para reproducibilidad
np.random.seed(42)

# Definir los estados y observaciones posibles
states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

# Definir las probabilidades iniciales de los estados
# Por ejemplo, hay un 60% de probabilidad de que comience lloviendo y un 40% de que esté soleado
start_probability = np.array([0.6, 0.4])

# Definir la matriz de transición entre estados
# Por ejemplo, si hoy está lloviendo, hay un 70% de probabilidad de que mañana también llueva
transition_probability = np.array([
    [0.7, 0.3],  # Probabilidades de transición desde 'Rainy'
    [0.4, 0.6]   # Probabilidades de transición desde 'Sunny'
])

# Definir la matriz de emisión de observaciones
# Por ejemplo, si está lloviendo, hay un 10% de probabilidad de que la observación sea 'walk'
emission_probability = np.array([
    [0.1, 0.4, 0.5],  # Probabilidades de observaciones desde 'Rainy'
    [0.6, 0.3, 0.1]   # Probabilidades de observaciones desde 'Sunny'
])

# Crear el modelo HMM con 2 estados ocultos
model = hmm.MultinomialHMM(n_components=2)

# Establecer las probabilidades iniciales, de transición y de emisión en el modelo
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability

# Generar una secuencia de observaciones y sus estados ocultos correspondientes
# La función sample genera una secuencia de observaciones y estados ocultos de longitud 20
observed_sequence, hidden_states = model.sample(20)

# Imprimir la secuencia de observaciones generada
print("Observed sequence:", observed_sequence)

# Predecir la secuencia de estados ocultos a partir de las observaciones generadas
# La función predict toma la secuencia de observaciones y devuelve la secuencia de estados ocultos más probable
predicted_hidden_states = model.predict(observed_sequence.reshape(-1, 1))

# Imprimir la secuencia de estados ocultos predicha
print("Predicted hidden states:", predicted_hidden_states)
