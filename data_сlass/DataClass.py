import numpy as np
from PyResearch.data_сlass.read_csv import read_csv


def set_Imax_and_t_max(I_A, time_data, time_duration, sampling_rate):
    eps = 0.05
    max_counter = 99  # костыль для 99 точек
    counter = 0  # костыль для 99 точек
    Imax_A = []
    Imax_A_time = []

    number_of_points = int(time_duration / sampling_rate)
    if number_of_points > len(time_data):
        number_of_points = len(time_data)

    for i in range(1, number_of_points - 2, 1):
        if I_A[i] - I_A[i + 1] > 0 and I_A[i - 1] - I_A[i] < 0 and I_A[i] > eps and counter < max_counter:
            Imax_A.append(I_A[i])
            Imax_A_time.append(time_data[i])
            counter += 1
    return np.array(Imax_A), np.array(Imax_A_time)


def set_relative_Imax(Imax):
    return np.divide(Imax, Imax[0])


def time_shift(Imax_time):
    for i in range(len(Imax_time)):
        Imax_time = np.around(Imax_time - Imax_time[0], 2)
    return Imax_time


class DataClass:
    def __init__(self, datatype, filepath, filename, time_duration, sampling_rate=50e-6):
        try:
            if datatype == "csv":
                data = read_csv(filepath, filename)
            # comtrade
        except ValueError:
            print("Specify the supported source data file type")
        else:
            self.sampling_rate = sampling_rate  # 50 ms (base RTDS rate)
            self.time_duration = time_duration

            self.time = np.array(data[0])

            self.I_A = np.array(data[1])
            self.I_B = np.array(data[2])
            self.I_C = np.array(data[3])

            self.brk = np.array(data[4])

            self.U_A = np.array(data[5])
            self.U_B = np.array(data[6])
            self.U_C = np.array(data[7])

            self.Imax_A, self.Imax_A_time = set_Imax_and_t_max(self.I_A, self.time, self.time_duration,
                                                               self.sampling_rate)

            self.Imax_A_time = time_shift(self.Imax_A_time)

            self.Imax_A_relative = set_relative_Imax(self.Imax_A)

            self.Imax_A_relative_time = np.empty([len(self.Imax_A_time)])

            self.Imax_A_relative_time_partial = []
            self.Imax_A_relative_partial = []

    def set_relative_time(self, tau):
        """input tau in ms"""
        Imax_A_relative_time = []

        for i in range(len(self.Imax_A_time)):
            Imax_A_relative_time.append(self.Imax_A_time[i] / (tau * 0.001))
        self.Imax_A_relative_time = np.array(Imax_A_relative_time)

    # def set_partial(self, tau, max_value):
    #     Imax_A_relative_time_partial = []
    #     Imax_A_relative_partial = []
    #
    #     for i in range(len(self.Imax_A_relative_time)):
    #         current_item = self.Imax_A_relative_time[i] / (tau * 0.001)
    #         if current_item <= max_value:
    #             Imax_A_relative_time_partial.append(current_item)
    #             Imax_A_relative_partial.append(self.Imax_A_relative[i])
    #     self.Imax_A_relative_time_partial = np.array(Imax_A_relative_time_partial)
    #     self.Imax_A_relative_partial = np.array(Imax_A_relative_partial)



    # def set_relative_time(self, tau):
    #     """input tau in ms"""
    #     Imax_A_relative_time = []
    #     for i in range(len(self.Imax_A_time)):
    #         current_item = self.Imax_A_time[i] / (tau * 0.001)
    #         if current_item <= 5:
    #             Imax_A_relative_time.append(current_item)
    #
    #     self.Imax_A_relative_time = np.array(Imax_A_relative_time)

    # def set_Imax_A_to_relative_time(self):
    #     Imax_A_to_relative_time = []
    #     for i in range(len(self.Imax_A_relative_time)):
    #         Imax_A_to_relative_time.append(self.Imax_A[i] / self.Imax_A[0])
    #     self.Imax_A_to_relative_time = np.array(Imax_A_to_relative_time)
