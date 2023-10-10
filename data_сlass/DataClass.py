import numpy as np
from PyResearch.data_сlass.read_csv import read_csv


def set_Imax_and_t_max(I_ph: np.ndarray,
                       time_data: np.ndarray,
                       time_duration: float,
                       sampling_rate: float = 50e-6):

    eps = 0.08
    max_counter = 99  # костыль для 99 точек
    counter = 0  # костыль для 99 точек
    Imax_ph = []
    Imax_ph_time = []

    number_of_points = int(time_duration / sampling_rate)
    if number_of_points > len(time_data):
        number_of_points = len(time_data)

    for i in range(1, number_of_points - 2, 1):
        if np.abs(I_ph[i]) - np.abs(I_ph[i + 1]) > 0 and \
                np.abs(I_ph[i - 1]) - np.abs(I_ph[i]) < 0 and \
                np.abs(I_ph[i]) > eps and counter < max_counter:

            Imax_ph.append(I_ph[i])
            Imax_ph_time.append(time_data[i])
            counter += 1
    if len(Imax_ph) == 0:
        return np.array([0]), np.array([0])
    else:
        return np.array(Imax_ph), np.array(Imax_ph_time)

# def set_Imax_and_t_max(I_ph, time_data, time_duration, sampling_rate):
#     eps = 0.05
#     T = 20e-3
#     number_of_max = int(time_duration / T)
#
#     Imax_ph = np.zeros(number_of_max)
#     Imax_ph_time = np.zeros(number_of_max)
#     counter = 0
#
#     number_of_points = int(time_duration / sampling_rate)
#     if number_of_points > len(time_data):
#         number_of_points = len(time_data)
#
#     for i in range(1, number_of_points - 2, 1):
#         if np.abs(I_ph[i]) - np.abs(I_ph[i + 1]) > 0 and \
#                 np.abs(I_ph[i - 1]) - np.abs(I_ph[i]) < 0 and \
#                 np.abs(I_ph[i]) > eps:
#
#             Imax_ph[counter] = I_ph[i]
#             Imax_ph_time[counter] = time_data[i]
#             counter += 1
#     return Imax_ph, Imax_ph_time


# def time_shift(Imax_time):
#     for i in range(len(Imax_time)):
#         Imax_time = np.around(Imax_time - Imax_time[0], 2)
#     return np.array(Imax_time)

# def set_relative_time(Imax_time, tau):
#     """input tau in ms"""
#     Imax_relative_time = []
#     for i in range(len(Imax_time)):
#         Imax_relative_time.append(Imax_time[i] / (tau * 0.001))
#     return np.array(Imax_relative_time)

# def set_partial_relative_time(relative_time, relative_current,  max_value: int = 5):
#     """тут можно узнать нужный номер и выполнить обрезку"""
#     Imax_relative_time_partial = []
#     Imax_relative_partial = []
#
#     for i in range(len(relative_time)):
#         if relative_time[i] <= max_value:
#             Imax_relative_time_partial.append(relative_time[i])
#             Imax_relative_partial.append(relative_current[i])
#     return Imax_relative_time_partial, Imax_relative_partial

def set_relative_Imax(Imax: np.ndarray):
    return np.divide(Imax, Imax[0])

def time_shift(Imax_time: np.ndarray):
    return np.round(np.array(Imax_time - Imax_time[0]), 2)

def set_relative_time(Imax_time: np.ndarray,
                      tau: int):
    return np.array(Imax_time / (tau * 0.001))

def set_partial_relative_time(relative_time: np.ndarray,
                              relative_current: np.ndarray,
                              max_value: int = 5):
    count = 0
    for i in range(len(relative_time)):
        if relative_time[i] <= max_value:
            count += 1
        else:
            break
    return relative_time[:count], relative_current[:count]


class DataClass:
    def __init__(self, datatype, filepath, filename, tau: int,  time_duration, sampling_rate=50e-6):
        """добавить проверку datatype"""

        try:
            if datatype == "csv":
                data = read_csv(filepath, filename)
            # comtrade
        except ValueError:
            print("Specify the supported source data file type")
        else:
            self.tau = tau
            self.sampling_rate = sampling_rate  # 50 ms (base RTDS rate)
            self.time_duration = time_duration

            self.time = np.array(data[0])

            self.I_A = np.array(data[1])
            self.I_B = np.array(data[2])
            self.I_C = np.array(data[3])

            self.brk_A = np.array(data[4])
            self.brk_B = np.array(data[5])
            self.brk_C = np.array(data[6])

            self.U_A = np.array(data[7])
            self.U_B = np.array(data[8])
            self.U_C = np.array(data[9])

            # Curve of maximums
            self.Imax_A, self.Imax_A_time = set_Imax_and_t_max(self.I_A, self.time, self.time_duration, self.sampling_rate)
            self.Imax_B, self.Imax_B_time = set_Imax_and_t_max(self.I_B, self.time, self.time_duration, self.sampling_rate)
            self.Imax_C, self.Imax_C_time = set_Imax_and_t_max(self.I_C, self.time, self.time_duration, self.sampling_rate)

            self.Imax_A_time = time_shift(self.Imax_A_time)
            self.Imax_B_time = time_shift(self.Imax_B_time)
            self.Imax_C_time = time_shift(self.Imax_C_time)

            # Curve of relative maximums
            self.Imax_A_relative = set_relative_Imax(self.Imax_A)
            self.Imax_B_relative = set_relative_Imax(self.Imax_B)
            self.Imax_C_relative = set_relative_Imax(self.Imax_C)

            # Relative time axis
            self.Imax_A_relative_time = set_relative_time(self.Imax_A_time, self.tau)
            self.Imax_B_relative_time = set_relative_time(self.Imax_B_time, self.tau)
            self.Imax_C_relative_time = set_relative_time(self.Imax_C_time, self.tau)

            # Partial relative time for approximation
            self.Imax_A_relative_time_partial, self.Imax_A_relative_partial = \
                set_partial_relative_time(self.Imax_A_relative_time, self.Imax_A_relative)
            self.Imax_B_relative_time_partial, self.Imax_B_relative_partial = \
                set_partial_relative_time(self.Imax_B_relative_time, self.Imax_B_relative)
            self.Imax_C_relative_time_partial, self.Imax_C_relative_partial = \
                set_partial_relative_time(self.Imax_C_relative_time, self.Imax_C_relative)

    # def set_relative_time(self, tau):
    #     """input tau in ms"""
    #     Imax_A_relative_time = []
    #
    #     for i in range(len(self.Imax_A_time)):
    #         Imax_A_relative_time.append(self.Imax_A_time[i] / (tau * 0.001))
    #     self.Imax_A_relative_time = np.array(Imax_A_relative_time)

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
