import numpy as np

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz si es invertible."""
    try:
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        return "La matriz no es invertible"

# Ejemplo de uso
A = np.array([[1, 0, 3], [2, 2, 1], [0, 1, 0]])
inversa_A = calcular_inversa(A)
print(inversa_A)