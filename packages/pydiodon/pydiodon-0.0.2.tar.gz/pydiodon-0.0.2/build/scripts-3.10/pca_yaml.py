#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
af, 
started May 8th, 2021
version 21.05.09
"""

import argparse
import yaml
import pydiodon as dio

### defining the arguments with argparse 

parser = argparse.ArgumentParser(description='')
parser.add_argument('-c', '--config', dest='config', type=str, help='configuration file',required=True)
args		= parser.parse_args()
config		= args.config
configfile	= config + ".yaml"
yam			= yaml.load(open(configfile), Loader=yaml.SafeLoader)

# ------ data set

filename		= yam['filename']
fmt				= yam['fmt']
delimiter		= yam['delimiter']
colnames		= yam['colnames']
rownames		= yam['rownames']
datasetname		= yam['datasetnames']
dtype			= yam['dtype']


# ------ pca()

pca_pretreatment	= yam['pca_pretreatment']
pca_k				= int(yam['pca_k'])
pca_meth			= yam['pca_meth']
pca_correlmat		= yam['pca_correlmat']


# -------- scatter plot Y 

scatY			= yam['scatY']
scatY_n_axis	= int(yam['scatY_n_axis'])
scatY_dot_size	= int(yam['scatY_dot_size'])
scatY_color	= yam['scatY_color']
# scatY_names	= yam['scatY_color']
scatY_title	= yam['scatY_title']
scatY_x11		= yam['scatY_x11']
scatY_plotfile	= yam['scatY_plotfile']
scatY_fmt		= yam['scatY_fmt']


# ------------ heatmap Y

hmY				= yam['hmY']
hmY_axis_1		= int(yam['hmY_axis_1'])
hmY_axis_2		= int(yam['hmY_axis_2'])
hmY_bins		= int(yam['hmY_bins'])
hmY_range		= yam['hmY_range']
hmY_log			= yam['hmY_log']
hmY_scale		= yam['hmY_scale']
hmY_title		= yam['hmY_title']
hmY_x11			= yam['hmY_x11']
hmY_plotfile	= yam['hmY_plotfile']
hmY_fmt			= yam['hmY_fmt']


# ---------- plot eigenvalues

pltL 			= yam['pltL']
eig_frac		= yam['eig_frac']
eig_cum			= yam['eig_cum']
eig_dot_size	= int(yam['eig_dot_size'])
eig_nb_val		= int(yam['eig_nb_val'])
eig_col			= yam['eig_col']
eig_title		= yam['eig_title']
eig_x11			= yam['eig_x11']
eig_plotfile	= yam['eig_plotfile']
eig_fmt			= yam['eig_fmt']


# --------- plot V

pltVar			= yam['pltVar']
var_n_axis		= int(yam['var_n_axis'])
var_varnames	= yam['var_varnames']
var_x11			= yam['var_x11']
var_plotfile	= yam['var_plotfile']
var_fmt			= yam['var_fmt']


# -------- plot correlation matrix

imcorrel		= yam['imcorrel']
corr_x11		= yam['corr_x11']
corr_plotfile	= yam['corr_plotfile']
corr_fmt		= yam['corr_fmt']


# ---------- plotting quality per item

pltQual				= yam['pltQual']
pltQual_r			= int(yam['pltQual_r'])
pltQual_col			= yam['pltQual_col']
pltQual_title		= yam['pltQual_title']
pltQual_x11			= yam['pltQual_x11']
pltQual_plotfile	= yam['pltQual_plotfile']
pltQual_fmt			= yam['pltQual_fmt']




# ----------------------------------------------------------------------
#
#		running ...
#
# ----------------------------------------------------------------------

print("loading file ...")

if rownames and colnames:
	A, rn, cn 	= dio.loadfile(filename, fmt=fmt, rownames=rownames, colnames=colnames)
if not rownames and not colnames:
	A			= dio.loadfile(filename, fmt=fmt, rownames=rownames, colnames=colnames)

# running pca()
Y, L, V, C = dio.pca(A, pretreatment=pca_pretreatment, k=pca_k, meth=pca_meth, correlmat=pca_correlmat)

# scatterplot of the components
if scatY:
	dio.plot_components_scatter(Y, n_axis=scatY_n_axis, dot_size=scatY_dot_size, color=scatY_color, names=[], title=scatY_title, x11=scatY_x11, plotfile=scatY_plotfile, fmt=scatY_fmt)

# heatmap of the components
if hmY:
	dio.plot_components_heatmap(Y, axis_1=hmY_axis_1, axis_2=hmY_axis_2, bins=hmY_bins, range=None, log=hmY_log, scale=hmY_scale, title=hmY_title, x11=hmY_x11, imfile=hmY_plotfile, fmt=hmY_fmt)

# plot of eigenvalues
if pltL:
	dio.plot_eig(L, frac=eig_frac, cum=eig_cum, dot_size=eig_dot_size, nb_val=eig_nb_val, col=eig_col, title=eig_title, x11=eig_x11, plotfile=eig_plotfile, fmt=eig_fmt)

# plot of the correlation circle
if pltVar:
	dio.plot_var(V, varnames=var_varnames, n_axis=var_n_axis, x11=var_x11, plotfile=var_plotfile, fmt=var_fmt)

# plot correlation matrix
if imcorrel:
	dio.plot_correlation_matrix(C, x11=corr_x11, plotfile=corr_plotfile, fmt=corr_fmt)

# plotting quality per item
if pltQual:
	Qual = dio.get_quality_per_item(Y,r=pltQual_r, col=pltQual_col, title=pltQual_title, x11=pltQual_x11, plotfile=pltQual_plotfile, fmt=pltQual_fmt)
	dio.plot_components_quality(Qual, pltQual_r, Y, n_axis=2, cmap="viridis", diam=50, title=None, x11=True, plotfile=None, fmt="png")


