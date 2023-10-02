import numpy as np
import matplotlib.pyplot as plt

a = np.zeros((3, 4))

buffer = []
buffer.append([0, 1, 2, 3])
buffer.append([2, 4, 5, 2])
buffer.append([1, 3, 3])


for i in range(a.shape[0]):
    while len(buffer[i]) < a.shape[1]:
        buffer[i].append(None)
    a[i] = buffer[i]

x = a[:, 3]
print(a)
print()
print(x)

x_data = []
for i in range(a.shape[1]):
    x_data.append(a[:, i])

plt.boxplot(x_data)
plt.show()
