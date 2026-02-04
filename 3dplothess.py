import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d import Axes3D

# Función
def C(x, y):
    return (x**2)/2 - x + y**2 - 4*y + x*y + 100

# Gradiente
def grad_C(x, y):
    dC_dx = x - 1 + y
    dC_dy = 2*y - 4 + x
    return dC_dx, dC_dy

# Hessiana (constante)
def hessiana_C():
    return np.array([[1, 1],
                     [1, 2]])

# Elipse de curvatura en base a la Hessiana
def plot_hessian_ellipse(ax, x0, y0, scale=0.5):
    H = hessiana_C()
    eigvals, eigvecs = np.linalg.eigh(H)
    angle = np.degrees(np.arctan2(eigvecs[1, 0], eigvecs[0, 0]))
    width, height = 2 * scale * np.sqrt(eigvals)
    ell = Ellipse((x0, y0), width, height, angle=angle, edgecolor='red',
                  facecolor='none', lw=1)
    ax.add_patch(ell)

# Mallado
x = np.linspace(-4, 4, 30)
y = np.linspace(-4, 4, 30)
X, Y = np.meshgrid(x, y)
Z = C(X, Y)
U, V = grad_C(X, Y)

# Figura
fig, ax = plt.subplots(figsize=(8, 6))
contours = ax.contour(X, Y, Z, levels=20, cmap='viridis')
ax.quiver(X, Y, U, V, color='gray', alpha=0.5)

# Elipses de la Hessiana
points = [(-2, -2), (0, 0), (2, 2), (2, -2), (-2, 2)]
for x0, y0 in points:
    plot_hessian_ellipse(ax, x0, y0)

ax.set_title('Curvas de nivel, gradiente y elipses de curvatura (Hessiana)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')

plt.show()