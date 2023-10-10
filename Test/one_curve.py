import math

from PyResearch.data_сlass.DataClass import DataClass

from PyResearch.GUI import plot_value as gui_iv
from PyResearch.GUI import generic_curve as gui_generic
from PyResearch.GUI import compare_two_graph as gui_two_graph
from PyResearch.GUI.compare_two_graph import set_relative_error

from PyResearch.approximation.approximation import *
from PyResearch.XML_Parser.ModelData import ModelData

import matplotlib.pyplot as plt


data = []
tau = []


"""read_data"""
tau.append(180)
data.append(DataClass("csv", "data2/", "tau_" + str(tau[0]), time_duration=2.5))
data[0].set_relative_time(tau[0])

"""graphs"""
# gui_iv.plot_instant_value(data[0], tau[0])
# gui_generic.plot_generic_curve(data, display_mode="partial")


"""approximation"""
"""
[-0.3, -0.3, -0.296, -0.29, -0.285, -0.281, -0.277, -0.274, -0.272, -0.27,
 -0.268, -0.266, -0.265, -0.264, -0.263, -0.262, -0.262, -0.261, -0.261, -0.26, -0.26, -0.26, -0.259, -0.259, -0.259]
[0.711, 0.724, 0.739, 0.755, 0.768, 0.782, 0.793, 0.804, 0.812, 0.821,
 0.829, 0.836, 0.843, 0.849, 0.854, 0.859, 0.863, 0.868, 0.872, 0.876, 0.88, 0.883, 0.887, 0.889, 0.892]
"""

max_value = 10
x_data = []
y_data = []
for i in range(len(data[0].Imax_A_relative_time)):
    if data[0].Imax_A_relative_time[i] <= max_value:
        x_data.append(data[0].Imax_A_relative_time[i])
        y_data.append(data[0].Imax_A_relative[i])

args = approximation('exp_2',
                     x_data,
                     y_data,
                     print_coef=True)


# args = approximation('exp_1',
#                      data[0].Imax_A_relative_time,
#                      data[0].Imax_A_relative,
#                      print_coef=True)


# approximated_curve = exp_1(data[0].Imax_A_relative_time, args[0], args[1])

approximated_curve = exp_2(data[0].Imax_A_relative_time, args[0], args[1])

# approximated_curve = exp_5(data[0].Imax_A_relative_time, args[0], args[1], args[2])


# # approximated_curve = exp_1(data[0].Imax_A_relative_time, -0.3, 0.711)

plt.plot(data[0].Imax_A_relative_time, data[0].Imax_A_relative)
plt.plot(data[0].Imax_A_relative_time, approximated_curve)
plt.show()


"""model_data"""
md = ModelData("Model1")                        # model_data
X = 2 * math.pi * md.f * md.R * tau[0] * 1e-3   # X is variable

coef_A0 = math.sqrt(2 / 3) * md.U_nom / (math.sqrt(X ** 2 + md.R ** 2)) * (2 - md.B_s + md.B_r)

print(f'A0_calculated = {round(coef_A0, 3)}')
print(f'A0_curve_of_I_max = {round(data[0].Imax_A[0], 3)}')


"""comparison"""
approximated_graph = approximated_curve * coef_A0
error = set_relative_error(data[0].Imax_A, approximated_graph)

gui_two_graph.compare_two_graph(data[0].Imax_A_time, data[0].Imax_A,
                                data[0].Imax_A_time, approximated_graph,
                                tau=tau[0],
                                error_data=error,
                                plot_error=True)



# plt.plot(data[0].Imax_A_time, error)
# plt.grid(True)
# plt.show()


"""мгновенные и огибающая"""
# plt.plot(data[0].time - 0.52, data[0].I_A, color='black', linewidth=0.5)
# plt.plot(data[0].Imax_A_time, data[0].Imax_A, color='red', linewidth=1)
# plt.plot(data[0].Imax_A_time, approximated_graph, color='green', linewidth=1)
# plt.show()
