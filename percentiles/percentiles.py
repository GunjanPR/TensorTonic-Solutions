import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.sort(x)
    q_v = np.array([])
    for i in q:
        p = (i/100.0) * (len(x)-1)
        p_v = x[int(np.floor(p))] + (p - int(p)) * (x[int(np.ceil(p))] - x[int(np.floor(p))])
        q_v = np.append(q_v,p_v)
    return(q_v)