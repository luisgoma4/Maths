# writte some one variable functions and represent them in a graph
import numpy as np
import matplotlib.pyplot as plt             

def plot_function(f, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = f(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"f(x) = {f.__name__}(x)")
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()  

# Example functions
def f1(x):
    return x**2 
def f2(x):
    return np.sin(x)
def f3(x):
    return np.exp(-x**2)      

plot_function(f1, x_range=(-10, 10))

# now plot in the same figure three grafs, the function, its derivative and its integral
def plot_function_with_derivative_and_integral(f, x_range=(-10, 10), num_points=1000):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y = f(x)
    
    # Derivative
    h = 1e-5
    y_derivative = (f(x + h) - f(x - h)) / (2 * h)
    
    # Integral using cumulative trapezoidal rule
    y_integral = np.cumsum(y) * (x[1] - x[0])
    
    plt.figure(figsize=(12, 8))
    
    # Function plot
    plt.subplot(3, 1, 1)
    plt.plot(x, y, label=f"f(x) = {f.__name__}(x)")
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    
    # Derivative plot
    plt.subplot(3, 1, 2)
    plt.plot(x, y_derivative, label="f'(x)", color='orange')
    plt.title("Derivative Plot")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    
    # Integral plot
    plt.subplot(3, 1, 3)
    plt.plot(x, y_integral, label="∫f(x)dx", color='green')
    plt.title("Integral Plot")
    plt.xlabel("x")
    plt.ylabel("∫f(x)dx")
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.grid()
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Example functions
def f1(x):
    return x**2
def f2(x):
    return np.sin(x)
def f3(x):  
    return np.exp(-x**2)

plot_function_with_derivative_and_integral(f1, x_range=(-10, 10))
plot_function_with_derivative_and_integral(f2, x_range=(-10, 10))
plot_function_with_derivative_and_integral(f3, x_range=(-10, 10))   