import numpy as np
import matplotlib.pyplot as plt

# Definición del campo vectorial
def sistema(A, J):
    A_prime = A + J
    J_prime = -A + J
    return A_prime, J_prime

# Crear una cuadrícula de puntos (A, J)
A_vals = np.linspace(-5, 5, 20)
J_vals = np.linspace(-5, 5, 20)
A, J = np.meshgrid(A_vals, J_vals)

# Calcular las derivadas en cada punto
A_prime, J_prime = sistema(A, J)

# Normalizar los vectores para que el gráfico sea más claro
magnitude = np.sqrt(A_prime**2 + J_prime**2)
A_prime_norm = A_prime / magnitude
J_prime_norm = J_prime / magnitude

# Graficar el campo vectorial
plt.figure(figsize=(8, 6))
plt.quiver(A, J, A_prime_norm, J_prime_norm, angles='xy')
plt.xlabel('A')
plt.ylabel('J')
plt.title("Campo vectorial del sistema: A' = A + J, J' = -A + J")
plt.grid()
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.show()