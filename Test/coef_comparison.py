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
from PyResearch.GUI.coef_comparison import coef_comparison

quantity_of_graph = 25
quantity_of_args = 2
coef = np.zeros((quantity_of_args, quantity_of_graph))

data = []
tau = []

for i in range(quantity_of_graph):
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "data2/", "tau_" + str(tau[i])))
    data[i].set_relative_time(tau[i])

    args = approximation('exp_1',
                         data[i].Imax_A_relative_time,
                         data[i].Imax_A_relative,
                         print_coef=False)

    for j in range(quantity_of_args):
        coef[j, i] = round(args[j], 3)


# gui_iv.plot_instant_value(data[3], tau[3])
# gui_gc.plot_group_of_curves(data, tau, show_="half")
# gui_generic.plot_generic_curve(data)

average_C0 = round(np.sum(coef[0])/np.size(coef[0]), 3)
average_C1 = round(np.sum(coef[1])/np.size(coef[1]), 3)

print(average_C0)
print(average_C1)

coef_comparison(coef, tau)

