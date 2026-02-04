#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 17:35:44 2025

@author: luisga
"""

import numpy as np

def diagonalizar_matriz(A):
    # Calculamos los autovalores y autovectores
    valores, vectores = np.linalg.eig(A)
    
    # Matriz diagonal con los autovalores
    D = np.diag(valores)
    
    # Matriz de paso con los autovectores como columnas
    P = vectores
    
    # Matriz inversa de P
    P_inv = np.linalg.inv(P)
    
    return D, P, P_inv

# Ejemplo de uso
A = np.array([[3, -5, -3], 
              [-3, 7, 5], 
              [0, 0, -1]])
print(A)



D, P, P_inv = diagonalizar_matriz(A)

print("Matriz diagonal D:")
print(D)
print("\nMatriz de cambio de base P:")
print(P)
print("\nMatriz inversa de P:")
print(P_inv)
