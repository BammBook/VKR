import numpy as np
import matplotlib.pyplot as plt
from PyResearch.GUI.presentation import presentation

from PyResearch.approximation.approximation import *

# for phase A
average_C0_1ph = -0.257
average_C1_1ph = 0.876

# for phase B, C
average_C0_2ph = -0.235
average_C1_2ph = 0.884

# for phase B, C
average_C0_3ph_1 = -0.239
average_C1_3ph_1 = 0.869

# for phase A, B, C
# average_C0_3ph_2 = 0
# average_C1_3ph_2 = 0

x_data = np.arange(0, 5, 0.01)
generic_curve_1 = exp_1(x_data, average_C0_1ph, average_C1_1ph)
generic_curve_2 = exp_1(x_data, average_C0_2ph, average_C1_2ph)
generic_curve_3 = exp_1(x_data, average_C0_3ph_1, average_C1_3ph_1)

presentation()
plt.plot(x_data, generic_curve_1)
plt.plot(x_data, generic_curve_2)
plt.plot(x_data, generic_curve_3)
plt.legend(['1ф.БТН', '2ф.БТН', '3ф.БТН (1 тип)'])

plt.xlim([x_data[0], x_data[-1]])
plt.ylim([-0.05, 1.05])

plt.xlabel('t/'r'$\tau$, о.е.', loc="center", fontsize=12)
plt.ylabel('k_з, о.е.', loc="center", fontsize=12)

plt.show()
