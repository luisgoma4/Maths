import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Lista global para almacenar configuraciones de ondas
ondas_config = []

def agregar_onda(w=2*np.pi, k=np.pi, L=2, T=2, n_frames=100):
    """
    Agrega una configuración de onda a la lista global de ondas a animar.
    """
    ondas_config.append({
        'w': w,
        'k': k,
        'L': L,
        'T': T,
        'n_frames': n_frames
    })

def mostrar_animaciones():
    """
    Muestra todas las ondas almacenadas en una figura con subgráficos animados.
    """
    num_ondas = len(ondas_config)
    if num_ondas == 0:
        print("No hay ondas para mostrar. Usa agregar_onda primero.")
        return

    ncols = 2
    nrows = (num_ondas + 1) // ncols

    fig, axs = plt.subplots(nrows, ncols, figsize=(8, 4 * nrows), squeeze=False)
    fig.suptitle('Onda Estacionaria: y(x,t) = 2A sin(kx) cos(wt)', fontsize=14)

    lines = []
    datos = []
    t_vals = []

    # Preparar cada subplot
    for idx, config in enumerate(ondas_config):
        w, k, L, T, n_frames = config['w'], config['k'], config['L'], config['T'], config['n_frames']
        A = 1
        x = np.linspace(0, L, 500)
        t = np.linspace(0, T, n_frames)
        y = 2 * A * np.sin(k * x) * np.cos(w * t[0])

        row, col = divmod(idx, ncols)
        ax = axs[row][col]
        ax.set_xlim(0, L)
        ax.set_ylim(-2 * A, 2 * A)
        ax.set_title(f"w={w:.2f}, k={k:.2f}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        line, = ax.plot(x, y, lw=2)
        lines.append(line)
        datos.append((x, w, k))
        t_vals.append(t)

    # Rellenar subgráficos vacíos si hay un número impar
    for idx in range(len(ondas_config), nrows * ncols):
        row, col = divmod(idx, ncols)
        axs[row][col].axis("off")

    def actualizar(frame):
        for i, line in enumerate(lines):
            x, w, k = datos[i]
            t = t_vals[i][frame % len(t_vals[i])]
            y = 2 * np.sin(k * x) * np.cos(w * t)
            line.set_ydata(y)
        return lines

    ani = animation.FuncAnimation(fig, actualizar, frames=ondas_config[0]['n_frames'], interval=50, blit=True)
    plt.tight_layout()
    plt.show()

# Ejemplo de uso:
agregar_onda(w=2*np.pi, k=np.pi)
agregar_onda(w=4*np.pi, k=2*np.pi)
agregar_onda(w=np.pi, k=0.5*np.pi)
mostrar_animaciones()
