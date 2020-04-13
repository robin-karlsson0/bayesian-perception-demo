import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def bayes_inf(mu_mle, sigma_mle, mu_0, sigma_0, N=1):
    '''Returns parameters for posterior.
    Args:
        mu_mle, mu_mle: 
        mu_0, sigma_0: Prior
    Ref: Bishop (2006) p.98
    '''
    mu = sigma_mle*mu_0 / (N*sigma_0 + sigma_mle) + N*sigma_0*mu_mle / (N*sigma_0 + sigma_mle)
    
    sigma = sigma_mle*sigma_0 / (sigma_mle + N*sigma_0)
    
    return mu, sigma


def plot(mu_lst, sigma_lst, range_min, range_max, vert_line=None, labels=None, res=200):
    
    dist_N = len(mu_lst)
    
    for i in range(dist_N):
        x = np.linspace(range_min, range_max, res)
        if labels is None:
            label = f"{i}"
        else:
            label = labels[i]
        
        plt.plot(x, stats.norm.pdf(x, mu_lst[i], sigma_lst[i]), label=label)
            
    if vert_line is not None:
        plt.axvline(vert_line, 0, 1, linestyle='--')
    
    if labels is not None:
        plt.legend()
    
    plt.show()
    
    