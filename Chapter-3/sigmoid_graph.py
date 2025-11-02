import matplotlib.pylab as plt
import numpy as np
from sigmoid import sigmoid

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.savefig("result_sigmoid.png")
