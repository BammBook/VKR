import numpy as np
import matplotlib.pyplot as plt
from GUI.presentation import presentation
from data_сlass.DataClass import DataClass
from data_сlass.help_functions import *
from XML_Parser.ModelData import ModelData

from approximation.approximation import *
from approximation.approximation import *

def compare_max(data_time, data_max_time,
                data_Imax_relative_time,
                data_current, data_max_current,
                average_C0,
                average_C1,
                tau: int,
                coef_A,
                phase,
                title
                ):
    approximated_curve = exp_1(data_Imax_relative_time,
                               average_C0,
                               average_C1)
    md = ModelData("Model1")
    X = 2 * math.pi * md.f * md.R * tau * 1e-3  # X is variable

    approximated_graph = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * approximated_curve * (
                1 + coef_A)

    """мгновенные и огибающая"""
    presentation()
    plt.plot(data_time, data_current, color='black', linewidth=0.5)
    plt.plot(data_max_time, approximated_graph, color='red', linewidth=2)
    plt.plot(data_max_time, data_max_current, color='grey', linewidth=0.02)
    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel(f'I_{phase}(t), кА', loc="center", fontsize=12)
    plt.legend([f'i_{phase}(t) фактическое (RTDS)', f'i_{phase}_max(t) рассчитанное'])

    plt.xlim([0, data_time[-1]])
    box = dict(facecolor='white', edgecolor='black')
    plt.text(0.7 * data_time[-1],
             0.7 * max(data_max_current),
             f'{title}\nФаза {phase}\n'r'$\tau$ =' + f'{tau} мс',
             bbox=box)

    plt.show()


# 1 Phase BNT
# for phase A
average_C0_1ph = -0.273
average_C1_1ph = 0.771

# 2 Phase BNT
# for phase B, C (Grounded)
average_C0_2ph = -0.234
average_C1_2ph = 0.876

# 3 Phase BNT (type 1)
# for phase B, C
average_C0_3ph_1 = -0.239
average_C1_3ph_1 = 0.869

# 3 Phase BNT (type 2)
# for phase A
average_C0_3ph_2 = -0.266
average_C1_3ph_2 = 0.781

average_C0_diff_time = -0.285
average_C1_diff_time = 0.914



# коэф. затухания
x_data = np.arange(0, 5, 0.01)
generic_curve_1ph = exp_1(x_data, average_C0_1ph, average_C1_1ph)
generic_curve_2ph = exp_1(x_data, average_C0_2ph, average_C1_2ph)
generic_curve_3ph_1 = exp_1(x_data, average_C0_3ph_1, average_C1_3ph_1)
generic_curve_3ph_2 = exp_1(x_data, average_C0_3ph_2, average_C1_3ph_2)
generic_curve_diff_time = exp_1(x_data, average_C0_diff_time, average_C1_diff_time)


generic_curve = generic_curve_1ph

# presentation()  # коэффииенты затухания
# plt.plot(x_data, generic_curve_1ph)
# plt.plot(x_data, generic_curve_2ph)
# plt.plot(x_data, generic_curve_3ph_1)
# plt.plot(x_data, generic_curve_3ph_2)
# plt.legend(['1ф.БТН', '2ф.БТН', '3ф.БТН (1 тип)', '3ф.БТН (2 тип)'])
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
B_r = 0.42
ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A

# coef_A_1ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_1ph[0], omega_t0=ang_1ph[1], BNT_type='1ph_BNT')
# coef_A_1ph_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_1ph[0], omega_t0=ang_1ph[1], BNT_type='1ph_BNT')

coef_A_1ph_cold = 0.39
coef_A_1ph_hot = 0.06

# coef_A_2ph_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_2ph[0], omega_t0=ang_2ph[1], BNT_type='2ph_BNT')
# coef_A_2ph_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_2ph[0], omega_t0=ang_2ph[1], BNT_type='2ph_BNT')

coef_A_2ph_cold = 0.39-0.13
coef_A_2ph_hot = 0.06-0.13

coef_A_3ph_1_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph_1_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])

coef_A_3ph_2_cold = coef_A(B_s=B_s_cold, B_r=B_r, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])
coef_A_3ph_2_hot = coef_A(B_s=B_s_hot, B_r=B_r, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])




curve_C_1ph_cold = math.sqrt(2) * effective_current(coef_A_1ph_cold) * generic_curve
curve_C_1ph_hot = math.sqrt(2) * effective_current(coef_A_1ph_hot) * generic_curve

curve_C_2ph_cold = math.sqrt(2) * effective_current(coef_A_2ph_cold) * generic_curve
curve_C_2ph_hot = math.sqrt(2) * effective_current(coef_A_2ph_hot) * generic_curve

curve_C_3ph_1_cold = math.sqrt(2) * effective_current(coef_A_3ph_1_cold) * generic_curve
curve_C_3ph_1_hot = math.sqrt(2) * effective_current(coef_A_3ph_1_hot) * generic_curve

curve_C_3ph_2_cold = math.sqrt(2) * effective_current(coef_A_3ph_2_cold) * generic_curve
curve_C_3ph_2_hot = math.sqrt(2) * effective_current(coef_A_3ph_2_hot) * generic_curve



# presentation()  # коэффициенты С
# plt.grid(True)
# plt.plot(x_data, curve_C_1ph_cold)
# plt.plot(Ttau, C_b_1_cold)
#
# plt.legend(['1ф.БТН, холоднокат.',
#             'Кривая по РУ, холоднокат.'])
# plt.xlim([x_data[0], x_data[-1]])
# plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
# plt.ylabel('C_b, о.е.', loc="center", fontsize=12)
# plt.show()


# presentation()  # коэффициенты С
# plt.grid(True)
# plt.plot(x_data, curve_C_1ph_hot)
# plt.plot(Ttau, C_b_1_hot)
#
# plt.legend(['1ф.БТН, горячекат.',
#             'Кривая по РУ, гоячекат.'])
# plt.xlim([x_data[0], x_data[-1]])
# plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
# plt.ylabel('C_b, о.е.', loc="center", fontsize=12)
# plt.show()


# presentation()  # коэффициенты С
# plt.grid(True)
# plt.plot(x_data, curve_C_2ph_cold)
# plt.plot(Ttau, C_b_2_cold)
#
# plt.legend(['2ф.БТН, холоднокат.',
#             'Кривая по РУ, холоднокат.'])
# plt.xlim([x_data[0], x_data[-1]])
# plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
# plt.ylabel('C_b, о.е.', loc="center", fontsize=12)
# plt.show()


# presentation()  # коэффициенты С
# plt.grid(True)
# plt.plot(x_data, curve_C_2ph_hot)
# plt.plot(Ttau, C_b_2_hot)
#
# plt.legend(['2ф.БТН, горячекат.',
#             'Кривая по РУ, горячекат.'])
# plt.xlim([x_data[0], x_data[-1]])
# plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
# plt.ylabel('C_b, о.е.', loc="center", fontsize=12)
# plt.show()
