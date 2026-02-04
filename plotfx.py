
import numpy as np
import matplotlib.pyplot as plt

def plot(fucn, min=-10, max=10, step=0.1, title=''):
    
    x = np.arange(min, max, step)
    y = fucn(x)
    
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid()
    plt.show()
    
func = lambda x: ((x+2)**2-1)
plot(func, -10, 10, 0.1, 'Quadratic Function')
