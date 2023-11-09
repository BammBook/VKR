import math

import numpy as np
from matplotlib import pyplot as plt

from GUI.presentation import presentation
from XML_Parser.ModelData import ModelData
from approximation.approximation import exp_1
from GUI.compare_two_graph import set_relative_error


def compare_max(data_time, data_max_time,
                data_Imax_relative_time,
                data_current, data_max_current,
                average_C0,
                average_C1,
                tau: int,
                coef_A,
                phase,
                title,
                model_data,
                error=False):
    """
    сравение огибающей кривой максимумов и рассчитываемой кривой
    """

    approximated_curve = exp_1(data_Imax_relative_time,
                               average_C0,
                               average_C1)
    md = ModelData(model_data)
    # X = 2 * math.pi * md.f * md.R * tau * 1e-3  # X is variable
    approximated_graph = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(md.X ** 2 + md.R ** 2)) * approximated_curve * (1 + coef_A)

    """мгновенные и огибающая"""
    presentation()
    plt.plot(data_time, data_current, color='black', linewidth=0.5)
    plt.plot(data_max_time, approximated_graph, color='red', linewidth=2)
    plt.plot(data_max_time, data_max_current, color='grey', linewidth=0.5)
    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(f'I_{phase}(t), кА', loc="center", fontsize=12)
    plt.legend([f'i_{phase}(t) фактическое (RTDS)', f'i_{phase}_max(t) рассчитанное'])
    plt.grid(True)

    plt.xlim([0, data_max_time[-1]])

    max = np.max(data_current)
    min = np.min(data_current)
    # if np.abs(max) > np.abs(min):
    #     plt.ylim([-0.05 * max, 1.05 * max])
    # else:
    #     plt.ylim([1.05 * min, 0.05 * np.abs(min)])

    box = dict(facecolor='white', edgecolor='black')
    if np.abs(max) > np.abs(min):
        y_position = 0.7 * max
    else:
        y_position = 0.7 * min
    plt.text(0.7 * data_max_time[-1],
             y_position,
             f'{title}\nФаза {phase}\n'r'$\tau$ =' + f'{tau} мс',
             bbox=box)

    plt.show()

    if error:
        # error = set_relative_error(data_max_current, approximated_graph)
        error = np.round(np.abs(np.abs(data_max_current - approximated_graph)/data_max_current)*100, 2)
        print(error)
        # output = []
        # for i in range(len(error)):
        #     if i % 5 == 0:
        #         output.append(round(error[i]*100, 2))
        # print(output)

        presentation()
        plt.grid(True)
        plt.plot(data_max_time, error)
        plt.xlabel('t, с', loc="center", fontsize=12)
        plt.ylabel(''r'$\delta$, %', loc="center", fontsize=12)
        plt.xlim([0, data_max_time[-1]])

        plt.show()
