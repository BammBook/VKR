import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PyResearch.data_сlass.DataClass import DataClass
from PyResearch.XML_Parser.ModelData import ModelData


def compare_two_graph(x_real: list, y_real: list,
                      x_appr: list, y_appr: list,
                      tau: int = 0,
                      error_data: list = None,
                      plot_error: bool = False,
                      max_error: float = 10.0):

    time = []
    for i in range(0, len(x_real)):
        if x_real[i]/(tau*1e-3) < 5:
            time.append(x_real[i])

    x_real = x_real[:len(time)]
    y_real = y_real[:len(time)]
    x_appr = x_appr[:len(time)]
    y_appr = y_appr[:len(time)]
    error_data = error_data[:len(time)]

    if plot_error is not True:

        two_graph(x_real, y_real,
                  x_appr, y_appr,
                  tau=tau)
        plt.show()

    else:

        fig1 = plt.subplot(2, 1, 1)
        two_graph(x_real, y_real,
                  x_appr, y_appr,
                  tau=tau)
        mpl.rcParams['font.family'] = 'Times New Roman'
        fig2 = plt.subplot(2, 1, 2)

        max_error_list = np.full(len(x_real), max_error)

        mpl.rcParams['font.family'] = 'Times New Roman'
        plt.plot(x_real, error_data, color='black')
        mpl.rcParams['lines.linewidth'] = 1.5

        plt.plot(x_real, max_error_list, color='red')
        mpl.rcParams['lines.linewidth'] = 1.0

        plt.xlabel('t, с', loc="center", fontsize=12)
        plt.ylabel(''r'$\delta$, %', loc="center", fontsize=12)

        plt.xlim([0, x_real[np.size(x_real) - 1]])
        plt.ylim([-0.05 * np.max(error_data), 1.05 * np.max(error_data)])

        plt.grid()
        mpl.rcParams['grid.color'] = 'grey'
        mpl.rcParams['grid.linewidth'] = 0.5

        plt.legend(['Погрешность', 'Допустимая погрешность'])

        plt.show()


def set_relative_error(y_real: list,
                       y_appr: list):

    error = np.round(np.abs(np.multiply(np.divide(np.subtract(y_real, y_appr), y_real), 100)), 3)
    return error


def two_graph(x_real: list, y_real: list,
              x_appr: list, y_appr: list,
              title_1: str = 'Реальное значение',
              title_2: str = 'Аппроксимированное значение',
              tau=0):

    mpl.rcParams['font.family'] = 'Times New Roman'

    plt.plot(x_real, y_real, color='black')
    mpl.rcParams['lines.linewidth'] = 1

    plt.plot(x_appr, y_appr, color='red')
    mpl.rcParams['lines.linewidth'] = 1.5

    plt.xlabel('t, с', loc="center", fontsize=12)
    plt.ylabel('Iₐ(t), кА', loc="center", fontsize=12)

    plt.xlim([0, x_real[np.size(x_real) - 1]])
    plt.ylim([-0.05 * np.max(y_real), 1.05 * np.max(y_real)])

    if tau <= 0:
        pass
    else:
        box = dict(facecolor='white', edgecolor='black')
        plt.text(0.7 * x_real[np.size(x_real) - 1],
                 0.7 * np.max(y_real),
                 ''r'$\tau$ =' + f'{tau} мс',
                 bbox=box)

    plt.grid()
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

    plt.legend([title_1, title_2])













#     if plot_error is not True:
#
#         two_graph(x_real, y_real,
#                   x_appr, y_appr,
#                   tau=tau)
#         plt.show()
#
#     else:
#
#         fig1 = plt.subplot(2, 1, 1)
#         two_graph(x_real, y_real,
#                   x_appr, y_appr,
#                   tau=tau)
#         mpl.rcParams['font.family'] = 'Times New Roman'
#         fig2 = plt.subplot(2, 1, 2)
#
#         max_error_list = np.full(len(x_real), max_error)
#
#         mpl.rcParams['font.family'] = 'Times New Roman'
#         plt.plot(x_real, error_data, color='black')
#         mpl.rcParams['lines.linewidth'] = 1.5
#
#         plt.plot(x_real, max_error_list, color='red')
#         mpl.rcParams['lines.linewidth'] = 1.0
#
#         plt.xlabel('t, с', loc="center", fontsize=12)
#         plt.ylabel(''r'$\delta$, %', loc="center", fontsize=12)
#
#         plt.xlim([0, x_real[np.size(x_real) - 1]])
#         plt.ylim([-0.05 * np.max(error_data), 1.05 * np.max(error_data)])
#
#         plt.grid()
#         mpl.rcParams['grid.color'] = 'grey'
#         mpl.rcParams['grid.linewidth'] = 0.5
#
#         plt.legend(['Погрешность', 'Допустимая погрешность'])
#
#         plt.show()
#
#
# def set_relative_error(y_real: list,
#                        y_appr: list):
#
#     error = np.round(np.abs(np.multiply(np.divide(np.subtract(y_real, y_appr), y_real), 100)), 3)
#     return error
#
#
# def two_graph(x_real: list, y_real: list,
#               x_appr: list, y_appr: list,
#               title_1: str = 'Реальное значение',
#               title_2: str = 'Аппроксимированное значение',
#               tau=0):
#     mpl.rcParams['font.family'] = 'Times New Roman'
#
#     plt.plot(x_real, y_real, color='black')
#     mpl.rcParams['lines.linewidth'] = 1
#
#     plt.plot(x_appr, y_appr, color='red')
#     mpl.rcParams['lines.linewidth'] = 1.5
#
#     plt.xlabel('t, с', loc="center", fontsize=12)
#     plt.ylabel('Iₐ(t), кА', loc="center", fontsize=12)
#
#     plt.xlim([0, x_real[np.size(x_real) - 1]])
#     plt.ylim([-0.05 * np.max(y_real), 1.05 * np.max(y_real)])
#
#     if tau <= 0:
#         pass
#     else:
#         box = dict(facecolor='white', edgecolor='black')
#         plt.text(0.7 * x_real[np.size(x_real) - 1],
#                  0.7 * np.max(y_real),
#                  ''r'$\tau$ =' + f'{tau} мс',
#                  bbox=box)
#
#     plt.grid()
#     mpl.rcParams['grid.color'] = 'grey'
#     mpl.rcParams['grid.linewidth'] = 0.5
#
#     plt.legend([title_1, title_2])
