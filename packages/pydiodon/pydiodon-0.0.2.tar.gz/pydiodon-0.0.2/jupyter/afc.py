#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pydiodon as dio

A, rownames, colnames = dio.load_dataset("guiana_trees")

L, Y_r, Y_c = dio.coa(A)

dio.plot_coa(Y_r, Y_c,colnames=colnames) 
