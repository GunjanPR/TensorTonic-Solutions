from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x_s = set(x)
    x_d = {}
    for i in x:
        if i not in x_d:
            x_d[i] = 1
        else:
            x_d[i] = x_d[i] + 1
    return({'mean':float(np.mean(x)),'median':float(np.median(x)),'mode':float(max(x_d, key=x_d.get))})