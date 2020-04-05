import rmsd
import numpy as np
from sklearn.metrics import pairwise_distances

__all__ = ['crmsd_kabsch', 'drmsd']


def crmsd_kabsch(A, B):
    # Translate
    A -= rmsd.centroid(A)
    B -= rmsd.centroid(B)

    # Rotate
    U = rmsd.kabsch(A, B)
    A = np.dot(A, U)

    return rmsd.rmsd(A, B)


def drmsd(A, B):
    # Pairs of distances for each pointset
    D_A = pairwise_distances(A)
    D_B = pairwise_distances(B)

    return np.sqrt(np.mean(np.power(D_A - D_B, 2)))
