import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.9, 1.1, 10000)
y1 = 4.1 * (1 - x) / 2.8
y2 = 9.7 * (1 - x) / 6.6
plt.plot(x, y1)
plt.plot(x, y2)
plt.scatter([1], [0], color="red")
plt.close()

x = np.linspace(0.3, 0.4, 10000)
y1 = 4.11 * (1 - x) / 2.8
y2 = 9.7 * (1 - x) / 6.6
plt.plot(x, y1, "g")
plt.plot(x, y2, "y")
plt.scatter([1], [0], color="red")
plt.close()
plt.show()
