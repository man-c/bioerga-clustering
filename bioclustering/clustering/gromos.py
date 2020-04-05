import numpy as np


def gromos(D, cutoff):
    D_cutoff = (D <= cutoff)

    # clustering indices
    I = np.zeros(len(D)) - 1
    # medoids indices
    M = []
    n_clusters = 0

    while (1):
        # print(np.sum(D_cutoff,1))
        medoid_idx = np.argmax(np.sum(D_cutoff, 1))
        neighbors_idx = np.argwhere(D_cutoff[medoid_idx] > 0).flatten()
        # print(medoid_idx)
        # print(neighbors_idx)
        if len(neighbors_idx) == 0:
            break
        I[neighbors_idx] = n_clusters
        M.append(medoid_idx)
        n_clusters += 1
        # D_cutoff[medoid_idx,:]=False
        # D_cutoff[:, medoid_idx]=False
        D_cutoff[neighbors_idx, :] = False
        D_cutoff[:, neighbors_idx] = False
        # print('----\n')
    return I, M


def test_gormos(N=100, cutoff=0.4):
    D = np.random.rand(N, N)
    np.fill_diagonal(D, 0)
    D = np.tril(D) + np.tril(D, -1).T
    print('Start clustering')
    [I, M] = gromos(D, cutoff)
    return D, I, M
