
import numpy as np
import memray
from scipy.linalg import lu_factor, lu

n = 4096
rng = np.random.default_rng(seed=123)
A = rng.random((n, n))

with memray.Tracker("lu_inplace.bin", native_traces=True):
    lu(A, overwrite_a=True)
