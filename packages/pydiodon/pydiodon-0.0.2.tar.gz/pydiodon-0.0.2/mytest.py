#!/usr/bin/env python3

import sys

sys.path.insert(0, '.')
import pydiodon as dio

filename = "pca_template_withnames.txt"
A, rownames, colnames = dio.loadfile(filename, colnames=True, rownames=True)
print('COLNAMES', colnames, 'ROWNAMES',rownames)
dio.writefile(A, 'dataWithColAndRow.txt', colnames=colnames, rownames=rownames)
