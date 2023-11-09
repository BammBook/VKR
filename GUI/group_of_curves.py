import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from data_сlass.DataClass import DataClass
from typing import Literal

_TYPES = Literal["all", "half"]
_PHASES = Literal["A", "B", "C"]


def plot_group_of_curves(data: list[DataClass],
                         tau: list[int],
                         y_title='K_з(t), o.е.',
                         show_: _TYPES = "half",
                         phase_: _PHASES = "A"):
    """
    график кривых затухания с разными tau
    """
    if show_ == "half":
        half_checker = True
    elif show_ == "all":
        half_checker = False
    else:
        raise ValueError("Invalid sim type. Expected one of: %s" % _TYPES)

    legend = []

    mpl.rcParams['font.family'] = 'Times New Roman'
    mpl.rcParams['lines.linewidth'] = 0.9

    for i in range(len(data)):
        if i % 2 == 1 and i != len(data) and half_checker:
            pass
        else:
            legend.append(''r'$\tau$ = ' + str(tau[i]) + ' мс')
            if phase_ == "A":
                plt.plot(data[i].Imax_A_time,
                         data[i].Imax_A_relative,
                         label=''r'$\tau$ = ' + str(tau[i]) + ' мс')
            elif phase_ == "B":
                plt.plot(data[i].Imax_B_time,
                         data[i].Imax_B_relative,
                         label=''r'$\tau$ = ' + str(tau[i]) + ' мс')
            elif phase_ == "C":
                plt.plot(data[i].Imax_C_time,
                         data[i].Imax_C_relative,
                         label=''r'$\tau$ = ' + str(tau[i]) + ' мс')
            else:
                raise ValueError("Invalid sim type. Expected one of: %s" % _PHASES)

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(y_title, loc="center", fontsize=12)

    plt.xlim([0, 0.8 * data[0].time[np.size(data[0].time) - 1]])
    plt.ylim([-0.05, 1.05])

    # plt.legend(bbox_to_anchor=(1, 1))
    plt.legend(legend, loc='upper right')

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.4

    plt.show()
