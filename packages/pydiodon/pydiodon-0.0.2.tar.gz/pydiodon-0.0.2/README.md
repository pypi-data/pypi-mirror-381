# pydiodon

## What it is ##

numpy library for linear dimension reduction, part of diodon project

## Overview

The library provides functions to call most common linear dimension reduction methods, like
- PCA (Principal Component Analysis)
- CoA (Correspondence Analysis)
- MDS (Multidimensional Scaling)

Those three can be considered as parts of the release.

Other methods have been coded too, but tests are ongoing and the result is not garanteed, like:
- PCA-IV (PCA with Instrulental Variables, equivalent to PLS)
- PCAmet (PCA with metrics on spaces spanned by the rows and the columns)
- Can (Canonical Analysis)
- MCoA (Multiple Correspondence Analysis)
- MCan (Multiple Canonical Analysis)

Finally, a few tools are available (like plotting or computing indices) to facilitate the interpretaton of the results.

## Install
`
The installation procedure is given for Linux Ubunto 20 and up.

Diodon is written in python 3.8. Such a version or up must be present on the computer. The following python librairies must be installed:
- time
- os
- sys
- h5py
- numpy
- scipy
- matplotlib.pyplot

To install pydiodon, the user must have a directory named `diodon` somewhere in his/her computer. Installation is along the following steps:

```sh
# create directory diodon
[...]$mkdir diodon

# go into this directory,
$cd diodon

# clone pydiodon
$git clone git@gitlab.inria.fr:diodon/pydiodon.git

# go into pydiodon subdirectory
$cd pydiodon

# install pydiodon with a setup.py
$sudo python3 setup.py install
```


## To get started ..


Here is a simple toy example of Principal Components Analysis on a small random matrix.

First, create a toy matrix:

```python
# importing library
>>> import numpy as np # for creating the random matrix
>>> import pydiodon as dio
# creating a random matrix
>>> m = 10
>>> n = 5
>>> A = np.random.randn(m,n)
```

Then, the diodon command to perform PCA:

```python
# running PCA
>>> Y, L, V	= dio.pca(A, pretreatment="standard", k=-1, meth="svd")
```

Followed by a few functions for plotting the results

```python
# plotting the results
>>> dio.plot_eig(L, frac=True, cum=True, dot_size=20, title = "cumulated eigenvalues")
>>> dio.plot_components_scatter(Y, dot_size=5, title="Principal components")
>>> dio.plot_var(V, varnames=None)
```

## Why another library for Linear Dimension Reduction?

There exists several excellent libraries for PCA and related methods, especially in R, or some methods in Scikit-learn in python (see
https://scikit-learn.org/stable/modules/decomposition.html#decompositions).

A specific effort has been made for efficiency when analysing large datasets, and motivates the development and disseminatuon of library Diodon. The limiting factors are currently:
- the time for I/O
- the available RAM
and not the calculation time. The effort has focused on computing the SVD of a given matrix, which is a key step providing the results for any method.

Progresses in efficiency have been obtained through three choices, available when useful:
- use Random projection methods for computing the SVD of a large matrix
- bind numpy calls of functions with codes written in C++ with xxxx
- task based programming with Chameleon (for MDS only, on HPC architectures with distributed memory)

Using random projection methods is not new here. See e.g.https://scikit-learn.org/stable/modules/random_projection.html in scikit learn. In diodon, Gaussian Random Projectkon only has been implemented.

For the connection between MDS and rSVD, see
- P. Blanchard, P. Chaumeil, J.-M. Frigerio, F. Rimet, F. Salin, S. Thérond,
O. Coulaud, and A. Franc. A geometric view of Biodiversity: scaling to metage-
nomics. Research Report RR-9144, INRIA ; INRA, January 2018

For development of this approach with task based programming, distributed memory and chameleon, see
- E. Agullo, O. Coulaud, A. Denis, M. Faverge, A. Franc, J.-M. Frigerio, N. Furmento, A. Guilbaud, E. Jeannot, R. Peressoni, F. Pruvost, and S. Thibault. Task-based randomized singular value decomposition and multidimensional scaling. Research Report RR-9482, Inria Bordeaux - Sud Ouest ; Inrae - BioGeCo, September 2022.


## Datasets for tutorials

Three small datasets are available for learning how to use the library:
- *diatoms_sweden*: An array species x environment for diatoms in Scandinavia for PCA
- *example_coa*: An example from the book Lebart, Morineau & Fénelon, 1982, for CoA
- *guiana_trees*: A dissimilarity array between barcodes of Amazonian trees in French Guiana for MDS.

These datasets are available in a dedicated git, named *data4test*. To get it, just clone it at same level than *pydiodon*, i.e. in diodon directory. The procedure is as follows:

```sh
# go into directory diodon
$cd [..]/diodon

# clone the git
$git clone git@gitlab.inria.fr:diodon/data4tests.git
```


Then, datasets are in directory *.../diodon/data4tests*.


 To load a dataset, for example the dataset for PCA, be in directory *pydiodon/jupyter* (see why below), and simply type:

 ```python
 >>> import pydiodon as dio
 >>> A, rn, cn = dio.load_dataset("diatoms_sweden")
 ```

Then, the array will be in `A`, and rownames and colnames respectively in `rn` and `cn`. here is a simple example for MDS:

```python
>>> import pydiodon as dio
>>> A, rn, cn = dio.load_dataset("guiana_trees")
>>> X, S = dio.mds(A)
>>> dio.plot_components_scatter(X)
```

The dataset can be downloaded from any directory, provided the path to *diodon/data4tests* is specified as a second argument of function load_dataset(). This second argument has been set by default as the path from the directory with Jupyter notebooks, to be downloaded easily for any notebook. Let us assume the user has created a directory *diodon/pydiodon/myproject* and is in directory *myproject*. Then, load_dataset() will work with default setting. Let us assume now that the user has a own directory *diodon/myprojects/thisproject*. Then, loading a dataset is made through:

```python
>>> import pydiodon as dio
>>> A, rn, cn = dio.load_dataset("gjuiana_trees", datadir="../../data4tests/")
```

Do not forget the "/" at the end of the name of the directory.


## Tutorials with Jupyter notebooks

Several notebooks are available as tutorials, one for one method, as follows

| Notebook | method | ipynb | html |
|----------|--------|-------|------|
| pca_with_diodon | PCA | yes | yes|
| coa_with_diodon | CoA | yes | yes|
| mds_with_diodon | MDS | yes | yes|


The notebooks are given in two formats:
- ipynb, where they are interactive
- html, where they are frozen

For those who wish to play with the interactive version ipynb, it is advised to :
- create a directory not followed by the git and copy the notebooks, as
```sh
# be in $pydiodon
$mkdir my_notebooks

# copy the notebooks
$cd my_notebooks
$cp ../jupyter/*.ipynb .
```
- change the names, parameters, values in this directory only. Indeed, diodon team may wish to update a jupyter notebook, and push the change on the git. If the user has changeed himself/herself the same notebook, there will be a cnflict of versions.

## Documentation

The library is documented with Sphynx. html file is available at

## ID card

**maintainer:** Alain Franc

*mail:* alain.franc@inrae.fr

**contributors:**

- Olivier Coulaud
- Alain Franc
- Jean-Marc Frigerio
- Romain Peressoni
- Florent Pruvost

**started:**  21/02/17
**version:** 22.11.07

**release:** ongoing

**licence:** GPL-3
