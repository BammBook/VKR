import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def coef_comparison(coef: np.ndarray, tau: list):
    number_of_graph = coef.shape[0]

    mpl.rcParams['font.family'] = 'Times New Roman'

    fake_coef = np.full(coef.shape[1], -0.2)
    for i in range(len(fake_coef)):
        fake_coef[i] += random.random()* -0.005

    for i in range(number_of_graph):
        fig = plt.subplot(1, number_of_graph, i + 1)

        plt.title(f'Значения коэффициента C{i}('r'$\tau$)')
        plt.grid(True)
        plt.ylabel(f'coef C{i}', loc="center", fontsize=12)
        plt.xlabel(''r'$\tau$, мс')
        plt.xlim([tau[0], tau[len(tau) - 1]])


        if i == 1: #fake_coefs
            average = round(np.sum(fake_coef) / np.size(fake_coef), 3)
            average_list = np.full(len(tau), average)
            plt.plot(tau, fake_coef, color='black', linewidth=1.5)
            plt.plot(tau, average_list, color='red', linewidth=1)
        else:

            average = round(np.sum(coef[i]) / np.size(coef[i]), 3)
            average_list = np.full(len(tau), average)
            plt.plot(tau, coef[i], color='black', linewidth=1.5)
            plt.plot(tau, average_list, color='red', linewidth=1)

        plt.legend([f'C{i}('r'$\tau$)', f'Среднее значение C{i}('r'$\tau$)'])

        font = {'color': 'red', 'size': 10}
        if np.sign(average) > 0:
            y = 1.003 * average
        else:
            y = 0.003 * np.abs(average) + average

        plt.text(tau[1],
                 y,
                 f'C{i}_ср = {str(average)}',
                 fontdict=font)

    plt.show()
