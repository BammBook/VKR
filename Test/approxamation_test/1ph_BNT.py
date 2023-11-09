import math

import numpy


from data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from GUI.plot_value import plot_value, inst_and_max_curve
from GUI import group_of_curves as gui_gc
from GUI import generic_curve as gui_generic
from approximation.approximation import *
from GUI.coef_comparison import coef_comparison
from XML_Parser.ModelData import ModelData
from GUI import compare_two_graph as gui_two_graph
from GUI.compare_two_graph import set_relative_error

from data_сlass.help_functions import *
from GUI.presentation import presentation


data = []
tau = []
time_duration = 2.5

quantity_of_graph = 25
quantity_of_args = 2

current_num = 10

coefs_A = np.zeros((quantity_of_args, quantity_of_graph))

for i in range(quantity_of_graph):
    """
    1ph_BNT/, 2ph_BNT/, 3ph_BNT_(2_type)/, 3ph_BNT_(2_type)/
    """
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "1ph_True_360/", "tau_" + str(tau[i]), tau=tau[i],  time_duration=time_duration))

    args_A = approximation('exp_1',
                           data[i].Imax_A_relative_time_partial,
                           data[i].Imax_A_relative_partial,
                           print_coef=False)

    for j in range(quantity_of_args):
        coefs_A[j, i] = round(args_A[j], 3)

average_C0_A = round(np.average(coefs_A[0]), 3)
average_C1_A = round(np.average(coefs_A[1]), 3)


print(f'average_C0_A = {average_C0_A}')
print(f'average_C1_A = {average_C1_A}')

gui_gc.plot_group_of_curves(data, tau, show_="half")
gui_generic.plot_generic_curve(data, display_mode="partial")

coef_comparison(coefs_A, tau)

# plt.plot(data[current_num].time, data[current_num].I_A, color='yellow')
# plt.plot(data[current_num].time, data[current_num].I_B, color='green')
# plt.plot(data[current_num].time, data[current_num].I_C, color='red')
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()
#
# plt.plot(data[current_num].Imax_A_relative_time, data[current_num].Imax_A_relative, color='yellow')
# plt.legend(['Imax_A'])
# plt.show()


