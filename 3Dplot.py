import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos la función
def C(x, y):
    return (x**2)/2 - x + y**2 - 4*y + x*y + 100

# Gradiente de C
def grad_C(x, y):
    dC_dx = x - 1 + y
    dC_dy = 2*y - 4 + x
    return dC_dx, dC_dy

# Matriz Hessiana (constante en este caso)
def hessiana_C():
    return np.array([[1, 1],
                     [1, 2]])

# Mallado
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)
Z = C(X, Y)

# Gradiente
U, V = grad_C(X, Y)

# Figura
fig = plt.figure(figsize=(14, 6))

# Superficie 3D
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.set_title('Superficie de C(x, y)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('C(x, y)')

# Campo de gradiente
ax2 = fig.add_subplot(1, 2, 2)
ax2.contour(X, Y, Z, levels=20, cmap='viridis')
ax2.quiver(X, Y, U, V, color='red')
ax2.set_title('Campo de gradiente de C(x, y)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.tight_layout()
plt.show()

# Mostrar matriz Hessiana
print("Matriz Hessiana de C(x, y):")
print(hessiana_C())