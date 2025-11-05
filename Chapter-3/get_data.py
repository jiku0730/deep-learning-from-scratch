import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

def get_data():
    (_, _), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False, one_hot_label=False)
    return x_test, t_test
