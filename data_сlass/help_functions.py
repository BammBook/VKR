import math
from typing import Literal
import matplotlib.pyplot as plt

"""Кривые Засыпкина (Из РУ)"""

Ttau = [0.000, 0.250, 0.500, 0.750, 1.000, 1.250, 1.500, 1.750, 2.000, 2.250, 2.500, 2.750, 3.000, 3.250, 3.500, 3.750,
        4.000, 4.250, 4.500, 4.750, 5.000]
C_b_1_cold = [1.100, 0.967, 0.866, 0.790, 0.726, 0.675, 0.629, 0.585, 0.550, 0.517, 0.488, 0.462, 0.437, 0.413, 0.392,
              0.371, 0.351, 0.340, 0.323, 0.307, 0.290]
C_b_1_hot = [0.78, 0.68, 0.62, 0.57, 0.53, 0.49, 0.46, 0.43, 0.41, 0.38, 0.36, 0.34, 0.325, 0.305, 0.285, 0.27, 0.255, 0.24, 0.23, 0.22, 0.21]
C_b_2_cold = [0.81, 0.74, 0.67, 0.62, 0.57, 0.54, 0.51, 0.48, 0.455, 0.43, 0.41, 0.39, 0.37, 0.36, 0.35, 0.34, 0.33, 0.32, 0.31, 0.305, 0.295]
C_b_2_hot = [0.57, 0.53, 0.49, 0.46, 0.43, 0.41, 0.39, 0.37, 0.355, 0.34, 0.33, 0.32, 0.305, 0.295, 0.28, 0.27, 0.26, 0.25, 0.242, 0.235, 0.23]
C_b_1_1_cold = [1.87, 1.43, 1.18, 0.92, 0.74, 0.6, 0.51, 0.44, 0.38, 0.34, 0.28, 0.24, 0.2, 0.18, 0.15, 0.12, 0.11, 0.1, 0.095, 0.09, 0.08]
C_b_1_1_hot = [0.68, 0.54, 0.42, 0.34, 0.25, 0.21, 0.18, 0.15, 0.12, 0.11, 0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.038, 0.037, 0.036, 0.035]


BNT_TYPE_LIST = Literal['1ph_BNT', '2ph_BNT', '3ph_BNT_1_type', '3ph_BNT_2_type']


def coef_A(B_s, B_r, omega_t, omega_t0):
    """коэффициент смещения А"""
    coef_A = -math.cos(omega_t+omega_t0) + math.cos(omega_t0) - B_s + B_r

    return coef_A-1


def effective_current(coef_A: float):
    """коэффициент действующего значения """
    first_part_1 = (coef_A ** 2 + 0.5)
    second_part_1 = (1 - 1 / math.pi * math.acos(coef_A))
    third_part_1 = 3 / (2 * math.pi) * coef_A * math.sqrt(1 - coef_A ** 2)

    I_relative_value = round(math.sqrt(first_part_1 * second_part_1 + third_part_1), 3)

    return I_relative_value


def first_harm_effective(coef_A: float):
    """относительное действующee значениее первой гармоники"""
    first_part = 1/math.pi * math.acos(coef_A)
    second_part = coef_A / math.pi * math.sqrt(1 - coef_A ** 2)

    I_first_harm_effective = 1 / math.sqrt(2) * (1 - first_part + second_part)

    return I_first_harm_effective

"""тест кривых Засыпкина"""
# plt.plot(Ttau, C_b_1_cold)
# plt.plot(Ttau, C_b_1_hot)
# plt.show()
#
# plt.plot(Ttau, C_b_2_cold)
# plt.plot(Ttau, C_b_2_hot)
# plt.show()
#
# plt.plot(Ttau, C_b_1_1_cold)
# plt.plot(Ttau, C_b_1_1_hot)
# plt.show()
