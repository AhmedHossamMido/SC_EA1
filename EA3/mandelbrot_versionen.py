import numba
import numpy as np

# -------------------------------
# Escape-Time-Funktion (Skalar)
# -------------------------------
def escape_time(p, maxiter):
    z = 0j
    for i in range(maxiter):
        z = z*z + p
        if abs(z) > 2:
            return i
    return maxiter

# -------------------------------
# Variante 1: np.vectorize
# -------------------------------
def mandelbrot_set_np_vectorized(P, maxiter):
    vectorized_escape_time = np.vectorize(escape_time)
    return vectorized_escape_time(P, maxiter)

# -------------------------------
# Variante 2: numba.vectorize
# -------------------------------
@numba.vectorize(['int32(complex128, int32)'])
def escape_time_numba(p, maxiter):
    z = 0j
    for i in range(maxiter):
        z = z*z + p
        if abs(z) > 2:
            return i
    return maxiter

def mandelbrot_set_numba_vectorized(P, maxiter):
    return escape_time_numba(P, maxiter)

# -------------------------------
# Variante 3: numba.vectorize mit Parallelisierung
# -------------------------------
@numba.vectorize(['int32(complex128, int32)'], target='parallel')
def escape_time_numba_par(p, maxiter):
    z = 0j
    for i in range(maxiter):
        z = z*z + p
        if abs(z) > 2:
            return i
    return maxiter

def mandelbrot_set_numba_vectorized_par(P, maxiter):
    return escape_time_numba_par(P, maxiter)

# -------------------------------
# Setup: Gitter + Parameter
# -------------------------------
def create_grid():
    real_param = (-1.5, 1.1, 500)  # Weniger Punkte für schnelleres Profiling
    imag_param = (-1.5j, 1.1j, 500)
    XX, YY = np.meshgrid(np.linspace(*real_param), np.linspace(*imag_param))
    return XX + YY

# -------------------------------
# Main: Methoden aufrufen
# -------------------------------
if __name__ == "__main__":
    P = create_grid()
    maxiter = 200

    # Alle Varianten einmal durchlaufen lassen
    mandelbrot_set_np_vectorized(P, maxiter)
    mandelbrot_set_numba_vectorized(P, maxiter)
    mandelbrot_set_numba_vectorized_par(P, maxiter)
