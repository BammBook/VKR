import math

import numpy as np
import matplotlib.pyplot as plt
from GUI.presentation import presentation
from GUI.two_curves import two_curves
from data_сlass.DataClass import DataClass
from data_сlass.help_functions import *
from XML_Parser.ModelData import ModelData

from approximation.approximation import *
from GUI.compare_max import compare_max




# 1 Phase BNT
# for phase A
average_C0_1ph = -0.273
average_C1_1ph = 0.771

# 2 Phase BNT
# for phase B, C (Grounded)
average_C0_2ph = -0.234
average_C1_2ph = 0.876

# 2 Phase BNT
# for phase B, C (NO Grounded)
average_C0_2ph_no_Gnd = -0.271
average_C1_2ph_no_Gnd = 0.915

# 3 Phase BNT (type 1)
# for phase B, C
average_C0_3ph_1 = -0.239
average_C1_3ph_1 = 0.869

# 3 Phase BNT (type 2)
# for phase A
average_C0_3ph_2 = -0.266
average_C1_3ph_2 = 0.781

average_C0_diff_time_A = -0.285
average_C1_diff_time_A = 0.914

average_C0_diff_time_C = -0.3
average_C1_diff_time_C = 0.828


# коэф. затухания
x_data = np.arange(0, 5, 0.01)
generic_curve_1ph = exp_1(x_data, average_C0_1ph, average_C1_1ph)
generic_curve_2ph = exp_1(x_data, average_C0_2ph, average_C1_2ph)
generic_curve_2ph_no_Gnd = exp_1(x_data, average_C0_2ph_no_Gnd, average_C1_2ph_no_Gnd)
generic_curve_3ph_1 = exp_1(x_data, average_C0_3ph_1, average_C1_3ph_1)
generic_curve_3ph_2 = exp_1(x_data, average_C0_3ph_2, average_C1_3ph_2)
generic_curve_diff_time = exp_1(x_data, average_C0_diff_time_A, average_C1_diff_time_A)

generic_curve = generic_curve_1ph
generic_curve_diff_time_C = exp_1(x_data, average_C0_diff_time_C, average_C1_diff_time_C)
# presentation()  # коэффииенты затухания
# plt.grid(True)
# plt.plot(x_data, generic_curve_1ph)
# plt.plot(x_data, generic_curve_2ph_no_Gnd)
# plt.plot(x_data, generic_curve_2ph)
# plt.plot(x_data, generic_curve_3ph_1)
# plt.plot(x_data, generic_curve_3ph_2)
# plt.plot(x_data, generic_curve_diff_time)
# # plt.plot(x_data, generic_curve_diff_time_C)
#
# plt.legend(['1ф.БТН', '2ф.БТН (Изолир.)', '2ф.БТН (Заземл.)', '3ф.БТН (1 тип)', '3ф.БТН (2 тип)', 'Последовательный БТН (ф.А)'])
#
# plt.xlim([x_data[0], x_data[-1]])
# plt.ylim([-0.05, 1.05])
#
# plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
# plt.ylabel('k_з, о.е.', loc="center", fontsize=12)
#
# plt.show()

"""---------"""

B_s_cold = 1.21
B_s_hot = 1.38
B_r = 0.4
ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_2ph_no_Gnd = [1 * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A

coef_A_1ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
coef_A_1ph_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
# print(f'coef_A_1ph_cold = {round(coef_A_1ph_cold, 3)}')
# print(f'coef_A_1ph_hot = {round(coef_A_1ph_hot, 3)}\n')

coef_A_2ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
coef_A_2ph_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
# print(f'coef_A_2ph_cold = {round(coef_A_2ph_cold, 3)}')
# print(f'coef_A_2ph_hot = {round(coef_A_2ph_hot, 3)}\n')

coef_A_2ph_no_Gnd_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_2ph_no_Gnd[0], omega_t0=ang_2ph_no_Gnd[1])
coef_A_2ph_no_Gnd_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_2ph_no_Gnd[0], omega_t0=ang_2ph_no_Gnd[1])

coef_A_3ph_1_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph_1_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])

coef_A_3ph_2_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])
coef_A_3ph_2_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])

coef_A_diff_time_cold = coef_A_1ph_cold + 0.37 + 0.5 * B_r
coef_A_diff_time_hot = coef_A_1ph_hot + 0.37 + 0.5 * B_r
# print(coef_A_diff_time_cold)
# print(coef_A_diff_time_hot)

"""кривые С"""
curve_C_1ph_cold = math.sqrt(2) * effective_current(coef_A_1ph_cold) * generic_curve
curve_C_1ph_hot = math.sqrt(2) * effective_current(coef_A_1ph_hot) * generic_curve
# print(effective_current(coef_A_1ph_cold))
curve_C_2ph_cold = math.sqrt(2) * effective_current(coef_A_2ph_cold) * generic_curve
curve_C_2ph_hot = math.sqrt(2) * effective_current(coef_A_2ph_hot) * generic_curve

curve_C_2ph_no_Gnd_cold = math.sqrt(2) * effective_current(coef_A_2ph_no_Gnd_cold) * generic_curve_diff_time
curve_C_2ph_no_Gnd_hot = math.sqrt(2) * effective_current(coef_A_2ph_no_Gnd_hot) * generic_curve_diff_time

curve_C_3ph_1_cold = math.sqrt(2) * effective_current(coef_A_3ph_1_cold) * generic_curve
curve_C_3ph_1_hot = math.sqrt(2) * effective_current(coef_A_3ph_1_hot) * generic_curve

curve_C_3ph_2_cold = math.sqrt(2) * effective_current(coef_A_3ph_2_cold) * generic_curve
curve_C_3ph_2_hot = math.sqrt(2) * effective_current(coef_A_3ph_2_hot) * generic_curve

curve_C_diff_time_cold = math.sqrt(2) * effective_current(coef_A_diff_time_cold) * generic_curve_diff_time
curve_C_diff_time_hot = math.sqrt(2) * effective_current(coef_A_diff_time_hot) * generic_curve_diff_time


"""первая гармоника"""
curve_first_harm_eff_1ph_cold = first_harm_effective(coef_A_1ph_cold) * generic_curve
curve_first_harm_eff_1ph_hot = first_harm_effective(coef_A_1ph_hot) * generic_curve
# print(first_harm_effective(coef_A_1ph_cold))
curve_first_harm_eff_2ph_cold = first_harm_effective(coef_A_2ph_cold) * generic_curve
curve_first_harm_eff_2ph_hot = first_harm_effective(coef_A_2ph_hot) * generic_curve

curve_first_harm_eff_2ph_no_Gnd_cold = first_harm_effective(coef_A_2ph_no_Gnd_cold) * generic_curve_diff_time
curve_first_harm_eff_2ph_no_Gnd_hot = first_harm_effective(coef_A_2ph_no_Gnd_hot) * generic_curve_diff_time

curve_first_harm_eff_3ph_1_cold = first_harm_effective(coef_A_3ph_1_cold) * generic_curve
curve_first_harm_eff_3ph_1_hot = first_harm_effective(coef_A_3ph_1_hot) * generic_curve

curve_first_harm_eff_3ph_2_cold = first_harm_effective(coef_A_3ph_2_cold) * generic_curve
curve_first_harm_eff_3ph_2_hot = first_harm_effective(coef_A_3ph_2_hot) * generic_curve

curve_first_harm_diff_time_cold = first_harm_effective(coef_A_diff_time_cold) * generic_curve_diff_time
curve_first_harm_diff_time_hot = first_harm_effective(coef_A_diff_time_hot) * generic_curve_diff_time

"""first harmonic effective"""
# two_curves(x_data, curve_first_harm_eff_1ph_cold,
#            x_data, curve_first_harm_eff_1ph_hot,
#            legend=['1ф.БТН, холоднокат.', '1ф.БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')
#
# two_curves(x_data, curve_first_harm_eff_2ph_cold,
#            x_data, curve_first_harm_eff_2ph_hot,
#            legend=['2ф.БТН, холоднокат.', '2ф.БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')

# two_curves(x_data, curve_first_harm_eff_2ph_no_Gnd_cold,
#            x_data, curve_first_harm_eff_2ph_no_Gnd_hot,
#            legend=['2ф.БТН (Изолир.), холоднокат.', '2ф.БТН (Изолир.), горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')
#
# two_curves(x_data, curve_first_harm_eff_3ph_1_cold,
#            x_data, curve_first_harm_eff_3ph_1_hot,
#            legend=['3ф.БТН (1 тип), холоднокат.', '3ф.БТН (1 тип), горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')
#
# two_curves(x_data, curve_first_harm_eff_3ph_2_cold,
#            x_data, curve_first_harm_eff_3ph_2_hot,
#            legend=['3ф.БТН (2 тип), холоднокат.', '3ф.БТН (2 тип), горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')

# two_curves(x_data, curve_first_harm_diff_time_cold,
#            x_data, curve_first_harm_diff_time_hot,
#            legend=['Последовательный БТН, холоднокат.', 'Последовательный БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_1г, о.е.')

"""coefficient C curve"""
# two_curves(x_data, curve_C_1ph_cold,
#            x_data, curve_C_1ph_hot,
#            legend=['1ф.БТН, холоднокат.', '1ф.БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_b, о.е.')
#
# two_curves(x_data, curve_C_2ph_cold,
#            x_data, curve_C_2ph_hot,
#            legend=['2ф.БТН, холоднокат.', '2ф.БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_b, о.е.')

two_curves(x_data, curve_C_2ph_no_Gnd_cold,
           x_data, curve_C_2ph_no_Gnd_hot,
           legend=['2ф.БТН, холоднокат.', '2ф.БТН, горячекат.'],
           xlabel='t/'r'$\tau$',
           ylabel='C_b, о.е.')

# two_curves(x_data, curve_C_3ph_1_cold,
#            x_data, curve_C_3ph_1_hot,
#            legend=['3ф.БТН (1 тип), холоднокат.', '3ф.БТН (1 тип), горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_b, о.е.')
#
# two_curves(x_data, curve_C_3ph_2_cold,
#            x_data, curve_C_3ph_2_hot,
#            legend=['3ф.БТН (2 тип), холоднокат.', '3ф.БТН (2 тип), горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_b, о.е.')

# two_curves(x_data, curve_C_diff_time_cold,
#            x_data, curve_C_diff_time_hot,
#            legend=['Последовательный БТН, холоднокат.', 'Последовательный БТН, горячекат.'],
#            xlabel='t/'r'$\tau$',
#            ylabel='C_b, о.е.')



# """Сравнение максимумов"""
md = ModelData("Model1")
time_duration = 2.5
tau = 200

data_1ph = DataClass("csv", "1ph_True_360/", "tau_" + str(tau), tau=tau, time_duration=time_duration)
# #
# compare_max(data_time=data_1ph.time,
#             data_max_time=data_1ph.Imax_A_time,
#             data_Imax_relative_time=data_1ph.Imax_A_relative_time,
#             data_current=data_1ph.I_A,
#             data_max_current=data_1ph.Imax_A,
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_1ph_cold,
#             phase='A',
#             title="1ф. БТН")
# #
# data_2ph = DataClass("csv", "2ph_True_Gnd/", "tau_" + str(tau), tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data_2ph.time,
#             data_max_time=data_2ph.Imax_B_time,
#             data_Imax_relative_time=data_2ph.Imax_B_relative_time,
#             data_current=data_2ph.I_B,
#             data_max_current=data_2ph.Imax_B,
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_2ph_cold,
#             phase='B',
#             title="2ф. БТН")
#
# data_3ph_1 = DataClass("csv", "3ph_BNT_(1_type)/", "tau_" + str(tau), tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data_3ph_1.time,
#             data_max_time=data_3ph_1.Imax_B_time,
#             data_Imax_relative_time=data_3ph_1.Imax_B_relative_time,
#             data_current=data_3ph_1.I_B,
#             data_max_current=data_3ph_1.Imax_B,
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_3ph_1_cold,
#             phase='B',
#             title="3ф. БТН (1 тип)")
#
# data_3ph_2 = DataClass("csv", "3ph_BNT_(2_type)/", "tau_" + str(tau), tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data_3ph_2.time,
#             data_max_time=data_3ph_2.Imax_A_time,
#             data_Imax_relative_time=data_3ph_2.Imax_A_relative_time,
#             data_current=data_3ph_2.I_A,
#             data_max_current=data_3ph_2.Imax_A,
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_3ph_2_cold,
#             phase='A',
#             title="3ф. БТН (2 тип)")

# data_2ph_diff_time = DataClass("csv", "2ph_diff_time/", "tau_" + str(tau), tau=tau, time_duration=time_duration)
# "model_data/csv_files/220kV/BTN3phase.csv"
# compare_max(data_time=data_2ph_diff_time.time,
#             data_max_time=data_2ph_diff_time.Imax_C_time,
#             data_Imax_relative_time=data_2ph_diff_time.Imax_C_relative_time,
#             data_current=-data_2ph_diff_time.I_C,
#             data_max_current=data_2ph_diff_time.Imax_C,
#             average_C0=average_C0_diff_time_C,
#             average_C1=average_C1_diff_time_C,
#             tau=tau,
#             coef_A=coef_A_diff_time_cold,
#             phase='С',
#             title="Последовательный БТН\n(разновременный)",
#             model_data="Model1")
