#!/usr/bin/env python3

import sys
sys.path.append("../")
import pydiodon as dio
import numpy as np

epsi		= 1e-6
failures	= ["none"]

# ----------------------------------------------------------------------
#
#				 tests
#
# ----------------------------------------------------------------------

def test_center_col():
	"""
	"""
	n = 4 ; p = 3
	A = np.arange(n*p)
	A.shape=(n,p)
	Ac, m = dio.center_col(A)
	#
	m_exp	= np.array([4.5, 5.5, 6.5], dtype=float)
	Ac_exp	= np.array([[-4.5, -4.5, -4.5],[-1.5, -1.5, -1.5],[1.5, 1.5, 1.5],[4.5,4.5,4.5]], dtype=float)
	#
	Delta_Ac	= np.max(np.abs(Ac-Ac_exp))
	Delta_m		= np.max(np.abs(m - m_exp))
	#
	Delta 		= np.maximum(Delta_Ac,Delta_m)
	assert Delta < epsi
	#
"""
	if Delta < epsi:
		print("test on center_col(): success")
		return True
	else:
		print("test on center_col(): failed")
		return False
"""

# ----------------------------------------------------------------------

def test_center_row():
	"""
	"""
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
	"""
	if Delta < epsi:
		print("test on center_row(): success")
		return True
	else:
		print("test on center_row(): ailed")
		return False
	"""
	assert Delta < epsi

# ----------------------------------------------------------------------
#
#			running tests
#
# ----------------------------------------------------------------------

test_center_col()
test_center_row()


