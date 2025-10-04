#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
A python library for linear dimension reduction.




**Identity card**


:authors:        - Alain Franc and Jean-Marc Frigerio
:mail:           - alain.franc@inria.fr
:contributors:   - Olivier Coulaud
                 - Romain Peressoni
                 - Florent Pruvost
:maintainer:     Alain Franc
:started:        21/02/17
:version:        25.04.03
:release:        0.1.0
:licence:        GPL-3.0 or later

This file is part of diodon project. You can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.


Information: the development of this library still is ongoing. When a
function has not been tested or its development still in infancy, this is
indicated in its documentation, and it is advised not to use it.

"""
print("loading pydiodon - version 25.04.03")

# as usual ...
import os
import sys

import shutil
import functools
import multiprocessing
import gc

# numpy, scipy
import numpy as np						# For arrays and basic linalg
import numpy.linalg	as nplin			# basic linear algebra (svd, qr)
import scipy as scp
import scipy.interpolate as sin			# for splines

# plots
import matplotlib.pyplot as plt			# for plots

# for testing time needed for a procedure
import time

# for loading hdf5
import h5py

#for spawn (send plot functions to multiprocessing or not (diosh))
from parametrizedDeco import spawn
skip = 'diosh' in sys.modules or 'yapsh' in sys.modules

########################################################################
#																	   #
#       Core Algorithms in linear algebra                			   #
#		- EVD														   #
#		- SVD														   #
#		- PCA														   #
#																	   #
########################################################################


# ----------------------------------------------------------------------
#
#	Eigendecomposition of a matrix
#
# ----------------------------------------------------------------------

def mat_evd(mat, k=-1):
	""" Computes the eigenvalues and eigenvectors of a matrix

	Parameters
	----------

	mat : a numpy array, `n x n` (a matrix)

	k : an integer
		the number of eigenvalues/vectors to be computed

	Returns
	-------

	V : a 2D numpy array
		of size `n x k`: the `k` eigenvectors

	L : a 1D numpy array
		a vector ; the first `k` eigenvalues

	Notes
	-----

	if `k=-1`, all eigenvalues and eigenvectors are returned.

	This simply uses ``numpy.linalg.eigh()``, and adds some features like

	- sorts eigenvalues in decreasing order
	- sorts eigenvectors in corresponding order
	- sets to zero the imaginary parts (numerical approximation)

	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> # building a symmetric matrix
		>>> n = 5
		>>> A = np.random.random((n,n))
		>>> A = (A + A.T)/2
		>>> # computing eigenvalues and eigenvectors
		>>> V, L = dio.mat_evd(A)

	version 21.03.21, 22.09.21, 22.10.13, 22.10.25
	"""

	# computation of eigenvalues and eigenvectors of Gram matrix
	res		= np.linalg.eigh(mat)     # eigenvalues and eigenvectors

	# L: eigenvalues
	L 		= res[0].real             # eigenvalues of <mat>
	vp_or	= L.ravel().argsort()     # increasing order
	vp_or	= vp_or[::-1]             # decreasing order
	L 		= L[vp_or]                # eigenvalues, decreasing

	# V: eigenvectors
	V = res[1]                      # eigenvectors
	V = V[:,vp_or]                  # according to eigenvalue order

	if k>0:
		L = L[0:k]             	  # first k axis
		V = V[:,0:k].real          # filtering out imaginary part (numerical inaccuracy)

	return V, L

# ----------------------------------------------------------------------
#
#		SVD through Gaussian random Projection
#
# ----------------------------------------------------------------------

def svd_grp(A, k):
	r""" SVD of a (large) matrix by *Gaussian Random Projection*


	Parameters
	----------

	A : a 2D numpy array
		the matrix to be studied (dimension :math:`n \\times p`)

	k : an integer
		the number of components to be computed

	Returns
	-------

	U : a 2D numpy array
		(dimension :math:`n \\times k`)

	S : a 1D numpy array
		(`k` values)

	V : a 2D numpy array
		(dimension :math:`p \\times k`)

	Notes
	-----

	Builds the SVD of `A` as :math:`A = U\Sigma V^t` where :math:`\Sigma` is the
	diagonal matrix with diagonal `S` and :math:`V^t` is the transpose of `V`.


	Here are the different steps of the computation:

	1. `A` is a :math:`n \\times p` matrix
	2. builds :math:`\Omega`, a :math:`p \\times k` random matrix (Gaussian)
	3. computes `Y = A`:math:`\Omega` (dimension :math:`n \\times k`)
	4. computes a QR decomposition of Y
		| `Y = QR`, with
		| `Q` is orthonormal (:math:`n \\times k`)
		| `R`	is upper triangular (`:math:`k \\times k`)
	5. computes `B = Q^t A`
		`B` is `:math:`k \\times p` (with `k < p`) and its SVD is supposed to be close to the one of `A`
	6. :math:`U_B`, `S`, and `V` are SVD of `B`:
			:math:`B = U_B S V'`, `S` is diagonal
	7. then, :math:`U_A`, `S` and `V` are close to svd of `A` : :math:`A = U_A S V'`

	*Sizes and computation of the matrices*

	============== =================== ============
	matrix         value               size
	============== =================== ============
	`A`            input               :math:`n \\times p`
	:math:`\Omega` random              :math:`p \\times k`
	`Y`            :math:`A\Omega`     :math:`n \\times k`
	`Q`            `Y = QR`            :math:`n \\times k`
	`B`            `B = Q^t A`         :math:`k \\times p`
	:math:`U_B`    :math:`B = U_BSV^t` :math:`k \\times k`
	`U`            :math:`U = QU_B`    :math:`n \\times k`
	============== =================== ============



	References
	----------

	[1] Halko & al., 2011, *SIAM Reviews*, **53(2):** 217-288


	af, rp, fp
	21.03.21; 22.06.16, 22.10.28
	"""
	p 			= A.shape[1]
	print("Computing Omega")
	Omega 		= np.random.randn(p,k).astype(A.dtype) # Computing Omega
	print("Computing A*Omega")
	Y 			= np.dot(A, Omega)		# Y = A\Omega
	print("running QR")
	Q, R 		= nplin.qr(Y)			# QR(Y)
	print("computing B")
	B 			= np.dot(Q.T,A)			# B = Q'A
	print("running SVD of B")
	U_B, S, VT	= nplin.svd(B, full_matrices=False)	    	# B = UB*S*VB'
	print("computing U")
	U			= np.dot(Q,U_B)			# A \sim U*S*VB'
	#
	return U, S, VT


# ----------------------------------------------------------------------
#
#			pca_evd(), pca_svd(), pca_grp()
#
# ----------------------------------------------------------------------

def pca_evd(A):
	"""runs the PCA with eigendecomposition of A'A

	Notes
	-----

	No documentation (used behind pca_core)
	21/06/27
	"""
	C		= A.T @ A
	V, L	= mat_evd(C)
	Y		= A @ V
	#
	return Y, L, V

# ----------------------------------------------------------------------

def pca_svd(A):
	""" runs the PCA with SVD of A

	Notes
	-----

	No documentation (used behind pca_core)
	21/06/27
	"""
	U, S, VT	= np.linalg.svd(A, full_matrices=False)
	V			= VT.T
	Y			= U @ np.diag(S)
	L			= S*S
	#
	return Y,L,V

# ----------------------------------------------------------------------

def pca_grp(A, k):
	""" runs the PCA with SVD with gaussian random projection

	Notes
	-----

	No documentation (used behind pca_core)
	21.06.27
	"""
	U, S, VT	= svd_grp(A, k)
	V			= VT.T
	Y			= U @ np.diag(S)
	L			= S*S
	#
	return Y, L, V




# ----------------------------------------------------------------------
#
#				pca_core()
#
# ----------------------------------------------------------------------

def pca_core(A, k=-1, meth="svd"):
	r""" core method for PCA (Principal Component Analysis) of an array

	Parameters
	----------

	A : a `n x p`  numpy array,
		array to be analysed

	k : an integer
		number of axis to compute

	meth : a string
		method for numerical computing

	Returns
	-------

	Y : a 2D numpy array, `n x k`
		matrix of principal components

	L : a 1D numpy array
		vector of eigenvalues


	V : a 2D numpy array, `p x k`
		matrix of eigenvectors (new basis)

	Notes
	-----

	`A` is an array, and ``pca_core`` computes the PCA of `A`, without any centering
	nor scaling nor weights nor constraints. PCA with centering, scaling,
	weights or constraints is called by function ``pca()`` which in turns calls this function `pca_core()`.

	if `k = -1`, all axis are computed. If `k > 0`, only `k`
	first axis and components are computed.

	if `meth` is

	- `evd`, runs by eigendecomposition of `A'A`
	- `svd`, runs by singular value decomposition of `A`
	- `grp`, runs by SVD of `A` with Gaussian random projection

	 Default value is `svd`.

	| With EVD, it runs as follows:
	| 1. Computes the correlation matrix :math:`C=A'A`
	| 2. Computes the eigevalues and eigevectors of :math:`C`: :math:`Cv_j = \lambda_j v_j`
	| 3. Computes the principal components as :math:`y_j=Av_j`, or, globally, :math:`Y=AV`

	| with SVD, it runs as follows:
	| 1. :math:`U,\Sigma,V = SVD(A)`
	| 2. :math:`Y = U\Sigma`
	| 3. :math:`L=\Sigma^2`

	**Example**

	This is an example of a standard PCA of a random matrix, with :math:`m` rows and
	:math:`n` columns, with elements as realisation of a Gaussian law with mean 0 and
	standrd deviation 1. As such, there is no need to center nor to scale,
	and the use of ``pca_core()`` is relevant.

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> m = 200 ; n = 50
		>>> A = np.random.randn(m,n)
		>>> L, V, Y = dio.pca_core(A)
		>>> plt.plot(L) ; plt.show()
		>>> plt.scatter(Y[:,0],Y[:,1]) ; plt.show()

	*af, revised 21.03.01; 21.06.27; 22.09.23, 22.10.13*
	"""

	if meth=="evd":
		Y, L, V	= pca_evd(A)
	#
	if meth=="svd":
		Y, L, V	= pca_svd(A)
	#
	if meth=="grp":
		if k==-1:
			exit("in pca_grp(), a value for k must be given explicitly")
		Y, L, V = pca_grp(A,k)
	#
	if meth in ['evd', 'svd']:
		if k > 0:
			Y   = Y[:,0:k]
			L   = L[0:k]
			V   = V[:,0:k]
	#
	return Y, L, V


########################################################################
#
#       Multidimensional Scaling
#
########################################################################



def mds(dis, k=-1, meth="svd", loop=True, Y_file=None, L_file=None):
	r""" Multidimensional Scaling of a distance or dissimilarity array

	Parameters
	----------

	dis : numpy array, `n x n`
		distances or dissimilarities

	k : integer
		number of axis

	meth : string
		method for MDS (see notes)

	no_loop : boolean
		see notes

	Returns
	-------

	X : 2D numpy array,
		`n x k`, coordinates of points

	S : 1D numpy array
		`k` values, singular values      |


	Notes
	-----

	**Objective**: builds a point cloud where one point represents an item, such that the discrepancies beween distances in a matrix `dis` and between associated
	points in :math:`R^k` is as small as possible.	It is classical MDS, not Least Square Scaling.

	| **Procedure:** There are three steps
	| 1. computes the Gram matrix `G` between items from distance matrix `dis`
	| 2. runs a SVD or EVD of `G`
	| 3. computes the coordinates from the SVD (or EVD) in `X`

	| **argument no_loop** : it is used in the computation of the Gram matrix:
	| - if `n` is large, ``no_loop=False`` is recommended
	| - if not, ``no_loop=True`` is recommended (default value)

	| **methods for MDS:** the argument ``meth`` specifies which method is selected for the core of MDS. Default value is ``svd``.  Let `G` be the Gram matrix associated to the distance array.
	| - if ``meth=svd``, the a SVD of `G` is run
	| - if ``meth=grp``, the SVD is run with Gaussian Random Projection
	| - if ``meth=evd``, the eigenvalues and eigenvectors of `G` are computed

	| Here are some suggestions for selection of the method:
	| - if `n` is not too large (:math:`n < 10,000`), ``svd`` method is recommended
	| - if `n` is large, ``grp`` method is recommended, and compulsory if `n` is very large
	| - if `k` is small, :math:`k \simeq 10`, ``evd`` method is recommended.

	| **computations** : EVD or SVD of the Gram matrix are two equivalent ways to compute a solution. Let `G` be the Gram matrix. They are linked by
	| - EVD: :math:`GU = US` ; `U` is the matrix of columnwise eigenvectors of `G` and `S` the diagonal matrix of its eigenvalues
	| - SVD: :math:`G = USU'` is the SVD of `G` (which is symmetric, `U'` is the transpose of `U`)
	| Then, in both cases, if `X` is the matrix of coordinates of `n` items in :math:`R^r`, :math:`X = US^{1/2}`

	**Examples**

	This is a first toy example for running a MDS.


	First, building a Euclidean distance matrix.

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> import scipy.spatial.distance as ssd # for computing distances
		>>> # creates a m x n point cloud
		>>> m = 10 ; n = 4
		>>> A = np.random.randn(m,n)
		>>> # computes the pairwise distances
		>>> D = ssd.pdist(A)
		>>> D = ssd.squareform(D)	# distance matrix in square form

	Second, run the MDS

	.. code:: python

		>>> # runs the MDS
		>>> X, S = dio.mds(D)

	Third, interpret the quality and displays the result

	.. code:: python

		>>> # plotting the quality
		>>> plt.plot(S, color="red")
		>>> plt.title("Eigenvalues")
		>>> plt.show()
		>>> # plotting the point cloud
		>>> F1 = X[:,0] ; F2 = X[:,1]
		>>> plt.scatter(F1, F2, c="chartreuse", s=20)
		>>> plt.xlabel("axis 1")
		>>> plt.ylabel("axis 2")
		>>> plt.show()


	This example is in ``mds_xmpl_1.py``

	Here is now a real life example.

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> #
		>>> rank = 200
		>>> filename = "guiana_trees.dissw"
		>>> Dis, rn, cn = dio.load(filename, rownames=True, colnames=True)
		>>> X, S = dio.mds(Dis, k=rank)


	This is focused on running the MDS of `Dis` . Here is a complementary example for visualizing the results.

	.. code:: python

		>>> # plotting the singular values
		>>> plt.plot(S, color="red")
		>>> plt.title("Quality along the axis")
		>>> plt.show()
		>>> # plotting the point cloud, axis 1 and 2
		>>> F1 = X[:,0]; F2 = X[:,1]; F3 = X[:,2]
		>>> plt.scatter(F1,F2,c="blue", s=5)
		>>> plt.xlabel("axis 1")
		>>> plt.ylabel("axis 2")
		>>> plt.title("data set: Guiana trees")
		>>> plt.show()


	This example is in ``mds_xmpl_guiana_trees.py``


	- The data set can be downloaded from https://doi.org/10.15454/XSJ079 where it is dataset  ``guiana_trees.dissw``.
	- Related publication: Caron, H, Molino, J‐F, Sabatier, D, et al. Chloroplast DNA variation in a hyperdiverse tropical tree community. *Ecol Evol.* 2019; **9:** 4897– 4905. https://doi.org/10.1002/ece3.5096
	- Can be downloaded from Wiley website at https://onlinelibrary.wiley.com/doi/pdf/10.1002/ece3.5096 doi: DOI: 10.1002/ece3.5096


	**References**

	| [1] T.F. Cox and M. A. A. Cox. *Multidimensional Scaling - Second edition*, volume **88** of Monographs on Statistics and Applied Probability. Chapman & al., 2001.
	| [2] I. Borg and P. J. F. Groenen. *Modern Multidimensional Scaling*. Springer Series in Statistics. Springer, second edition, 2005.
	| [3] K. V. Mardia, J.T. Kent, and J. M. Bibby. *Multivariate Analysis. Probability and Mathematical Statistics*. Academic Press, 1979.

	**Diodon notes:** section 10



	*07/11/2017 - revised 21.03.20, 22.10.13*

	"""
	n 	= dis.shape[0]
	if k==-1:
		if meth=="grp":
			print(f'!!! warning ... {k}=-1 should not be used with meth {meth} !!!')
		k = n

	# computes gram matrix from dis
	print("... computation of Gram matrix")
	gram		= dis2gram(dis, loop=loop)
	print("... done!")

	# mds core (svd or evd)
	if meth=="grp":
		print("running SVD GRP")
		U, S, V		= svd_grp(gram,k)			# svd by random projection
		print("SVD GRP done!")
		cond 		= [0 for i in range(k)]					# positive eigenvalues only
		for i in range(k):
			if U[0,i]*V[0,i] > 0:							# for v_i = u_i (and not -u_i)
				cond[i] = 1
		#print(cond)
		which 	= [i for i, item in enumerate(cond) if item==1]
		U		= U[:,which]		# first k axis with equivalent >0 eigenvalue
		S		= S[which]		    # first k singular values with equivalent >0 eigenvalue
		L		= S*S				# the squares of the singular values are returned
	#
	if meth=="svd":
		U, S, VT	= nplin.svd(gram, full_matrices=False)	# with svd() of numpy.linalg
		V			= VT.T									# svd() yields gram = U*S*V
		cond 		= [0 for i in range(n)]
		for i in range(n):
			if U[0,i]*V[0,i] > 0:
				cond[i] = 1
		which 	= [i for i, item in enumerate(cond) if item==1]
		print(len(which), "positive eigenvalues")
		which_k	= which[0:k]
		U		= U[:,which_k]		# first k axis with equivalent > 0 eigenvalue
		S		= S[which_k]		# first k singular values with equivalent >0 eigenvalue
		L		= S*S				# the squares of the singular values are returned
	#
	if meth=="evd":
		U, L	= mat_evd(gram, k)
		cond	= [1]*k
		for i in range(k):
			if L[i]<0:
				cond[i] = 0
		which = [i for i, item in enumerate(cond) if item==1]
		U	= U[:,which]
		L	= L[which]

	# Computation of components
	
	# nb: one can use a right product by diagonal matrix SR because its size is reasonable
	 
	SR		= np.diag(np.sqrt(S))	# singular values (diagonal matrix)
	Y		= np.dot(U, SR)			# array of coordinates

	
	# Saving the components
	
	if Y_file:
		write_ascii(Y, filename=Y_file, delimiter='\t', colnames=False, rownames=False, np_fmt='%.7e', dtype='float32')
		
	if L_file:
		write_ascii(S, filename=L_file, delimiter='\t', colnames=False, rownames=False, np_fmt='%.7e', dtype='float32')
		
	#
	
	L	= S*S
	
	return Y, L

########################################################################
#`
#       Correspondence Analysis
#
########################################################################

def coa(X, k=-1, meth="svd", transpose=False):
	""" Correspondance Analysis of an array

	Parameters
	----------

	X : a 2D numpy array, `n x p`
		array to be analysed

	k : an integer
		number of axis to compute

		default is $k=-1$ (all components are cimputed)

	meth : a string
		method for numerical computing

		one string among `evd`, `svd`, `grp` (see notes)

		default value is $svd$

	transpose : a boolean
		if True, matrix $A$ is transposed (usually because n < p)

		default is `False`


	Returns
	-------

	L : a 1D numpy array
		the eigenvalues

	Y_r : a 2D numpy array,`n x k`
		coordinates of row points

	Y_c : a 2D numpy array, `p x k`
		coordinates of column points


	Notes
	-----


	If :math:`k=-1`, all axis are computed. If :math:`k > 0`, only `k`
	first axis and components are computed.


	*methods for SVD*

	==== ======================================
	svd  SVD with `numpy.linalg.svd()`
	grp  SVD with gaussian random projection
	==== ======================================

	**Example**

	This example should be run from the directory where `diodon_companion` has been cloned for the dataset `example_coa` to be found.

	.. code:: python

		>>> import pydiodon as dio
		>>> A, headers, rownames = dio.load("example_coa")
		>>> L, Y_r, Y_c	= dio.coa(A)


	and, to plot the row and column components

	.. code:: python

		>>> dio.plot_coa(Y_r,Y_c, rownames=rownames, colnames=headers)

	**note on the example**

	The dataset is in `text` format with tabs as delimiters. It contains
	headers and row names. These are default parameters for functions
	`dio.load()`


	**References:**

	Nenadic & Greenacre, *Journal of Statistical Software*, **20(3):** 2-13, 2007

	Lebart, Morineau & Fénelon, 1982, pp. 305-320

	*af, revised 21.02.21, 22.11.05, 23.06.13*
	"""


	### ------------------- transposes X if n < p

	if transpose:
		X	= X.T
		print("The array has been transposed (transpose=True).")

	n			= X.shape[0]
	p			= X.shape[1]

	### -------------------- marginals computation

	N			= float(np.sum(X))
	X			= X/N
	margin_row	= np.sum(X, axis=1)	# row margins
	margin_col	= np.sum(X, axis=0)	# column margin

	### -------------------- tests if no margin is zero (suitable)

	n_i0		= margin_row.tolist().count(0)
	n_j0		= margin_col.tolist().count(0)
	if n_i0 > 0:
		print("\nwarning: some rows have zero sum")
		print("this will lead to an error (division by zero)\n")
	if n_j0 > 0:
		print("\nwarning: some columns have zero sum")
		print("this will lead to an error (division by zero)\n")


	### ---------------------- pretreatment: building SG

	sqrt_margin_row	= np.sqrt(margin_row)		# square root of row margins
	sqrt_margin_col	= np.sqrt(margin_col)		# square root of column margins
	#
	SG	= np.zeros((n,p)).astype(X.dtype)
	for i in range(n):
		for j in range(p):
			SG[i,j]			= (X[i,j]-margin_row[i]*margin_col[j])/(sqrt_margin_row[i]*sqrt_margin_col[j])

	### --------------------- SVD of SG

	if meth=="svd":
		U, S, VT	= np.linalg.svd(SG, full_matrices=False)
		V			= VT.T
		#
		#
		if k > 0:
			U   	= U[:,0:k]
			S		= S[0:k]
			V		= V[:,0:k]
		if k==-1:
			k = p
	#
	if meth=="grp":
		if k==-1:
			exit("in coa() with grp, a value for k must be given explicitly")
		U, S, VT	= svd_grp(SG, k)
		V		= VT.T
	#
	L		= S*S

	### --------------------- post-treatment to get the principal components

	Y_r	= np.zeros((n,k)).astype(X.dtype)
	Y_c	= np.zeros((p,k)).astype(X.dtype)
	for i in range(n):
		for j in range(k):
			Y_r[i,j]	= U[i,j]*S[j]/sqrt_margin_row[i]
	for i in range(p):
		for j in range(k):
			Y_c[i,j]	= V[i,j]*S[j]/sqrt_margin_col[i]
	#

	return	L, Y_r, Y_c



########################################################################
#
#       Principal Component Analysis
#
########################################################################



def pca(A, pretreatment="standard", k=-1, meth="svd"):
	""" Principal Component Analysis

	Parameters
	----------

	A : a 2D numpy array, `n x p`
		the array to be analyzed

	k : integer
		number of axes to be computed

	meth : string
		   method for numerical calculation (see notes)

	pretreatment : string
				   which pretreatment to apply ;

				   accepted values are: ``standard``, ``bicentering``, ``col_centering``, ``row_centering``, ``scaling``

				   see notes for details

	Returns
	-------

	Y : a 2D numpy array, `n x k`
		matrix of principal components

	L : a 1D numpy array
		vector of eigenvalues

	V : a 2D numpy array, `p x k`
		matrix of eigenvectors (new basis)

	Notes
	-----

	The method runs as follows:

	- first  it implements the required pretreatments
	- second: it runs the function `pca_core` on the transformed matrix
	- third: it returns the eigenvalues, the principal axis, the principal components and the correlation matrix if required

	**methods for PCA:** the argument ``meth`` specifies which method is selected for the core of MDS. Default value is ``svd``.
	Let `A` be the the matrix to analyse.

	- if ``meth=svd``, the a SVD of `A` is run
	- if ``meth=grp``, the SVD is run with Gaussian Random Projection
	- if ``meth=evd``, the eigenvalues and eigenvectors of `A` are computed


	**pretreatments:** here are the accepted pretreatments:

	- ``standard``: the matrix is centered and scaled columnwise
	- ``bicentering``: Matrix is centered rwowise and columnwise; it is a useful alternative to CoA known as "double averaging"

	**Examples**

	This is an example of a standard PCA of a random matrix, with :math:`m` rows and
	:math:`n` columns, with elements as realisation of a uniform law between 0 and 1.

	First build the random matrix

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> m = 200 ; n = 50
		>>> A = np.random.random((m,n))

	Second, run the PCA

	.. code:: python

		>>> L, V, Y = dio.pca(A)

	Third, plots some results (eigenvectors and point cloud)

	.. code:: python

		>>> plt.plot(L) ; plt.show()
		>>> plt.scatter(Y[:,0],Y[:,1]) ; plt.show()


	The above program runs centered scaled PCA, with here default option ``pretreatment="standard"``.
	For PCA without centering nor scaling, the command is

	.. code:: python

		>>> L, V, Y, C = dio.pca(A, standard=False)

	For PCA with column centering but without scaling, the command is

	.. code:: python

		>>> L, V, Y, C = dio.pca(A, standard=False, col_centering=True)

	(in such a case, the argument ``standard`` must be set to ``False``. If
	not, the array will be scaled as well). Scaling without centering is quite unusual.


	For bicentering, the command is

	.. code:: python

		>>> L, V, Y, C = dio.pca(A, bicenter=True)

	These are the most usuful options for pretreatment.

	Y, L, V
	Prescribed rank is simply called by (with standard pretreatment)

	.. code:: python

		>>> rank = 10
		>>> L, V, Y = dio.pca(A, k=rank)


	for having the 10 first components and axis only.

	*revised* 21.03.03 - 21.04.20
	"""
	### ------------ displaying choices

	(m,n)	= A.shape
	print("\n-----------------------------------------")
	print("running pca(), version 21.05.05")
	print("Matrix A has", m, "rows and", n, "columns")
	print("rank is",k, "(full rank if k = -1)")
	print("pretreatment is", pretreatment)
	print("method is", meth)
	print("------------------------------------------\n")

	### ------------ preparation

	# transposition if necessary

	if n > m:
		print("more columns than rows => matrix is transposed")
		A = A.T
		transpose = True
	else:
		transpose = False


	# ------------ pretreatments
	#

	accepted = ["standard","bicentering", "scaling", "col_centering", "row_centering"]
	if pretreatment not in accepted:
		print("selected pretreatment is", pretreatment)
		print("it is not recognized. Accepted strings are")
		print(accepted)
		exit("\n => pca() terminated")

	if pretreatment=="standard":
		A, m	= center_col(A)
		A, a 	= scale(A)
	#
	if pretreatment=="bicentering":
		m, r, c, A = bicentering(A)

	#
	if pretreatment=="col_centering":
		A, m	= center_col(A)

	#
	if pretreatment=="row_centering":
		A, m	= center_row(A)

	#
	if pretreatment=="scaled":
		A, a = scale(A)
	#
	# ------------- core PCA after pretreatment
	#
	Y, L, V		= pca_core(A, k=k, meth=meth)
	#
	if transpose:
		V = np.dot(A,V)					# V n x n -> p x n
		Y = np.dot(A.T,V)				# Y is n x n
	#
	return Y, L, V



# ----------------------------------------------------------------------

def quality(Y):
	r"""computes the quality of projection per item and pr axis

	 Parameters
	----------

	Y : a 2D  :math:`n \\times p` numpy array
		a matrix of principal components

	Returns
	-------

	Qual_axis : 2D numpy array
		Qual_axis[i,j]: quality of the projection of item i on axis j
		
	Qual_cum :  2D numpy array
		the rowise cumulated quality per axis up to `j` in column `j`.


	Notes
	-----

	The quality of the projection of the dataset on a subspace spanned by principal axis is a scalar giving a global estimate of the quality.
	However, the quality of projection may differ from item to item: some can be well projected on plane `(1,2)` and some other not. This function
	computes and plots the quality of projection of each item on subspace :math:`E_r` spanned by `r` first axis.

	More precisely, for each row `i` of the matrix of components `Y`

	it computes:     
	 
	1) the norm of each item: :math:`norm[i] = \sum_j Y[i,j]^2`    
	
	2) `Qual\_axis`: the quality of projection per axis: :math:`Qual\_axis[i,j] = Y[i,j]^2 / norm[i]`   
	
	3) `Qual\_cum` : the cumulated quality of projection up to axis `j`: :math:`Qual\_cum[i,j] = \sum_{k \leq j} Qual\_axis[i,k]`



	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> Qual_axis, Qual_cum = dio.quality(Y)


	af, revised 22.10.28, 23.01.18, 25.02.20
	"""
	(n,p)		= Y.shape
	Y2			= Y*Y
	norm_item	= np.sum(Y2, axis=1)
	Qual_axis	= np.zeros((n,p), dtype=float)
	for i in range(n):
		Qual_axis[i,:]	= Y2[i,:]/norm_item[i]
	Qual_cum 	= np.cumsum(Qual_axis, axis=1)
	#
	return Qual_axis, Qual_cum
	
	

########################################################################
#
#       Principal Component Analysis with metrics
#
########################################################################




def pca_met(A, M, N, k=-1, pretreatment="col_centering", meth="svd"):
	r""" PCA of an array with metrics on rows and/or columns - without guaranty

	Parameters
	----------

	A : a  :math:`n \\times p` 2D numpy array
		the array to be analysed


	N : a 2D numpy array
		a Symmetric Definite Positive (SDP) matrix defining an inner product
		on :math:`R^n`

	P : a 2D numpy array
		a SDP matrix defining an inner product
		on :math:`R^p`

	k : an integer
		the number of axis to be computed

		if :math:`k = -1`, all axis are computed

	pretreatment : a string
		the pretreatment to apply

		possible values are: ``col\_centering ``

	meth : a string
		method for numerical calculation of PCA

	Returns
	-------

	Y : a :math:`n \\times k` 2D numpy array
		the princial components

	L : a `k` 1D numpy array
		the eigenvalues

	V : a  :math:`p \\times k`  2D numpy array
		the new basis

	Notes
	-----

	If :math:`A` has :math:`n` rows and `p` columns, we assume that an inner product
	has been defined on :math:`R^n` by a SDP matrix `N` and on :math:`R^p` by a SDP matrix `P`.

	This is how the algorithm works:

	-  first: computes the square roots of `N` and `P`; this is done with a ``SVD``. If
	:math:`N = M^2` and :math:`N = U \Sigma U^t` (:math:`U=V` in the SVD because `N` is symmetric),
	then :math:`M = U \Sigma^{1/2} U^t`; simlarily, if :math:`P=Q^2`, Then :math:`Q = V\Phi^{1/2} V^t`
	if the SVD of `P` is :math:`P = V \Phi V^t`.

	- second: computes :math:`R = MAQ`

	- third: run the ``PCA`` of `R`: :math:`(Z, \Lambda, X) = PCA(R)`

	- fourth: computes :math:`M^{-1}` and :math:`Q^{-1}` as :math:`M^{-1}=U \Sigma^{-1/2} U^t` and
	:math:`Q^{-1}=V \Phi^{-1/2} V^t`

	- fifth: computes :math:`Y = M^{-1}Z` and :math:`V = Q^{-1}X`


	The result is :math:`(Y, V, \Lambda)`


	Let us note that ``numpy`` contains a function, called ``scipy.linalg.sqrtm`` which computes
	the square root of a square `n` `x` `n` matrix, from algorithm published in Deadman, E., Higham, N. J. and Ralha, R.
	(2013) “Blocked Schur Algorithms for Computing the Matrix Square Root, Lecture Notes in Computer Science, 7782. pp. 171-182,
	which is not used here. Indeed, using the SVD permits to compute easily :math:`M=N^{1/2}` and :math:`M^{-1}=N^{-1/2}`, and the
	same for `P`.

	**Warnings**

	- Pretreatment has not been implemented, but centering by column
	- still under work - not frozen for a release

	**Diodon Documentation**

	- see section 6, and algorithm ``pca_met()`` in section 11.

	28/12/2017, revised 22.09.28
	"""

	print("Pretreatment has not been implemented, but centering by column")
	print("!!! still under development - not frozen for a release !!!\n")

	n	= A.shape[0]
	p	= A.shape[1]
	row	= False
	col	= False
	#
	if pretreatment=="col_centering":
		A, m = center_col(A)

	if N.ndim==2:
		U, S, UT	= nplin.svd(N, full_matrices=False)
		Sqr			= np.sqrt(S)
		M			= U @ Sqr @ UT
		Minv		= U @ (1/Sqr) @ UT
	#
	if P.ndim==2:
		W, T, WT	= nplin.svd(P, full_matrices=False)
		Tqr			= np.sqrt(T)
		Q			= W @ Tqr @ WT
		Qinv		= W @ (1/Tqr) @ WT
	#
	if N.ndim==1:
		M		= np.sqrt(N)
		Minv	= 1/M
		MA		= np.zeros((n,p))
		for i in range(n):
			MA[i,:]	= A[i,:]*M[i]
		row		= True
	#
	if P.ndim==1:
		Q		= np.sqrt(P)
		Qinv	= 1/Q
		AQ		= np.zeros((n,p))
		for j in range(p):
			AQ[:,j]	= A[:,j]*Q[j]
		col 	= True

	#
	if row==False:
		if col==False:
			R		= M @ A @ Q
		if col==True:
			R		= M @ AQ
	if row==True:
		if col==False:
			R		= MA @ Q
		if col==True:
			R		= np.zeros((n,p))
			for j in range(p):
				R[:,j]	= MA[:,j]*Q[j]

	### --------- PCA core of R

	Z, L, X = pca_core(R, k)


	### ---------- back to initial space

	if k==-1:
		k = p
	#
	if row==False:
		Y		= Minv @ Z
	if row==True:
		Y	= np.zeros((n,k))
		for i in range(n):
			Y[i,:]	= Z[i,:]*Minv[i]
	#
	if col==False:
		V		= Qinv @ X
	if col==True:
		V		= np.zeros((p,k))
		for i in range(n):
			V[i,:]	= X[i,:]*Qinv[i]

	### --------- result ...

	return Y, L, V

########################################################################
#
#       Principal Component Analysis with instrumental variables
#
########################################################################



def pca_iv(A, B, k=-1, meth="svd", pretreatment="col_centering", transpose=False):
	""" PCA of an array with instrumental variables

	Parameters
	----------

	A : a numpy array, the items/variable to be analyzed

	B : a numpy array, the intrumental variables

	k : an integer

	meth : a string ; method for numerical calculation

	pretreatment : a string, the pretreatment of `A` and `B`
		currently, only `col_centering`is implemented


	Returns
	-------

	Y : a `n` `x` `k` 2D numpy array
		the components

	L : a `k` 1D numpy array
		the eigenvalues

	V : a `p` `x` `k` 2D numpy array
		the new basis

	A_proj : a `n` `x` `p` 2D numpy array
		the projection of `A` on the subspace of :math:`R^n` spanned by the columns of `B`


	Notes
	-----

	`A_pre` is a copy of `A` for tracking preatreatments, and recover the
	matrix analyzed after preatreatments, without impacting `A`


	The algorithm is as follows:

	- Build :math:`P = B(B'B)^{-1}B'` which is the projector in :math:`R^n` on the subspace spanned by the columns of `B`.

	- build `A_proj = PA` which is the projection of `A` on the subspace spanned by the columns of `B`

	- do PCA of `A_proj` : `Y,L,V = PCA(A_proj)`

	**warning**

	This has not been tested; no guarantee on the quality of the result.


	21/02/2018, révised 22.09.28, 22.10.14
	"""

	# ---------- pretreatment
	#
	#
	A_pre	= A.copy()
	B_pre	= B.copy()

	if pretreatment=="col_centering":
		A_pre	= center_col(A_pre)
		B_pre	= center_col(B_pre)

	# ----------- projector on B
	#
	#
	P		= project_on(B_pre)		# P = B(B'B)^{-1}B'
	A_proj	= P @ A_pre				# A_proj = PA


	# ----------- PCA

	Y, L, V = pca(A_proj, k=k, meth=meth)

	return L, V, Y, A_pre, A_proj





# ----------------------------------------------------------------------
#
#		PCA-IV: interpretation
#
# ----------------------------------------------------------------------

def pca_iv_qual_proj(A, A_proj):
	"""
	**Computes the quality of the projection of `A` on the space spanned by the columns of `B`

	Parameters
	----------

	A : a `n` `x` `p`   2D numpy array
		the matrix to be analyzed by PVA_iv

	A_proj : a `n` `x` `p`   2D numpy array
		the projection of `A` on the subspace of :math:`R^n` spanned by the columns of `B`

	Returns
	-------

	rho : a real
			the quality of the projection


	Notes
	-----

	`rho` is the ratio of the square norm of `A_proj` upon the square norm of `A`

	22.09.28

	"""
	nA		= np.linalg.norm(A)
	nAp		= np.linalg.norm(A_proj)
	rho		= (nAp*nAp)/(nA*nA)
	#
	return rho

# ----------------------------------------------------------------------

def pca_iv_qual_proj_axis(A, A_proj, title=None, x11=True, imfile=None, fmt="png"):
	"""
	**Computes and plots the quality of projection of each column of `A` on `Ap`

	Notes
	-----

	Documentation ongoing

	*af, 21/02/2018*
	"""

	nA			= np.linalg.norm(A, axis=0)
	nAp			= np.linalg.norm(A_proj, axis=0)
	rho_axis	= (nAp*nAp)/(nA*nA)
	#
	plt.plot(rho_axis, c="red")
	plt.xlabel("variables of dataset")
	plt.ylabel("quality of projection per variable")
	if title:
		plt.title(title)
	if imfile:
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	if x11:
		plt.show()
	#
	return rho_axis

# ----------------------------------------------------------------------

#def pca_iv_regressors(A,B,P,Q,Y,V, varnames, n_axis=3, x11=True, imfile=None, fmt="png"):
def pca_iv_regressors(A,Q, V, varnames, n_axis=3, x11=True, imfile=None, fmt="png"):
	"""
	**will probably be deprecated

	Notes
	-----

	Documentation ongoing

	22.10.26
	"""
	R = np.dot(A,V)
	R = np.dot(Q,R)
	p = R.shape[0]
	#
	for i in range(p):
		print(i, "->", varnames[i])
	#
	pl_col	= ["red", "green", "blue", "orange", "cyan", "magenta", "purple", "lightgreen"]
	plt.plot([0,p],[0,0],c="black")
	for j in range(n_axis):
		plt.plot(R[:,j], c=pl_col[j])
		plt.text(p-1, R[p-1,j], "axis "+str(1+j))
	plt.xlabel("Instrumental variables")
	plt.ylabel("weight")
	if imfile:
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	if x11:
		plt.show()
	#
	return R

########################################################################
#
# 			pretreatments
#
########################################################################

# ----------------------------------------------------------------------
#
#	Centering
#
# ----------------------------------------------------------------------

def bicentering(A):
	r"""Bicentering a matrix

	Parameters
	----------

	A : a `n x p` numpy array
		the matrix to be bicentered

	Returns
	-------

	m	: a float
		global mean of the matrix

	r : a 1D numpy array (`n` values)
		rowise means

	c	: a 1D numpy arrau (`p` values)
		columnwise means

	R	: a 2D numpy array (`n x p`)
		bicentered matrix

	Notes
	-----

	If `A` is a matrix, builds a matrix `R` of same dimension centered
	on rows and columns.

	:math:`m = (1/np) \sum_{i,j} a_{ij}`

	:math:`r = (r_1,...,r_n)` with
	:math:`r_i = (1/p)\sum_j a_{ij} - m`

	:math:`c = (c_1,...,c_p)` with
	:math:`c_j = (1/n)\sum_i a_{ij} - m`

	such that

	:math:`\sum_ir_i = \sum_jc_j=0`

	and

	for any row `i`, :math:`\sum_j R_{ij}=0` and for any column `j`, :math:`\sum_i R_{ij}=0`

	The matrix `R` can describe interactions in a additive model with two categorical variables, as in

	:math:`a_{ij} = m + r_i + c_j + R_{ij}`

	**example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> m, r, c, R = dio.bicenter(A)

	af, revised 21.02.19, 22.09.21, 22.10.13

	"""
	n	= A.shape[0]
	p	= A.shape[1]
	m 	= np.mean(A)
	r	= np.mean(A, axis=1) - m
	c	= np.mean(A, axis=0) - m
	en	= np.ones(n).astype(A.dtype)
	ep	= np.ones(p).astype(A.dtype)
	R	= A - m - np.outer(en,c) - np.outer(r,ep)
	#
	return m, r, c, R

# ----------------------------------------------------------------------

def centering_operator(m):
	"""Centering operator for a matrix

	will probably be deprecated (22.09.21)

	**argument**

	`m` : an integer ; vector or matrix dimension

	**returns**

	`H`: a numpy array, `m x m`

	**Notes**

	If `A` is a `n x p` matrix

	- :math:`HA` is `A` with centered columns 	(`H` is `n x n`)
	- :math:`AH` is `A` with centered row 		(`H` is `p x p`)

	**example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape = (n,p)
		>>> H_row = dio.centering_operator(p)
		>>> H_col = dio.centering_operator(n)
		>>> Ar = A @ H_row
		>>> Ac = H_col @ A

	revised 21.02.27
	"""
	E	= np.ones((m,m))
	I	= np.identity(m)
	H	= I - E/m
	H	= np.array(H, dtype=float)
	#
	return H

# ----------------------------------------------------------------------

def center_col(A):
	"""centers a matrix columnwise

	Parameters
	----------

	A : a 2D numpy array `n` x `p`
		the matrix to be centered

	Returns
	-------

	Ac	: a 2D numpy array
		`n` x `p`, centered columnwise

	m : 1D numpy array, `p` values
			means per column
			
	
	Notes
	-----

	**example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> Ac, m = dio.center_col(A)



	*af, rp, 21.02.19, 22.10.13*
	"""
	m	= np.mean(A, axis=0)
	Ac	= A - m

	#
	return Ac, m

	# ----------------------------------------------------------------------

def center_row(A):
	"""centers a matrix row-wise

	Parameters
	----------

	A : a 2D numpy array, `n` x `p`
		the matrix to be centered

	Returns
	-------

	Ac : a 2D `n` x `p` numpy array
		A  centered row-wise

	m : a 1D numpy array (`n` values)
		means per row


	Notes
	-----
	
	
	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> Ac, m = dio.center_row(A)



	*af & rp, 21.02.19, 22.10.13*
	"""
	Ac		= A.copy()
	(n,p)	= A.shape
	m		= np.mean(A, axis=1)
	for j in range(p):
		Ac[:,j]	= A[:,j] - m
	#
	return Ac, m

# ----------------------------------------------------------------------

def scale(A):
	r"""Scales a matrix columnwise

	Parameters
	----------

	A : a 2D numpy array, `n` x `p`
		the matrix to be scaled

	Returns
	-------

	As : a 2D numpy array
			matrix `A` with scaled columns

	a : a 1D numpy array, `p` values
			the norm of each column of `A`

	Notes
	-----

	It is recommended to center `A` columnwise before scaling.

	Each coordinates :math:`a_{ij}` of `A` is replaced by
	:math:`a_{ij} / ||a_{.j}||` where :math:`||a_{.j}||` is the norm
	of column `j`:  :math:`||a_{.j}||^2 = \sum_i a_{ij}^2`

	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape =(n,p)
		>>> Ac, m = dio.center_col(A)
		>>> As, s = dio.scale(Ac)

	af, 21.02.19, 22.10.13
	"""
	p	= A.shape[1]
	a	= nplin.norm(A, axis=0)
	As	= A.copy()
	for j in range(p):
		As[:,j] = A[:,j]/a[j]
	#
	return As, a

# ----------------------------------------------------------------------

def get_correlation_matrix(A):
	""" Gets the correlation matrix

	Parameters
	----------

	A : a 2D `n x p` array
		the dataset


	Returns
	-------

	C : a `p x p` coorrelation matrix


	Notes
	-----

	The computation of the correlation matrix, or variance-covariance matrix, is relevant
	for standard pretreatment only. Then, `S` is centered-scaled matrix from `A`, then :math:`C = S^t S`.

	To compte `C`, the function computes `S` by centering columnwise and scaling the input matrix `A`.

	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> import numpy as np
		>>> # building a toy matrix
		>>> m = 10; n = 5
		>>> A = np.random.randn(m,n)
		>>> # computes the correlation matrix
		>>> C = dio.get_correlation_matrix(A)
		>>> print(C)

	af, 23.01.19
	"""

	A, m	= center_col(A)
	A, a 	= scale(A)
	C		= A.T @ A
	#
	return C

# ----------------------------------------------------------------------
#
#	from distance matrix to gram matrix
#
# ----------------------------------------------------------------------

def dis2gram(dis, loop=True):
	r"""Computes a Gram matrix knowing a distance matrix


	Parameters
	----------


	dis: a 2D numpy array, size `n x  n`, of floats
			is a distance or dissimilarity matrix to be analyzed

	Returns
	-------

	gram : a 2D numpy array, size `n` x  `n`,  of floats
			the associated Gram matrix

	Notes
	-----

	if
	:math:`d_{i.}^2 = (1/n) \sum_j d_{ij}^2` and :math:`d_{..}^2 = (1/n^2) \sum_{i,j} d_{ij}^2`

	then

	:math:`gram[i,j] = -(1/2) (d_{ij}^2 - d_{i.}^2 - d_{.j}^2 + d_{..}^2)`

	*af, 07/11/2017, 22.10.13*
	"""
	#
	n		= dis.shape[0]						# number of items
	e_n		= np.ones(n).astype(dis.dtype)		# (1, ..., 1) n times
	#
	if loop==False:
		print("Computing Gram matrix without loops ...")
		t 		= time.time()
		dis		= dis*dis                			# dis*dis componenwise
		di_  	= dis.mean(axis=1)                 # mean per row
		d_j  	= dis.mean(axis=0)                 # mean per column
		d__  	= dis.mean()                       # global mean
		print("distance matrix squared")
		#
		s_row  	= np.outer(di_, e_n)                # one row with row mean
		gram	= dis - s_row
		del s_row
		gc.collect()
		s_col  	= np.outer(e_n, d_j)                # one column with column mean
		gram	= gram - s_col
		del s_col
		gc.collect()
		gram	= (-.5)*(gram + d__)
		#s_3  	= d__ * np.ones(shape=(n, n)).astype(dis.dtype)	# same dimension as dis with '1'
		#gram   	= (-.5)*(dis2 - s_1 - s_2 + s_3)    # covariance matrix
		t_inner = time.time()
		print("...took:", t_inner - t_inner, "sec.")
		#
	else:		# loop = True
		print("Computing Gram matrix with loops ...")
		t 		= time.time()
		print("squaring the matrix in place ...")
		"""
		for i in range(n):
			if i % 100 == 0:
				print('row ',i," / ",n, end='\r')		
			for j in range(i,n):
				x			= dis[i,j]
				y			= x*x
				dis[i,j] 	= y
				dis[j,i]	= y
		"""
		dis			= dis*dis
		t_square 	= time.time()
		print("... took:", t_square - t, "sec.")
		print("computing margins ...")
		di_  	= dis.mean(axis=1)                 # mean per row
		d_j  	= dis.mean(axis=0)                 # mean per column
		d__  	= dis.mean()                       # global mean
		t_marg	= time.time()
		print("... took:", t_marg - t_square, "sec.")
		print("computing inner products ...")
		print("margins on rows")
		for i in range(n):
			if i % 100 == 0:
				print('row ',i," / ",n, end='\r')
			dis[i,:]	= dis[i,:] - di_[i]
		print("margins on columns")
		for j in range(n):
			if j % 100 == 0:
				print('col ',j," / ",n, end='\r')
			dis[:,j]	= dis[:,j] - d_j[j]
		dis	= dis + d__
		"""	
			for j in range(i,n):
				y			= dis[i,j] - di_[i] - d_j[j] + d__
				dis[i,j]	= y
				dis[j,i]	= y
		"""
		gram = (-.5)*dis
		t_inner = time.time()
		print("...took:", t_inner - t_marg, "sec.")
		#
	return gram


# ----------------------------------------------------------------------

def project_on(A):
	r"""Builds the projection operator on space spanned by the columns of an array


	Parameters
	----------

	A : a :math:`n \\times p` 2D numpy array
		the projector is on the space in :math:`\mathbf{R}^n` spanned by the columns of `A`

	Returns
	-------
	P : a 2D numpy array, :math:`n \\times n`
		the projector

	Notes
	-----

	This function uses the QR decomposition of `A`, which avoids to compute
	:math:`(A'A)^{-1}` which is costly (one product, one inverse). It proceeds as

	- A = QR
	- P = QQ'

	**Example**

	.. code:: python

		import numpy as np
		import pydiodon as dio
		n = 10 ; p = 5
		A = np.random.randn(n,p)
		P = project_on(A)


	*af, 22/02/2018, 22.10.13, 22.10.28*
	"""
	Q, R	= nplin.qr(A)
	P		= Q @ Q.T
	#
	return P, Q




########################################################################
#
#			io_utils
#
########################################################################


def loadfile(filename, fmt=None, delimiter="\t", rownames=False, colnames=False, datasetname='values', dtype='float32'):
  """A generic function for loading datasets as numpy arrays


  Parameters
  ----------

  filename : string
             contains the data set to be loaded (compulsory)


  fmt : string
        explicit format of the file (optional);
        if it is not given the format will be guessed from the suffix (see notes)


  delimiter : character
              the delimiter between values in a row


  colnames : boolean or string; whether column names
             - for an ascii file, it is boolean, as True if column names are as first row in the file, and False otherwise;

             - for an hdf5 file, gives the name of the dataset with the column names

             - optional, default value is `False`


  rownames : boolean or string; whether row names

             - for an ascii file, it is boolean, as True if row names are as first column in the file, and False otherwise

             - for an hdf5 file, gives the name of the dataset with the row names

             - optional, default value is None.


  datasetname : string
                - for hdf5 files : hdf5 dataset for values

                - optional, default value is "value"

  Returns
  -------

  A : a numpy array
      the values of the data set

  rn : list of strings
       row names (optional)

  cn : list of strings
       column names (optional)

  Notes
  -----

  - Recognized formats are: ``ascii``, ``hdf5`` and ``compressed ascii``.

  - Delimiters in ascii format can be blanks, comma, semi-columns, tabulations

  - Ascii data sets with ``tab`` delimiters are expected to be with suffix ``.txt`` or ``.tsv``.

  - Ascii data sets with other delimiters are expected to be with siffix ``.csv``.

  When the filename is read, the function splits the name on the last dot, and
  interprets the string after as the suffix. Then, there is a call

  - to ``load_ascii()`` if the suffix is ``.txt``, ``tsv``, ``.gz`` or ``.bz2``,

  - to ``load_hdf5`` if the suffix is ``h5`` or ``hdf5``,

  - and unzips the file before a call to ``load_ascii()`` if the sufix is ``zip``.

  Examples
  --------

  Here is a call for loading an ``ascii`` file with extension ``.txt`` hence with tab as delimiters, and with rownames and colnames.
  In such a case, the call must specifiy that there are colnames and rownames to be read:

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_withnames.txt"
    >>> A, colnames, rownames = dio.loadfile(filename, colnames=True, rownames=True)
    >>> print(A)
    >>> print(colnames)
    >>> print(rownames)

  If it is not specified (default values), an array without colnames and rownames will be loaded, as in

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_nonames.txt"
    >>> A = dio.loadfile(filename)


  Here is a call of a ``.csv`` file where delimiters have to be specified:

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_nonames.csv"
    >>> A = dio.loadfile(filename, delimiter = ";")

  Here is how to load a ``zip`` file from a ``.txt`` file:

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_nonames.txt.zip"
    >>> A = dio.loadfile(filename)
    >>> print(A)

  and from a ``.csv`` file with semi-column as delimiter

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_nonames.csv.zip"
    >>> A = dio.loadfile(filename, delimiter=";")


  Here is an example for loading a ``hdf5`` file with `values`, `colnames`
  and `rownames` as datasets:

  .. code:: python

    >>> import pydiodon as dio
    >>> filename = "pca_template_withnames.h5"
    >>> A, colnames, rownames = dio.loadfile(filename, colnames='colnames', rownames='rownames')


  version 21.03.23

  """
  # looks whether the dataset is pydiodon dataset list
  # if yes, reads it
  # if not, looks into current directory
  #
  if not os.path.exists(filename):
    filen = f'{os.environ["HOME"]}/.pydiodon/datasets/{filename}'
    if not os.path.exists(filen):
      exit(f"Can't find either {filename} or {filen}")
    filename = filen
  #
  # splits file name in two parts: filanename = <basename>.<suffix>
  # the suffix   is the string after  the last "."
  # the basename is the string before the last "."
  #
  basename, suffix = os.path.splitext(filename)
  #
  # preparation
  #
  res = []
  suffix_list  = ('.txt','.csv', '.tsv', '.dissw','.gz', '.bz2')
  h5_list      = ('.h5', '.hdf5')
  #
  # recognizes and loads ascii files
  #
  if (fmt=="ascii") or  (suffix in suffix_list):
    res = load_ascii(filename, delimiter=delimiter, colnames=colnames, rownames=rownames, dtype=dtype)
  #
  # recognizes and loads zip files
  #
  elif suffix == '.zip':
    #unzip filename, do not overwrite if file already exists
    os.system(f'unzip -n {filename} > /dev/null')
    filename = basename
    res = load_ascii(filename, delimiter=delimiter, colnames=colnames, rownames=rownames, dtype=dtype)
  #
  # recognizes and loads hdf5 files
  #
  elif (fmt == 'hdf5'  ) or (suffix in h5_list):
    res = load_hdf5(filename, datasetname=datasetname, colnames=colnames, rownames=rownames)
  #
  # of not ...
  #
  else:
    exit("Unknown format for " + filename)
  #
  return res

# ----------------------------------------------------------------------

def load_ascii(filename, delimiter="\t", colnames=True, rownames=True, dtype=float):
  """Loads an ascii file as a numpy array

  Parameters
  ----------

  filename : string
             the name of the file to load

  delimiter : character
              delimiters between values in a row

  colnames : boolean
             True if there are column names in the first row of the file
             False otherwise

  rownames : boolean
             True if there are rownames in the first column of the file
             False otherwise

  dtype : string
          as dtype in numpy.loadtxt (type of values in the numpy array)



  Returns
  -------

  A : a 2D numpy array
        the values in the file

  rn : list of strings
         row names (if ``rownames==True``)

  cn : list of strings
         column names (if ``colnames==True``)

  """
  if not colnames and not rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=dtype)
    return A

  if colnames and rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=object)
    cn = A[0,1:].astype(str).tolist()
    rn = A[1:,0].astype(str).tolist()
    A = A[1:,1:]
    A = np.array(A, dtype=dtype)
    return A, rn, cn

  if colnames and not rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=object)
    cn = A[0,:].astype(str).tolist()
    A  = A[1:,:]
    A  = np.array(A, dtype=dtype)
    return A, cn

  if not colnames and rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=object)
    rn =  A[:,0].astype(str).tolist()
    A = A[:,1:]
    A = np.array(A, dtype=dtype)
    return A, rn

# ----------------------------------------------------------------------

def load_hdf5(filename, datasetname, colnames, rownames):
  """loads a hdf5 file as a numpy array

  Parameters
  ----------

  filename : string
             the name of the file

  datasetname : string
                the name of the hdf5 dataset with data values

  Returns
  -------
     see loadfile
  """
  hf = h5py.File(filename,'r')
  A = hf[datasetname][:]

  if not colnames and not rownames:
    return A

  if colnames and rownames:
    pl_colnames = [ i.decode('utf_8') for i in hf['colnames'] ]
    pl_rownames = [ i.decode('utf_8') for i in hf['rownames'] ]
    return A, pl_rownames, pl_colnames

  if colnames and not rownames:
    pl_colnames = [ i.decode('utf_8') for i in hf['colnames'] ]
    return A, pl_colnames

  if not colnames and rownames:
    pl_rownames = [ i.decode('utf_8') for i in hf['rownames'] ]
    return A, pl_rownames

# ----------------------------------------------------------------------

def load_dataset(dataset):
	"""Loads datasets provided as examples after having cloned companion git of (py)diodon.

	Parameters
	----------

	dataset : a string
			the dataset to be load dataset, ed

	datadir : a string
			the path to find the dataset

	Notes
	-----

	The datasets are called in this function by a nickname, not by the filename. Nicknames are

	- `diatoms_sweden` for the PCA on a site $\\times$ environment array
	- `example_CoA` for an example for Correspondance Analysis
	- `Guiana_trees` for an example for MDS (molecular distances between markers on trees in French Guiana)

	It is recommended to use this function after having cloned in ones machine the project `diodon_companion` from gitlab (see the readme at section `install`).

	Then, go into directory `$diodon_companion`, where the dataset are, start a pydiodon session, and it should work.

	If the user wishes to use this function from another directory, the path (absoute or relative) to the directory where the datasets are is given as variable
	`datadir`.


	af, 23.01.13
	"""
	accepted_files = ('ade4_doubs_env.txt','ade4_doubs_fish.txt','diatoms_sweden.txt',
			'CoA_LMF82.txt','laurales.sw.dis','guiana_trees.sw.dis',)

	if dataset not in accepted_files:
		print(f'\n\nPlease choose among {accepted_files}\n\n')
		return
	
	datadir = os.path.dirname(__file__)

	# install with pip install -e .
	if datadir.endswith('/pydiodon/src'):
		datadir = f'{datadir[:-4]}/data4tests/'

	# install with pip3 install git+https://gitlab.inria.fr/diodon/pydiodon (or pip install .)
	elif datadir.endswith('site-packages'):
		datadir = f'{os.environ["HOME"]}/.local/share/pydiodon/'
		
	else:
		print(f"\n\nCant'find installation directory for dataset {datadir=} {dataset=}\n")
	#
	infile = datadir + dataset
	#
	A, rownames, colnames = load_ascii(infile, delimiter="\t", rownames=True, colnames=True)
	print("dataset", dataset, "loaded, with", A.shape[0], "rows and", A.shape[1], "columns.")
	#
	return A, rownames, colnames

# ----------------------------------------------------------------------
def copy_dataset(dataset):
	"""
	"""
	datadir = os.path.dirname(__file__)

	# install with pip install -e .
	if datadir.endswith('/pydiodon/src'):
		datadir = f'{datadir[:-4]}/datasets/'

	# install with pip3 install git+https://gitlab.inria.fr/diodon/pydiodon or pip install .
	elif datadir.endswith('site-packages'):
		datadir = f'{os.environ["HOME"]}/.local/share/pydiodon/'
		
	else:
		print(f"\n\nCant'find installation directory for dataset {dataset}\n")
	#
	if dataset=="diatoms_sweden":
		datafile	=  "diatoms_sweden.txt"
	#
	elif dataset == "example_coa":
		datafile	=  "CoA_LMF82.tsv"
	#
	elif dataset == "guiana_trees":
		datafile	=  "guiana_trees.sw.dis"
	#
	else:
		print(f"\n\nCant'find dataset: {dataset}\n\tplease choose between: diatoms_sweden, example_coa and guiana_trees\n")

	shutil.copy2(f'{datadir}{datafile}', '.')

# ======================================================================

def writefile(A, filename, fmt=None, delimiter="\t", colnames=False, rownames=False, datasetname='values', np_fmt='%.18e', dtype='float32'):
	"""A generic function for saving a numpy array as a file

	Parameters
	----------

	A : a numpy array
	  the array to be saved as a file

	filename : string
			 the name of the file for saving the array (compulsory)

	fmt : string
		explicit format of the file (compulsory)
		one item among ``ascii``, ``hdf5``, ``zip`` ; see notes


	delimiter : character
		the delimiter between values in a row

	colnames : boolean or string
		 column names

		 for an ascii file, it is boolean, with True if column names are as first row in the file, and False otherwise

		 for an hdf5 file, gives the name of the dataset with the column names

		 | optional
		 | default value is None.

	rownames : boolean or string
		 row names

		 for an ascii file, it is boolean, as True is row names are as first column in the file, and False otherwise

		 for an hdf5 file, gives the name of the dataset with the row names

		 | optional
		 | default value is None.

	datasetname : string
			| for writing files in hdf5 format only : hdf5 dataset for values
			| optional
			| default value is "value"

	fmt : string
		   is exactly the parameter ``fmt`` of ``numpy.savetxt()`` for print format in ascii files
		   to be done

	dtype : to be done

	Returns
	-------

	writes a file

	Notes
	-----

	It writes the array in a file and returns no value. Parameters and choices are mirrored
	from function ``loadfile()`` as it is the reverse operation.

	Possible formats are: ``ascii``, ``hdf5`` and ``compressed ascii``.
	Delimiters in ascii format can be blanks, comma, semi-columns, tabulations.
	Ascii data sets with ``tab`` delimiters are expected to be with suffix ``.txt``.
	Ascii data sets with other delimiters are expected to be with siffix ``.csv``.


	*jmf & af, 21.04.22, 22.10.28*

	"""
	print("-> pydiodon:writefile()")
	print("writing", filename)
	basename, suffix = os.path.splitext(filename)
	suffix_list  = ('.txt','.csv', '.gz', '.bz2')
	h5_list      = ('.h5', '.hdf5')
	#
	# recognizes and writes ascii file
	#
	if (fmt=="ascii") or (suffix in suffix_list):
		write_ascii(A, filename, delimiter=delimiter, colnames=colnames, rownames=rownames, np_fmt=np_fmt, dtype=dtype)
	#
	# recognizes and writes zip file
	#
	elif suffix == '.zip':
		write_ascii(A, basename,  delimiter=delimiter, colnames=colnames, rownames=rownames, np_fmt=np_fmt, dtype=dtype)
		cmd = f'zip {filename} {basename} && rm -f {basename}'
		os.system(cmd)
	#
	# recognizes and writes hdf5 file
	#
	elif fmt == 'hdf5' or (suffix in h5_list):
		write_hdf5(A, filename, datasetname=datasetname, colnames=colnames, rownames=rownames)
	#
	# or not ...
	#
	else:
		exit("Unknown format for " + filename)

# ----------------------------------------------------------------------

def write_ascii(A, filename, delimiter='\t', colnames=False, rownames=False, np_fmt='%.18e', dtype='float32'):
	"""Write an ascii file

	Notes
	-----

	Not expected to be used by the user (see writefile())
	22.10.28
	"""

	if  not colnames and not rownames:
		np.savetxt(filename, A, delimiter=delimiter, fmt=np_fmt)
		return
	elif colnames and not rownames:
		header = '\t' + '\t'.join('\t',colnames)
		np.savetxt(filename, A, delimiter=delimiter, header=header, fmt=np_fmt,comments='')
		return
	elif rownames and not colnames:
		np_fmt = ['%s'] + ['%d'] * A.shape[1]
		rownames = np.array(rownames, dtype=object)[:, np.newaxis]
		np.savetxt(filename,np.hstack((rownames, A)), delimiter=delimiter,fmt=np_fmt)
	elif rownames and colnames:
		np_fmt = ['%s'] + ['%d'] * A.shape[1]
		rownames = np.array(rownames, dtype=object)[:, np.newaxis]
		header = '\t' + '\t'.join(colnames)
		np.savetxt(filename,np.hstack((rownames, A)), delimiter=delimiter, header=header,fmt=np_fmt, comments='')
# ----------------------------------------------------------------------

def write_hdf5(A, filename, colnames=False, rownames=False, datasetname='values', dtype='float32'):
	"""Write a hdf5 file

	Notes
	-----

	No documentation because is not expected to be used by the user (see writefile())
	22.10.28

	"""
	with h5py.File(filename, 'w') as h5:
		h5.create_dataset(name=datasetname, data=A, dtype=dtype,compression="gzip", compression_opts=9)
		if colnames:
			colnames = np.array(colnames,dtype="<S255")
			h5.create_dataset(name='colnames', data=colnames, dtype='<S255', compression="gzip",compression_opts=9)
		if rownames:
			rownames = np.array(rownames,dtype="<S255")
			h5.create_dataset(name='rownames', data=rownames, dtype='<S255', compression="gzip",compression_opts=9)




########################################################################
#
#			plotting
#
########################################################################

# Here are the functions for plotting

# plot-eig()							plotting eigenvalues
# plot_components_scatter()				scatter pplot of components
# plot_components_splines()				parallel coordinates
# plot_cumulated_quality_per_item()		xx
# plot_var()							plotting principal axis
# plot_var_heatmap()					plotting heatmap of V

@spawn(skip=skip)
def plot_eig(L, k=-1, frac=True, cum=False, Log=False, dot_size=-1, col="red", title=False, pr=False, x11=True, plotfile=None, fmt="png"):
	r"""Plots the singular or eigenvalues

	Parameters
	----------

	L	: 1D numpy array
		the eigenvalues of `A'A`

	k : integer
		| the number of eigenvalues to plot or print
		| default value is -1, which means all positive eigenvalues

	frac : boolean
		if True, the fraction of the norm of `A'A` is displayed per eigenvalue

	cum : boolean
		if true, the cumulated eigenvalues are displayed
		can be combined with `frac=True`

	Log : Boolean
		if True, the Log of the genvalues is displayed

	dot_size : integer
		if > 0, a dot is displayed per eigenvalue

	nb_val : integer
		number of eigen,values to display;

		if `nb_val=-1`, all eigenvalues are displayed

	col : string
		color for the plot

	title : string
		title on top of the plot;

		if `None`, no title is displayed

	pr : boolean
		| prints on the screen the eigenvalues if True
		| inherits the choices for k, frac and cum.

	x11 : Boolean
		if True, the plot is displayed on screen

	plotfile : string
		if not `None`, the save is save in a file named `plotfile`

	fmt : string
		the format of the plot;

		accepted formats are `png`, `eps`, `pdf`


	Notes
	-----

	- The eigenvalues :math:`L_i` are such that :math:`\sum_i L_i = ||A'A||^2`. Then, the quality of representation in axis `i` is :math:`L_i/\sum_j L_j`.
	  This is displayed by setting `frac=True`.
	- the cumulated eigenvalues are simply given by :math:`\psi_i = \sum_{j \leq i}L_j`



	af, 25/10/2017 - revised 19.09.18, 22.10.14
	"""
	#print("-> pydiodon:plot_eig()")
	# print(L/np.sum(L))
	#
	y	= L
	if Log:
		frac 	= False
		cum		= False
		y		= np.log(1+L)
	#
	sumL	= np.sum(L)
	frcL	= L/sumL
	#
	if frac==True:
		y	= frcL
	#
	if cum==True:
		y	= np.cumsum(frcL)
	#
	M 	= np.max(y)
	buf	= M/50
	#
	if k>0:
		y	= y[0:k]
	#
	if pr:
		if frac:
			if cum:
				print("Cumulated fractions of the inertia:")
			else:
				print("Fraction of the inertia per axis:")
		else:
			print("Eigenvalues:")
		pl_str		= [str(np.round(1000*val)/1000) for val in y]
		pl_print	= (" ; ").join(pl_str)
		print(pl_print)
	#
	plt.plot(y, c=col)
	plt.plot([-.5, len(y)],[0,0], c="black")
	plt.plot([0, 0],[-buf,M+buf], c="black")
	#
	if dot_size>0:
		plt.scatter(range(len(y)), y, c=col, s=dot_size)
	if title:
		plt.title(title)
	plt.xlabel("rank")
	if cum==True:
		plt.ylabel("value (cumulated)")
	else:
		plt.ylabel("value")
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	if x11:
		plt.show()
	else:
		plt.close()
		
# ----------------------------------------------------------------------

@spawn(skip=skip)
def hist_eig(L, bins=20, histtype='bar', col="blue"):
	"""
	"""
	plt.hist(L, bins=bins, density=True, histtype=histtype, color=col)
	plt.show()


# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_components_scatter(Y, axis_1=1, axis_2=2, dot_size=20, color="red", cmap=None, names=[], title=None, x11=True, plotfile=None, fmt="png"):
	"""Scatter plot of the result of a Principal Component Analysis

	Parameters
	----------

	Y : a :math:`n \\times k` 2D numpy array,
		the matrix of columnwise principal components

	axis_1 : an integer, the first axis
		axis are labelled from 1 to `k`

	axis_2 : an integer, the second axis
		second axis is labelled from `axis_1 + 1` to `k`

	dot_size : an integer
		the size of dots in the plot, one dot per item

	color : a string
		color of doats in the plot

	names : a list of `n` strings
		labels of dots in the plot

	title : string
		title of the plot

	x11 : boolean
		the plot is displayed on the scvreen if `x11=True`

	plotdir : string
		relative directory where to save the plot

	plotfile : string
		name of the file to save the plot

		the plot is not saved if `plotfile=None`

	fmt : string
		format of the file to save the plot.

		accepted values are `png`, `eps`, `pdf`.

	Returns
	-------

	a scatter plot

	Notes
	-----

	None

	*af, 21/02/2018, revised 22.10.14, 23.01.13*
	"""

	# row and column points
	i 	= axis_1 -1
	j	= axis_2 -1
	#
	F1	= Y[:,i]
	F2	= Y[:,j]
	plt.scatter(F1,F2, c=color, s=dot_size)
	#
	#if len(names)>0:
	if len(names)>0:
		for i, item in enumerate(names):
			plt.text(F1[i], F2[i], item)
	#
	if title:
		plt.title(title)
	#
	plt.xlabel("Axis " + str(axis_1))
	plt.ylabel("Axis " + str(axis_2))
	if cmap:
		plt.colorbar()
	#
	if plotfile:
		imfile = plotfile + "_"+ str(axis_1) + "_" + str(axis_2)
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	#
	if x11:
		plt.show()


# ------------------------------------------------------------------
@spawn(skip=skip)
def plot_components_splines(Y, n_axis=-1, v_col="red", title=None, x11=True, plotfile=None, fmt="png"):
	r"""Plots principal components as lines smoothed with cublic splines, one per item

	Parameters
	----------

	Y : a 2D numpy array of principal components

	n_axis : an integer, number of axis to include in the plot
		default value is n_axis=-1 (all axis are considered)

	v_col	: a string or a list; colors for splines
		default value is "red"
		if a list : as list with one color per item

	title : a string ; title for the plot
		default value is None, no title

	x11 : boolean ; whether to display the plot on the screen or not
		default value is True, with display

	imfile : a string ; name of a file for saving the plot
		default value is None, no saving

	fmt : a string ; format for saving the plot
		possible values are: "png", "eps", "pdf"


	Notes
	-----

	This displays parallel coordinates with one line per row of `Y`.
	up to `n_axis` components. See https://en.wikipedia.org/wiki/Parallel_coordinates
	for a presentation of parallel coordinates.

	Let `Y` be the array of principal components. Let `n\_axis=k`. An item `i` is
	row `i` of `Y`, restricted to `k` first columns: `y_i = Y[i, 1:k]`.
	Then, there is one curve per item, passing through the `k` points `(1,Y[i,1])`,
	`(2, Y[i,2])`, ..., `(k,Y[i,k])`. Here, these lines are not piecewise linear,
	but smoothed by cubic splines.


	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> dio.plot_components_splines(Y)


	af, 23.01.18
	"""
	print("[pydiodon]:[plot_components_splines()]")
	# if one color only, translate it as a uniform color vector
	n_item		= Y.shape[0]
	n_coord		= Y.shape[1]
	if type(v_col)==str:
		v_col 	= [v_col]*n_item
	#
	if n_axis==-1:
		n_axis	= n_coord
	else:
		n_axis	= min(n_axis, n_coord)
	#
	x   = np.arange(n_axis)
	xs  = np.linspace(0, n_axis-1, 1000)
	#
	for i in range(n_item):
		y   = Y[i,list(range(n_axis))]
		spl = sin.UnivariateSpline(x, y, s=0)
		ys  =  spl(xs)
		plt.plot(xs, ys, color=v_col[i])
	#
	if title:
		plt.title(title)
	#
	plt.xlabel("Axis")
	plt.ylabel("Components")
	#
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	#
	if x11:
		plt.show()


# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_quality(Qual_axis, Qual_cum, r=2, cum=False, sort=False, col="blue", title=None, x11=True, plotfile=None, fmt="png"):
	r"""plots the quality per item

	 Parameters
	----------

	Y : a 2D  :math:`n \\times p` numpy array
		a matrix of principal components

	r : an integer, the axis for plotting cumulated quality
		default value is 2 (for permitting cumulated quality)

	sort : boolean
		| whether to sort or not the items according to their quality of projection
		| default value is False
		
	cum : a boolean
		| whether to use cumulated quality from axis 1 to `r` 
		
	col : a string
		| the color to use for plotting the quality
		| default value is `blue`

	title : string
		title of the plot

	x11 : boolean
		the plot is displayed on the scvreen if `x11=True`

	plotfile : string
		name of the file to save the plot

		the plot is not saved if `plotfile=None`

	fmt : string
		format of the file to save the plot.

		accepted values are `png`, `eps`, `pdf`.


	Returns
	-------

	a plot


	Notes
	-----

	The quality of the projection of the dataset on a subspace spanned by principal axis is a scalar giving a global estimate of the quality.
	However, the quality of projection may differ from item to item: some can be well projected on plane `(1,2)` and some other not. This function
	computes and plots the quality of projection of each item on subspace :math:`E_r` spanned by `r` first axis.

	More precisely, for each row `i` of the matrix of components `Y`

	* it computes `Qual` with :math:`Qual[i,r] = \sum_{j \leq r} Y[i,j]^2 / \sum_{k \leq p} Y[i,k]^2` for :math:`1 \leq i \leq n` and :math:`1 \leq r \leq p`
	* once an axis `r` has been selected, it draws the plot of :math:`(i, Q(i,r))` for :math:`1 \leq i \leq n` with `i` on `x` axis.

	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> Qual_axis, Qual_cum = dio.quality(Y)
		>>> dio.plot_quality(Y)

	or, for sorting the items in decreasing quality, and with cumulated quality

	.. code:: python

		>>> dio.plot_quality(Y, cum=True, sort=True)

	af, revised 22.10.28, 23.01.18, 25.02.21
	"""

	j	= r-1
	if cum:
		y	= Qual_cum[:,j].tolist()
	else:
		y	= Qual_axis[:,j].tolist()
	#
	if sort:
		y	= sorted(y)
		y	= y[::-1]
	plt.plot(y, c=col)
	plt.xlabel("item")
	if cum:
		plt.ylabel("quality of projection up to axis " + str(r))
	else:
		plt.ylabel("quality of projection on axis " + str(r))
	if title:
		plt.title(title)
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	if x11:
		plt.show()
	#

# ----------------------------------------------------------------------
#@spawn launch plot_components_scatter, not plt.show ==> NO SPAWN
def plot_components_quality(Y, Qual_cum, axis_1=1, axis_2=2, r=2, cmap="ocean", diam=50, title=None, x11=True, plotfile=None, fmt="png"):
	"""Scatter plot of the principal components with each dot colored according to the cumulated quality of the item for a given axis

	Parameters
	----------

	Y : a 2D numpy array
		matrix of principal components

	Qual : a 2D numpy array
		| matrix of cumulated quality per item over all principal axis
		| computed by diodon.plot_cumulated_quality_per_item(Y, ...)

	axis_1 : an integer
		| x axis of the plot
		| default value is 1

	axis_2 : an integer
		| y axis of the plot
		| default value is 2

	r : an integer
		| the number of first axis over which to compute the cumulated quality per item
		| default value is r=2

	cmap : a string
		| the colormap selected for visualizing the quality by a color
		| default value is "ocean"

	diam : an integer
		| dot size of each item
		| default value is 50

	title : a string
		| title for the plot
		| default value is None (no title)

	x11 : a boolean
		| whether to display the plot on the screen
		| default value is True

	plotfile : a string
		| name of the file where to save the plot
		| default value is None (plot not saved)

	fmt : a string
		| format for the file where to save the plot
		| possible values are `png`, `eps`, `pdf`
		| default value is `png`

	Notes
	-----


	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> Qual = dio.plot_cumulated_quality_per_item(Y)
		>>> dio.plot_components_quality(Y, Qual)

	af, revised 23.01.18
	"""
	qual 	= Qual_cum[:,r]
	d_size	= diam*qual
	plot_components_scatter(Y, axis_1=axis_1, axis_2=axis_2, dot_size=d_size, color=qual, cmap=cmap, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_var(V, varnames=None, axis_1 = 1, axis_2 = 2, title=None, x11=True, plotfile=None, fmt="png"):
	"""Plots the correlations between the variables

	Parameters
	----------

	V : a :math:`p \\times p` 2D numpy array
		column `k` of `V` is the `k-`th principal axis

	varnames : a list of strings
		| the names of the variables (the columns of `A` on which the PCA has been done)
		| default value is None (no names are displayed)

	axis_1 : an integer
		| the first principal axis to be displayed
		| default value is 1

	axis_2 : an integer
		| the second principal axis to be displayed
		| default value is 2

	title : string
		| title of the plot
		| default value is None (no title)

	x11 : boolean
		| the plot is displayed on the screen if `x11=True`
		| default value is True

	plotfile : string
		| name of the file to save the plot
		| defaulkt value is None (plot not saved)


	fmt : string
		| format of the file to save the plot.
		| accepted values are `png`, `eps`, `pdf`.

	Notes
	-----

	returns a plot


	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> dio.plot_var(V, varnames=cn)

	af, 22.10.28
	"""
	#
	p	= V.shape[0]
	i	= axis_1 - 1
	j	= axis_2 - 1
	#
	fig, ax	= plt.subplots()
	circle	= plt.Circle((0, 0), radius=1, color='r', fill=False)
	ax.add_patch(circle)
	#
	for k in range(p):
		xy = (V[k,i], V[k,j])
		plt.plot([0, V[k,i]],[0,V[k,j]], c="blue")
		if varnames:
			plt.text(V[k,i],V[k,j], varnames[k])
	#
	plt.xlabel("axis " + str(i+1))
	plt.ylabel("axis " + str(j+1))
	#
	if plotfile:
		imfile = plotfile + "_"+str(1+i) + "_" + str(1+j)
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	if x11:
		plt.show()

# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_var_heatmap(V, varnames=None, cmap="ocean", title=None, x11=True, plotfile=None, fmt="png"):
	"""Plots a heatmap of the coordinates of the principal axis

	Parameters
	----------

	V : a :math:`p \\times p` 2D numpy array
		the coordinates of the principal axis in the basis of the variables

	varnames : a list of strings
		| the names of the variables
		| (names of the columns of `A` on which PCA has been done)

	cmap : a string
		| the matplotlib colormap for drawing the heatmap
		| default value is `viridis`

	title : string
		title of the plot

	x11 : boolean
		the plot is displayed on the scvreen if `x11=True`

	plotfile : string
		name of the file to save the plot

		the plot is not saved if `plotfile=None`

	fmt : string
		format of the file to save the plot.

		accepted values are `png`, `eps`, `pdf`.

	Returns
	-------

	a heatmap


	Notes
	-----


	**Example**


	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> Y, L, V = dio.pca(A)
		>>> dio.plot_var_heatmap(V, varnames=cn)

	af, 22.10.28, revised 23.01.19
	"""

	if varnames:
		str_varnames	= (" ; ").join(varnames)
		print("varnames are")
		print(str_varnames)
	#
	plt.imshow(V, cmap=cmap)
	plt.colorbar()
	#
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	if x11:
		plt.show()


# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_correlation_matrix(C, cmap="ocean", x11=True, plotfile=None, fmt="png"):
	"""Plots a heatmap of the correlation matrix

	Parameters
	----------

	C : a 2D `p x p` numpy array
		The correlation matrix to be plotted

	cmap : a string
		| the matplotlib colormap to use
		| default value is "ocean"

	x11 : boolean
		| whether to display the plot on the screen
		| default value is True

	plotfile :  string
		| the name of the file where to save the plot
		| default value is None (plot not saved)

	fmt : a string
		| the format of the file where the plot is saved
		| possible values are `png`, `eps`, `pdf`.

	Returns
	-------

	Notes
	-----

	For knowing all possible colormaps, see https://matplotlib.org/stable/tutorials/colors/colormaps.html

	**Example**

	.. code:: python

		>>> import pydiodon as dio
		>>> A, rn, cn = dio.load_dataset("diatoms_sweden")
		>>> C = dio.get_correlation_matrix(A)
		>>> dio.plot_correlation_matrix(C)


	af, 22.10.27, revised 23.01.19
	"""
	plt.imshow(C, cmap=cmap)
	plt.colorbar()
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	if x11:
		plt.show()

# ----------------------------------------------------------------------
@spawn(skip=skip)
def plot_coa(Y_r, Y_c, axis_1=1, axis_2=2, col_dsize=20, row_dsize=20, row_col="blue", col_col="red", rownames=[], colnames=[], title=None, x11=True, plotfile=None, fmt="png"):
	"""Scatter plot of the result of a Correspondence Analysis

	Parameters
	----------

	Y_r : a 2D numpy array
		the principal components for the rows

	Y_c : a 2D numpy array
		the principal components for the columns

	axis_1 : an integer
		the first axis of the scatter plot (starting at 1)

	axis_2 : an integer
		the second axis of the scatter plot (starting at 1)

	col_dsize : an integer
		| dot size for dots associated with columns
		| default value is 20

	row_dsize : an integer
		| dot size for dots associated with rows
		| default value is 20

	row_col : a string
		| color for dots associated with rows
		| default value is `blue`


	col_col : a string
		| color for dots associated with columns
		| default value is `red`


	rownames : a list
		| list of names of rows to be plotted
		| default value is [] (no name is plotted)

	colnames : a list
		| list of names of columns to be plotted
		| defalt value is [] (no name is plotted)

	title : a string
		| the title of the plot
		| default value is `None` (no title)

	x11 : a boolean
		| whether to display the plot on the screen
		| default value is `True` (plot displayed)

	plotfile : a string
		| the name of the file where to save the plot
		| default value is `None` (plot not saved)

	fmt : a string
		| format of the file where the plot is saved
		| possible values are : `png`, `eps`, `pdf`
		| default value is `png`

	Returns
	-------

	a scatter plot

	Notes
	-----

	The numbering of the axis in calling the function is natural, and bagins at 1. It is translated
	to start at 0 as in python in the function itself.

	*af, 25/10/2017, revised 22.10.26*
	"""

	print("plotting axis", axis_1, "and", axis_2, "...")
	i	= axis_1 - 1
	j	= axis_2 - 1
	F1	= Y_r[:,i]
	F2	= Y_r[:,j]
	G1	= Y_c[:,i]
	G2	= Y_c[:,j]
	plt.scatter(F1,F2, c=row_col, s=row_dsize)
	plt.scatter(G1,G2, c=col_col, s=col_dsize)
	plt.xlabel("Axis " + str(axis_1))
	plt.ylabel("Axis " + str(axis_2))
	#
	#if len(rownames)>0:
	if rownames:
		for k in range(len(F1)):
			plt.text(F1[k], F2[k], rownames[k])
	#if len(colnames) > 0:
	if colnames:
		for k in range(len(G1)):
			plt.text(G1[k], G2[k], colnames[k])
	#
	if title:
		plt.title(title)
	#
	if plotfile:
		imfile = plotfile + "_"+str(1+i) + "_" + str(1+j)
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	#
	if x11:
		plt.show()

# ----------------------------------------------------------------------


def hovering(F1, F2, label, prefix=None, c="b", s=20):
	"""Display a label of one dot selected with the mouse in a scatter plot

	Parameters
	----------

	F1 : 1D numy array
			first axis

	F2 : 1D numpy array
			second axis

	prefix : forgotten

	c	: string
			forgotten

	s	: integer
			forgotten

	Notes
	-----

	A scatter plot with F1 on axis 1 and F2 on axis 2 is displayed.
	When the mouse clicks on a point, a comment is displayed on the console
	with the index of the item cliked, and the value of the label for this item


	This is event based, i.e. cliking with the mouse can be repeated as many
	times as wished.

	Adapted from http://matplotlib.sourceforge.net/examples/event_handling/pick_event_demo.html

	*af, 25/10/2017*
	"""

	if 1: # picking on a scatter plot (matplotlib.collections.RegularPolyCollection)
		#
		def onpick(event):
			ind = event.ind
			print(prefix, np.take(label, ind))

		fig = plt.figure()
		ax1 = fig.add_subplot(111)
		col = ax1.scatter(F1, F2, c=c, s=s, picker=True)
		fig.canvas.mpl_connect('pick_event', onpick)
		plt.show()

# ----------------------------------------------------------------------

@spawn(skip=skip)
def plot_components_heatmap(Y, axis_1=1, axis_2=2, bins=256, cmap="ocean", range=None, log=True, scale=False, title=None, x11=True, imfile=None, fmt="png"):
	"""Builds the density heatmap of the point cloud of the components of a PCA

	Parameters
	----------

	Y : a :math:`n \\times k` 2D numpy array
		array of the components

	bins : an integer
		the size of the image, in pixels

	axis_1 : an integer
		| first axis to be plotted
		| columns in the image

	axis_2 : an integer
		| second axis of Y
		| rows in the image


	bins : an integer
		| the size of the image
		| it is also the number of classes per axis in the 2D histogram

	cmap : a string
		| the matplotlib colormap for the heatmap
		| default value is `ocean`
		| classical default value in matplotlib is `viridis`
		| see https://matplotlib.org/stable/tutorials/colors/colormaps.html for a choice

	range : is `None`
		compulsory for callind 2D histogram

	log : a boolean
		| whether to translate the densities in a logarithmic scale
		| default value is `True`

	scale : a boolean
		| deprecated
		| default value is `False`

	title : a string
		| the title of the heatmap
		| default value is `None` (no title)

	x11 : a boolean
		| whether to display the plot on the screen
		| default value is `True` (plot displayed)

	plotfile : a string
		| the name of the file where to save the plot
		| default value is `None` (plot not saved)

	fmt : a string
		| format of the file where the plot is saved
		| possible values are : `png`, `eps`, `pdf`
		| default value is `png`


	Returns
	-------

	a heatmap



	Notes
	-----
	`Y` is a numpy array of coordinates, as produced by the MDS

	when two axis are selected

	- the two components are extracted
	- a 2D histogram of their values is computed with a call to `np.histogram2d()`
	- the heatmap is drawn with the values of the 2D histogram


	af, 25/01/2020, revised 22.10.36

	"""
	# getting components on selected axis
	F1					= Y[:,axis_1-1]
	F2					= Y[:,axis_2-1]

	# builds count matrix
	if not range:
		range =  None
	H, xedges, yedges = np.histogram2d(F1, F2, bins=bins, range=range)

	# log transform (scale deprecated)
	if log:
		H	= np.log(1+H)
	if scale:
		M	= np.max(H)
		H	= np.round((H/float(M))*255)
		H 	= np.array(H, dtype=int)
	# plotting count matrix
	plt.imshow(H, cmap=cmap)
	plt.xlabel("axis " + str(axis_1))
	plt.ylabel("axis " + str(axis_2))
	#
	if title:
		plt.title(title)
	plt.colorbar()
	if imfile:
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	if x11:
		plt.show()

# ----------------------------------------------------------------------


########################################################################
#
#		That's all folks!
#
########################################################################







