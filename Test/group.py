import math

from PyResearch.data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from PyResearch.GUI import plot_value as gui_iv
from PyResearch.GUI import group_of_curves as gui_gc
from PyResearch.GUI import generic_curve as gui_generic
from PyResearch.approximation.approximation import *
from PyResearch.XML_Parser.ModelData import ModelData
from PyResearch.GUI import compare_two_graph as gui_two_graph
from PyResearch.GUI.compare_two_graph import set_relative_error

quantity_of_graph = 25
data = []
tau = []

args = []
C = []
C0 = []
C1 = []

for i in range(quantity_of_graph):
    tau.append((i + 1) * 20)
    # data.append(DataClass("csv", "data2/", "tau_" + str(tau[i]), time_duration=2.5))
    data.append(DataClass("csv", "data3/", "tau_" + str(tau[i]), time_duration=2.5))

    data[i].set_relative_time(tau[i])

    # args = approximation('exp_1',
    #                      data[i].Imax_A_relative_time,
    #                      data[i].Imax_A_to_relative_time,
    #                      print_coef=False)
    #
    # C0.append(args[0])
    # C1.append(args[1])

# gui_iv.plot_instant_value(data[3], tau[3])
# gui_gc.plot_group_of_curves(data, tau, show_="all")
gui_generic.plot_generic_curve(data, display_mode="partial")

# current_num = 10
# print(round(C0[current_num], 3))
# print(round(C1[current_num], 3))
#
# approximated_curve = exp_1(data[current_num].Imax_A_relative_time,
#                            C0[current_num],
#                            C1[current_num])
#
# plt.plot(data[current_num].Imax_A_relative_time * tau[current_num] * 1e-3, approximated_curve)
# plt.plot(data[current_num].Imax_A_time, data[current_num].Imax_A_relative)
# plt.show()
# """model_data"""
# md = ModelData("Model1")  # model_data
# X = 2 * math.pi * md.f * md.R * tau[current_num] * 1e-3  # X is variable
#
# coef_A0 = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (2 - md.B_s + md.B_r)
#
# """comparison"""
# approximated_graph = approximated_curve * coef_A0
#
# error = set_relative_error(data[current_num].Imax_A, approximated_graph)
#
# gui_two_graph.compare_two_graph(data[current_num].Imax_A_time, data[current_num].Imax_A,
#                                 data[current_num].Imax_A_time, approximated_graph,
#                                 tau=tau[current_num],
#                                 error_data=error,
#                                 plot_error=True)

# plt.plot(data[current_num].Imax_A_time, error)
# plt.grid(True)
# plt.show()
