import math

import numpy
import seaborn

from PyResearch.data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from PyResearch.GUI.plot_value import plot_value, inst_and_max_curve
from PyResearch.GUI import group_of_curves as gui_gc
from PyResearch.GUI import generic_curve as gui_generic
from PyResearch.approximation.approximation import *
from PyResearch.GUI.coef_comparison import coef_comparison
from PyResearch.XML_Parser.ModelData import ModelData
from PyResearch.GUI import compare_two_graph as gui_two_graph
from PyResearch.GUI.compare_two_graph import set_relative_error
import seaborn as sns

data = []
tau = []
time_duration = 2.5

quantity_of_graph = 25
quantity_of_args = 2

coef_A = np.zeros((quantity_of_args, quantity_of_graph))
coef_B = np.zeros((quantity_of_args, quantity_of_graph))
coef_C = np.zeros((quantity_of_args, quantity_of_graph))

for i in range(quantity_of_graph):
    """
    1ph_BNT/, 2ph_BNT/, 3ph_BNT_(2_type)/, 3ph_BNT_(2_type)/
    """
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "3ph_BNT_(1_type)/", "tau_" + str(tau[i]), tau=tau[i],  time_duration=time_duration))

    args_B = approximation('exp_1',
                           data[i].Imax_B_relative_time_partial,
                           data[i].Imax_B_relative_partial,
                           print_coef=False)
    args_C = approximation('exp_1',
                           data[i].Imax_C_relative_time_partial,
                           data[i].Imax_C_relative_partial,
                           print_coef=False)

    for j in range(quantity_of_args):
        coef_B[j, i] = round(args_B[j], 3)
        coef_C[j, i] = round(args_C[j], 3)

average_C0_B = round(np.average(coef_B[0]), 3)
average_C1_B = round(np.average(coef_B[1]), 3)
print(f'average_C0_B = {average_C0_B}')
print(f'average_C1_B = {average_C1_B}')

average_C0_C = round(np.average(coef_C[0]), 3)
average_C1_C = round(np.average(coef_C[1]), 3)
print(f'average_C0_C = {average_C0_C}')
print(f'average_C1_C = {average_C1_C}')

current_num = 10
plt.plot(data[current_num].time, data[current_num].I_A, color='yellow')
plt.plot(data[current_num].time, data[current_num].I_B, color='green')
plt.plot(data[current_num].time, data[current_num].I_C, color='red')
plt.legend(['I_A', 'I_B', 'I_C'])
plt.show()

plt.plot(data[current_num].Imax_B_relative_time, data[current_num].Imax_B_relative, color='green')
plt.plot(data[current_num].Imax_C_relative_time, data[current_num].Imax_C_relative, color='red')
plt.legend(['Imax_B', 'Imax_C'])
plt.show()



