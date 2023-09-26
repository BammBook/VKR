import math

from PyResearch.data_сlass.DataClass import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.optimize import least_squares
from scipy.optimize import curve_fit
import numpy as np
from PyResearch.GUI import instant_value as gui_iv
from PyResearch.GUI import group_of_curves as gui_gc
from PyResearch.GUI import generic_curve as gui_generic
from PyResearch.approximation.approximation import *

from typing import Literal

from scipy.optimize import curve_fit
from numpy import array, exp
import matplotlib.pyplot as plt

quantity_of_graph = 25
data = []
tau = []

# for i in range(quantity_of_graph):
#     tau.append((i + 1) * 20)
#     data.append(DataClass("csv", "data2/", "tau_" + str(tau[i])))
#     data[i].set_relative_time(tau[i])
#
# gui_iv.plot_instant_value(data[3], tau[3])
# gui_gc.plot_group_of_curves(data, tau, show_="half")
# gui_generic.plot_generic_curve(data)


tau.append(500)
data.append(DataClass("csv", "data2/", "tau_" + str(tau[0])))
data[0].set_relative_time(tau[0])


# print(data[0].time)

# gui_iv.plot_instant_value(data[0], tau=tau[0])
# gui_gc.plot_group_of_curves(data, tau)

args = approximation('exp_1',
                     data[0].Imax_A_relative_time,
                     data[0].Imax_A_relative,
                     print_coef=True)


func = exp_1(data[0].Imax_A_relative_time, args[0], args[1])


# plt.plot(data[0].Imax_A_relative_time, data[0].Imax_A_relative)
# plt.plot(data[0].Imax_A_relative_time, func)
# plt.show()

R = 1
X = math.pi * 100 * R * tau[0] * 1e-3
coef = math.sqrt(2 / 3) * 230 / (math.sqrt(X ** 2 + R ** 2)) * 0.75
Itog = coef * func

# plt.plot(data[0].Imax_A_time, data[0].Imax_A)
# plt.plot(data[0].Imax_A_time, Itog)
# plt.show()

print('A0_real= ', data[0].Imax_A[0])
print('A0_coef = ', coef)



# """мгновенные и огибающая"""
# plt.plot(data[0].time - 0.5, data[0].I_A)
# plt.plot(data[0].Imax_A_time, data[0].Imax_A)
# plt.show()

"""мгновенные и огибающая огибающая"""
plt.plot(data[0].time - 0.52, data[0].I_A)
plt.plot(data[0].Imax_A_time, data[0].Imax_A)
plt.show()

"""мгновенные и аппроксимированная огибающая"""
plt.plot(data[0].time - 0.52, data[0].I_A)
plt.plot(data[0].Imax_A_time, Itog)
plt.show()
