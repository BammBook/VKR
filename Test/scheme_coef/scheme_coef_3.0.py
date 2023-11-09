import math

import np as np
import numpy as np
from matplotlib import pyplot as plt

from XML_Parser.ModelData import ModelData
from data_сlass.DataClass import DataClass
from data_сlass.EffectiveCurrents import EffectiveCurrents
from data_сlass.help_functions import *

"""
определение коэффициентов схемы для разных реле.
продход основан на мгновенных значениях, получаемых с помощью коэффициента смещения А 
учитывается сдвиг фаз между максимумами 
"""


BTN_TYPE = ''

B_s = 1.21

B_r = 0.42



# phase_shift_2 = 2 * math.pi / 3





if BTN_TYPE == '1ph':
    print(f'scheme coef linear (1ph) = {1.00}')
    print(f'scheme coef zero seq (1ph) = {1.00}')


if BTN_TYPE == '2ph':
    phase_shift_2ph = math.pi / 3

    B_r_B = B_r
    B_r_C = B_r

    ang_2ph_B = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
    ang_2ph_C = [(5 / 6) * math.pi, (1 / 6) * math.pi]  # phase C

    coef_A_2_phase_B = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_2ph_B[0], omega_t0=ang_2ph_B[1])
    coef_A_2_phase_C = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_2ph_C[0] - phase_shift_2ph, omega_t0=ang_2ph_C[1])

    print(f'coef_A_2_phase_B = {round(coef_A_2_phase_B, 2)}')
    print(f'coef_A_2_phase_C = {round(coef_A_2_phase_C, 2)}\n')

    value_B = 1 + coef_A_2_phase_B
    value_C = 1 + coef_A_2_phase_C

    print(f'B_r_B = {B_r_B}')
    print(f'B_r_C = {B_r_C}\n')

    print(f'1 + coef_A_2_phase_B = {round(value_B, 2)}')
    print(f'1 + coef_A_2_phase_C = {round(value_C, 2)}\n')

    linear = math.fabs(value_B) + math.fabs(value_C)

    print(f'linear = {round(linear, 2)}')

    scheme_coef = linear/math.fabs(value_B)

    print(f'scheme_coef_linear (2ph) = {round(scheme_coef, 2)}')


if BTN_TYPE == '3ph1':

    phase_shift_3ph1 = math.pi / 3

    B_r_B = B_r
    B_r_C = B_r

    ang_3ph_1_B = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
    ang_3ph_1_C = [(5 / 6) * math.pi, (1 / 6) * math.pi]  # phase C

    coef_A_3ph1_phase_B = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_3ph_1_B[0], omega_t0=ang_3ph_1_B[1])
    coef_A_3ph1_phase_C = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_3ph_1_C[0] - phase_shift_3ph1, omega_t0=ang_3ph_1_C[1])

    print(f'coef_A_3ph1_phase_B = {round(coef_A_3ph1_phase_B, 2)}')
    print(f'coef_A_3ph1_phase_C = {round(coef_A_3ph1_phase_C, 2)}\n')

    value_B = 1 + coef_A_3ph1_phase_B
    value_C = 1 + coef_A_3ph1_phase_C

    print(f'B_r_B = {B_r_B}')
    print(f'B_r_C = {B_r_C}\n')

    print(f'1 + coef_A_3ph1_phase_B = {round(value_B, 2)}')
    print(f'1 + coef_A_3ph1_phase_C = {round(value_C, 2)}\n')

    linear = math.fabs(value_B) + math.fabs(value_C)

    print(f'linear = {round(linear, 2)}')

    scheme_coef = linear/math.fabs(value_B)

    print(f'scheme_coef_linear (3ph1) = {round(scheme_coef, 2)}')


if BTN_TYPE == '3ph2':

    phase_shift_3ph2 = math.pi / 3

    B_r_A = B_r
    B_r_C = B_r

    ang_3ph_2_A = [1 * math.pi, 0 * math.pi]  # phase A
    ang_3ph_2_B = [2/3 * math.pi, 1/3 * math.pi]  # phase B
    ang_3ph_2_C = [4/3 * math.pi, -1/3 * math.pi]  # phase C

    coef_A_3ph2_phase_A = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_3ph_2_A[0], omega_t0=ang_3ph_2_A[1])
    coef_A_3ph2_phase_C = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_3ph_2_C[0] + phase_shift_3ph2, omega_t0=ang_3ph_2_C[1])

    print(f'coef_A_3ph2_phase_A = {round(coef_A_3ph2_phase_A, 2)}')
    print(f'coef_A_3ph2_phase_C = {round(coef_A_3ph2_phase_C, 2)}\n')

    value_A = 1 + coef_A_3ph2_phase_A
    value_C = 1 + coef_A_3ph2_phase_C

    print(f'B_r_A = {B_r_A}')
    print(f'B_r_C = {B_r_C}\n')

    print(f'1 + coef_A_3ph2_phase_A = {round(value_A, 2)}')
    print(f'1 + coef_A_3ph2_phase_C = {round(value_C, 2)}\n')

    linear = math.fabs(value_A) + math.fabs(value_C)

    print(f'linear = {round(linear, 2)}')

    scheme_coef = linear/math.fabs(value_A)

    print(f'scheme_coef_linear (3ph2) = {round(scheme_coef, 2)}')


if BTN_TYPE == 'diff_time':

    phase_shift_3ph2 = math.pi / 3

    B_r_A = B_r
    B_r_B = 0.5 * B_r
    B_r_C = 0.5 * B_r

    ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A

    ang_3ph_2_A = [1 * math.pi, 0 * math.pi]  # phase A
    ang_3ph_2_B = [2/3 * math.pi, 1/3 * math.pi]  # phase B
    ang_3ph_2_C = [4/3 * math.pi, -1/3 * math.pi]  # phase C

    coef_A_3ph2_phase_A = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_3ph_2_A[0], omega_t0=ang_3ph_2_A[1])
    coef_A_3ph2_phase_C = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_3ph_2_C[0] + phase_shift_3ph2, omega_t0=ang_3ph_2_C[1])

    print(f'coef_A_3ph2_phase_A = {round(coef_A_3ph2_phase_A, 2)}')
    print(f'coef_A_3ph2_phase_C = {round(coef_A_3ph2_phase_C, 2)}\n')

    value_A = 1 + coef_A_3ph2_phase_A
    value_C = 1 + coef_A_3ph2_phase_C

    print(f'B_r_A = {B_r_A}')
    print(f'B_r_C = {B_r_C}\n')

    print(f'1 + coef_A_3ph2_phase_A = {round(value_A, 2)}')
    print(f'1 + coef_A_3ph2_phase_C = {round(value_C, 2)}\n')

    linear = math.fabs(value_A) + math.fabs(value_C)

    print(f'linear = {round(linear, 2)}')

    scheme_coef = linear/math.fabs(value_A)

    print(f'scheme_coef_linear (3ph2) = {round(scheme_coef, 2)}')


# coef_A_3_phase_A = coef_A(B_s=B_s, B_r=B_r, omega_t=ang_3ph_2_A[0], omega_t0=ang_3ph_2_A[1])
# coef_A_3_phase_B = coef_A(B_s=B_s, B_r=0.5 * B_r, omega_t=ang_3ph_2_B[0], omega_t0=ang_3ph_2_B[1])
# coef_A_3_phase_C = coef_A(B_s=B_s, B_r=0.5 * B_r, omega_t=ang_3ph_2_C[0], omega_t0=ang_3ph_2_C[1])
#
#
# print(f'1 + coef_A_3_phase_A = {round(coef_A_3_phase_A + 1, 2)}')
# print(f'1 + coef_A_3_phase_B = {round(coef_A_3_phase_B + 1, 2)}')
# print(f'1 + coef_A_3_phase_C = {round(coef_A_3_phase_C + 1, 2)}')

B_s = 1.21
B_r_A = 0.0641


ang_1ph_A = [1 * math.pi, 0 * math.pi]  # phase A

phase_shift_2ph = math.pi / 3

coef_A_1_phase_A = coef_A(B_s=B_s, B_r=B_r, omega_t=ang_1ph_A[0], omega_t0=ang_1ph_A[1])

print(f'effective current A = {coef_A_1_phase_A + 1}')
time_duration = 2.5

md = ModelData("Model220")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)

"""1 phase"""
data = DataClass("csv", "220kV_new/", "220_BTN1phaseA0B180C180", tau=tau, time_duration=time_duration)
eff_curr = EffectiveCurrents("csv", "220kV_new/", "220_BTN1phaseA0B180C180", time_duration=time_duration)
