import numpy as np
import matplotlib.pylab as plt
from step_function_for_array import step_function
from sigmoid import sigmoid

x = np.arange(-5.0 , 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x, y1, label="step_function")
plt.plot(x, y2, linestyle="--", label="sigmoid_function")
plt.ylim(-0.1, 1.1)
plt.legend()
plt.title("step vs sigmoid")
plt.savefig("result_step_vs_sigmoid.png")
