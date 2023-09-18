from data_class.DataClassNP import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from GUI import instant_value as plot_iv

quantity_of_graph = 25
data = []

# for i in range(quantity_of_graph):
#     tau = (i + 1) * 20
#     data.append(DataClass("csv", "data2/", "tau_" + str(tau)))
#     data[i].set_relative_time(tau)

tau = 200
data.append(DataClass("csv", "data2/", "tau_" + str(tau)))
data[0].set_relative_time(tau)

# print(data[20].Imax_A_time[0])
# print(data[20].Imax_A_time[1])
# test = DataClass("csv", "data2/", "tau_40")
# print(test.Imax_A_relative)

plot_iv.plot_instant_value(data[0].time, data[0].I_A, tau=tau)
