import numpy as np
from .rmsd_dist import *


def create_distance_mat(X, dist_func):
    n = len(X)
    D = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            D[i, j] = (dist_func(X[i], X[j]))
    return D
