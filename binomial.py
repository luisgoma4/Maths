import numpy as np  
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import factorial

def binomial_distribution():
    n_flips = 1000
    p = 0.5
    k = np.arange(0, n_flips + 1)  # Valores enteros posibles de caras (should start at 0)

    # Usamos la fórmula del coeficiente binomial con factoriales:
    # P(k) = C(n, k) * p^k * (1-p)^(n-k)
    # C(n, k) = n! / (k! * (n-k)!)
    coef = factorial(n_flips) / (factorial(k) * factorial(n_flips - k))
    probabilities = coef * (p ** k) * ((1 - p) ** (n_flips - k))  # Fixed exponent

    plt.figure(figsize=(10, 6))
    plt.plot(k, probabilities, label='Binomial Distribution (manual)', color='green')
    plt.title('Binomial Distribution (n=1000, p=0.5) - Manual Calculation')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.xlim(400, 600)  # Zoom in around the mean
    plt.ylim(0, 0.03)   # Adjusted y-axis limit
    plt.grid()
    plt.legend()
    plt.show()

binomial_distribution()