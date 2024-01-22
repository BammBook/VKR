import matplotlib.pyplot as plt
import numpy as np

from GUI.presentation import presentation
from approximation.approximation import exp_1
from data_сlass.help_functions import *
from GUI.compare_two_graph import *
from data_сlass.EffectiveCurrents import EffectiveCurrents
from GUI.compare_effective_current import compare_effective_current
from typing import Literal

time_duration = 2.5

average_C0_1ph = -0.273
average_C1_1ph = 0.771

average_C0_diff_time_C = -0.3
average_C1_diff_time_C = 0.828

start = 220
if start == 220:
    B_s = 1.16
    B_r_nom = 0.598
    B_r_A = 0.33/B_r_nom
    B_r_B = -0.17/B_r_nom
    B_r_C = -0.17/B_r_nom
if start == 110:
    B_s = 1.21
    B_r_nom = 0.31
    B_r_A = 0.18/B_r_nom
    B_r_B = -0.17/B_r_nom
    B_r_C = -0.17/B_r_nom

ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A
ang_diff_time = [1 * math.pi - math.radians(210), math.radians(210)]  # phase C


coef_A_1ph_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
coef_A_2ph_cold = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
coef_A_3ph1_cold = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph2_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])
coef_A_diff_time_cold = coef_A_1ph_cold + 0.37 + 0.5 * B_r_A




if start == 220:

    model_110 = ModelData("Model220_comp")
    tau = model_110.X / (2 * math.pi * 50 * model_110.R) * 1000

    data_220_1ph = DataClass("csv", "220_11.12/", "1ph_220_Broe_0.34_Bs_1.16", tau=tau, time_duration=time_duration)
    generic_curve_220 = exp_1(data_220_1ph.Imax_A_relative_time_partial,
                              average_C0_1ph,
                              average_C1_1ph)

    convert_to_named_units_coef_220 = math.sqrt(2 / 3) * model_110.U_nom / (math.sqrt(model_110.X ** 2 + model_110.R ** 2))
    coef = 1 + coef_A_1ph_cold

    effective_coef = effective_current(coef_A_1ph_cold)
    # Zasypcin_curve = C_b_1_cold / (1 + coef_A_1ph_cold) * convert_to_named_units_coef
    Zasypcin_curve = C_b_1_cold / effective_coef * convert_to_named_units_coef_220


    effective_curve = convert_to_named_units_coef_220 * generic_curve_220 * coef

    time_shift = 0.01

    presentation()
    plt.grid(True)
    plt.plot(data_220_1ph.time, data_220_1ph.I_A, color='grey', linewidth=0.3)
    plt.plot(data_220_1ph.Imax_A_time + time_shift, data_220_1ph.Imax_A, color='grey')
    plt.plot(data_220_1ph.Imax_A_time[:len(effective_curve)] + time_shift, effective_curve)
    plt.plot(Ttau*tau/1000 + time_shift, Zasypcin_curve)
    plt.legend(['Мгновенное значение тока ф. А', 'Опыт RTDS', 'Расчетная огибающая максимумов', 'Огибающая по Засыпкину'])
    plt.xlim([0, 0.5])

    plt.show()

if start == 110:

    model_110 = ModelData("Model110_comp")
    tau = model_110.X / (2 * math.pi * 50 * model_110.R) * 1000

    data_110_1ph = DataClass("csv", "110_11.12/", "1ph_110_Broe_0.18_Bs_1.21", tau=tau, time_duration=time_duration)
    # plt.plot(data_110_1ph.time, data_110_1ph.I_A)
    # plt.show()
    generic_curve_110 = exp_1(data_110_1ph.Imax_B_relative_time_partial,
                              average_C0_1ph,
                              average_C1_1ph)

    convert_to_named_units_coef_110 = math.sqrt(2 / 3) * model_110.U_nom / (math.sqrt(model_110.X ** 2 + model_110.R ** 2))
    coef = 1 + coef_A_1ph_cold

    effective_coef = effective_current(coef_A_1ph_cold)
    # Zasypcin_curve = C_b_1_cold / (1 + coef_A_1ph_cold) * convert_to_named_units_coef
    Zasypcin_curve = C_b_1_cold / effective_coef * convert_to_named_units_coef_110


    effective_curve = convert_to_named_units_coef_110 * generic_curve_110 * coef

    time_shift = 0.01
    time_shift_2 = 0.617

    presentation()
    plt.grid(True)
    plt.plot(data_110_1ph.time, data_110_1ph.I_B, color='grey', linewidth=0.3)
    plt.plot(data_110_1ph.Imax_B_time + time_shift_2, data_110_1ph.Imax_B, color='grey')
    plt.plot(data_110_1ph.Imax_B_time[:len(effective_curve)] + time_shift_2, effective_curve)
    plt.plot(Ttau*tau/1000 + time_shift_2, Zasypcin_curve)
    plt.legend(['Мгновенное значение тока ф. А', 'Опыт RTDS', 'Расчетная огибающая максимумов', 'Огибающая по Засыпкину'])
    plt.xlim([0.6, 0.7])

    plt.show()


