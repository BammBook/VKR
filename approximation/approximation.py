from scipy.optimize import least_squares
import numpy as np
from scipy.optimize import curve_fit
from typing import Literal
from functools import partial


def exp_1(values_x, coef0, coef1):
    """custom"""
    return np.exp(coef0 * (values_x ** coef1))

def exp_2(values_x, coef0, coef1):
    """first_type_exp"""
    return coef0 * np.exp(values_x * coef1)

def exp_3(values_x, coef0, coef1):
    """second_type_exp"""
    return coef0 * values_x ** coef1

def exp_5(values_x, coef0, coef1, coef2):
    """first_type_exp"""
    return coef0 + coef1 * np.exp(values_x * coef2)

def exp_4(values_x, tau, coef0, coef1, coef2):

    return np.exp(coef0 * values_x + coef1 * tau * 1e-3 + coef2 * (values_x / (tau * 1e-3)))


model_list_name = Literal['exp_1', 'exp_2', 'exp_3', 'exp_5']

model_dictionary = {'exp_1': exp_1, 'exp_2': exp_2, 'exp_3': exp_3, 'exp_5': exp_5}


def approximation(function_name: model_list_name,
                  x_data: list,
                  y_data: list,
                  tau=None,
                  print_coef=False):

    if tau is not None:
        fit_function = partial(model_dictionary.get(function_name), tau=tau)
    else:
        fit_function = model_dictionary.get(function_name)

    args, covar = curve_fit(fit_function, x_data, y_data)

    if print_coef:
        print("\nType of approximation function: " + function_name)
        for i in range(len(args)):
            print(f'C{i} = {round(args[i], 3)}')
        print()

    return args
