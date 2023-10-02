import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyResearch.data_сlass.DataClass import DataClass
from typing import Literal

_TYPES = Literal["full", "partial"]


def plot_generic_curve(data: list[DataClass],
                       display_mode: _TYPES = "partial",
                       max_value: int = 5):
    mpl.rcParams['font.family'] = 'Times New Roman'
    mpl.rcParams['lines.linewidth'] = 0.9

    for i in range(len(data)):

        if display_mode == "full":
            x_data = data[i].Imax_A_relative_time
            y_data = data[i].Imax_A_relative
        elif display_mode == "partial":
            x_data = []
            y_data = []
            for j in range(len(data[i].Imax_A_relative_time)):
                if data[i].Imax_A_relative_time[j] <= max_value:
                    x_data.append(data[i].Imax_A_relative_time[j])
                    y_data.append(data[i].Imax_A_relative[j])
        else:
            raise ValueError("Invalid sim type. Expected one of: %s" % _TYPES)

        plt.plot(x_data, y_data)

        if i == 0:
            plt.xlim([0, x_data[len(x_data) - 1]])
            plt.ylim([-0.05, 1.05])

    plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
    plt.ylabel('K_з(t/'r'$\tau$), о.е.', loc="center", fontsize=12)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.4

    plt.show()
