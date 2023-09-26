import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyResearch.data_сlass.DataClass import DataClass


def plot_generic_curve(data: list[DataClass]):
    mpl.rcParams['font.family'] = 'Times New Roman'
    mpl.rcParams['lines.linewidth'] = 0.9

    for i in range(len(data)):
        plt.plot(data[i].Imax_A_relative_time,
                 data[i].Imax_A_relative)
        # legend.append(''r'$\tau$ = ' + str(tau[i]) + ' мс')

    plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
    plt.ylabel('Iₐ(t/'r'$\tau$), о.е.', loc="center", fontsize=12)

    plt.xlim([0, data[0].Imax_A_relative_time[np.size(data[0].Imax_A_relative_time) - 1]])
    plt.ylim([-0.05, 1.05])

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.4

    plt.show()
