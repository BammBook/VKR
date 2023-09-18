import csv
import math


class DataClass:
    def __init__(self):
        self.time = list()

        self.I_A = list()
        self.I_B = list()
        self.I_C = list()

        self.brk = list()

        self.U_A = list()
        self.U_B = list()
        self.U_C = list()

        self.Imax_A = list()
        self.Imax_A_relative = list()

        self.Imax_A_time = list()
        self.Imax_A_relative_time = list()

    def read_csv(self, filepath, filename):
        with open("../" + filepath + filename + ".csv", encoding='utf-8') as row_file:
            file_reader = csv.reader(row_file, delimiter=",")
            count = 0
            for row in file_reader:
                # добавить считывание количества переменных
                if count == 0:
                    pass
                else:
                    self.time.append(float(row[0]))
                    self.I_A.append(float(row[1]))
                    self.I_B.append(float(row[2]))
                    self.I_C.append(float(row[3]))
                    self.brk.append(float(row[4]))
                    self.U_A.append(float(row[5]))
                    self.U_B.append(float(row[6]))
                    self.U_C.append(float(row[7]))
                count += 1
            # print('file was read')

    def set_Imax(self):
        eps = 0.05
        for i in range(1, len(self.time) - 2, 1):
            if self.I_A[i] - self.I_A[i + 1] > 0 and self.I_A[i - 1] - self.I_A[i] < 0 and self.I_A[i] > eps:
                self.Imax_A.append(self.I_A[i])
                self.Imax_A_time.append(self.time[i])

    def set_relative_Imax(self, A0):
        for i in range(len(self.Imax_A)):
            self.Imax_A_relative.append(self.Imax_A[i] / A0)

    def time_shift(self, time_shift):
        for i in range(len(self.Imax_A_time)):
            self.Imax_A_time[i] = round(self.Imax_A_time[i] - time_shift, 2)

    def set_relative_time(self, tau):
        """input tau in ms"""
        for i in range(len(self.Imax_A_time)):
            self.Imax_A_relative_time.append(self.Imax_A_time[i] / (tau * 0.001))
