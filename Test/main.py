import xml.dom.minidom

from DATA.DataClass import DataClass
from XML_Parser.ModelData import ModelData

quantity_of_graph = 25
data = []


# for i in range(quantity_of_graph):
#     tau = (i + 1) * 20
#     data.append(DataClass())
#
#     data[i].read_csv("csv_files/data2/", "tau_" + str(tau))
#     data[i].set_Imax()
#     data[i].time_shift(data[i].Imax_A_time[0])
#     data[i].set_relative_time(tau)
#     data[i].set_relative_Imax(data[i].Imax_A[0])


# print(data[24].time)

# plt.plot(data[24].time, data[24].I_A)
# plt.plot(data[21].Imax_A_time, data[21].Imax_A)
# plt.grid(True)
# plt.show()

# print(data[5].Imax_A_time[0])
# print(data[5].Imax_A_time[1])
# print(data[5].Imax_A_time[2])
# print()
# print(len(data[0].Imax_A_time))
# print(len(data[24].Imax_A_time))


# plt.plot(data[1].Imax_A_relative_time, data[1].Imax_A_relative, data[24].Imax_A_relative_time, data[24].Imax_A_relative)
# plt.show()



model = ModelData("Model1")

print(model.U_nom)
