import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyResearch.data_сlass.DataClass import DataClass

def set_relative_error(y_real: list,
                       y_appr: list):
    error = np.abs(np.multiply(np.divide(np.subtract(y_real, y_appr), y_real), 100))
    return error


def compare_two_graph(x_real: list, y_real: list,
                      x_appr: list, y_appr: list,
                      title_1: str = 'Реальное значение',
                      title_2: str = 'Аппроксимированное значение',
                      tau=0):

    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.plot(x_real, y_real, color='black')
    mpl.rcParams['lines.linewidth'] = 1

    plt.plot(x_appr, y_appr, color='red')
    mpl.rcParams['lines.linewidth'] = 1.5

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel('Iₐ(t), кА', loc="center", fontsize=12)

    plt.xlim([0, x_real[np.size(x_real) - 1]])
    plt.ylim([-0.05 * np.max(y_real), 1.05 * np.max(y_real)])

    if tau <= 0:
        pass
    else:
        box = dict(facecolor='white', edgecolor='black')
        plt.text(0.7 * x_real[np.size(x_real) - 1],
                 0.7 * np.max(y_real),
                 ''r'$\tau$ =' + f'{tau} мс',
                 bbox=box)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

    plt.legend([title_1, title_2])

    plt.show()


