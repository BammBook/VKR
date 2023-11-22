import numpy as np

from data_сlass.read_csv import read_csv

def time_axis_shift(data):
    """считает сколько значений меньше нуля"""
    counter = 0
    for item in data:
        if item <= 0:
            counter += 1
    return counter

class EffectiveCurrents:
    """
    Data-class для осциллограмм действующих значений токов
    """
    def __init__(self, datatype, filepath, filename, time_duration, sampling_rate=50e-6):
        try:
            if datatype == "csv":
                data = read_csv(filepath, filename)
            # comtrade
        except ValueError:
            print("Specify the supported source data file type")
        else:
            # counter = time_axis_shift(data[0])

            self.time = np.array(data[0])

            self.I_3I0_eff = np.array(data[1])

            self.I_AB_eff = np.array(data[2])
            self.I_A_eff_ph = np.array(data[3])

            self.I_BC_eff = np.array(data[4])
            self.I_B_eff_ph = np.array(data[5])

            self.I_CA_eff = np.array(data[6])
            self.I_C_eff_ph = np.array(data[7])





