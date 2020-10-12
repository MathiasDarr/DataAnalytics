from pyspark.ml.linalg import DenseVector, SparseVector, DenseMatrix, SparseMatrix
x = [SparseVector(3, {0: 1.0}).toArray()] + \
    [SparseVector(3, {1: 1.0}).toArray()] + \
    [SparseVector(3, {0: 1.0}).toArray()]

import numpy as np
np.array(x)