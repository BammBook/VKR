import math

import numpy as np
from matplotlib import pyplot as plt

from GUI.presentation import presentation
from approximation.approximation import exp_1
from XML_Parser.ModelData import ModelData
from data_сlass.help_functions import *
from typing import Literal

"""scheme coefficients matrix"""
BTN_TYPES = Literal['1ph', '2ph', '3ph1', '3ph2', 'diff_time']
RELAY_TYPES = Literal['phase', 'linear', 'zero_sequence']

columns = {'1ph': 0, '2ph': 1, '3ph1': 2, '3ph2': 3, 'diff_time': 4}
rows = {'phase': 0, 'linear': 1, 'zero_sequence': 2}

SCHEME_COEFFICIENTS = np.array([[1, 1, 1, 1, 1],
                                [1, math.sqrt(3), math.sqrt(3), 1.26, 1.7],
                                [1, 1, 1, 0.7, 0.7]])


def compare_effective_current(eff_curr_time,
                              eff_curr_data,
                              model_Imax_relative_time,
                              model_Imax_time,
                              model_data_name,
                              average_C0,
                              average_C1,
                              btn_type: BTN_TYPES,
                              relay_type: RELAY_TYPES,
                              coef_A,
                              title,
                              phase):

    """
    Сравнение действующего тока снятого с модели и расчетного
    """
    column = columns.get(btn_type)
    row = rows.get(relay_type)
    scheme_coef = SCHEME_COEFFICIENTS[row, column]

    generic_curve = exp_1(model_Imax_relative_time,
                          average_C0,
                          average_C1)

    md = ModelData(model_data_name)
    convert_to_named_units_coef = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(md.X ** 2 + md.R ** 2))

    curve_first_harm_eff = scheme_coef * convert_to_named_units_coef * first_harm_effective(coef_A) * generic_curve

    presentation()
    plt.grid(True)
    plt.plot(eff_curr_time, eff_curr_data, color='red')
    plt.plot(model_Imax_time, curve_first_harm_eff, color='blue')
    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(f'I_1г_{phase}, кА', loc="center", fontsize=12)
    plt.legend([f'I_1г_{phase} Фактическое (RTDS)', f'I_1г_{phase} Рассчитанное'])

    # plt.xlim([0, model_Imax_time[-1]])

    max = curve_first_harm_eff[0]

    box = dict(facecolor='white', edgecolor='black')

    plt.text(0.7 * model_Imax_time[-1],
             0.7 * max,
             f'{title}\n{phase}',
             bbox=box)

    """relative error"""
    samle_rate = 50e-6
    time_ax_points = model_Imax_time * samle_rate

    buffer_time = []
    buffer_current = []
    for i in range(len(eff_curr_time)):
        if i % 400 == 0 and eff_curr_time[i] > 0 and eff_curr_time[i] <= model_Imax_time[-1]:
            buffer_time.append(round(eff_curr_time[i], 2))
            buffer_current.append(eff_curr_data[i])

    buffer_time = np.array(buffer_time)
    buffer_current = np.array(buffer_current)

    print(f'len_curve_first_harm_eff = {len(curve_first_harm_eff)}')
    print(f'len_eff_curr_data = {len(buffer_time)}')

    print(model_Imax_relative_time)
    print()
    print(buffer_time)


    # error = (buffer_current - curve_first_harm_eff)/buffer_current
    # print(error)

    plt.show()


