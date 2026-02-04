import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animar_onda_estacionaria(w=2*np.pi, k=np.pi, L=2, T=2, n_frames=100):
    """
    Anima una onda estacionaria del tipo: y(x, t) = 2 * A * sin(kx) * cos(wt)
    
    Parámetros:
    - w: frecuencia angular (rad/s)
    - k: número de onda (rad/m)
    - L: longitud del dominio espacial
    - T: duración total del ciclo en segundos (por defecto un periodo completo)
    - n_frames: número de cuadros de la animación
    """
    A = 1  # amplitud
    x = np.linspace(0, L, 500)
    t_vals = np.linspace(0, T, n_frames)

    fig, ax = plt.subplots()
    line, = ax.plot(x, np.zeros_like(x), lw=2)
    ax.set_ylim(-2*A, 2*A)
    ax.set_xlim(0, L)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Onda Estacionaria: y(x,t) = 2A sin(kx) cos(wt)')

    def actualizar(frame):
        t = t_vals[frame]
        y = 2 * A * np.sin(k * x) * np.cos(w * t)
        line.set_ydata(y)
        return line,

    ani = animation.FuncAnimation(
        fig, actualizar, frames=n_frames, interval=50, blit=True
    )
    plt.show()

    

# Ejemplo de uso:
animar_onda_estacionaria(w=10*np.pi, k=np.pi/6, L=24)  # puedes cambiar w y k aquí

