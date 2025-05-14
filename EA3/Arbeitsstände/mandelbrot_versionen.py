
import numpy as np  # Importiert das numpy-Modul für numerische Berechnungen
import numba  # Importiert das numba-Modul für JIT-Kompilierung und Parallelisierung

# Funktion zur Berechnung der "Escape-Time" für einen Punkt p im Mandelbrot-Set
def escape_time(p, maxiter):
    z = 0j  # Startwert (Komplexe Zahl 0)
    for i in range(maxiter):  # Schleife bis zur maximalen Iterationsanzahl
        z = z*z + p  # Berechne den nächsten Punkt im Iterationsprozess
        if abs(z) > 2:  # Wenn der Betrag von z größer als 2 wird, verlässt der Punkt das Mandelbrot-Set
            return i  # Gib die Anzahl der Iterationen bis zum Verlassen zurück
    return maxiter  # Wenn der Punkt das Set nicht verlässt, gebe die maximale Iterationsanzahl zurück

# Vektorisiertes Mandelbrot-Set mit numpy (nicht parallelisiert)
def mandelbrot_set_np_vectorized(P, maxiter):
    vectorized_escape_time = np.vectorize(escape_time)  # Vektorisiere die escape_time Funktion
    return vectorized_escape_time(P, maxiter)  # Berechne das Mandelbrot-Set für alle Punkte in P

# Funktion zur Berechnung der Escape-Time mit numba für bessere Performance
@numba.vectorize(['int32(complex128, int32)'])  # Dekorator für numba, der den Code für die JIT-Kompilierung vorbereitet
def escape_time_numba(p, maxiter):
    z = 0j  # Startwert (Komplexe Zahl 0)
    for i in range(maxiter):  # Schleife bis zur maximalen Iterationsanzahl
        z = z*z + p  # Berechne den nächsten Punkt im Iterationsprozess
        if abs(z) > 2:  # Wenn der Betrag von z größer als 2 wird, verlässt der Punkt das Mandelbrot-Set
            return i  # Gib die Anzahl der Iterationen zurück
    return maxiter  # Wenn der Punkt das Set nicht verlässt, gebe die maximale Iterationsanzahl zurück

# Vektorisiertes Mandelbrot-Set mit numba (JIT-Kompilierung)
def mandelbrot_set_numba_vectorized(P, maxiter):
    return escape_time_numba(P, maxiter)  # Berechne das Mandelbrot-Set für alle Punkte in P mit numba

# Funktion zur Berechnung der Escape-Time mit numba und Parallelisierung für bessere Performance
@numba.vectorize(['int32(complex128, int32)'], target='parallel')  # Dekorator für numba, parallelisierte Berechnung
def escape_time_numba_par(p, maxiter):
    z = 0j  # Startwert (Komplexe Zahl 0)
    for i in range(maxiter):  # Schleife bis zur maximalen Iterationsanzahl
        z = z*z + p  # Berechne den nächsten Punkt im Iterationsprozess
        if abs(z) > 2:  # Wenn der Betrag von z größer als 2 wird, verlässt der Punkt das Mandelbrot-Set
            return i  # Gib die Anzahl der Iterationen zurück
    return maxiter  # Wenn der Punkt das Set nicht verlässt, gebe die maximale Iterationsanzahl zurück

# Vektorisiertes Mandelbrot-Set mit numba und Parallelisierung
def mandelbrot_set_numba_vectorized_par(P, maxiter):
    return escape_time_numba_par(P, maxiter)  # Berechne das Mandelbrot-Set für alle Punkte in P mit numba (parallel)

# Erstelle ein Gitter von komplexen Zahlen für die Berechnung des Mandelbrot-Sets
real_param = (-1.5, 1.1, 300)  # Bereich für die realen Teile der komplexen Zahlen
imag_param = (-1.5j, 1.1j, 300)  # Bereich für die imaginären Teile der komplexen Zahlen
XX, YY = np.meshgrid(np.linspace(*real_param), np.linspace(*imag_param))  # Erstelle das Gitter
P = XX + YY  # Kombiniere reale und imaginäre Teile zu komplexen Zahlen
maxiter = 200  # Setze die maximale Anzahl der Iterationen auf 200

# Rufe die drei Varianten der Mandelbrot-Berechnung einmal auf (keine Ausgabe erzeugen)
mandelbrot_set_np_vectorized(P, maxiter)  # Berechnung mit numpy-Vektorisierung
mandelbrot_set_numba_vectorized(P, maxiter)  # Berechnung mit numba-Vektorisierung
mandelbrot_set_numba_vectorized_par(P, maxiter)  # Berechnung mit numba-Vektorisierung und Parallelisierung
