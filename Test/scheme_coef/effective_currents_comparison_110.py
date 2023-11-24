import matplotlib.pyplot as plt

from data_сlass.help_functions import *
from GUI.compare_two_graph import *
from data_сlass.EffectiveCurrents import EffectiveCurrents
from GUI.compare_effective_current import compare_effective_current
from typing import Literal


BTN_TYPES = Literal['1ph', '2ph', '3ph1', '3ph2', 'diff_time']
RELAY_TYPES = Literal['phase', 'linear', 'zero_sequence']
VOLTAGE_LEVELS = Literal['220', '110']
MODEL_NAMES = Literal['Model220', 'Model110']


# file_names = {'1ph': '_BTN1phaseA0B180C180',
#               '2ph': '_BTN2phase',
#               '3ph1': '_BTN3phase90',
#               '3ph2': '_BTN3phase0',
#               'diff_time': '_BTN3phaseA0B90C90'}

#1 ms
# file_names = {'1ph': 'BTN1phaseA0BC18',
#               '2ph': 'BTN2phaseBC(A18)',
#               '3ph1': 'BTN3phase90',
#               '3ph2': 'BTN3phase0',
#               'diff_time': 'BTNA0BC90'}

#2 ms
file_names = {'1ph': 'BTN1phaseA0BC18',
              '2ph': 'BTN2phaseBC(A36)',
              '3ph1': 'BTN3phase90',
              '3ph2': 'BTN3phase0',
              'diff_time': 'BTNA0BC90'}


def data_reader(voltage_level,
                btn_type: BTN_TYPES,
                model_name,
                filepath,
                time_duration):

    file_name = file_names.get(btn_type)

    md = ModelData(model_name)
    X_eq = md.X
    R_eq = md.R
    tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)

    data = DataClass("csv",
                     filepath,
                     voltage_level + file_name, tau=tau, time_duration=time_duration)

    eff_curr = EffectiveCurrents("csv",
                                 filepath,
                                 "Id" + voltage_level + file_name,
                                 time_duration=time_duration)

    return data, eff_curr


time_duration = 2.5

average_C0_1ph = -0.273
average_C1_1ph = 0.771

average_C0_diff_time_C = -0.3
average_C1_diff_time_C = 0.828

B_s = 1.21
B_r_A = 0.0711
B_r_B = 0.0
B_r_C = 0.0711

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
# coef_A_diff_time_cold = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_diff_time[0], omega_t0=ang_diff_time[1])

start = '3ph2'
filepath = 'BTN_110kV_24.11/'
model_name = 'Model110'
voltage_level = '110'

if start == '1ph':

    data_1ph, eff_curr_1ph = data_reader(voltage_level=voltage_level,
                                         btn_type='1ph',
                                         model_name=model_name,
                                         filepath=filepath,
                                         time_duration=time_duration)


    # plt.plot(data_220_1ph.time, data_220_1ph.I_A)
    # plt.plot(data_220_1ph.time, data_220_1ph.I_B)
    # plt.plot(data_220_1ph.time, data_220_1ph.I_C)
    # plt.legend(['I_A', 'I_B', 'I_C'])
    # plt.show()
    #
    # plt.plot(eff_curr_220_1ph.time, eff_curr_220_1ph.I_A_eff_ph)
    # plt.plot(eff_curr_220_1ph.time, eff_curr_220_1ph.I_3I0_eff)
    # plt.legend(['I_ph', 'I_zero_seq'])
    # plt.show()

    compare_effective_current(eff_curr_time=eff_curr_1ph.time,
                              eff_curr_data=eff_curr_1ph.I_A_eff_ph,
                              model_Imax_relative_time=data_1ph.Imax_A_relative_time_partial,
                              model_Imax_time=data_1ph.Imax_A_time[:len(data_1ph.Imax_A_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='1ph',
                              relay_type='phase',
                              coef_A=coef_A_1ph_cold,
                              title='1-фазный БТН',
                              phase='Фазный ток ф.A')

    compare_effective_current(eff_curr_time=eff_curr_1ph.time,
                              eff_curr_data=eff_curr_1ph.I_AB_eff,
                              model_Imax_relative_time=data_1ph.Imax_A_relative_time_partial,
                              model_Imax_time=data_1ph.Imax_A_time[:len(data_1ph.Imax_A_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='1ph',
                              relay_type='linear',
                              coef_A=coef_A_1ph_cold,
                              title='1-фазный БТН',
                              phase='Линейный ток (контур АВ)')

    compare_effective_current(eff_curr_time=eff_curr_1ph.time,
                              eff_curr_data=eff_curr_1ph.I_3I0_eff,
                              model_Imax_relative_time=data_1ph.Imax_A_relative_time_partial,
                              model_Imax_time=data_1ph.Imax_A_time[:len(data_1ph.Imax_A_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='1ph',
                              relay_type='zero_sequence',
                              coef_A=coef_A_1ph_cold,
                              title='1-фазный БТН',
                              phase='Ток НП')

    # compare_effective_current(eff_curr_time=eff_curr_220_1ph.time,
    #                           eff_curr_data=eff_curr_220_1ph.I_A_eff_ph,
    #                           model_Imax_relative_time=data_220_1ph.Imax_A_relative_time,
    #                           model_Imax_time=data_220_1ph.Imax_A_time[:len(data_220_1ph.Imax_A_relative_time)]+0.01,
    #                           model_data_name="Model220",
    #                           average_C0=average_C0_1ph,
    #                           average_C1=average_C1_1ph,
    #                           btn_type='1ph',
    #                           relay_type='phase',
    #                           coef_A=coef_A_1ph_cold,
    #                           title='1-фазный БТН',
    #                           phase='Фазный ток ф.A')

if start == '2ph':

    data_2ph, eff_curr_2ph = data_reader(voltage_level=voltage_level,
                                         btn_type='2ph',
                                         model_name=model_name,
                                         filepath=filepath,
                                         time_duration=time_duration)
    # plt.plot(data_220_2ph.time, data_220_2ph.I_A)
    # plt.plot(data_220_2ph.time, data_220_2ph.I_B)
    # plt.plot(data_220_2ph.time, data_220_2ph.I_C)
    # plt.legend(['I_A', 'I_B', 'I_C'])
    # plt.show()
    #
    # plt.plot(eff_curr_220_2ph.time, eff_curr_220_2ph.I_A_eff_ph)
    # plt.plot(eff_curr_220_2ph.time, eff_curr_220_2ph.I_B_eff_ph)
    # plt.plot(eff_curr_220_2ph.time, eff_curr_220_2ph.I_C_eff_ph)
    # plt.legend(['I_A', 'I_B', 'I_C'])
    # plt.show()

    compare_effective_current(eff_curr_time=eff_curr_2ph.time,
                              eff_curr_data=eff_curr_2ph.I_C_eff_ph,
                              model_Imax_relative_time=data_2ph.Imax_C_relative_time_partial,
                              model_Imax_time=data_2ph.Imax_C_time[:len(data_2ph.Imax_C_relative_time_partial)],
                              time_shift=0.016,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='2ph',
                              relay_type='phase',
                              coef_A=coef_A_2ph_cold,
                              title='2-фазный БТН',
                              phase='Фазный ток ф.C')

    compare_effective_current(eff_curr_time=eff_curr_2ph.time,
                              eff_curr_data=eff_curr_2ph.I_BC_eff,
                              model_Imax_relative_time=data_2ph.Imax_B_relative_time_partial,
                              model_Imax_time=data_2ph.Imax_B_time[:len(data_2ph.Imax_B_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='2ph',
                              relay_type='linear',
                              coef_A=coef_A_2ph_cold,
                              title='2-фазный БТН',
                              phase='Линейный ток (контур BC)')

    compare_effective_current(eff_curr_time=eff_curr_2ph.time,
                              eff_curr_data=eff_curr_2ph.I_3I0_eff,
                              model_Imax_relative_time=data_2ph.Imax_B_relative_time_partial,
                              model_Imax_time=data_2ph.Imax_B_time[:len(data_2ph.Imax_B_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='2ph',
                              relay_type='zero_sequence',
                              coef_A=coef_A_2ph_cold,
                              title='2-фазный БТН',
                              phase='Ток НП')

if start == '3ph1':

    data_3ph1, eff_curr_3ph1 = data_reader(voltage_level=voltage_level,
                                           btn_type='3ph1',
                                           model_name=model_name,
                                           filepath=filepath,
                                           time_duration=time_duration)
    # plt.plot(data_3ph1.time, data_3ph1.I_A)
    # plt.plot(data_3ph1.time, data_3ph1.I_B)
    # plt.plot(data_3ph1.time, data_3ph1.I_C)
    # plt.legend(['I_A', 'I_B', 'I_C'])
    # plt.show()

    compare_effective_current(eff_curr_time=eff_curr_3ph1.time,
                              eff_curr_data=eff_curr_3ph1.I_C_eff_ph,
                              model_Imax_relative_time=data_3ph1.Imax_C_relative_time_partial,
                              model_Imax_time=data_3ph1.Imax_C_time[:len(data_3ph1.Imax_C_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph1',
                              relay_type='phase',
                              coef_A=coef_A_3ph1_cold,
                              title='3-фазный БТН\n(тип 1)',
                              phase='Фазный ток ф.C')

    compare_effective_current(eff_curr_time=eff_curr_3ph1.time,
                              eff_curr_data=eff_curr_3ph1.I_BC_eff,
                              model_Imax_relative_time=data_3ph1.Imax_C_relative_time_partial,
                              model_Imax_time=data_3ph1.Imax_C_time[:len(data_3ph1.Imax_C_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph1',
                              relay_type='linear',
                              coef_A=coef_A_3ph1_cold,
                              title='3-фазный БТН\n(тип 1)',
                              phase='Линейный ток (контур ВС)')

    compare_effective_current(eff_curr_time=eff_curr_3ph1.time,
                              eff_curr_data=eff_curr_3ph1.I_3I0_eff,
                              model_Imax_relative_time=data_3ph1.Imax_C_relative_time_partial,
                              model_Imax_time=data_3ph1.Imax_C_time[:len(data_3ph1.Imax_C_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph1',
                              relay_type='zero_sequence',
                              coef_A=coef_A_3ph1_cold,
                              title='3-фазный БТН\n(тип 1)',
                              phase='ток НП')

if start == '3ph2':

    data_3ph2, eff_curr_3ph2 = data_reader(voltage_level=voltage_level,
                                           btn_type='3ph2',
                                           model_name=model_name,
                                           filepath=filepath,
                                           time_duration=time_duration)

    compare_effective_current(eff_curr_time=eff_curr_3ph2.time,
                              eff_curr_data=eff_curr_3ph2.I_A_eff_ph,
                              model_Imax_relative_time=data_3ph2.Imax_A_relative_time_partial,
                              model_Imax_time=data_3ph2.Imax_A_time[:len(data_3ph2.Imax_A_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph2',
                              relay_type='phase',
                              coef_A=coef_A_3ph2_cold,
                              title='3-фазный БТН\n(тип 2)',
                              phase='Фазный ток ф.A')

    compare_effective_current(eff_curr_time=eff_curr_3ph2.time,
                              eff_curr_data=eff_curr_3ph2.I_CA_eff,
                              model_Imax_relative_time=data_3ph2.Imax_C_relative_time_partial,
                              model_Imax_time=data_3ph2.Imax_C_time[:len(data_3ph2.Imax_C_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph2',
                              relay_type='linear',
                              coef_A=coef_A_3ph2_cold,
                              title='3-фазный БТН\n(тип 2)',
                              phase='Линейный ток (контур CA)')

    compare_effective_current(eff_curr_time=eff_curr_3ph2.time,
                              eff_curr_data=eff_curr_3ph2.I_3I0_eff,
                              model_Imax_relative_time=data_3ph2.Imax_C_relative_time_partial,
                              model_Imax_time=data_3ph2.Imax_C_time[:len(data_3ph2.Imax_C_relative_time_partial)],
                              time_shift=0.015,
                              model_data_name=model_name,
                              average_C0=average_C0_1ph,
                              average_C1=average_C1_1ph,
                              btn_type='3ph2',
                              relay_type='zero_sequence',
                              coef_A=coef_A_3ph2_cold,
                              title='3-фазный БТН\n(тип 2)',
                              phase='Ток НП')

if start == 'diff_time':

    data_diff_time, eff_curr_diff_time = data_reader(voltage_level=voltage_level,
                                                     btn_type='diff_time',
                                                     model_name=model_name,
                                                     filepath=filepath,
                                                     time_duration=time_duration)
    # plt.plot(data_220_diff_time.time, data_220_diff_time.I_A)
    # plt.plot(data_220_diff_time.time, data_220_diff_time.I_B)
    # plt.plot(data_220_diff_time.time, data_220_diff_time.I_C)
    # plt.legend(['I_A', 'I_B', 'I_C'])
    # plt.show()

    compare_effective_current(eff_curr_time=eff_curr_diff_time.time,
                              eff_curr_data=eff_curr_diff_time.I_C_eff_ph,
                              model_Imax_relative_time=data_diff_time.Imax_C_relative_time_partial,
                              model_Imax_time=data_diff_time.Imax_C_time[:len(data_diff_time.Imax_C_relative_time_partial)],
                              time_shift=0.017,
                              model_data_name=model_name,
                              average_C0=average_C0_diff_time_C,
                              average_C1=average_C1_diff_time_C,
                              btn_type='diff_time',
                              relay_type='phase',
                              coef_A=coef_A_diff_time_cold,
                              title='Последовательный БТН',
                              phase='Фазный ток ф.C')

    compare_effective_current(eff_curr_time=eff_curr_diff_time.time,
                              eff_curr_data=eff_curr_diff_time.I_CA_eff,
                              model_Imax_relative_time=data_diff_time.Imax_C_relative_time_partial,
                              model_Imax_time=data_diff_time.Imax_C_time[:len(data_diff_time.Imax_C_relative_time_partial)],
                              time_shift=0.016,
                              model_data_name=model_name,
                              average_C0=average_C0_diff_time_C,
                              average_C1=average_C1_diff_time_C,
                              btn_type='diff_time',
                              relay_type='linear',
                              coef_A=coef_A_diff_time_cold,
                              title='Последовательный БТН',
                              phase='Линейный ток (контур CA)')

    compare_effective_current(eff_curr_time=eff_curr_diff_time.time,
                              eff_curr_data=eff_curr_diff_time.I_3I0_eff,
                              model_Imax_relative_time=data_diff_time.Imax_C_relative_time_partial,
                              model_Imax_time=data_diff_time.Imax_C_time[:len(data_diff_time.Imax_C_relative_time_partial)],
                              time_shift=0.019,
                              model_data_name=model_name,
                              average_C0=average_C0_diff_time_C,
                              average_C1=average_C1_diff_time_C,
                              btn_type='diff_time',
                              relay_type='zero_sequence',
                              coef_A=coef_A_diff_time_cold,
                              title='Последовательный БТН',
                              phase='Ток НП')

