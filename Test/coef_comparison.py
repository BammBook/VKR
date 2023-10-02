import math

import numpy
import seaborn

from PyResearch.data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from PyResearch.GUI import instant_value as gui_iv
from PyResearch.GUI import group_of_curves as gui_gc
from PyResearch.GUI import generic_curve as gui_generic
from PyResearch.approximation.approximation import *
from PyResearch.GUI.coef_comparison import coef_comparison
from PyResearch.XML_Parser.ModelData import ModelData
from PyResearch.GUI import compare_two_graph as gui_two_graph
from PyResearch.GUI.compare_two_graph import set_relative_error
import seaborn as sns

quantity_of_graph = 25
quantity_of_args = 2
coef = np.zeros((quantity_of_args, quantity_of_graph))

data = []
tau = []
max_value = 5
time_duration = 2.5

for i in range(quantity_of_graph):
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "data2/", "tau_" + str(tau[i]), time_duration=time_duration))
    data[i].set_relative_time(tau[i])

    box_plot_data = []
    y_data = []
    for j in range(len(data[i].Imax_A_relative_time)):
        if data[i].Imax_A_relative_time[j] <= max_value:
            box_plot_data.append(data[i].Imax_A_relative_time[j])
            y_data.append(data[i].Imax_A_relative[j])

    data[i].Imax_A_relative_time_partial = box_plot_data
    data[i].Imax_A_relative_partial = y_data

    args = approximation('exp_3',
                         box_plot_data,
                         y_data,
                         print_coef=False)

    # args = approximation('exp_1',
    #                      data[i].Imax_A_relative_time,
    #                      data[i].Imax_A_relative,
    #                      print_coef=False)

    for j in range(quantity_of_args):
        coef[j, i] = round(args[j], 3)

"""graphs"""
# gui_iv.plot_instant_value(data[3], tau[3])
# gui_gc.plot_group_of_curves(data, tau, show_="half")
# gui_generic.plot_generic_curve(data, display_mode="full")

average_C0 = round(np.sum(coef[0]) / np.size(coef[0]), 3)
average_C1 = round(np.sum(coef[1]) / np.size(coef[1]), 3)

# average_C0 = round(coef[0, 10], 3)
# average_C1 = round(coef[1, 10], 3)
# print(average_C0)
# print(average_C1)


"""compare coefficient"""
coef_comparison(coef, tau)
#
# current_num = 20
#
# approximated_curve = exp_1(data[current_num].Imax_A_relative_time,
#                            average_C0,
#                            average_C1)

# """model_data"""
# md = ModelData("Model1")  # model_data
# X = 2 * math.pi * md.f * md.R * tau[current_num] * 1e-3  # X is variable
#
# coef_A0 = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (2 - md.B_s + md.B_r)
# approximated_graph = approximated_curve * coef_A0

# """мгновенные и огибающая"""
# mpl.rcParams['font.family'] = 'Times New Roman'
# plt.plot(data[current_num].time - 0.52, data[current_num].I_A, color='black', linewidth=0.5)
# plt.plot(data[current_num].Imax_A_time, approximated_graph, color='red', linewidth=2)
# plt.plot(data[current_num].Imax_A_time, data[current_num].Imax_A, color='grey', linewidth=0.02)
#
# plt.xlabel('t, с', loc="center", fontsize=12)
# plt.ylabel('Iₐ(t), кА', loc="center", fontsize=12)
# plt.legend(['iₐ(t) фактическое (RTDS)', 'iₐ_max(t) рассчитанное'])
#
# plt.xlim([0, data[current_num].Imax_A_time[len(data[0].Imax_A_time)-1]])
# box = dict(facecolor='white', edgecolor='black')
# plt.text(0.7 * data[current_num].Imax_A_time[len(data[0].Imax_A_time)-1],
#          0.7 * data[current_num].Imax_A[0],
#          ''r'$\tau$ =' + f'{tau[current_num]} мс',
#          bbox=box)
# plt.show()


# """comparison"""
#
# error = set_relative_error(data[current_num].Imax_A, approximated_graph)
#
# gui_two_graph.compare_two_graph(data[current_num].Imax_A_time, data[current_num].Imax_A,
#                                 data[current_num].Imax_A_time, approximated_graph,
#                                 tau=tau[current_num],
#                                 error_data=error,
#                                 plot_error=True)


"""box_plot"""
# md = ModelData("Model1")
# number_of_measurement_point = len(data[0].Imax_A_time)
# error = np.zeros((quantity_of_graph, number_of_measurement_point))
#
# for i in range(quantity_of_graph):
#     approximated_curve = exp_1(data[i].Imax_A_relative_time,
#                                average_C0,
#                                average_C1)
#     # model_data
#     X = 2 * math.pi * md.f * md.R * tau[i] * 1e-3  # X is variable
#     coef_A0 = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (2 - md.B_s + md.B_r)
#     approximated_graph = approximated_curve * coef_A0
#
#     error[i] = set_relative_error(data[i].Imax_A, approximated_graph)
#
# print(error.shape)
#
#
# box_plot_data = []
# step = 10
# t_labels = []
#
#
# for i in range(0, error.shape[1], step):
#     box_plot_data.append(error[:, i])
#     t_labels.append(str(round(i * 0.02, 1)))
#


"""box_plot_2"""
md = ModelData("Model1")
number_of_measurement_point = len(data[0].Imax_A_time)
# error = np.zeros((quantity_of_graph, number_of_measurement_point))

error = []

# матрица со строками разной длины. Значеняи ошибки от времени
for i in range(quantity_of_graph):

    approximated_curve = exp_1(data[i].Imax_A_relative_time,
                               average_C0,
                               average_C1)
    # model_data
    X = 2 * math.pi * md.f * md.R * tau[i] * 1e-3  # X is variable
    coef_A0 = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (2 - md.B_s + md.B_r)
    approximated_graph = approximated_curve * coef_A0

    error_buff = set_relative_error(data[i].Imax_A, approximated_graph)
    buffer = []
    for j in range(len(data[i].Imax_A_relative_time_partial)):
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

# print(box_plot_data)

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

[item.get_ydata() for item in box['whiskers']]


plt.show()
