# chaos_twin_functions.py
import numpy as np

def h(x):
    return x**3

def g(x):
    return np.sin(x)

def phi(x):
    return 0.1 * np.random.randn()
