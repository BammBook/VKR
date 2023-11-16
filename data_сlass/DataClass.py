import numpy as np

from data_сlass.read_csv import read_csv

def set_Imax_and_t_max(I_ph: np.ndarray,
                       time_data: np.ndarray,
                       time_duration: float,
                       sampling_rate: float = 50e-6):

    """
    функция определяет максимумы тока при БТН (огибающая максимумов)
    """
    eps = 0.4
    max_counter = 99  # костыль для 99 точек
    counter = 0  # костыль для 99 точек
    Imax_ph = []
    Imax_ph_time = []

    number_of_points = int(time_duration / sampling_rate)
    if number_of_points > len(time_data):
        number_of_points = len(time_data)

    for i in range(1, number_of_points - 2, 1):
        # if np.abs(I_ph[i]) - np.abs(I_ph[i + 1]) > 0 and \
        #         np.abs(I_ph[i - 1]) - np.abs(I_ph[i]) < 0 and \
        #         np.abs(I_ph[i]) > eps and counter < max_counter:
        #
        #     Imax_ph.append(I_ph[i])
        #     Imax_ph_time.append(time_data[i])
        #     counter += 1
        if I_ph[i+1] > I_ph[i] and I_ph[i-1] < I_ph[i] and np.abs(I_ph[i]) > eps and counter < max_counter:

                Imax_ph.append(I_ph[i])
                Imax_ph_time.append(time_data[i])
                counter += 1

    if len(Imax_ph) == 0:
        return np.array([0]), np.array([0])
    else:
        return np.array(Imax_ph), np.array(Imax_ph_time)


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
        """
        data-class для осциллограмм БТН и образованных от них данных для исследований
        """
        try:
            if datatype == "csv":
                data = read_csv(filepath, filename)
            # comtrade добавить позже
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


