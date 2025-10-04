#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
What it does: unitary tests for diodon with pytest

contributors: alain franc, jean-marc frigerio, florent pruvost
maintainer:   af
started:      Feb. 15, 2021
version       21.02.27
"""
import filecmp
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

path     = os.path.abspath(__file__)
dir_name = os.path.dirname(path)

sys.path.insert(0, '.')
import pydiodon as dio


class Test_io:
	"""
	"""
	### ------------------------ loadfile()
	
	def test_loadfile(self):
		#
		epsi=1e-9
		#
		print("dataset in txt format, with colnames and rownames")
		filename = "pca_template_withnames.txt"
		A, rownames, colnames  = dio.loadfile(filename, rownames=True,colnames=True)
		assert rownames[0]  == 'MA2'
		assert colnames[-1] == 'wine'
		assert A[0][0]      == 332

		print("\ndataset in txt format, without colnames and rownames")
		filename = "pca_template_nonames.txt"
		AA = dio.loadfile(filename)
		delta = np.max(np.abs(A-AA))
		assert delta < epsi

		print("\ndataset in csv format, with <;> as delim")
		filename = "pca_template_nonames.csv"
		AA = dio.loadfile(filename, delimiter = ";")
		delta = np.max(np.abs(A-AA))
		assert delta < epsi

		print("\ndataset in hdf5 format, without colnames and rownames")
		filename = "pca_template_nonames.h5"
		AA = dio.loadfile(filename, )
		delta = np.max(np.abs(A-AA))
		assert delta < epsi

		print("\ndataset in hdf5 format, with colnames and rownames")
		filename = "pca_template_withnames.h5"
		AA, rownames, colnames = dio.loadfile(filename, rownames=True, colnames=True)
		delta = np.max(np.abs(A-AA))
		assert delta < epsi
		assert rownames[0]  == 'MA2'
		assert colnames[-1] == 'wine'

	def test_writefile(self):
		#
		A, rownames, colnames = dio.loadfile("pca_template_withnames.h5", colnames=True, rownames=True)
		print("save file with dataset in txt format, without colnames and rownames")
		dio.writefile(A, 'data_nonames.txt',  np_fmt='%d')

		assert filecmp.cmp(f'{os.environ["HOME"]}/.pydiodon/datasets/pca_template_nonames.txt', 'data_nonames.txt', shallow=False)

		dio.writefile(A, 'data_withnames.txt', rownames=rownames, colnames=colnames, np_fmt='%d')

		assert filecmp.cmp(f'{os.environ["HOME"]}/.pydiodon/datasets/pca_template_withnames.txt', 'data_withnames.txt', shallow=False)



		





		
		

class Test_pretreatments:
	"""
	"""
	### -------------------------center_col()  

	def test_center_col(self):
		#
		epsi = 1e-6
		n = 4 ; p = 3
		A = np.arange(n*p)
		A.shape=(n,p)
		#		
		Ac, m = dio.center_col(A)
		#
		m_exp	= np.array([4.5, 5.5, 6.5], dtype=float)
		Ac_exp	= np.array([[-4.5, -4.5, -4.5],[-1.5, -1.5, -1.5],[1.5, 1.5, 1.5],[4.5,4.5,4.5]], dtype=float)
		#
		Delta_Ac	= np.max(np.abs(Ac-Ac_exp))
		Delta_m		= np.max(np.abs(m - m_exp))
		#
		Delta 		= np.maximum(Delta_Ac,Delta_m)
		#
		print("\nA =")
		print(A)
		print("columnwise centered matrix is")
		print(Ac)
		print("column means are")
		print(m)
		print("maximum discrepancy:", Delta)
		#
		if Delta < epsi:
			print("test on center_col(): success")
		else:
			print("test on center_col(): failed")
		#
		assert	Delta < epsi  

	### -------------------------center_row()   

	def test_center_row(self):
		epsi = 1e-6
		n = 4 ; p = 3
		A = np.arange(n*p)
		A.shape=(n,p)
		Ac, m = dio.center_row(A)
		#
		m_exp	= np.array([1,4,7,10], dtype=float)
		Ac_exp	= np.array([[-1,0,1],[-1,0,1],[-1,0,1],[-1,0,1]], dtype=float)
		#
		Delta_Ac	= np.max(np.abs(Ac-Ac_exp))
		Delta_m		= np.max(np.abs(m - m_exp))
		#
		Delta 		= np.maximum(Delta_Ac,Delta_m)
		#
		print("\nA =")
		print(A)
		print("rowwise  centered matrix is")
		print(Ac)
		print("row means are")
		print(m)
		print("maximum discrepancy:", Delta)
		#
		if Delta < epsi:
			print("test on center_row(): success")
		else:
			print("test on center_row(): failed")
		#
		assert	Delta < epsi 	
		
	### ---------------------------- centering operator
	
	def test_centering_operator(self):
		"""
		"""
		epsi = 1e-6
		n = 4 ; p = 3
		A = np.arange(n*p)
		A.shape=(n,p)
		#
		H_col = dio.centering_operator(n)
		H_row = dio.centering_operator(p)
		#
		Ac = H_col @ A
		Ar = A @ H_row
		#
		Acc = dio.center_col(A)[0]
		Arr = dio.center_row(A)[0]
		#
		Delta_c = np.max(np.abs(Ac - Acc))
		Delta_r = np.max(np.abs(Ar - Arr))
		Delta	= np.maximum(Delta_c,Delta_r)
		#
		if Delta < epsi:
			print("test on centering_operator(): success")
		else:
			print("test on centering_operator(): failed")
		#
		assert	Delta < epsi 	

# ======================================================================

class Test_methods():
	"""
	contains
		test_acp()
		test_center_col()
	"""

	# ----------------------------------------------------------------------

	def test_pca(self):
		"""
		Reference dataset is borrowed from
		Lebart, Morineau & Fénelon
		Traitement des Données Statistiques
		Dunod (Bordas), 1982
		Section IV.2. Analyse en composantes Principales
		Tableau 1, p.283
		"""
		# import reference dataset
		datafile	= dir_name + "/data4acp.csv"
		A			= np.loadtxt(datafile, delimiter="\t", dtype=float)
		colnames	= ["MA2","EM2","CA2","MA3","EM3","CA3","MA4", "EM4","CA4","MA5","EM5","CA5"]
		rownames	= ["bread","vegies","fruits","meat","poultry","milk","wine"]
		m			= A.shape[0]
		n			= A.shape[1]

		# imports correlation matrix in LMF
		correlfile	= dir_name + "/correlmat.csv"
		C_lmf		= np.loadtxt(correlfile, delimiter="\t",dtype=float)

		# import eigenvalues in LMF
		L_lmf		= np.array([4.3391, 1.8297, 0.6296, 0.1293, 0.0532, 0.0183, 0.0008], dtype=float)

		### ----------------------------Runs ACP in pydiodon


		# method: eigenvalues
		L, V, Y, C	= dio.pca(A, k=-1, meth="evd", correlmat=True)

		### --------------------- Comparisons

		# Comparison of correlation matrix
		print("\nCorrelation matrix")
		Delta_C		= np.max(np.abs(C - C_lmf))
		print("maximum discrepancy:", Delta_C)
		C3		= np.round(1000*C)/1000
		Diff3	= np.round(1000*(np.abs(C-C_lmf)))/1000
		print("Correlation matrix from pydiodon")
		print(C3)
		print("Absolute differences")
		print(Diff3)

		# Comparison of eigenvalues
		print("\nEigenvalues")
		L3	= np.round(1000*L)/1000
		print(L3)

		comp_ev	= np.abs(L-L_lmf)
		plt.plot(comp_ev)
		plt.xlabel("rank")
		plt.ylabel("|L-ev| - L: with diodon ; ev: in LMF")
		plt.title("plot of discrepencies between eigenvalues")
		#plt.show()
		plt.savefig("discrepencies.png", dpi=200)
		plt.close()


		plt.plot([0,5],[0,5], color="chartreuse")
		plt.scatter(L_lmf,L, c="red", s=20)
		plt.xlabel("eigenvalues in LMF")
		plt.ylabel("eigenvalues in pydiodon")
		plt.title("comparison of eigenvalues")
		#plt.show()
		plt.savefig("comparison.png", dpi=200)
		plt.close()

		# Comparison of principal components
		print("\nPrincipal components, with remark 5 of LMF p.288")
		c	= np.sqrt(m/n)
		print(c*Y)

		print("\nCorrelation circle")
	
	# ------------------------------------------------------------------
	
	def test_pca_core(self):
		"""
		"""
		epsi	= 1e-3
		m		= 10
		n		= 5
		A		= np.random.randn(m,n)
		#
		Le, Ve, Ye	= dio.pca_core(A, meth="evd", correlmat=False)
		Ls, Vs, Ys	= dio.pca_core(A, meth="svd", correlmat=False)
		#
		for j in range(n):
			if np.abs(Vs[0,j] + Ve[0,j]) < 1e-9:
				Vs[:,j]	= -Vs[:,j]
		#
		for j in range(n):
			if np.abs(Ys[0,j] + Ye[0,j]) < 1e-9:
				Ys[:,j]	= -Ys[:,j]
		#
		"""
		print("\nVe =")
		print(Ve)
		print("Vs = ")
		print(Vs)
		#
		print("\nYe =")
		print(Ye)
		print("Ys = ")
		print(Ys)
		#	
		"""	
		Delta_L	= np.max(np.abs(Le-Ls))
		print("\ndiscrepancy for L", Delta_L)
		#
		Delta_V	= np.max(np.abs(Ve-Vs))
		print("discrepancy for V", Delta_V)
		#
		Delta_Y	= np.max(np.abs(Ye-Ys))
		print("discrepancy for Y", Delta_Y)
		#
		if Delta_L < epsi:
			print("\ntest on pca_core(), output L: success")
		else:
			print("\ntest on pca_core(), output L: failed")
		#
		if Delta_V < epsi:
			print("test on pca_core(), output V: success")
		else:
			print("test on pca_core(), output V: failed")
		#
		if Delta_Y < epsi:
			print("test on pca_core(), output Y: success")
		else:
			print("test on pca_core(), output Y: failed")
		#		
		assert Delta_L < epsi
		assert Delta_V < epsi
		
		
 
