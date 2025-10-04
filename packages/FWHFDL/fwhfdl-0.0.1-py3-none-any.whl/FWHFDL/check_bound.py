import numpy as np


def check_bound(arr, lb, ub):
    arr = np.where(arr < lb, lb, arr)
    arr = np.where(arr > ub, ub, arr)
    return arr
