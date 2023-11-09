import math

import np as np
import numpy as np
from matplotlib import pyplot as plt

from XML_Parser.ModelData import ModelData
from data_сlass.DataClass import DataClass
from data_сlass.EffectiveCurrents import EffectiveCurrents
from data_сlass.help_functions import *


time_duration = 2.5

md = ModelData("Model220")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)

"""1ph, 2ph, 3ph1, 3ph2, diff_time"""
BTN_type = '3ph2'

if BTN_type == '1ph':
    """1 phase"""
    data = DataClass("csv", "220kV_new/", "220_BTN1phaseA0B180C180", tau=tau, time_duration=time_duration)
    eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN1phaseA0B180C180", time_duration=time_duration)

    print(f'scheme coef linear = {round(np.max(eff_curr.I_AB_eff) / np.max(eff_curr.I_A_eff_ph), 2)}')
    print(f'scheme coef zero seq = {round(np.max(eff_curr.I_3I0_eff) / np.max(eff_curr.I_A_eff_ph), 2)}')

    plt.plot(data.time, data.I_A)
    plt.plot(data.time, data.I_B)
    plt.plot(data.time, data.I_C)
    plt.legend(['I_A', 'I_B', 'I_C'])
    plt.show()

    plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
    plt.plot(eff_curr.time, eff_curr.I_CA_eff)
    plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
    plt.legend(['фазный', 'линейный', 'ток НП'])
    plt.show()


if BTN_type == '2ph':
    """2 phase"""
    data = DataClass("csv", "220kV_new/", "220_BTN2phase", tau=tau, time_duration=time_duration)
    eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN2phase", time_duration=time_duration)
    print(np.max(data.I_B))
    print(np.min(data.I_C))
    print(f'scheme coef linear (inst) = {round((np.max(data.I_B) - np.min(data.I_C))/ np.max(data.I_B), 2)}')


    print(f'scheme coef linear = {round(np.max(eff_curr.I_BC_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')
    print(f'scheme coef zero seq = {round(np.max(eff_curr.I_3I0_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')


    plt.plot(data.time, data.I_A)
    plt.plot(data.time, data.I_B)
    plt.plot(data.time, data.I_C)
    plt.legend(['I_A', 'I_B', 'I_C'])
    plt.show()

    """2 phase, 3 phase 1"""
    plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
    plt.plot(eff_curr.time, eff_curr.I_BC_eff)
    plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
    plt.legend(['фазный', 'линейный', 'ток НП'])
    plt.show()

if BTN_type == '3ph1':
    """3 phase 1"""
    data = DataClass("csv", "220kV_new/", "220_BTN3phase90", tau=tau, time_duration=time_duration)
    eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase90", time_duration=time_duration)

    print(f'scheme coef linear = {round(np.max(eff_curr.I_BC_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')
    print(f'scheme coef zero seq = {round(np.max(eff_curr.I_3I0_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')

    plt.plot(data.time, data.I_A)
    plt.plot(data.time, data.I_B)
    plt.plot(data.time, data.I_C)
    plt.legend(['I_A', 'I_B', 'I_C'])
    plt.show()

    """2 phase, 3 phase 1"""
    plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
    plt.plot(eff_curr.time, eff_curr.I_BC_eff)
    plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
    plt.legend(['фазный', 'линейный', 'ток НП'])
    plt.show()



if BTN_type == '3ph2':
    """3 phase 2"""
    data = DataClass("csv", "220kV_new/", "220_BTN3phase0", tau=tau, time_duration=time_duration)
    eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase0", time_duration=time_duration)

    print(f'scheme coef linear = {round(np.max(eff_curr.I_CA_eff) / np.max(eff_curr.I_A_eff_ph), 2)}')
    print(f'scheme coef zero seq = {round(np.max(eff_curr.I_3I0_eff) / np.max(eff_curr.I_A_eff_ph), 2)}')

    plt.plot(data.time, data.I_A)
    plt.plot(data.time, data.I_B)
    plt.plot(data.time, data.I_C)
    plt.legend(['I_A', 'I_B', 'I_C'])
    plt.show()

    plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
    plt.plot(eff_curr.time, eff_curr.I_CA_eff)
    plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
    plt.legend(['фазный', 'линейный', 'ток НП'])
    plt.show()


if BTN_type == 'diff_time':
    """diff time"""
    data = DataClass("csv", "220kV_new/", "220_BTN3phaseA0B90C90", tau=tau, time_duration=time_duration)
    eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phaseA0B90C90", time_duration=time_duration)

    print(f'scheme coef linear = {round(np.max(eff_curr.I_CA_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')
    print(f'scheme coef zero seq = {round(np.max(eff_curr.I_3I0_eff) / np.max(eff_curr.I_C_eff_ph), 2)}')

    plt.plot(data.time, data.I_A)
    plt.plot(data.time, data.I_B)
    plt.plot(data.time, data.I_C)
    plt.legend(['I_A', 'I_B', 'I_C'])
    plt.show()

    plt.plot(eff_curr.time, eff_curr.I_C_eff_ph)
    plt.plot(eff_curr.time, eff_curr.I_CA_eff)
    plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
    plt.legend(['фазный', 'линейный', 'ток НП'])
    plt.show()


named_value_coef = math.sqrt(2/3) * md.U_nom / (math.sqrt(X_eq**2 + R_eq**2))

B_s = 1.21

B_r = 0.42
B_r_A = B_r
B_r_B = B_r
B_r_C = B_r

phase_shift_2ph = math.pi / 3
# phase_shift_2 = 2 * math.pi / 3

ang_2ph_B = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_2ph_C = [(5 / 6) * math.pi, (1 / 6) * math.pi]  # phase C

ang_3ph_1_B = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1_C = [(5 / 6) * math.pi, (1 / 6) * math.pi]  # phase B

ang_3ph_2_A = [1 * math.pi, 0 * math.pi]  # phase A
ang_3ph_2_B = [2/3 * math.pi, 1/3 * math.pi]  # phase B
ang_3ph_2_C = [4/3 * math.pi, -1/3 * math.pi]  # phase C


ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A


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

print(f'scheme_coef = {round(scheme_coef, 2)}')


# coef_A_3_phase_A = coef_A(B_s=B_s, B_r=B_r, omega_t=ang_3ph_2_A[0], omega_t0=ang_3ph_2_A[1])
# coef_A_3_phase_B = coef_A(B_s=B_s, B_r=0.5 * B_r, omega_t=ang_3ph_2_B[0], omega_t0=ang_3ph_2_B[1])
# coef_A_3_phase_C = coef_A(B_s=B_s, B_r=0.5 * B_r, omega_t=ang_3ph_2_C[0], omega_t0=ang_3ph_2_C[1])
#
#
# print(f'1 + coef_A_3_phase_A = {round(coef_A_3_phase_A + 1, 2)}')
# print(f'1 + coef_A_3_phase_B = {round(coef_A_3_phase_B + 1, 2)}')
# print(f'1 + coef_A_3_phase_C = {round(coef_A_3_phase_C + 1, 2)}')
