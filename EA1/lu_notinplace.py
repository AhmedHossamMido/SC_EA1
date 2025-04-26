import numpy as np
import memray
from scipy.linalg import lu_factor, lu

n = 4096  # Matrixgröße (4096x4096) => relativ große Matrix
rng = np.random.default_rng(seed=123)
A = rng.random((n, n))  # Erzeuge Zufallsmatrix

# Speichermessung nur innerhalb der LU-Funktion
with memray.Tracker("lu_notinplace.bin", native_traces=True):
    lu(A, overwrite_a=False)
