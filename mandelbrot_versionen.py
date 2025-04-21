
import numba
import numpy as np

def escape_time(p, maxiter):
    z = 0j
    for i in range(maxiter):
        z = z*z + p
        if abs(z) > 2:
            return i
    return maxiter

def mandelbrot_set_np_vectorized(P, maxiter):
    vectorized_escape_time = np.vectorize(escape_time)
    return vectorized_escape_time(P, maxiter)

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

# Gitter erstellen (kleiner für Profiling-Zwecke)
real_param = (-1.5, 1.1, 300)
imag_param = (-1.5j, 1.1j, 300)
XX, YY = np.meshgrid(np.linspace(*real_param), np.linspace(*imag_param))
P = XX + YY
maxiter = 200

# alle drei Varianten EINMAL aufrufen
mandelbrot_set_np_vectorized(P, maxiter)
mandelbrot_set_numba_vectorized(P, maxiter)
mandelbrot_set_numba_vectorized_par(P, maxiter)
