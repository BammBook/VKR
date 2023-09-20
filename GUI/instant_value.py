import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from data_class.DataClassNP import DataClass

def plot_instant_value(data: DataClass,  tau=0, y_title='Iₐ(t), кА'):
    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.plot(data.time, data.I_A, color='black')
    mpl.rcParams['lines.linewidth'] = 1

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(y_title, loc="center", fontsize=12)

    plt.xlim([0, data.time[np.size(data.time) - 1]])
    plt.ylim([-0.05 * np.max(data.I_A), 1.05 * np.max(data.I_A)])

    if tau <= 0:
        pass
    else:
        box = dict(facecolor='white', edgecolor='black')
        plt.text(0.7 * data.time[np.size(data.time) - 1],
                 0.7 * np.max(data.I_A),
                 ''r'$\tau$ =' + f'{tau} мс',
                 bbox=box)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

    plt.show()
