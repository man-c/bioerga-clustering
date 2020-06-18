## bioerga-clustering
Clustering and representation methods for proteins and protein trajectories in <b>Python</b> using several distance metrics.

<p align="center">
  <img height=220px src="./docs/images/gromos.png?raw=true">
</p>

The methods are implemented using several libraries, such as
* [PyEMMA](https://github.com/markovmodel/PyEMMA/) (molecular dynamics (MD) analysis, featurization and Markov State Models),
* [rmsd](https://github.com/charnley/rmsd) (root-mean-square deviation (RMSD) of molecules using rotation),
* [mdtraj](https://github.com/mdtraj/mdtraj) (pdb files handling),
* [scikit-learn](https://github.com/scikit-learn/scikit-learn) (machine learning methods in Python)

This project provides a number of tools and interfaces developed in the context of ["INSPIRED-ΕΚΠΑ"](https://www.inspired-ris.gr/subprojects.html) which is a subproject of ["INSPIRED](https://www.inspired-ris.gr/index_en.html) - The National Research Infrastructures on Integrated Structural Biology, Drug Screening Efforts & Drug target functional characterization". More information can be found on [bioerga](http://bioerga.di.uoa.gr/) the webpage of the [ΕρΓΑ](http://erga.di.uoa.gr/) Lab dedicated on research in the area of applications of informatics in biology.

#### Dependencies
~~~~~~~~~~~
- Python (>= 3.6)
- numpy (>=1.18)
- pyEMMA (>=2.5)
- mdshare (>=0.4)
- mdtraj (>=1.9)
- rmsd (>=1.3)
- scikit-learn (>=0.23)
~~~~~~~~~~~

#### Instalation
```bash
pip install -r requirements.txt
```

