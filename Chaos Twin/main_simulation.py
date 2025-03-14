# main_simulation.py
import numpy as np
import matplotlib.pyplot as plt
from chaos_twin_functions import h, g, phi

# Parameters
sigma = 3.0
delta = 0.5
kappa = 0.2
dt = 0.01
T = 1000
t = np.arange(0, T, dt)

# Initialize variables
x = np.zeros_like(t)
y = np.zeros_like(t)
x[0] = 0.5
y[0] = 1.0

# Simulation loop
for i in range(len(t) - 1):
    dx = sigma * (y[i] - x[i]) + delta * (h(x[i]) - g(x[i])) + kappa * phi(x[i])
    dy = -sigma * (x[i] - y[i]) + delta * (g(x[i]) - h(x[i]))
    x[i + 1] = x[i] + dx * dt
    y[i + 1] = y[i] + dy * dt

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)', alpha=0.7)
plt.title('Chaos Twin Simulation')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
