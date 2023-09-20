from data_class.DataClassNP import DataClass
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from GUI import instant_value as gui_iv
from GUI import group_of_curves as gui_gc

quantity_of_graph = 25
data = []
tau = []

for i in range(quantity_of_graph):
    tau.append((i + 1) * 20)
    data.append(DataClass("csv", "data2/", "tau_" + str(tau[i])))
    data[i].set_relative_time(tau[i])

# gui_iv.plot_instant_value(data[3], tau[3])
gui_gc.plot_instant_value(data, tau, show_="half")



# tau = 200
# data.append(DataClass("csv", "data2/", "tau_" + str(tau)))
# data[0].set_relative_time(tau)
# print(data[0].time)
#
# gui_iv.plot_instant_value(data[0], tau=tau)
