#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:30:54 2025

@author: luisga
"""

import numpy as np

def derivada(p):
    """Calcula la derivada de un polinomio representado por coeficientes."""
    n = len(p) - 1
    return np.array([p[i] * (n - i) for i in range(n)])

def newton_raphson(p, x0, tol=1e-6, max_iter=100):
    """Método de Newton-Raphson para encontrar una raíz del polinomio."""
    dp = derivada(p)
    for _ in range(max_iter):
        fx = np.polyval(p, x0)
        dfx = np.polyval(dp, x0)
        if abs(fx) < tol:
            return x0
        if dfx == 0:
            break
        x0 -= fx / dfx
    return None

def encontrar_raices(p, tol=1e-6):
    """Encuentra todas las raíces de un polinomio utilizando Newton-Raphson y deflación."""
    n = len(p) - 1
    raices = []
    while n > 0:
        x0 = np.random.uniform(-10, 10)
        raiz = newton_raphson(p, x0, tol)
        if raiz is not None:
            raices.append(raiz)
            p = np.polydiv(p, [1, -raiz])[0]  # División sintética
            n -= 1
        else:
            break
    return raices

# Ejemplo de uso
p = np.array([-3, -3, +6])  # Polinomio x^3 - 6x^2 + 11x - 6
raices = encontrar_raices(p)
print("Raíces:", raices)
