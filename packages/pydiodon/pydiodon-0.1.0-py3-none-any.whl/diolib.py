#!/usr/bin/env python3

import sys
import os
import traceback
import yaml
import numpy as np
import pydiodon as dio


# ======================================================================

class diodsl():
	"""
	"""
	def __init__(self,basename):
		"""
		"""
		
		### ------------- 
		self.basename	= basename
		self.configfile	= basename + '.yaml'
		self.yam		= {}

		print(f'\nconfigfile is {self.configfile}\n')
		
		### ------------ loading yaml file
		
		print("loading yaml file ...")
		try:
			self.yam = yaml.load(open(self.configfile), Loader=yaml.SafeLoader)
			print("yaml file loaded")
		except FileNotFoundError:
			pass
		except:
			print("exception while loading yaml file")
			traceback.print_exc()
		
	# ------------------------------------------------------------------
	#
	#					 loding a file
	#
	# ------------------------------------------------------------------
	
	def load_file(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		method		= self.yam[f_name]["method"]
		infile		= self.yam[f_name]["infile"]
		colnames	= self.yam[f_name]["colnames"]
		rownames	= self.yam[f_name]["rownames"]
		delimiter	= self.yam[f_name]["delimiter"]
		
		
		if delimiter.upper() == 'TAB': delimiter = '\t'
		#
		M, rn, cn	= dio.load_ascii(infile, delimiter=delimiter,colnames=colnames, rownames=colnames)
		#

		self.rn	= rn
		self.cn	= cn		
		#
		if method=="pca":
			self.A		= M
			self.Dis	= None
			self.T		= None
		#
		if method=="coa":
			self.T		= M
			self.A		= None
			self.Dis	= None
		#
		if method=="mds":
			self.Dis	= M
			self.A		= None
			self.T		= None
			
	load_ascii = load_file
	

	# ------------------------------------------------------------------
	#
	#                      PCA 
	#
	# ------------------------------------------------------------------
	

	
	def pca(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		pretreatment = self.yam[f_name]["pretreatment"]
		k            = self.yam[f_name]['k']
		meth         = self.yam[f_name]['meth']
		
		
		Y, L, V	= dio.pca(self.A, pretreatment=pretreatment, k=k, meth=meth)
		
		self.Y	= Y
		self.L	= L
		self.V	= V 
    
	# ------------------------------------------------------------------
	
	def get_correlation_matrix(self):
		"""
		"""
		self.C = dio.get_correlation_matrix(self.A)
		
	# ------------------------------------------------------------------
	
	def quality(self):
		"""
		"""
		
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		
		Qual_axis, Qual_cum	= dio.quality(self.Y)
		
		self.Qual_axis	= Qual_axis
		self.Qual_cum	= Qual_cum
		
		
	# ------------------------------------------------------------------
    #
    #                                MDS
    #
    # ------------------------------------------------------------------
    
	
	def mds(self):
		"""
		""" 
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		k		= self.yam[f_name]["k"]
		meth	= self.yam[f_name]["meth"]
		loop	= self.yam[f_name]["loop"]
		Y_file	= self.yam[f_name]["Y_file"]
		L_file	= self.yam[f_name]["L_file"]
		
		Y, L	= dio.mds(self.Dis, k, meth=meth, loop=loop, Y_file=Y_file, L_file=L_file)

		self.Y	= Y
		self.L	= L
		
	# ------------------------------------------------------------------
	#
	#					 plotting()
	#
	# ------------------------------------------------------------------
	
	
	def plot_components_scatter(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		axis_1		= self.yam[f_name]["axis_1"]
		axis_2		= self.yam[f_name]["axis_2"]
		dot_size	= self.yam[f_name]["dot_size"]
		color		= self.yam[f_name]["color"]
		cmap		= self.yam[f_name]["cmap"]
		names		= self.yam[f_name]["names"]
		title		= self.yam[f_name]["title"]
		x11			= self.yam[f_name]["x11"]
		plotfile	= self.yam[f_name]["plotfile"]
		fmt			= self.yam[f_name]["fmt"]

		dio.plot_components_scatter(self.Y, axis_1=axis_1, axis_2=axis_2, dot_size=dot_size, color=color, cmap=cmap, names=names, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

	# ------------------------------------------------------------------
	
	def plot_components_splines(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		n_axis		= self.yam[f_name]["n_axis"]
		v_col		= self.yam[f_name]["v_col"]
		title		= self.yam[f_name]["title"]
		x11			= self.yam[f_name]["x11"]
		plotfile	= self.yam[f_name]["plotfile"]
		fmt			= self.yam[f_name]["fmt"]

		dio.plot_components_splines(self.Y, n_axis=n_axis, v_col=v_col, title=title, x11=x11, plotfile=plotfile, fmt=fmt)



	# ------------------------------------------------------------------
	
	def plot_correlation_matrix(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		
		cmap		= self.yam[f_name]["cmap"]
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']

		dio.plot_correlation_matrix(self.C, cmap=cmap, x11=x11, plotfile=plotfile, fmt=fmt)

	
	# ------------------------------------------------------------------
	
	def plot_var(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		axis_1		= self.yam[f_name]['axis_1']
		axis_2		= self.yam[f_name]['axis_2']
		title		= self.yam[f_name]['title']
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']

		dio.plot_var(self.V, varnames=self.cn, axis_1=axis_1, axis_2=axis_2, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

	# ------------------------------------------------------------------
	
	def plot_eig(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		
		k			= self.yam[f_name]['k']
		frac		= self.yam[f_name]['frac']
		cum			= self.yam[f_name]['cum']
		Log			= self.yam[f_name]['Log']
		dot_size	= self.yam[f_name]['dot_size']
		col			= self.yam[f_name]['col']
		title		= self.yam[f_name]['title']
		pr			= self.yam[f_name]['pr']
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']


		dio.plot_eig(self.L, k=k, frac=frac, cum=cum, Log=Log, dot_size=dot_size, col=col, title=title, pr=pr, x11=x11, plotfile=plotfile, fmt=fmt)

	# ------------------------------------------------------------------
	
	def plot_quality(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		r			= self.yam[f_name]['r']
		cum			= self.yam[f_name]['cum']
		sort		= self.yam[f_name]['sort']
		col			= self.yam[f_name]['col']
		title		= self.yam[f_name]['title']
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']

		dio.plot_quality(self.Qual_axis, self.Qual_cum, r=r, cum=cum, sort=sort, col=col, title=title, x11=x11, plotfile=plotfile, fmt=fmt)
	
	# ------------------------------------------------------------------
	
	def plot_components_heatmap(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		axis_1		= self.yam[f_name]["axis_1"]
		axis_2		= self.yam[f_name]["axis_2"]
		bins		= self.yam[f_name]["bins"]
		cmap		= self.yam[f_name]["cmap"]
		range		= self.yam[f_name]["range"]
		log			= self.yam[f_name]["log"]
		scale		= self.yam[f_name]["scale"]
		title		= self.yam[f_name]['title']
		x11			= self.yam[f_name]['x11']
		imfile		= self.yam[f_name]['imfile']
		fmt			= self.yam[f_name]['fmt']
	
		dio.plot_components_heatmap(self.Y,  axis_1=axis_1, axis_2=axis_2, bins=bins, cmap=cmap, range=range, log=log, scale=scale, title=title, x11=x11, imfile=imfile, fmt=fmt )

	# ------------------------------------------------------------------
	
	def plot_components_quality(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		axis_1		= self.yam[f_name]["axis_1"]
		axis_2		= self.yam[f_name]["axis_2"]
		r			= self.yam[f_name]["r"]
		cmap		= self.yam[f_name]["cmap"]
		diam		= self.yam[f_name]["diam"]
		title		= self.yam[f_name]['title']
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']

		dio.plot_components_quality(self.Y, self.Qual_cum, axis_1=axis_1, axis_2=axis_2, cmap=cmap, diam=diam,  title=title, x11=x11, plotfile=plotfile, fmt=fmt)

	# ------------------------------------------------------------------
	def plot_var_heatmap(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		
		varnames	= self.yam[f_name]["varnames"]
		cmap		= self.yam[f_name]["cmap"]
		title		= self.yam[f_name]['title']
		x11			= self.yam[f_name]['x11']
		plotfile	= self.yam[f_name]['plotfile']
		fmt			= self.yam[f_name]['fmt']
		
		dio.plot_var_heatmap(self.V, varnames=varnames, cmap=cmap, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

	# ------------------------------------------------------------------
	#
	#                                COA
	#
	# ------------------------------------------------------------------
	
	
	def coa(self):
		"""
		""" 
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		
		k			= self.yam[f_name]["k"]
		meth		= self.yam[f_name]["meth"]
		transpose	= self.yam[f_name]["transpose"]

		L, Y_r, Y_c	= dio.coa(self.T, k=k, meth=meth,transpose=transpose)
		self.L   = L
		self.Y_r = Y_r
		self.Y_c = Y_c


	# ------------------------------------------------------------------
	
	def plot_coa(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method

		axis_1		= self.yam[f_name]["axis_1"]
		axis_2		= self.yam[f_name]["axis_2"]
		col_dsize	= self.yam[f_name]["col_dsize"]
		row_dsize	= self.yam[f_name]["row_dsize"]
		row_col		= self.yam[f_name]["row_col"]
		col_col		= self.yam[f_name]["col_col"]
		rownames	= self.yam[f_name]["rownames"]
		colnames	= self.yam[f_name]["colnames"]
		title		= self.yam[f_name]["title"]
		x11			= self.yam[f_name]["x11"]
		plotfile	= self.yam[f_name]["plotfile"]
		fmt			= self.yam[f_name]["fmt"]

		dio.plot_coa(self.Y_r, self.Y_c, axis_1=axis_1, axis_2=axis_2, col_dsize=col_dsize, row_dsize=row_dsize, row_col=row_col, col_col=col_col, rownames=rownames, colnames=rownames, title=title, x11=x11, plotfile=plotfile, fmt=fmt)

	#-------------------------------------------------------------------
	#
	#				 writing a file
	#
	# ------------------------------------------------------------------
	
	'''
	#def writefile(self):
		"""
		"""
		f_name	= sys._getframe().f_code.co_name 		# name of the method
		matrices = {'coa_or_pca_L' : 'L', 'coa_Y_r' : 'Y_r', 'coa_Y_c' : 'Y_c',
				'pca_or_mds_Y' : 'Y', 'pca_V' : 'V', 'mds_S': 'S'}
		matrix		= self.yam[f_name]['matrix']
		filename	= self.yam[f_name]['filename']
		fmt			= self.yam[f_name]['fmt']
		delimiter	= self.yam[f_name]["delimiter"]
		
		rownames	= self.yam[f_name]["rownames"]
		colnames	= self.yam[f_name]["colnames"]
		datasetname	= self.yam[f_name]["datasetname"]
		np_fmt		= self.yam[f_name]["np_fmt"]
		dtype		= self.yam[f_name]["dtype"]
		
		if delimiter.upper() == 'TAB': delimiter = '\t'

		matrix = getattr(self, matrices[matrix])

		print(f'{matrix=}')

		dio.writefile(matrix, filename, fmt=fmt, delimiter=delimiter, colnames=colnames, rownames=rownames, datasetname=datasetname, np_fmt=np_fmt, dtype=dtype)
    '''


	# ------------------------------------------------------------------
	#
	#          docstrings from pydiodon.py
	#
	# ------------------------------------------------------------------
	
	load_file.__doc__					= dio.load_ascii.__doc__
	load_ascii.__doc__					= dio.load_ascii.__doc__

	coa.__doc__							= dio.coa.__doc__
	mds.__doc__							= dio.mds.__doc__
	pca.__doc__							= dio.pca.__doc__
	get_correlation_matrix.__doc__		= dio.get_correlation_matrix.__doc__
	
	plot_coa.__doc__					= dio.plot_coa.__doc__
	plot_components_heatmap.__doc__		= dio.plot_components_heatmap.__doc__
	plot_components_quality.__doc__		= dio.plot_components_quality.__doc__
	plot_components_scatter.__doc__		= dio.plot_components_scatter.__doc__
	plot_components_splines.__doc__		= dio.plot_components_splines.__doc__
	plot_correlation_matrix.__doc__		= dio.plot_correlation_matrix.__doc__
	plot_quality.__doc__ 				= dio.plot_quality.__doc__
	plot_eig.__doc__					= dio.plot_eig.__doc__
	plot_var.__doc__					= dio.plot_var.__doc__
	plot_var_heatmap.__doc__			= dio.plot_var_heatmap.__doc__


# ======================================================================
#
#		end of diolib
#
# ======================================================================
