import math

from matplotlib import pyplot as plt

from XML_Parser.ModelData import ModelData
from data_сlass.DataClass import DataClass
from data_сlass.EffectiveCurrents import EffectiveCurrents

time_duration = 2.5

md = ModelData("Model220")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)


"""1 phase"""
# data = DataClass("csv", "220kV_new/", "220_BTN1phaseA0B180C180", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN1phaseA0B180C180", time_duration=time_duration)

"""2 phase"""
# data = DataClass("csv", "220kV_new/", "220_BTN2phase", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN2phase", time_duration=time_duration)

"""3 phase 1"""
data = DataClass("csv", "220kV_new/", "220_BTN3phase90", tau=tau, time_duration=time_duration)
eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase90", time_duration=time_duration)

"""3 phase 2"""
data = DataClass("csv", "220kV_new/", "220_BTN3phase0", tau=tau, time_duration=time_duration)
eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phase0", time_duration=time_duration)

"""diff_time"""
data = DataClass("csv", "220kV_new/", "220_BTN3phaseA0B90C90", tau=tau, time_duration=time_duration)
eff_curr = EffectiveCurrents("csv", "220kV_new/", "TO220_BTN3phaseA0B90C90", time_duration=time_duration)

plt.plot(data.time, data.I_A)
plt.plot(data.time, data.I_B)
plt.plot(data.time, data.I_C)
plt.legend(['I_A', 'I_B', 'I_C'])
plt.show()

"""1 phase, 3 phase 2, diff_time"""
plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
plt.plot(eff_curr.time, eff_curr.I_CA_eff)
plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
plt.legend(['фазный', 'линейный', 'ток НП'])
plt.show()

# """2 phase, 3 phase 1"""
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
# plt.legend(['фазный', 'линейный', 'ток НП'])
# plt.show()





time_duration = 2.5

md = ModelData("Model110")

X_eq = md.X
R_eq = md.R

tau = round(X_eq / (2 * math.pi * 50 * R_eq) * 1000, 2)


"""1 phase"""
# data = DataClass("csv", "110кV_new/", "110_BTN1phaseA0(B180C180)", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "110кV_new/", "TO110_BTN1phaseA0(B180C180)", time_duration=time_duration)

"""2 phase"""
# data = DataClass("csv", "110кV_new/", "110_BTN2phase", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "110кV_new/", "TO110_BTN2phase", time_duration=time_duration)

"""3 phase 1"""
# data = DataClass("csv", "110кV_new/", "110_BTN3phase90", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "110кV_new/", "TO110_BTN3phase90", time_duration=time_duration)
#
# """3 phase 2"""
# data = DataClass("csv", "110кV_new/", "110_BTN3phase0", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "110кV_new/", "TO110_BTN3phase0", time_duration=time_duration)
#
# """diff_time"""
# data = DataClass("csv", "110кV_new/", "110_BTN3phaseA0B90C90", tau=tau, time_duration=time_duration)
# eff_curr = EffectiveCurrents("csv", "110кV_new/", "TO110_BTN3phaseA0B90C90", time_duration=time_duration)

# plt.plot(data.time, data.I_A)
# plt.plot(data.time, data.I_B)
# plt.plot(data.time, data.I_C)
# plt.legend(['I_A', 'I_B', 'I_C'])
# plt.show()

# """1 phase, 3 phase 2, diff_time"""
# plt.plot(eff_curr.time, eff_curr.I_A_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_AB_eff)
# plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
# plt.legend(['фазный', 'линейный', 'ток НП'])
# plt.show()

# """2 phase, 3 phase 1"""
# plt.plot(eff_curr.time, eff_curr.I_B_eff_ph)
# plt.plot(eff_curr.time, eff_curr.I_BC_eff)
# plt.plot(eff_curr.time, eff_curr.I_3I0_eff)
# plt.legend(['фазный', 'линейный', 'ток НП'])
# plt.show()


