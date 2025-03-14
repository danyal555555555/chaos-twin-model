# plot_results.py
import numpy as np
import matplotlib.pyplot as plt

# Load data
def plot_results(t, x, y):
    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label='x(t)')
    plt.plot(t, y, label='y(t)', alpha=0.7)
    plt.title('Chaos Twin Simulation Results')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)
    plt.show()
