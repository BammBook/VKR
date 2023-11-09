import math

from XML_Parser.ModelData import ModelData
from data_сlass.EffectiveCurrents import EffectiveCurrents
import matplotlib.pyplot as plt
from data_сlass.help_functions import *


B_s = 1.21
B_r_B = 0.06
B_r_C = 0.1245


ang_1ph_A = [1 * math.pi, 0 * math.pi]  # phase A

ang_2ph_B = [(7 / 6) * math.pi, (-1 / 6) * math.pi]  # phase B
ang_2ph_C = [(5 / 6) * math.pi, (1 / 6) * math.pi]  # phase C

phase_shift_2ph = math.pi / 3

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


# coef_A_1_phase_A = coef_A(B_s=B_s, B_r=B_r_A, omega_t=ang_1ph_A[0], omega_t0=ang_1ph_A[1])
#
# print(f'coef A = {coef_A_1_phase_A + 1}')
# time_duration = 2.5
#
# md = ModelData("Model220")
#
# X_eq = md.X
# R_eq = md.R
#
# tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)
# convert_to_named_units_coef = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(md.X ** 2 + md.R ** 2))
#
# curve_first_harm_eff = convert_to_named_units_coef * first_harm_effective(coef_A_1_phase_A)
#
# print(f'effective current {curve_first_harm_eff}')



time_duration = 2.5

md = ModelData("Model220")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)
convert_to_named_units_coef = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(md.X ** 2 + md.R ** 2))

curve_first_harm_eff_B = convert_to_named_units_coef * first_harm_effective(coef_A_2_phase_B)
curve_first_harm_eff_C = convert_to_named_units_coef * first_harm_effective(coef_A_2_phase_C)
print(curve_first_harm_eff_B)
print(curve_first_harm_eff_C)


linear_model = curve_first_harm_eff_B + curve_first_harm_eff_C

print(f'effective current {linear_model}')




# time_duration = 2.5
#
# eff_curr_1ph = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN1phaseA0B180C180", time_duration=time_duration)
# plt.title('1-ф БТН')
# plt.plot(eff_curr_1ph.time, eff_curr_1ph.I_A_eff_ph)
# plt.plot(eff_curr_1ph.time, eff_curr_1ph.I_B_eff_ph)
# plt.plot(eff_curr_1ph.time, eff_curr_1ph.I_C_eff_ph)
# plt.legend(['I_A_ф', 'I_B_ф', 'I_C_ф'])
# plt.show()



eff_curr_2ph = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN2phase", time_duration=time_duration)
plt.title('2-ф БТН')
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_A_eff_ph)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_B_eff_ph)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_C_eff_ph)
plt.legend(['I_A_ф', 'I_B_ф', 'I_C_ф'])
plt.show()

plt.title('2-ф БТН')
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_AB_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_BC_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_CA_eff)
plt.legend(['I_AB_лин', 'I_BC_лин', 'I_CA_лин'])
plt.show()

plt.title('2-ф БТН')
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_BC_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_B_eff_ph)
plt.legend(['I_BC_лин (RTDS)', 'I_B_ф (RTDS)'])
plt.show()



eff_curr_3ph1 = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase90", time_duration=time_duration)

plt.title('2-ф БТН')
plt.plot(eff_curr_3ph1.time, eff_curr_3ph1.I_A_eff_ph)
plt.plot(eff_curr_3ph1.time, eff_curr_3ph1.I_B_eff_ph)
plt.plot(eff_curr_3ph1.time, eff_curr_3ph1.I_C_eff_ph)
plt.legend(['I_A_ф', 'I_B_ф', 'I_C_ф'])
plt.show()

plt.title('2-ф БТН')
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_AB_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_BC_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_CA_eff)
plt.legend(['I_AB_лин', 'I_BC_лин', 'I_CA_лин'])
plt.show()

plt.title('2-ф БТН')
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_BC_eff)
plt.plot(eff_curr_2ph.time, eff_curr_2ph.I_B_eff_ph)
plt.legend(['I_BC_лин (RTDS)', 'I_B_ф (RTDS)'])
plt.show()
