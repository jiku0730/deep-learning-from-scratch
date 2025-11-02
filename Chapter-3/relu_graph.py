import matplotlib.pylab as plt
import numpy as np
from relu import relu

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("ReLU function")
plt.savefig("result_ReLU.png")
