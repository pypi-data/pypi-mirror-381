#!/usr/bin/env python3

"""
**what it is:**

a python library for linear dimension reduction




**Content:**


============= ========== =======================================
block         functions  what it does                          
============= ========== =======================================
Core          mat_evd()  Core algorithms for dimension reduction 
              svd_grp()  SVD with random projection               
              core_pca() Core PCA                                
Demos         demo_coa() Demonstration of CoA                    
              demo_mds() Demonstration of MDS
              demo_pca() Demonstration of PCA
Methods       coa()      Correspondence Analysis          
              mds()      Multidimensional Scaling                
              pca()      Principal Component Analysis            
              pca_met()  PCA with metrics                        
              pca_iv()   PCA with latent variables               
Pretreatments bicenter() bicentering  
============= ========== =======================================                           


**Identity card**

:maintainer:     Alain Franc
:mail:           alain.franc@inrae.fr
:contributors:   - Alain Franc
                 - Jean-Marc Frigerio 
                 - Florent Pruvost
                 - Olivier Coulaud  
:started:        21/02/17
:version:        21.05.09
:release:        0.0.1
:licence:        GPL




"""
print('\n---------------------------')
print("pydiodon - version 21.05.09")
print("---------------------------\n")


# numpy, scipy
import numpy as np						# For arrays and basic linalg
import numpy.linalg	as nplin			# basic linear algebra (svd, qr)
import scipy as scp
#from scipy import ndimage as ndi		# 

# plots
import matplotlib.pyplot as plt			# for plots

# for testing time needed for a procedure
import time

# as usual ...
import os
import sys

# for loading hdf5
import h5py



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
	""" Computes the eigenvalues and eigenvectors of matrix

	Parameters
	----------

	mat : a numpy array, `n x n` (a matrix)
	
	k : an integer 
		the number of axis to be computed

	Returns
	-------
	
	Z : a numpy array
		of size `n x k`
		the `k` eigenvectors
	
	L : a 1D numpy array
		a vector ; the first `k` eigenvalues   
	
	Notes
	-----
	
	This simply uses `numpy.linalg.eigh()`, and adds some features like 
	
	- sorts eigenvalues in decreasing order
	- sorts eigenvectors in corresponding order
	- sets to zero the imaginary parts (numerical approximation)  

	version 21.03.21
	"""
	#
	# computation of eigenvalues and eigenvectors of Gram matrix
	# L: eigenvalues
	# Z: eigenvectors
	res		= np.linalg.eigh(mat)     # eigenvalues and eigenvectors
	L 		= res[0].real             # eigenvalues of <gram>
	vp_or	= L.ravel().argsort()     # increasing order
	vp_or	= vp_or[::-1]             # decreasing order
	L 		= L[vp_or]                # eigenvalues, decreasing

	# eigenvectors
	Z = res[1]                      # eigenvectors
	Z = Z[:,vp_or]                  # according to eigenvalue order
	
	if k>0:
		L = L[0:k]             	  # first k axis	
		Z = Z[:,0:k].real          # filtering out imaginary part (numerical inaccuracy)

	return Z, L

# ----------------------------------------------------------------------
#
#		SVD through Gaussian random Projection
#
# ----------------------------------------------------------------------

def svd_grp(A, k):
	""" SVD of a (large) matrix `A` by *Gaussian Random Projection*
	
	
	Parameters
	----------

	A : a numpy array
		the matrix to be studied (dimension `n x p`)
	
	k : an integer
		the number of components to be computed

	Returns
	-------

	U : a numpy array
		(dimension `n x k`)
	
	S : a 1D numpy array
		(`k` values)
	
	V : a numpy array
		(dimension `p x k`)

	Notes
	-----
	Here are the different steps of the computation:
	
	1. `A` is a `n x p` matrix
	2. builds :math:`\Omega`, a `p x k` random matrix (Gaussian) 
	3. computes `Y = A`:math:`\Omega` (dimension `n x k`)
	4. computes a QR decomposition of Y
		| `Y = QR`, with
		| `Q` is orthonormal (`n x k`)
		| `R`	is upper triangular (`k x k`)
	5. computes `B = Q'A` 
		`B` is `k x p` (with `k < p`) and its SVD is supposed to be close to the one of `A`
	6. :math:`U_B`, `S`, and `V` are SVD of `B`:
			:math:`B = U_B S V'`, `S` is diagonal
	7. then, :math:`U_A`, `S` and `V` are close to svd of `A` : :math:`A = U_A S V'` 

	*Sizes and computation of the matrices*
	
	============== =================== ============
	matrix         value               size
	============== =================== ============
	`A`            input               `n x p`
	:math:`\Omega` random              `p x k`
	`Y`            :math:`A\Omega`     `n x k`
	`Q`            `Y = QR`            `n x k`
	`B`            `B = Q'A`           `k x p`
	:math:`U_B`    :math:`B = U_BSV'`  `k x k`	
	`U`            :math:`U = QU_B`    `n x k`	
	============== =================== ============ 
	
	

	References
	----------
 
	[1] Halko & al., 2011, *SIAM Reviews*, **53(2):**217-288
	 
	 
	21.03.21
	"""
	p 			= A.shape[1]
	Omega 		= np.random.randn(p,k)	# Computing Omega
	Y 			= np.dot(A, Omega)		# Y = A\Omega
	Q, R 		= nplin.qr(Y)			# QR(Y)
	B 			= np.dot(Q.T,A)			# B = Q'A 
	U_B, S, VT	= nplin.svd(B)	    	# B = UB*S*VB'
	U			= np.dot(Q,U_B)			# A \sim U*S*VB'
	#
	return U, S, VT


########################################################################
#
#		core PCA
#
######################################################################## 

def pca_core(A, k=-1, meth="evd", correlmat=True):
	""" 
	
	**what it does**
	
	core method PCA (Principal Component Analysis) of an array `A`
	
	**arguments**
	
	| `A` : a numpy array, `n x p` ; array to be analysed
	| `k` : an integer ; number of axis to compute
	| `meth` : a string ; method for numerical computing
	
	**returns**
	
	| `L` ; a 1D numpy array ; vector of eigenvalues
	| `V` : a numpy array, `p x k` ; matrix of eigenvectors (new basis)
	| `Y` : a numpy array, `n x k` ; matrix of principl components
	
	**Notes**
	
	`A` is an array, and ``pca_core`` computes the PCA of `A`, without any centering 
	nor scaling nor weights nor constraint. PCA with centering, scaling, 
	weights or constraints calls this function `pca_core()`.
	
	if `k = -1`, all axis are computed. If `k > 0`, only `k` 
	first axis and components are computed.
	
	if `meth` is
	
	| - `evd`, runs by eigendecomposition of X'X
	| - `svd`, runs by singular value decomposition of X
	| - `grp`, runs by SVD of X with Gaussian random projection
	   
	
	| With EVD, it runs as follows:  
	| 1. Computes the correlation matrix :math:`C=A'A`    
	| 2. Computes the eigevalues and eigevectors of :math:`C`: :math:`Cv = \lambda v`   
	| 3. Computes the principal components as :math:`y=Av`, or, globally, :math:`Y=AV`
	
	| with SVD, it runs as follows:
	| 1. :math:`U,\Sigma,V = SVD(A)`
	| 2. :math:`Y = U\Sigma`
	| 3. :math:`L=\Sigma^2` 
	 
	**example**
	
	This is an example of a standard PCA of a random matrix, with :math:`m` rows and 
	:math:`n` columns, with elements as realisation of a uniform law between 0 and 1.
	As such, there is no need to center nor to scale, and the use of ``pca_core()`` is relevant.
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> m = 200 ; n = 50
		>>> A = np.random.random((m,n))
		>>> L, V, Y, C = dio.pca(A)
		>>> plt.plot(L) ; plt.show()
		>>> plt.scatter(Y[:,0],Y[:,1]) ; plt.show()
	   
	*revised 21.03.01*
	"""

	if meth=="evd":
		C		= A.T @ A
		V, L	= mat_evd(C)
		Y		= A @ V
	
	else:
		#
		if meth=="svd":
			U, S, VT	= np.linalg.svd(A, full_matrices=False)
			V			= VT.T
			if correlmat:
				C1	= V @ np.diag(S)
				C	= C1 @ C1.T
		#			
		if meth=="grp":
			U, S, VT	= svd_grp(A, k)			
			V       	= VT.T
			correlmat=False
		#
		if k > 0:
			U   = U[:,0:k]
			S   = S[0:k]
		#
		L	= S*S		
		Y	= U @ np.diag(S)
	#
	if correlmat:
		return Y, L, V, C
	else:
		return Y, L, V
	


# ======================================================================
#
#		Demos
#
# ======================================================================

def demo_mds(dataset, n_axis):
	"""

	**what it is**
	
	Demo for method MDS


	**arguments**
	
	`dataset` : a string ; the pairwise distance matrix to be studied
	
	
	`n_axis` : an integer ; the number of axis to compute


	**notes for dataset** 

	the following dataset is given in directory `dataset`:
	
	dataset	= "../../datasets/atlas_guyane_trnH_dissw.txt"
	
	It is a 1502 x 1502 pairwise distance matrix `dis` (real data)

	each row/column is a sequence of  barcode of a tree in Piste de Sainte Elie, French Guiana

	`D[i,j]` is the distance between sequence `i` and `j` from Smith-Waterman alignment score. 
	(distances computed by program disseq).


	**notes for `n_axis`**
	
	This represents the number of axis to be computed, which should be larger than the number of axis to be plotted with method `grp`. 


	**What it does**

	runs MDS of `dis` with three methods:

	- evd:	eigendecomposition of the Gram matrix
	- svd:	singular value decomposition of the gram matrix (svd() of numpy)
	- grp:	svd with random projection


	**What it produces**


	- for each method:	elapsed time
	- a plot, one color by method, of logarithms of k first eigen/singular values
	- the point cloud in axis (1,2), one plot per method

	warning; the plots may differ by a symmetry or a reflection.
	
	
	**usage**
	
	This demo is launched by program `xmpl_mds.py` in directory `diodon/python/xmpl/`
	
	.. code:: python 
	
		# import what is needed from diodon library
		import sys
		sys.path.append("/home/afranc/_AF/diodon/python")
		from demos import *

		# selects dataset and number of axis
		dataset	= "../../datasets/atlas_guyane_trnH_dissw.txt"
		n_axis	= 500

		# runs the demo
		demo_mds(dataset, n_axis)


	**contact**
	alain.franc@inra.fr


	*@ Pierroton, 07/11/2017, revised 15/01/2018 ; 07/04*
	"""


	# ----------------------------------------------------------------------
	#
	# Loading data
	#
	# ----------------------------------------------------------------------


	dis, headers, rownames = load(dataset, delimiter="\t", headers=True, rownames=True)
	n	= dis.shape[0]
	m	= dis.shape[1]
	print("data loaded ...")
	print("dis has " + str(n) + " rows and " + str(m) + " columns.")

	# ----------------------------------------------------------------------
	#
	# MDS
	#
	# ----------------------------------------------------------------------

	# with EVD
	
	t				= time.time()
	X_evd, S_evd	= mds(dis, n_axis, "evd")
	t_evd			= time.time()
	print("MDS with EVD took " + str(t_evd-t) + " seconds")
	pl				= [S_evd[i] for i in range(5)]
	print("SVD =", pl)

	# with svd()
	t				= time.time()
	X_svd, S_svd	= mds(dis, n_axis, "svd")
	t_svd			= time.time()
	print("MDS with SVD took " + str(t_svd-t) + " seconds")
	pl				= [S_svd[i] for i in range(5)]
	print("SVD =", pl)	

	# with grp
	t				= time.time()
	X_grp, S_grp	= mds(dis, n_axis, "grp")
	t_grp			= time.time()
	print("MDS with SVD-GRP took " + str(t_grp-t) + " seconds")
	pl				= [S_grp[i] for i in range(5)]
	print("SVD =", pl)
	
	
	# ----------------------------------------------------------------------
	#
	# Plotting
	#
	# ----------------------------------------------------------------------
	

	# plotting the singular values
	plt.plot(np.log(S_evd), "r")
	plt.plot(np.log(S_svd), "b")
	plt.plot(np.log(S_grp), "g")
	plt.xlabel("rank of eigen/singular value")
	plt.ylabel("log scale")
	plt.title("evd: red - svd: blue - grp: green")
	plt.show()


	# plotting of first coordinates
	#
	# evd
	plt.scatter(X_evd[:,0], X_evd[:,1], c="r", s=10)
	plt.xlabel("axis 1")
	plt.ylabel("axis 2")
	plt.title("method: evd")
	plt.show()

	# svd
	plt.scatter(X_svd[:,0], X_svd[:,1], c="b", s=10)
	plt.xlabel("axis 1")
	plt.ylabel("axis 2")
	plt.title("method: svd")
	plt.show()

	# grp
	plt.scatter(X_grp[:,0], X_grp[:,1], c="g", s=10)
	plt.xlabel("axis 1")
	plt.ylabel("axis 2")
	plt.title("method: grp")
	plt.show()

# ======================================================================

def demo_coa(dataset):
	"""
	**what it is**
	
	Demo for method CoA
	
	**argument**
	
	`dataset` ; string ; path and name of dataset to be analyzed
	
	**what it does**
	
	- loads the dataset
	
	- runs CoA on the dataset
	
	- displays several plots
	
	**note on the dataset**
	
	The dataset is the one used in Lebart, Morineau & Fénelon
	
	**usage**
	
	This demo is launched by program 
	`xmpl_coa.py` in directory `diodon/python/xmpl/`
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> dataset	= "../datasets/coa_xmpl_lmf.txt"
		>>> dio.demo_coa(dataset)
	
	@ Gazinet, 07/04/2018
	"""
	
	# ----------------------------------------------------------------------
	#
	# Loading data
	#
	# ----------------------------------------------------------------------


	A, headers, rownames = load(dataset, delimiter="\t", headers=True, rownames=True)
	n	= A.shape[0]
	m	= A.shape[1]
	print("data loaded ...")
	print("dis has " + str(n) + " rows and " + str(m) + " columns.")
	
	# ----------------------------------------------------------------------
	#
	# Analysis
	#
	# ----------------------------------------------------------------------	
	
	L, Y_r, Y_c	= coa(A)
	
	# ----------------------------------------------------------------------
	#
	# Plotting
	#
	# ----------------------------------------------------------------------	

	plot_coa(Y_r, Y_c, dot_size=40, n_axis=3)
	plot_coa(Y_r, Y_c, dot_size=40, n_axis=2, rownames=rownames)
	plot_coa(Y_r, Y_c, dot_size=40, n_axis=2, headers=headers)
	plot_coa(Y_r, Y_c, dot_size=40, n_axis=2, rownames=rownames, headers=headers)
	
	# hovering on rows
	print("start hovering on rows ....")
	F1		= Y_r[:,0]
	F2		= Y_r[:,1]
	label	= rownames
	hovering(F1, F2, label,s=40)

	# hovering on columns
	print("start hovering on columns ....")
	F1		= Y_c[:,0]
	F2		= Y_c[:,1]
	label	= headers
	hovering(F1, F2, label, c='r', s=40)	
	
# ======================================================================

def demo_pca(dataset, row_centering=False, col_centering=False,
			bicenter=False, scaled=False, transpose=False, big_row=False):
	"""
	**what it is**
	
	Demo for method PCA
	
	**argument**
	
	`dataset` ; string ; path and name of dataset to be analyzed
	
	**what it does**
	
	- loads the dataset
	
	- runs PCA on the dataset with options specified in the call
	
	- displays several plots
	
	**note on the dataset**
	
	The dataset is a set of ten environmental variables measured on 616 swedish rivers
	reference: Keck, F., Franc, A. and Kahlert, M. (2018) - Disentangling processes driving freshwater diatoms biogeography: a multiscale approach - J. of Biogeography
	
	**notes on the options**
	
	Classical options have been selected, i.e.
	
	- centering on columns
	
	- scaling columnwise
	
	**notes on the plots**
	
	Three classical plots are displayed:
	
	- the fraction of variance explanation cumulated over first eigenvalues
	
	- the point cloud in the first three new axis
	
	- the projecton of the variables in the new basis
	
	
	**usage**
	
	This demo is launched by program `xmpl_pca.py` in directory `diodon/python/xmpl/`
	
	.. code:: python 
	
		# imports diodon library
		import sys
		sys.path.append("/home/afranc/_AF/diodon/python/diodon")
		import diodon as dio

		# selects dataset 
		dataset	= "../datasets/diatoms_sweden.txt"

		# runs the demo
		dio.demo_pca(dataset, col_centering=True, scaled=True)
	
	*@Gazinet, 07/04/2018	
	"""
	
	# ----------------------------------------------------------------------
	#
	# Loading data
	#
	# ----------------------------------------------------------------------
	
	A, headers, rownames = load(dataset, delimiter="\t", headers=True, rownames=True)
	n	= A.shape[0]
	m	= A.shape[1]
	print("data loaded ...")
	print("Data array has " + str(n) + " rows and " + str(m) + " columns.")	
	
	# ----------------------------------------------------------------------
	#
	# Analysis
	#
	# ----------------------------------------------------------------------	
	
	L, V, Y = pca(A, row_centering=row_centering, col_centering=col_centering,
			bicenter=bicenter, scaled=scaled, transpose=transpose, big_row=big_row)
	print("PCA done!")
	
	# ----------------------------------------------------------------------
	#
	# plotting
	#
	# ----------------------------------------------------------------------
	
	plot_eig(L, frac=True, cum=True, dot_size=20)
	plot_pca(Y)
	plot_pca_axes(V, varnames=headers)
	

# ----------------------------------------------------------------------

def demo_pca_randommat(n,p, meth="unif", title=None):
	"""
	**what it is**
	
	PCA of random matrices
	
	**argument**
	
	`n` ; integer ; number of rows
	
	`p` ; integer ; number of columns
	
	`meth` ; string ; method for building random matrix
	
	**Notes**
	
	- builds a random matrix `A` with `n` rows and `p` columns with
	
		- uniform law on [0,1] if `meth = unif`
	
		- Gaussian law with :math:`\mu = 0` and :math:`\sigma = 1` if `meth = gauss`
	
	- runs PCA on the random matrix
	
	- displays the distribution of eigenvalues
	
	
	**usage**
	
	This demo is launched by program `xmpl_pca_randommat.py` in directory `diodon/python/xmpl/`
	
	.. code:: python 
	
		# imports diodon library
		import sys
		sys.path.append("/home/afranc/_AF/diodon/python/diodon")
		import diodon as dio

		# runs the demo
		meth = "gauss"
		n = 1000 ; p = 100  ; dio.demo_pca_randommat(n,p, meth=meth, title = "meth = " + meth + " ; n = " + str(n) + " ; p = " + str(p))
		n = 1000 ; p = 1000 ; dio.demo_pca_randommat(n,p, meth=meth, title = "meth = " + meth + " ; n = " + str(n) + " ; p = " + str(p))
	
	*@Gazinet, 08/04/2018		
	"""
	
	# creating the random matrix
	if meth=="unif":
		A = np.random.rand(n,p)
	if meth=="gauss":
		A = np.random.randn(n,p)
	# running PCA
	L,V,Y = pca(A, col_centering=True, scaled=True)
	
	# plotting
	plot_eig(L, frac=True, title=title)
	plot_eig(L, frac=True, cum=True, title=title)
	

########################################################################
#
#       Multidimensional Scaling
#
########################################################################



def mds(dis, k=-1, meth="svd", no_loop=True):
	"""
	
	**what it does**
	
	Multidimensional Scaling of a distance or dissimilarity array
	
	**arguments**
	
	+-----------+-------------+------------------------------+
	|`dis`      | numpy array | distances or dissimilarities |
	+-----------+-------------+------------------------------+
	| `k`       | integer     | number of axis               |
	+-----------+-------------+------------------------------+
	| `meth`    | string      | method for MDS (see notes)   |
	+-----------+-------------+------------------------------+
	| `no_loop` | boolean     | see notes                    |
	+-----------+-------------+------------------------------+
	
	**Returns**

	+-----+-------------+----------------+----------------------+
	| `X` | numpy array | 2D, `n x k`    | coordinates of items |
	+-----+-------------+----------------+----------------------+
	| `S` | numpy array | 1D, `k` values | singular values      |
	+-----+-------------+----------------+----------------------+
	
	**Notes**
	
	**Objective**: builds a point cloud where one point represents an item, such that the discrepancies beween distances in a matrix `dis` and between associated 
	points in :math:`R^k` is as small as possible.	
	
	| **Procedure:** There are three steps  
	| 1. computes the gram matrix `G` between items from distance matrix `dis`  
	| 2. runs a SVD or EVD of `G`  
	| 3. computes the coordinates from the SVD (or EVD) in `X`   
	
	| **argument no_loop** : it is used in the computton of the Gram matrix:
	| - if `n` is large, ``no_loop=False`` is recommended
	| - if not, ``no_loop=True`` is recommended (default value)
	
	| **methods for MDS:** the argument ``meth`` specifies which method is selected for the core of MDS. Default value is ``svd``.  Let `G` be the Gram matrix associated to the distance array.
	| - if ``meth=svd``, the a SVD of `G` is run
	| - if ``meth=grp``, the SVD is run with Gaussian Random Projection   
	| - if ``meth=evd``, the eigenvalues and eigenvectors of `G` are computed  
	 
	| Here are some suggestions for selection of the method:
	| - if `n` is not too large (:math:`n < 10 000`), ``svd`` method is recommended
	| - if `n` is large, ``grp`` method is recommended, and compulsory if `n` is very large 
	| - if `k` is small, :math:`k \simeq 10`, ``evd`` method is recommended.
	
	| **computations** : EVD or SVD of the Gram matrix are two equivalent ways to compute a solution. Let `G` be the Gram matrix. They are linked by
	| - EVD: :math:`GU = US` ; `U` is the matrix of columnwise eigenvectors of `G` and `S` the diagonal matrix of its eigenvalues
	| - SVD: :math:`G = USU'` is the SVD of `G` (which is symmetric, `U'` is the transpose of `U`)
	| Then, in both cases, if `X` is the matrix of coordinates of `n` items in :math:`R^r`, :math:`X = US^{1/2}`
	
	**examples**
	
	This is a firt toy example for running a MDS. 
	
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
		>>> # runs the MDS
		>>> X, S = dio.mds(D)
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
		>>> # plotting the point cloud, in three dimensions
		>>> F1 = X[:,0]; F2 = X[:,1]; F3 = X[:,2]
		>>> plt.scatter(F1,F2,c="blue", s=5)
		>>> plt.xlabel("axis 1")
		>>> plt.ylabel("axis 2")
		>>> plt.title("data set: Guiana trees")
		>>> plt.show()
		>>> plt.scatter(F1,F3,c="blue", s=5)
		>>> plt.xlabel("axis 1")
		>>> plt.ylabel("axis 3")
		>>> plt.title("data set: Guiana trees")
		>>> plt.show()
		>>> plt.scatter(F2,F3,c="blue", s=5)
		>>> plt.xlabel("axis 2")
		>>> plt.ylabel("axis 3")
		>>> plt.title("data set: Guiana trees")
		>>> plt.show()
	
	
	This example is in ``mds_xmpl_guiana_trees.py``   
		
		
	| The data set can be downloaded from https://doi.org/10.15454/XSJ079 where it is dataset  ``guiana_trees.dissw``.    
	| Related publication: Caron, H, Molino, J‐F, Sabatier, D, et al. Chloroplast DNA variation in a hyperdiverse tropical tree community. *Ecol Evol.* 2019; **9:** 4897– 4905. https://doi.org/10.1002/ece3.5096   
	| Can be downloaded from Wiley website at https://onlinelibrary.wiley.com/doi/pdf/10.1002/ece3.5096 doi: DOI: 10.1002/ece3.5096

	
	**References** 
	
	| [1] T.F. Cox and M. A. A. Cox. *Multidimensional Scaling - Second edition*, volume **88** of Monographs on Statistics and Applied Probability. Chapman & al., 2001.   
	| [2] I. Borg and P. J. F. Groenen. *Modern Multidimensional Scaling*. Springer Series in Statistics. Springer, second edition, 2005.
	| [3] K. V. Mardia, J.T. Kent, and J. M. Bibby. *Multivariate Analysis. Probability and Mathematical Statistics*. Academic Press, 1979.
	
	**Diodon note:** section 10
	


	*07/11/2017 - revised 21.03.20*
	
	"""
	n 	= dis.shape[0]
	if k==-1:
		k = n
	
	# computes gram matrix from dis
	gram		= dis2gram(dis, no_loop)	
							
	# mds core (svd or evd)
	if meth=="grp":
		U, S, V		= svd_grp(gram,k)			# svd by random projection
		cond 		= [0 for i in range(k)]					# positive eigenvalues only
		for i in range(k):
			if U[0,i]*V[0,i] > 0:							# for v_i = u_i (and not -u_i)
				cond[i] = 1
		#print(cond)
		which 	= [i for i, item in enumerate(cond) if item==1]
		U		= U[:,which]		# first k axis with equivalent >0 eigenvalue
		S		= S[which]		    # first k singular values with equivalent >0 eigenvalue	
	#	
	if meth=="svd":
		U, S, VT	= nplin.svd(gram, full_matrices=False)	# with svd() of numpy.linalg	
		V			= VT.T									# svd() yields gram = U*S*V
		cond 		= [0 for i in range(n)]
		for i in range(n):
			if U[0,i]*V[0,i] > 0:
				cond[i] = 1
		which 	= [i for i, item in enumerate(cond) if item==1]
		which_k	= which[0:k]
		U		= U[:,which_k]		# first k axis with equivalent > 0 eigenvalue
		S		= S[which_k]		# first k singular values with equivalent >0 eigenvalue
	#
	if meth=="evd":
		U, S	= mat_evd(gram, k)
		cond	= [1]*k
		for i in range(k):
			if S[i]<0:
				cond[i] = 0
		which = [i for i, item in enumerate(cond) if item==1]
		U	= U[:,which]
		S	= S[which]
	
	# Computation of components						
	SR			= np.diag(np.sqrt(S))					# singular values (diagonal matrix)
	X			= np.dot(U, SR)							# array of coordinates
	#
	return X, S
	
########################################################################
#
#       Correspondence Analysis
#
########################################################################

def coa(X, k=-1, meth="svd", transpose=False):
	"""
	**what it does**
	
	Correspondance Analysis of an array X
	
	**arguments**

	`X`: a numpy array, `n x p` ;
		array to be analysed
	
	`k`: an integer ; number of axis to compute
	
	`meth` : a string ; method for numerical computing
	
	**returns**
	
	`L` : a 1D numpy array	; vector of eigenvalues
	
	`Y_r` : a numpy array, `n x k` ; coordinates of row points
	
	`Y_c` : a numpy array, `p x k` ; coordinates of column points
	
	**Notes**
		
	If :math:`k=-1`, all axis are computed. If :math:`k > 0`, only `k` 
	first axis and components are computed.
	
  
	*methods for PCA core*
	
	==== ======================================
	evd  EVD
	svd  SVD with `numpy.linalg.svd()` 
	grp  SVD with gaussian random projection
	==== ======================================	   
	
	**example**
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> dataset = "../data4tests/coa4tests.txt"
		>>> A, headers, rownames = dio.load(dataset)
		>>> L, Y_r, Y_c	= dio.coa(A)
		
		
	**note on the example** 
	
	The dataset is in `text` format with tabs as delimiters. It contains 
	headers and row names. These are default parameters for fucntion 
	`dio.load()`
	
	  
	**Reference:**
	
	Nenadic & Greenacre, *Journal of Statistical Software*, **20(3):** 2-13, 2007
	
	Lebart, Morineau & Fénelon, 1982, pp. 305-320
	
	*revised 21.02.21*   
	"""


	# transposes X if n < p
	if transpose:
		X	= X.T
		print("The array has been transposed (transpose=True).")
		
	n			= X.shape[0]
	p			= X.shape[1]		
		
	# marginals computation
	N			= float(np.sum(X))
	X			= X/N
	margin_row	= np.sum(X, axis=1)	# sum per row
	margin_col	= np.sum(X, axis=0)	# sum per column
	# tests if no margin is zero (suitable)
	n_i0		= margin_row.tolist().count(0)
	n_j0		= margin_col.tolist().count(0)
	if n_i0 > 0:
		print("\nwarning: some rows have zero sum")
		print("this will lead to an error (division by zero)\n")
	if n_j0 > 0:
		print("\nwarning: some columns have zero sum")
		print("this will lead to an error (division by zero)\n")
		
	# diagonal matrices of weights on rows and columns
	w_row		= np.sqrt(1.0/margin_row)
	w_col		= np.sqrt(1.0/margin_col)		
	Dr			= np.diag(w_row)
	Dc			= np.diag(w_col)
	
	# Computation of matrix for SVD
	M			= np.outer(margin_row, margin_col)	# expected rank one matrix of products of marginals
	A			= np.dot(Dr, X-M)
	A			= np.dot(A,Dc)
	
	if meth=="svd":
		U, S, VT	= np.linalg.svd(A, full_matrices=False)
		V       	= VT.T	
	if meth=="grp":
		U, S, V = svd_grp(A, k)
		
	if k > 0:
			U   = U[:,0:k]
			S   = S[0:k]
	#
	L	= S*S
	Y	= np.dot(U,np.diag(S))
	Z	= np.dot(V,np.diag(S))
	Y_r	= np.dot(Dr, Y)
	Y_c	= np.dot(Dc,Z)
	
	return	L, Y_r, Y_c

		

########################################################################
#
#       Principal Component Analysis
#
########################################################################



def pca(A, pretreatment="standard", k=-1, meth="evd", correlmat=True):
	""" Principal Component Analysis
	
	Parameters
	----------
	
	A : a numpy array
		the array to be analyzed
	
	k : integer
		number of axes to be computed
	
	meth : string
		   method for numerical calculation (see notes)
	
	pretreatment : string
				   which pretreatment to apply   
				   accepted values: ``standard``, ``bicentering``, ``col_centering``, ``row_centering``, ``scaling`` 
				   see notes for details
	
	correlmat : boolean
				if True, the correlation matrix is available
	
	
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
 
	- "standard": the matrix is centered and scaled columnwise 
	- starndard=True: input matrix is centered columnwise and then scaled
	- bicentering=True: a useful alternative to CoA
	
	**examples**
	
	This is an example of a standard PCA of a random matrix, with :math:`m` rows and 
	:math:`n` columns, with elements as realisation of a uniform law between 0 and 1. 
	
	Let us start with standard PCA will all defaut arguments, as in 
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> import matplotlib.pyplot as plt
		>>> m = 200 ; n = 50
		>>> A = np.random.random((m,n))
		>>> L, V, Y, C = dio.pca(A)
		>>> plt.plot(L) ; plt.show()
		>>> plt.scatter(Y[:,0],Y[:,1]) ; plt.show()
	
	
	The above program runs centered scaled PCA, with here default option ``pretreatment=="standard"``.
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
	
	
	Prescribed rank is simply called by (with standard pretreatment)
	
	.. code:: python 
	
		>>> rank = 10
		>>> L, V, Y, C = dio.pca(A, k=rank)
	
	
	for having the 10 first components and axis only, and prescribed accuracy .	
	
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
	print("correlation matrix is", correlmat)
	print("------------------------------------------\n")
	
	### ------------ preparation
	
	# transposition if necessary
	
	if n > m:
		print("more columns than rows => matrix is transposed")
		A = A.T
		transpose = True
	else:
		transpose = False
		
	
	# no correlation matrix if grp method
	
	if meth=="grp":
		correlmat = False
		
	
	# ------------ pretreatments
	#
	
	accepted = ["standard","bicentering", "scaling", "col_centering", "row_centering"]
	if pretreatment not in accepted:
		print("required pretreatment is not recognized. Accepted strings are")
		print(accepted)
		#exit("pca() terminated with error")

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
	if correlmat:
		Y, L, V, C	= pca_core(A, k=k, meth=meth, correlmat=correlmat)
	else:
		Y, L, V		= pca_core(A, k=k, meth=meth, correlmat=correlmat)
	#
	if transpose:
		V = np.dot(A,V)					# V n x n -> p x n 
		Y = np.dot(A.T,V)				# Y is n x n
	#
	if correlmat:
		return Y, L, V, C
	else:
		return Y, L, V


	
########################################################################
#
#       Principal Component Analysis with metrics
#
########################################################################
		


def pca_met(A, k=-1, meth="evd", diag=True):
	"""
	
	**what it does**
	
	PCA of an array `A` with metrics on rows and/or columns
	
	**arguments**
	
	`A` : a numpy array
	
	
	`k` : an integer
	
	`meth` : a string ; method for numerical calculation
	
	`row_centering` : a boolean ; whether to center rowwise
	
	`col_centering` : a boolean ; whether to center columnwise
	
	`bicenter` : a boolean ; whether to center rowise and columnwise
	
	`scaled` : a boolean ; whether to scale
	
	** note: still under work **
	
	*@ Aillevillers, 28/12/2017*
	"""
	
	if diag==True:
		pass
	
	
	# ------------- core PCA after pretreatment
	#
	L, V, Y	= pca_core(A, k, meth)
	#
	return L, V, Y
	
########################################################################
#
#       Principal Component Analysis with instrumental variables
#
########################################################################
		


def pca_iv(A, B, k=-1, meth="evd", col_centering=False, scaled=False, transpose=False):
	"""
	
	**what it does**
	
	PCA of an array `A` with instrumental variables
	
	**arguments**
	
	`A` : a numpy array, the items/variable to be analyzed
	
	`B` : a numpy array, the intrumental variables
		
	`k` : an integer
	
	`meth` : a string ; method for numerical calculation
	
	`row_centering` : a boolean ; whether to center rowwise
	
	`col_centering` : a boolean ; whether to center columnwise
	
	`bicenter` : a boolean ; whether to center rowise and columnwise
	
	`scaled` : a boolean ; whether to scale
	
	** notes: still under work **
	
	`A_pre` is a copy of `A` for tracking preatreatments, and recover the
	matrix analyzed after preatreatments, without impacting `A` 
	
	
	The algorithm is as follows:
	
	- Build :math:`Q=(B'B)^{-1}B'` 
	
	- :math:`P = BQ = B(B'B)^{-1}B'` 
	
	- build :math:`A_proj = PA` 
	
	- do PCA of `A_proj` : :math:`L,V,Y = PCA(A_proj)`, with `Y = A_proj V = BR` with `R = QAV`
	
	*@ Cayenne, 21/02/2018*
	"""	
	
	# ---------- pretreatment
	#
	#
	A_pre	= A.copy()
	B_pre	= B.copy()
	
	if col_centering==True:
		A_pre	= center_col(A_pre)
		B_pre	= center_col(B_pre)
	#
	#
	if scaled==True:
		A_pre = scale(A_pre)	
		B_pre = scale(B_pre)	
		
	# ----------- projector on B
	#
	#
	P, Q	= project_on(B_pre)			# P = B(B'B)^{-1}B'
	A_proj	= np.dot(P,A_pre)			# A_proj = PA
	
	
	# ----------- PCA
	
	L, V, Y = pca(A_proj, transpose=transpose)
	
	return L, V, Y, A_pre, A_proj, P, Q
	
	
	


########################################################################
#
#		PCA-IV
#
########################################################################


def proj_qual_global(A, A_proj):
	"""
	"""
	nA		= np.linalg.norm(A)
	nAp		= np.linalg.norm(A_proj)
	rho		= (nAp*nAp)/(nA*nA)
	#
	return rho	
	
# ----------------------------------------------------------------------

def proj_qual_axis(A, A_proj, title=None, x11=True, imfile=None, fmt="png"):
	"""
	*af, @ Cayenne, 21/02/2018*
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
	"""
	bicentering a matrix
	
	**argument**
	
	`A` : a `n x p` numpy array ; the matrix to be bicentered   
	
	**returns**
	
	`m`	: a float	; global mean of the matrix    
	 
	`r` : a 1D numpy array (`n` values) ; rowise means    
	
	`c`	: a 1D numpy arrau (`p` values) ; columnwise means   
	
	`R`	: a 2D numpy array (`n x p`) ; bicentered matrix   
	
	**notes**  
	
	If `A` is a matrix, builds a matrix `R` of same dimension centered 
	on rows nd columns.
	
	:math:`\mu = (1/np) \sum_{i,j} a_{ij}`   
	
	:math:`r_i = (1/p)\sum_j a_{ij} - \mu`   
	
	:math:`c_j = (1/n)\sum_i a_{ij} - \mu`   
	
	such that  
	
	:math:`\sum_ir_i = \sum_jc_j=0`  
	
	and
	
	for any row `i`, :math:`\sum_j R_{ij}=0` and for any column `j`, :math:`\sum_i R_{ij}=0`

	**example**
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> m, r, c, R = dio.bicenter(A)
		
	revised 21.02.19

	"""
	n	= A.shape[0]
	p	= A.shape[1]
	m 	= np.mean(A)
	r	= np.mean(A, axis=1) - m
	c	= np.mean(A, axis=0) - m
	en	= np.ones(n)
	ep	= np.ones(p)
	R	= A - m - np.outer(en,c) - np.outer(r,ep)
	#
	return m, r, c, R
	 
# ----------------------------------------------------------------------

def centering_operator(m):
	"""
	Centering operator for a matrix
	
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
		>>> H_col = diod.centering_operator(n)
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
	"""
	centers a matrix columnwise
	
	**argument**
	
	`A` : a 2D numpy array, :math:`n \times p` ; a matrix
	
	**returns**
	
	`Ac`	: a :math:`n \times p` numpy array ; `A`, centered columnwise    
	`m`		: a 1D numpy array ; means per column 
	
	**example**
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> Ac, m = dio.center_col(A)
		

	
	*revised with R.P., @ Cestas, 21.02.19*
	"""
	m	= np.mean(A, axis=0)
	Ac	= A - m

	#
	return Ac, m
	
	# ----------------------------------------------------------------------
	
def center_row(A):
	"""
	centers a matrix row-wise
	
	**argument**
	
	`A` : a 2D numpy array, :math:`n x p` ; a matrix
	
	**returns**
	
	`Ac`	: a :math:`n x p` numpy array ; `A`, centered row-wise    
	`m`		: a 1D numpy array (`n` values); means per row
	
	**example**
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape=(n,p)
		>>> Ac, m = dio.center_row(A)
		

	
	*revised with R.P., @ Cestas, 21.02.19*
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
	"""
	scales a matrix columnwise
	
	**argument**
	
	`A` : a numpy array, `n x p` ; a matrix
	
	**returns**
	
	:math:`As` : a numpy array	 ; matrix `A` with scaled columns
	
	**Notes**
	
	It is recommended to center `A` columnwise before scaling. 
	
	Each coordinates :math:`a_{ij}` of `A` is replaced by 
	:math:`a_{ij} / ||a_{.j}||` where :math:`||a_{.j}||` is the norm 
	of column `j`:  :math:`||a_{.j}||^2 = \sum_i a_{ij}^2`
	
	**example**
	
	.. code:: python 
	
		>>> import pydiodon as dio
		>>> import numpy as np
		>>> n = 4 ; p = 3
		>>> A = np.arange(n*p)
		>>> A.shape =(n,p)
		>>> Ac, m = dio.center_col(A)  
		>>> As, s = dio.scale(Ac)
	
	21.02.19
	"""
	p	= A.shape[1]
	a	= nplin.norm(A, axis=0)
	A_s	= A.copy()
	for j in range(p):
		A_s[:,j] = A[:,j]/a[j]
	#
	return A_s, a 
	
# ----------------------------------------------------------------------
#
#	from distance matrix to gram matrix
#
# ----------------------------------------------------------------------
    
def dis2gram(dis, no_loop=True):
	"""
	Computes a Gram matrix `gram` knowing a distance matrix `dis`
	
	
	**arguments**
	
	
	`dis`: a numpy array, size `n x n`, of floats
			is a distance matrix
	
	**returns**
	
	
	`gram`: a numpy array, size `n x n` of floats
				is the associated Gram matrix
	
	**notes**
	
	if
	:math:`d_{i.}^2 = (1/n) \sum_j d_{ij}^2` and :math:`d_{..}^2 = (1/n^2) \sum_{i,j} d_{ij}^2`
	
	then
	
	:math:`gram[i,j] = -(1/2) (d_{ij}^2 - d_{i.}^2 - d_{.j}^2 + d_{..}^2)`
	
	*AF, Pierroton, 07/11/2017*
	"""
	#
	n		= dis.shape[0]						# number of items
	e_n		= np.ones(n)						# (1, ..., 1) n times
	if no_loop==True:
		dis2	= dis*dis                			# dis*dis componenwise
		di_  	= dis2.mean(axis=1)                 # mean per row
		d_j  	= dis2.mean(axis=0)                 # mean per column
		d__  	= dis2.mean()                       # global mean
		s_1  	= np.outer(di_, e_n)                # one row with row mean
		s_2  	= np.outer(e_n, d_j)                # one column with column mean
		s_3  	= d__ * np.ones(shape=(n, n)) 		# same dimension as dis with '1'
		gram   	= (-.5)*(dis2 - s_1 - s_2 + s_3)    # covariance matrix	
		#
	else:
		t 		= time.time()
		for i in range(n):
			for j in range(i,n):
				x			= dis[i,j]
				y			= x*x
				dis[i,j] 	= y
				dis[j,i]	= y
		t_square = time.time()
		print("squaring took:", t_square - t, "sec.")
		di_  	= dis.mean(axis=1)                 # mean per row
		d_j  	= dis.mean(axis=0)                 # mean per column		 
		d__  	= dis.mean()                       # global mean
		t_marg	= time.time()
		print("marginalization took:", t_marg - t_square, "sec.")
		for i in range(n):
			for j in range(i,n):
				y			= dis[i,j] - di_[i] - d_j[j] + d__
				dis[i,j]	= y
				dis[j,i]	= y
		gram = (-.5)*dis
		t_inner = time.time()
		print("computing inner products took:", t_inner - t_marg, "sec.")	
		#
	return gram	
		

# ----------------------------------------------------------------------

def project_on(A):
	"""
	Builds the projection operator on space spanned by the columns of A
	
	* af, @ Cayenne, 22/02/2018*
	"""
	C 		= np.dot(A.T,A)			# C = A'A
	C_inv 	= np.linalg.inv(C)		# C^{-1}
	Q		= np.dot(C_inv,A.T)		# (A'A)^{-1}A'
	P		= np.dot(A,Q)			# P = A(A'A)^{-1}A'
	#
	return P, Q




########################################################################
#
#			io_utils
#
########################################################################

def fortest():
	""" Trucmuche
	
	Parameters
	----------
	
	A : numpy array
		truc
		
	B : string
		cloche
	
	"""
# ----------------------------------------------------------------------

def loadfile(filename, fmt=None, delimiter="\t", colnames=False, rownames=False, datasetname='values', dtype='float32'):
  """A generic function for loading datasets as numpy arrays


  Parameters
  ----------
  
  filename : string
             contains the data set to be loaded (compulsory)   

               
  fmt : string 
        explicit format of the file (optional) 
        if it is not given the format will be guessed from the suffix (see notes)
        
                
  delimiter : character 
              the delimiter between values in a row
              

  colnames : boolean or string
             column names
             for an ascii file, it is boolean, as True is column names are as first row in the file, and False otherwise
             for an hdf5 file, gives the name of the dataset with the column names
             optional
             default value is None.
             
  rownames : boolean or string
             row names
             for an ascii file, it is boolean, as True is row names are as first column in the file, and False otherwise
             for an hdf5 file, gives the name of the dataset with the row names
             optional
             default value is None.             
             
  datasetname : string
                for hdf5 files : hdf5 dataset for values
                optional
                default value is "value"
  
  Returns
  -------
  
  A : a numpy array
      the values of the data set
      
  cn : list of strings 
       column names (optional)
       
  rn : list of strings
       row names (optional)
       
  Notes
  -----
  
  Recognized formats are: ``ascii``, ``hdf5`` and ``compressed ascii``.   
  Delimiters in ascii format can be blanks, comma, semi-columns, tabulations.  
  Ascii data sets with ``tab`` delimiters are expected to be with suffix ``.txt``.
  Ascii data sets with other delimiters are expected to be with siffix ``.csv``.
  
  When the filename is read, the function splits the name on the last dot, and
  interprets the string after as the suffix. Then, there is a call to ``load_ascii()`` if
  the suffix is ``.txt``, ``.gz`` or ``.bz2``, to ``load_hdf5`` if the suffix is ``h5`` or ``hdf5``,
  and unzips the file before a call to ``load_ascii()`` if the sufix is ``zip``.
           
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
  suffix_list  = ('.txt','.csv', '.dissw','.gz', '.bz2')
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

def load_ascii(filename, delimiter, colnames, rownames, dtype):
  """ Loads an ascii file as a numpy array
  
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
    A = np.loadtxt(filename, delimiter=delimiter, dtype=bytes)
    cn = A[0,1:].astype(str).tolist()
    rn = A[1:,0].astype(str).tolist()
    A = A[1:,1:]
    A = np.array(A, dtype=dtype)
    return A, rn, cn

  if colnames and not rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=bytes)
    cn = A[0,:].astype(str).tolist()
    A  = A[1:,:]
    A  = np.array(A, dtype=dtype)
    return A, cn
  
  if not colnames and rownames:
    A = np.loadtxt(filename, delimiter=delimiter, dtype=bytes)
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
             for an ascii file, it is boolean, as True is column names are as first row in the file, and False otherwise
             for an hdf5 file, gives the name of the dataset with the column names
             optional
             default value is None.
             
  rownames : boolean or string
             row names
             for an ascii file, it is boolean, as True is row names are as first column in the file, and False otherwise
             for an hdf5 file, gives the name of the dataset with the row names
             optional
             default value is None.             
             
  datasetname : string
                for writing files in hdf5 format only : hdf5 dataset for values
                optional
                default value is "value"
                
  np_fmt : string
           is xactly the parameter ``fmt`` of ``numpy.savetxt()`` for print format in ascii files
           to be done
                
  dtype : to be done
  
  Returns
  -------
  
  nothing
       
  Notes
  -----
  
  It writes the array in a file and returns no value. Parameters and choices are mirrored
  from function ``loadfile()`` as it is the reverse operation.
  
  Possible formats are: ``ascii``, ``hdf5`` and ``compressed ascii``.   
  Delimiters in ascii format can be blanks, comma, semi-columns, tabulations.  
  Ascii data sets with ``tab`` delimiters are expected to be with suffix ``.txt``.
  Ascii data sets with other delimiters are expected to be with siffix ``.csv``.
  
  
  *set  21.04.22, jmf & af*
    
  """
  
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
  """ Write an ascii file """
  
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
	""" Write a hdf5 file """
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

def plot_eig(L, frac=True, cum=False, dot_size=-1, nb_val=-1, col="red", title=None, x11=True, plotfile=None, fmt="png"):
	"""
	Plots the singular or eigenvalues
	
	Inputs
	------
	@ L		numpy array		vector of singular/eigenvalues
	
	Output
	------
	a plot
	
	@ gazinet ; 25/10/2017 - revised 18/09/2019
	"""
	sumL	= np.sum(L)
	frcL	= L/sumL
	#	
	if frac==True:
		L	= frcL
	#
	if cum==True:
		L	= np.cumsum(frcL)
	#
	if nb_val > 0:
		L	= L[0:(nb_val-1)]
	#
	M 	= np.max(L)
	buf	= M/50
	#
	plt.plot(L, c=col)
	plt.plot([-.5, len(L)],[0,0], c="black")
	plt.plot([0, 0],[-buf,M+buf], c="black")
	if dot_size>0:
		plt.scatter(range(len(L)), L, c=col, s=dot_size)
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
	
# ----------------------------------------------------------------------

def plot_components_scatter(Y, n_axis=3, dot_size=20, color="red", cmap=None, names=[], title=None, x11=True, plotfile=None, fmt="png"):
	"""
	Scatter plot of the result of a Principal Component Analysis
	
	**arguments**

	`Y`: a numpy array, `n x p` ; a matrix of principal components
	
	`n_axis`: an integer ; the number of axis to be plotted

	**notes** 
	
	Displays all plots axis_i  :math:`\\times`  axis_j for :math:`1 \leq i < j \leq n_{axis}`
	
	
	*@ Cayenne, 21/02/2018*
	"""

	# row and column points
	for i in range(n_axis):
		for j in range(i+1, n_axis):
			#
			F1	= Y[:,i]
			F2	= Y[:,j]
			plt.scatter(F1,F2, c=color, s=dot_size)
			#
			if len(names)>0:
				for i, item in enumerate(names):
					plt.text(F1[i], F2[i], item)
			#
			if title:
				plt.title(title)
			#
			plt.xlabel("Axis " + str(i+1))
			plt.ylabel("Axis " + str(j+1))
			if cmap:
				plt.colorbar()
			#
			if plotfile:
				imfile = plotfile + "_"+str(1+i) + "_" + str(1+j)
				plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
			#
			if x11:
				plt.show()
				
# ----------------------------------------------------------------------

def get_quality_per_item(Y,r=2, col="blue", title=None, x11=True, plotfile=None, fmt="png"):
	"""
	"""
	(n,p)	= Y.shape
	Y2		= Y*Y
	Qual 	= np.cumsum(Y2, axis=1)
	for i in range(n):
		Qual[i,:] = Qual[i,:]/Qual[i,p-1]
	#	
	plt.plot(Qual[:,r], c=col)
	plt.xlabel("item")
	plt.ylabel("quality of projection on axis < " + str(r))
	if title:
		plt.title(title)
	if plotfile:
		plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
	if x11:
		plt.show()
	#
	return Qual		

# ----------------------------------------------------------------------

def plot_components_quality(Qual,r, Y, n_axis=2, cmap="viridis", diam=50, title=None, x11=True, plotfile=None, fmt="png"):
	"""
	"""
	qual	= diam*Qual[:,r]
	plot_components_scatter(Y, n_axis=2, dot_size=qual, color=qual, cmap=cmap, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

# ----------------------------------------------------------------------

def plot_var(V, varnames, n_axis=2, x11=True, plotfile=None, fmt="png"):
	"""
	"""
	#
	p	= V.shape[0]
	for i in range(n_axis):
		for j in range(i+1,n_axis):
			#
			fig, ax = plt.subplots()
			circle = plt.Circle((0, 0), radius=1, color='r', fill=False)
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

def plot_correlation_matrix(C, x11=True, plotfile=None, fmt="png"):
	"""
	plots a heatmap of the correlation matrix
	"""
	plt.imshow(C)
	plt.colorbar()
	if plotfile:
		plt.savefig("%s.%s" % (plotfile, fmt), format=fmt)
	if x11:
		plt.show()

# ----------------------------------------------------------------------

def plot_coa(F, G, n_axis=3, dot_size=20, col_rows="blue", col_cols="red", rownames=None, headers=None, title=None, x11=True, plotfile=None, fmt="png"):
	"""
	Scatter plot of the result of a Correspondence Analysis
	
	**arguments**

	`F`: a numpy array, `n x n` ; a matrix
	
	`n_axis`: an integer ; the number of axis to be plotted

	**returns**
	
	`Z`: a numpy array, size `n x k` ; first `k` eigenvectors	
	
	**notes** 
	
	Dislays all plots axis_i  :math:`\\times`  axis_j for :math:`1 \leq i < j \leq n_{axis}`
	
	
	*@ Pierroton, 25/10/2017*
	"""

	# row and column points
	for i in range(n_axis):
		for j in range(i+1, n_axis):
			print("plotting axis", i+1, "and", j+1, "...")
			F1	= F[:,i]
			F2	= F[:,j]
			G1	= G[:,i]
			G2	= G[:,j]
			plt.scatter(F1,F2, c=col_rows, s=dot_size)
			plt.scatter(G1,G2, c=col_cols, s=dot_size)
			plt.xlabel("Axis " + str(i+1))
			plt.ylabel("Axis " + str(j+1))
			if rownames:
				for k in range(len(F1)):
					plt.text(F1[k], F2[k], rownames[k])
			if headers:
				for k in range(len(G1)):
					plt.text(G1[k], G2[k], headers[k])					
			if title:
				plt.title(title)
			if plotfile:
				imfile = plotfile + "_"+str(1+i) + "_" + str(1+j)
				plt.savefig("%s.%s" % (imfile, fmt), format=fmt)
			if x11:
				plt.show()			
				
# ----------------------------------------------------------------------


def hovering(F1, F2, label, prefix=None, c="b", s=20):
	"""
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


def plot_components_heatmap(Y, axis_1=0, axis_2=1, bins=256, range=None, log=True, scale=False, title=None, x11=True, imfile=None, fmt="png"):
	"""
	wid: builds the heatmap
	
	arguments
	---------
	@ Y			numpy array
	@ bins		integer		the size of the image
	@ axis_1	integer		first axis of Y
	@ axis_2	integer		second axis of Y
	@ fmt		string		format for writing the heatmap in a file
	
	output
	------
	none	(displays the count matrix on the screen and/or writes it in a file)
	
	Notes
	-----
	Y is a numpy array of coordinates, as produced by the MDS
	
	af, @ Gazinet, 25/01/2020
	
	"""
	# getting components on selected axis
	F1					= Y[:,axis_1]
	F2					= Y[:,axis_2]
	
	# builds count matrix
	H, xedges, yedges = np.histogram2d(F1, F2, bins=bins, range=range)
	
	# log transform (scale deprecated)
	if log:
		H	= np.log(1+H)
	if scale:
		M	= np.max(H)
		H	= np.round((H/float(M))*255)
		H 	= np.array(H, dtype=int)	

	# plotting count matrix
	plt.imshow(H)
	plt.xlabel("axis " + str(1+axis_1))
	plt.ylabel("axis " + str(1+axis_2))
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



	
	

	
