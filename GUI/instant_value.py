import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
def plot_instant_value(x_data, y_data, tau=None, y_title='Iₐ(t), кА'):
    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.plot(x_data, y_data, color='black')
    mpl.rcParams['lines.linewidth'] = 1

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(y_title, loc="center", fontsize=12)

    plt.xlim([0, x_data[np.size(x_data) - 1]])
    plt.ylim([-0.05 * np.max(y_data), 1.05 * np.max(y_data)])

    box = dict(facecolor='white', edgecolor='black')
    plt.text(0.7 * x_data[np.size(x_data) - 1],
             0.7 * np.max(y_data),
             ''r'$\tau$ =' + f'{tau} мс',
             bbox=box)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

    plt.show()
