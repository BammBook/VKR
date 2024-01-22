from data_сlass.help_functions import *
from GUI.compare_two_graph import *
from data_сlass.EffectiveCurrents import EffectiveCurrents
from GUI.compare_effective_current import compare_effective_current

time_duration = 2.5

md = ModelData("Model220")
# print('check')
X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)

average_C0_1ph = -0.273
average_C1_1ph = 0.771

average_C0_diff_time_C = -0.3
average_C1_diff_time_C = 0.828

B_s = md.B_s
B_r_A = 0.0879
B_r_B = 0.0862
B_r_C = -0.1742



ang_1ph = [1 * math.pi, 0 * math.pi]  # phase A
ang_2ph = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_1 = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_3ph_2 = [1 * math.pi, 0 * math.pi]  # phase A
ang_diff_time = [1 * math.pi - math.radians(210), math.radians(210)]  # phase C


coef_A_1ph_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_1ph[0], omega_t0=ang_1ph[1])
coef_A_2ph_cold = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_2ph[0], omega_t0=ang_2ph[1])
coef_A_3ph_1_cold = coef_A(B_s=B_s, B_r=B_r_B, omega_t=ang_3ph_1[0], omega_t0=ang_3ph_1[1])
coef_A_3ph_2_cold = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_3ph_2[0], omega_t0=ang_3ph_2[1])

# coef_A_diff_time_cold = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_diff_time[0], omega_t0=ang_diff_time[1])
coef_A_diff_time_cold = coef_A_1ph_cold + 0.37 + 0.5 * B_r_A
# print(f'coef_A_diff_time_cold = {coef_A_diff_time_cold}')


ang_diff_time_A = [1 * math.pi, 0 * math.pi]  # phase A
ang_diff_time_C = [1 * math.pi - math.radians(210), math.radians(210)]  # phase C
coef_A_diff_time_cold_A = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_diff_time_A[0], omega_t0=ang_diff_time_A[1])
coef_A_diff_time_cold_C = coef_A(B_s=B_s, B_r=B_r_C, omega_t=ang_diff_time_C[0], omega_t0=ang_diff_time_C[1])
# print(f'coef_A_diff_time_cold_A = {round(math.fabs(coef_A_diff_time_cold_A+1), 2)}')
# print(f'coef_A_diff_time_cold_C = {round(math.fabs(coef_A_diff_time_cold_C+1), 2)}')



data = DataClass("csv", "220kV_new/", "220_BTN1phaseA0B180C180", tau=tau, time_duration=time_duration)
# print(data.Imax_A)
compare_max(data_time=data.time,
            data_max_time=data.Imax_A_time[:len(data.Imax_A_relative_time_partial)]+0.009,
            data_Imax_relative_time=data.Imax_A_relative_time_partial,
            data_current=data.I_A,
            data_max_current=data.Imax_A[:len(data.Imax_A_relative_time_partial)],
            average_C0=average_C0_1ph,
            average_C1=average_C1_1ph,
            tau=tau,
            coef_A=coef_A_1ph_cold,
            phase='A',
            title="Однофазный БТН",
            model_data="Model220",
            error=True)
#
#
# data = DataClass("csv", "220kV_new/", "220_BTN2phase", tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_B_time[:len(data.Imax_B_relative_time_partial)]+0.01,
#             data_Imax_relative_time=data.Imax_B_relative_time_partial,
#             data_current=data.I_B,
#             data_max_current=data.Imax_B[:len(data.Imax_B_relative_time_partial)],
#             average_C0=average_C0_1ph,
#             average_C1=average_C1_1ph,
#             tau=tau,
#             coef_A=coef_A_2ph_cold,
#             phase='B',
#             title="Двухфазный БТН",
#             model_data="Model220",
#             error=True)



# data = DataClass("csv", "220kV_new/", "220_BTN3phase90", tau=tau, time_duration=time_duration)
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_B_time[:len(data.Imax_B_relative_time_partial)]+0.01,
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
#
# plt.plot(data.time, data.I_A)
# plt.plot(data.time, data.I_B)
# plt.plot(data.time, data.I_C)
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()
#
# compare_max(data_time=data.time,
#             data_max_time=data.Imax_C_time[:len(data.Imax_C_relative_time_partial)]+0.0128,
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
#
#
# eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase0", time_duration=time_duration)



# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
# plt.legend(['фазный', 'линейный', 'ток НП'])
# plt.show()



data = DataClass("csv", "220kV_new/", "220_BTN1phaseA0B180C180", tau=tau, time_duration=time_duration)
eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN1phaseA0B180C180", time_duration=time_duration)

# plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_C_eff_ph)
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()

compare_effective_current(eff_curr_time=eff_curr.time,
                          eff_curr_data=eff_curr.I_A_eff_ph,
                          model_Imax_relative_time=data.Imax_A_relative_time_partial,
                          model_Imax_time=data.Imax_A_time[:len(data.Imax_A_relative_time_partial)]+0.01,
                          model_data_name="Model220",
                          average_C0=average_C0_1ph,
                          average_C1=average_C1_1ph,
                          btn_type='1ph',
                          relay_type='phase',
                          coef_A=coef_A_1ph_cold,
                          title='1-фазный БТН',
                          phase='Фазный ток ф.A')

plt.plot(eff_curr.time, eff_curr.I_AB_eff)
plt.plot(eff_curr.time, eff_curr.I_BC_eff)
plt.plot(eff_curr.time, eff_curr.I_CA_eff)
plt.legend(['I_AB', 'I_BC', 'I_CA'])
plt.show()
#
#
#
#
# data = DataClass("csv", "220kV_new/", "220_BTN2phase", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN2phase", time_duration=time_duration)

# plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_C_eff_ph)
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()

# compare_effective_current(eff_curr_time=eff_curr.time,
#                           eff_curr_data=eff_curr.I_B_eff_ph,
#                           model_Imax_relative_time=data.Imax_B_relative_time_partial,
#                           model_Imax_time=data.Imax_B_time[:len(data.Imax_B_relative_time_partial)]+0.01,
#                           model_data_name="Model220",
#                           average_C0=average_C0_1ph,
#                           average_C1=average_C1_1ph,
#                           btn_type='2ph',
#                           relay_type='phase',
#                           coef_A=coef_A_2ph_cold,
#                           title='2-x фазный БТН',
#                           phase='фазный  ток B')


# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.legend(['линейный (RTDS)', 'фазный (RTDS)'])
# plt.show()
#
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.legend(['линейный (RTDS)', 'фазный (RTDS)'])
# plt.show()


# plt.plot(eff_curr.time, eff_curr.I_AB_eff)
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_CA_eff)
# plt.legend(['I_AB', 'I_BC', 'I_CA'])
# plt.show()
#
# compare_effective_current(eff_curr_time=eff_curr.time,
#                           eff_curr_data=eff_curr.I_3I0_eff,
#                           model_Imax_relative_time=data.Imax_B_relative_time_partial,
#                           model_Imax_time=data.Imax_B_time[:len(data.Imax_B_relative_time_partial)]+0.01,
#                           model_data_name="Model220",
#                           average_C0=average_C0_1ph,
#                           average_C1=average_C1_1ph,
#                           relay_type='phase',
#                           coef_A=coef_A_2ph_cold,
#                           title='БТН 2-го типа',
#                           phase='B')




# data = DataClass("csv", "220kV_new/", "220_BTN3phase0", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase0", time_duration=time_duration)
#
# plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_C_eff_ph)
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()

# compare_effective_current(eff_curr_time=eff_curr.time,
#                           eff_curr_data=eff_curr.I_A_eff_ph,
#                           model_Imax_relative_time=data.Imax_A_relative_time_partial,
#                           model_Imax_time=data.Imax_A_time[:len(data.Imax_A_relative_time_partial)]+0.01,
#                           model_data_name="Model220",
#                           average_C0=average_C0_1ph,
#                           average_C1=average_C1_1ph,
#                           coef_A=coef_A_2ph_cold,
#                           phase='A')
#
# plt.plot(eff_curr.time, eff_curr.I_AB_eff)
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_CA_eff)
# plt.legend(['I_AB', 'I_BC', 'I_CA'])
# plt.show()
#
