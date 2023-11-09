import matplotlib as mpl
import matplotlib.pyplot as plt


def presentation():
    """
    используется для задания единого стиля графикам
    """
    mpl.rcParams['font.family'] = 'Times New Roman'
    # plt.grid(which='major', linewidth=0.8)
    mpl.rcParams['grid.color'] = 'grey'
    mpl.rcParams['grid.linewidth'] = 0.5

