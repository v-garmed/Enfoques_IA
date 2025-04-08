import matplotlib.pyplot as plt

# Definimos los posibles valores del dado
valores_dado = [1, 2, 3, 4, 5, 6]

# Distribución de probabilidad uniforme (todas las caras tienen la misma probabilidad)
probabilidades = [1/6] * 6

# Mostramos la distribución de probabilidad
for valor, prob in zip(valores_dado, probabilidades):
    print(f"P({valor}) = {prob}")

# Graficamos la distribución
plt.bar(valores_dado, probabilidades, color='skyblue', edgecolor='black')
plt.xlabel('Valor del dado')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad del Dado')
plt.ylim(0, 0.25)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
