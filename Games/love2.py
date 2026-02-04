import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definición del sistema de ecuaciones
def sistema(t, Y):
    A, J = Y
    dA_dt = - A + J
    dJ_dt = -A + J
    return [dA_dt, dJ_dt]

# Crear una cuadrícula de puntos
A_vals = np.linspace(-5, 5, 20)
J_vals = np.linspace(-5, 5, 20)
A, J = np.meshgrid(A_vals, J_vals)

# Evaluar el campo vectorial
A_prime, J_prime = sistema(0, [A, J])
magnitude = np.sqrt(A_prime**2 + J_prime**2)
A_prime_norm = A_prime / magnitude
J_prime_norm = J_prime / magnitude

# Preparar la figura
plt.figure(figsize=(10, 8))

# Dibujar el campo vectorial
plt.quiver(A, J, A_prime_norm, J_prime_norm, angles='xy', color='gray', alpha=0.6)

# Puntos iniciales para las trayectorias
puntos_iniciales = [
    (-4, -4), (-2, 2), (2, -2), (4, 4), (0, 1), (1, 0), (-1, -1), (3, 0)
]

# Tiempos para integrar
t_span = (0, 10)
t_eval = np.linspace(*t_span, 300)

# Graficar trayectorias
for A0, J0 in puntos_iniciales:
    sol = solve_ivp(sistema, t_span, [A0, J0], t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1], label=f"A0={A0}, J0={J0}")

# Curvas de campo constante
# Usaremos V(A, J) = A² + J² como ejemplo (tipo energía)
V = A**2 + J**2
contours = plt.contour(A, J, V, levels=10, cmap='Blues', alpha=0.6)
plt.clabel(contours, inline=True, fontsize=8)

# Formato de la gráfica
plt.xlabel('A')
plt.ylabel('J')
plt.title("Campo vectorial, trayectorias y curvas de campo constante")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()