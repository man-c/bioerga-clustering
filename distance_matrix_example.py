import bioclustering
import numpy as np

A = np.array([[1.0, 1.0],
              [1.0, 2.0],
              [2.0, 1.5]])

# Same "molecule"
B = np.array([[1.0, 1.0],
              [1.0, 2.0],
              [2.0, 1.5]])

B *= 1.4

# Translate
B -= 3

C=np.array([A,B])

# Distance matrices using c-rmsd and d-rmsd
D_crmsd=bioclustering.molecule_distances.create_distance_mat(C, bioclustering.molecule_distances.crmsd_kabsch)
D_drmsd=bioclustering.molecule_distances.create_distance_mat(C, bioclustering.molecule_distances.drmsd)
