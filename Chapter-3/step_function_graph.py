import numpy as np
import matplotlib.pylab as plt
from step_function_for_array import step_function

x = np.arange(-5.0 , 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.savefig("result.png")
