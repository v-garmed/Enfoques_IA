from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Datos: tamaño de la casa (m2), precio (mil dólares)
X = np.array([[50], [60], [100], [120], [150]])
y = np.array([100, 120, 200, 240, 300])

reg = DecisionTreeRegressor(max_depth=3)
reg.fit(X, y)

# Predecir precio para una casa de 110 m2
print("Predicción para 110 m2:", reg.predict([[110]]))
