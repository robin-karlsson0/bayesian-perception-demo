import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def expectation(a, b):
    return a / (a + b)


def variance(a, b):
    return a * b / ( (a + b)**2 * (a + b + 1) )


def plot(a_lst, b_lst, labels=None, res=200):
    
    dist_N = len(a_lst)
    
    for i in range(dist_N):
        x = np.linspace(0, 1, res)
        if labels is None:
            label = f"{i}"
        else:
            label = labels[i]
    
        plt.plot(x, stats.beta.pdf(x, a_lst[i], b_lst[i]), label=label)
    
    if labels is not None:
        plt.legend()
    
    plt.show()