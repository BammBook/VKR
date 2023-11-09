from GUI.presentation import presentation
import numpy as np
from matplotlib import pyplot as plt


def two_curves(x1_data: np.ndarray,
               y1_data: np.ndarray,
               x2_data: np.ndarray,
               y2_data: np.ndarray,
               legend: list,
               xlabel: str,
               ylabel: str):

    """
    два любых графика
    """
    presentation()

    fig, ax = plt.subplots()
    ax.plot(x1_data, y1_data)
    ax.plot(x2_data, y2_data)

    plt.legend(legend)

    plt.xlim([x1_data[0], x1_data[-1]])
    plt.xlabel(xlabel, loc="center", fontsize=12)
    plt.ylabel(ylabel, loc="center", fontsize=12)

    ax.grid(which="both", color='grey')
    ax.minorticks_on()

    plt.show()
