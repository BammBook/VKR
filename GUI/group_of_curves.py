import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from data_class.DataClassNP import DataClass
from typing import Literal

_TYPES = Literal["all", "half"]


def plot_instant_value(data: list[DataClass],
                       tau: list[int],
                       y_title='Iₐ(t), o.е.',
                       show_: _TYPES = "half"):
    if show_ == "half":
        half_checker = True
    elif show_ == "all":
        half_checker = False
    else:
        raise ValueError("Invalid sim type. Expected one of: %s" % _TYPES)

    mpl.rcParams['font.family'] = 'Times New Roman'
    mpl.rcParams['lines.linewidth'] = 0.9

    for i in range(len(data)):
        if i % 2 == 1 and i != len(data) and half_checker:
            pass
        else:
            plt.plot(data[i].Imax_A_time,
                     data[i].Imax_A_relative,
                     label=''r'$\tau$ = ' + str(tau[i]) + ' мс')

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(y_title, loc="center", fontsize=12)

    plt.xlim([0, 0.8 * data[0].time[np.size(data[0].time) - 1]])
    plt.ylim([-0.05, 1.05])

    plt.legend(bbox_to_anchor=(1, 1))

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.4

    plt.show()
