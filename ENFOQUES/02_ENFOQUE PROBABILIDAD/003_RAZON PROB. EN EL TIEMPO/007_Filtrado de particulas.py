import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
n_particles = 1000
true_pos = 0.0
vel = 1.0
noise_process = 1.0
noise_measure = 2.0
steps = 10

# Inicializar partículas y pesos
particles = np.random.normal(0.0, 5.0, n_particles)
weights = np.ones(n_particles) / n_particles

# Simulación del sistema
for t in range(steps):
    # Movimiento real del objeto
    true_pos += vel + np.random.normal(0, noise_process)
    
    # Medición observada con ruido
    z = true_pos + np.random.normal(0, noise_measure)

    # PREDICCIÓN: mover partículas
    particles += vel + np.random.normal(0, noise_process, n_particles)

    # ACTUALIZACIÓN: calcular pesos según la medición
    weights *= np.exp(-0.5 * ((z - particles) / noise_measure) ** 2)
    weights += 1.e-300  # evitar división por cero
    weights /= np.sum(weights)

    # RESAMPLING: muestreo según pesos
    indices = np.random.choice(range(n_particles), size=n_particles, p=weights)
    particles = particles[indices]
    weights = np.ones(n_particles) / n_particles  # reiniciar pesos

    # Estimación actual
    estimate = np.mean(particles)
    print(f"Paso {t+1} -> Posición real: {true_pos:.2f}, Estimada: {estimate:.2f}")

