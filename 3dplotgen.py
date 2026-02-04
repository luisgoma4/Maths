# Escribe una funcion que tome como entrada la ecuacion de una superficie en funcion de x, y
# represente graficamente la superficie en tres dimensiones, y que represente tambien el campo vectorial de gradientes en dos dimensiones

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def representar_superficie_y_gradiente(f_expr):
    # Definimos variables simbólicas
    x = sp.symbols('x')
    y = sp.symbols('y')
    # Calculamos gradiente y hessiana
    grad = [sp.diff(f_expr, var) for var in (x, y)]
    hess = sp.hessian(f_expr, (x, y))
    
    # Imprimimos la hessiana
    print("Hessiana:")
    sp.pprint(hess)

    # Convertimos a funciones numéricasP
    f_num = sp.lambdify((x, y), f_expr, 'numpy')
    grad_num = [sp.lambdify((x, y), g, 'numpy') for g in grad]
    
    # Dominio
    X_vals = np.linspace(-20, 20, 40)
    Y_vals = np.linspace(-20, 20, 40)
    X, Y = np.meshgrid(X_vals, Y_vals)
    Z = f_num(X, Y)
    
    # Gradiente numérico
    U = grad_num[0](X, Y)
    V = grad_num[1](X, Y)

    # Gráfica
    fig = plt.figure(figsize=(12, 6))

    # Superficie
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='Spectral', alpha=0.8)
    ax1.set_title("Superficie f(x, y)")
    ax1.set_xlabel('x')
    ax1.set_ylabel('y') 
    
    # Campo de gradiente
    ax2 = fig.add_subplot(122)
    ax2.contourf(X, Y, Z, cmap='Spectral', alpha=0.6)
    ax2.quiver(X, Y, U, V, color='r')
    ax2.set_title("Campo del gradiente ∇f")
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')


    plt.tight_layout()
    plt.show()

x, y = sp.symbols('x y')
f = x**3-6*y*x+y**2+7
representar_superficie_y_gradiente(f)