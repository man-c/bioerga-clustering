import bioclustering
import numpy as np
import mdtraj


if __name__=='__main__':
    # load trajectory from pdb file
    traj=mdtraj.load_pdb('data/2eqq.pdb')
    # keep only coordinates
    X=traj.xyz
    # create distance matrix using c-RMSD
    D=bioclustering.molecule_distances.create_distance_mat(X, bioclustering.molecule_distances.crmsd_kabsch)
    print('cutoff:', np.mean(D))
    [I,M]=bioclustering.clustering.gromos(D, np.mean(D))
    print(I, M)

    # create distance matrix using d-RMSD
    D=bioclustering.molecule_distances.create_distance_mat(X, bioclustering.molecule_distances.drmsd)
    print('cutoff:', np.mean(D))
    [I,M]=bioclustering.clustering.gromos(D, np.mean(D))
    print(I, M)

    # create atom distances vectors
    X_atom_dists=[]
    for mol in X:
        X_atom_dists.append(bioclustering.featurization.atom_distances_vector(mol))
