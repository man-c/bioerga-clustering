from sklearn.metrics import pairwise_distances


def atom_distances_vector(X):
    D = pairwise_distances(X)
    return D.flatten()