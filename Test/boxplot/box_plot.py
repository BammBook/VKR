import math

import numpy


from data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from GUI import plot_value as gui_iv
from GUI import group_of_curves as gui_gc
from GUI import generic_curve as gui_generic
from approximation.approximation import *
from GUI.coef_comparison import coef_comparison
from XML_Parser.ModelData import ModelData
from GUI import compare_two_graph as gui_two_graph
from GUI.compare_two_graph import set_relative_error


from data_сlass.help_functions import coef_A

quantity_of_graph = 25
quantity_of_args = 2
coef = np.zeros((quantity_of_args, quantity_of_graph))

data = []
tau = []
max_value = 5
time_duration = 2.5

for i in range(quantity_of_graph):
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "BNT_2ph_no_gnd/", "tau_" + str(tau[i]), tau=tau[i],  time_duration=time_duration))


average_C0 = -0.273
average_C1 = 0.771

average_C0_diff_time = -0.285
average_C1_diff_time = 0.914

B_s_cold = 1.21
B_r = 0

ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_2ph_no_Gnd = [1 * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A

coef_A_1ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
coef_A_2ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
coef_A_2ph_no_Gnd_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_2ph_no_Gnd[0], omega_t0=ang_2ph_no_Gnd[1])
coef_A_3ph_1_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph_2_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])
coef_A_diff_time_cold = coef_A_1ph_cold + 0.37 + 0.5*B_r


"""box_plot"""
md = ModelData("Model1")
number_of_measurement_point = len(data[0].Imax_B_time)
# error = np.zeros((quantity_of_graph, number_of_measurement_point))

error = []

# матрица со строками разной длины. Значеняи ошибки от времени
for i in range(quantity_of_graph):

    approximated_curve = exp_1(data[i].Imax_B_relative_time,
                               average_C0_diff_time,
                               average_C1_diff_time)
    # model_data
    X = 2 * math.pi * md.f * md.R * tau[i] * 1e-3  # X is variable
    coef = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (1+coef_A_2ph_no_Gnd_cold)
    approximated_graph = approximated_curve * coef

    error_buff = set_relative_error(data[i].Imax_B, approximated_graph)
    buffer = []
    for j in range(len(data[i].Imax_B_relative_time_partial)):
        buffer.append(error_buff[j])
    error.append(buffer)
# print(error)

step = 10
# box_plot_data = [[] for i in range(10)]


box_plot_data = []

for j in range(0, len(error[-1]), 10):
    buffer = []
    for i in range(len(error)):
        if len(error[i]) > j - 1:
            buffer.append(error[i][j])
    box_plot_data.append(buffer)

print(box_plot_data)

max_err_time = np.arange(1, 11)
max_err = np.full(np.size(max_err_time), 10)

numbers = np.arange(0, 10, 1)
t_labels = np.round(0.2 * numbers, 1)

mpl.rcParams['font.family'] = 'Times New Roman'
plt.xlabel('t, с', loc="center", fontsize=12)
plt.ylabel(''r'$\delta$, %', loc="center", fontsize=12)
plt.grid(True)

plt.plot(max_err_time, max_err, color='red')
plt.legend([''r'$\delta$ = 10%'])
box = plt.boxplot(box_plot_data, labels=t_labels)

medians = [round(item.get_ydata()[1], 2) for item in box['medians']]
average_medians = np.round(np.average(medians), 2)
for med in medians:
    print(med)
print('average medians = ', average_medians)


total = 0
for i in range(len(box_plot_data)):
    counter = 0
    for j in range(len(box_plot_data[i])):
        if box_plot_data[i][j] > 10:
            counter += 1
            total += 1
    print(counter)
print('total = ', total)

plt.show()

