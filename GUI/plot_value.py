import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyResearch.data_сlass.DataClass import DataClass


def plot_value(time: np.ndarray,
               y_data: np.ndarray,
               tau=None,
               phase='A'):

    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.plot(time, y_data, color='black')
    mpl.rcParams['lines.linewidth'] = 1

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(f'I_{phase}(t), кА', loc="center", fontsize=12)

    plt.xlim([0, time[-1]])
    max = np.max(y_data)
    min = np.min(y_data)
    if np.abs(max) > np.abs(min):
        plt.ylim([-0.05 * max, 1.05 * max])
    else:
        plt.ylim([1.05 * min, 0.05 * np.abs(min)])

    if tau is None:
        pass
    else:
        box = dict(facecolor='white', edgecolor='black')
        if np.abs(max) > np.abs(min):
            y_position = 0.7 * max
        else:
            y_position = 0.7 * min
        plt.text(0.7 * time[-1],
                 y_position,
                 ''r'$\tau$ =' + f'{tau} мс',
                 bbox=box)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

    plt.show()


def inst_and_max_curve(real_time: np.ndarray,
                       real_value: np.ndarray,
                       max_time: np.ndarray,
                       max_I: np.ndarray,
                       tau=None,
                       phase='A'):
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.plot(real_time - 0.52, real_value, color='black', linewidth=0.5)
    plt.plot(max_time, max_I, color='red', linewidth=2)

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(f'I_{phase}(t), кА', loc="center", fontsize=12)
    plt.legend([f'i_{phase}(t) фактическое (RTDS)', f'i_{phase}_max(t) рассчитанное'])

    plt.xlim([0, real_time[-1]])
    max = np.max(real_value)
    min = np.min(real_value)
    if np.abs(max) > np.abs(min):
        plt.ylim([-0.05 * max, 1.05 * max])
    else:
        plt.ylim([1.05 * min, 0.05 * np.abs(min)])
    box = dict(facecolor='white', edgecolor='black')
    plt.text(0.7 * real_time[-1],
             0.7 * max_I[0],
             ''r'$\tau$ =' + f'{tau} мс',
             bbox=box)
    plt.show()
