import math

import matplotlib.pyplot as plt
import numpy

from data_сlass.DataClass import DataClass

import numpy as np

from GUI import group_of_curves as gui_gc
from GUI import generic_curve as gui_generic
from approximation.approximation import *
from GUI.coef_comparison import coef_comparison

from data_сlass.help_functions import *
from Test.all_BNT_types import compare_max
from XML_Parser.ModelData import ModelData
from GUI.compare_max import compare_max
from GUI.compare_two_graph import *

time_duration = 2.5

md = ModelData("Model110")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)
# print(tau)
# print(X_eq)
# print(R_eq)

average_C0_1ph = -0.273
average_C1_1ph = 0.771

average_C0_diff_time_C = -0.3
average_C1_diff_time_C = 0.828

B_s = md.B_s
B_r_A = 0.0165
B_r_B = 0.0
B_r_C = -0.0165


ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A


coef_A_1ph_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
coef_A_2ph_cold = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
coef_A_3ph_1_cold = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph_2_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])
coef_A_diff_time_cold = coef_A_1ph_cold + 0.37 + 0.5 * B_r_A

# data = DataClass("csv", "110кV_new/", "110_BTN1phase", tau=tau, time_duration=time_duration)




# data = DataClass("csv", "110кV_new/", "110_BTN1phase", tau=tau, time_duration=time_duration)
#
#
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_A_time[:len(data.Imax_A_relative_time_partial)]+0.009,
#             data_Imax_relative_time=data.Imax_A_relative_time_partial,
#             data_current=data.I_A,
#             data_max_current=data.Imax_A[:len(data.Imax_A_relative_time_partial)],
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_1ph_cold,
#             phase='A',
#             title="Однофазный БТН",
#             model_data="Model110",
#             error=True)



# data = DataClass("csv", "110кV_new/", "110_BTN2phase", tau=tau, time_duration=time_duration)
# # plt.plot(data.Imax_C_time, data.Imax_C)
# # print(data.Imax_C_time)
# # print(data.Imax_C)
# # plt.show()
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_C_time[:len(data.Imax_C_relative_time_partial)]+0.0085,
#             data_Imax_relative_time=data.Imax_C_relative_time_partial,
#             data_current=-data.I_C,
#             data_max_current=-data.Imax_C[:len(data.Imax_C_relative_time_partial)],
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_2ph_cold,
#             phase='C',
#             title="Двухфазный БТН",
#             model_data="Model220",
#             error=True)
# # #
#
# data = DataClass("csv", "220kV_new/", "220_BTN3phase90", tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_B_time[:len(data.Imax_B_relative_time_partial)]+0.011,
#             data_Imax_relative_time=data.Imax_B_relative_time_partial,
#             data_current=data.I_B,
#             data_max_current=data.Imax_B[:len(data.Imax_B_relative_time_partial)],
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_3ph_1_cold,
#             phase='B',
#             title="Трехфазный БТН\n(1 типа)",
#             model_data="Model220",
#             error=True)
# #
# data = DataClass("csv", "220kV_new/", "220_BTN3phase0", tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_A_time[:len(data.Imax_A_relative_time_partial)]+0.01,
#             data_Imax_relative_time=data.Imax_A_relative_time_partial,
#             data_current=data.I_A,
#             data_max_current=data.Imax_A[:len(data.Imax_A_relative_time_partial)],
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_3ph_2_cold,
#             phase='A',
#             title="Трехфазный БТН\n(2 типа)",
#             model_data="Model220",
#             error=True)
#
# data = DataClass("csv", "220kV_new/", "220_BTN3phaseA0B90C90", tau=tau, time_duration=time_duration)
# plt.plot(data.time, data.I_A)
# plt.show()
# print(data.Imax_A_time)
# print(data.Imax_A)
# plt.plot(data.Imax_A_time, data.Imax_A)
# plt.show()
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_C_time[:len(data.Imax_C_relative_time_partial)]+0.012,
#             data_Imax_relative_time=data.Imax_C_relative_time_partial,
#             data_current=-data.I_C,
#             data_max_current=-data.Imax_C[:len(data.Imax_C_relative_time_partial)],
#             average_C0=average_C0_diff_time_C,
#             average_C1=average_C1_diff_time_C,
#             tau=tau,
#             coef_A=coef_A_diff_time_cold,
#             phase='C',
#             title="Последовательный БТН\n(разновр.)",
#             model_data="Model220",
#             error=True)
