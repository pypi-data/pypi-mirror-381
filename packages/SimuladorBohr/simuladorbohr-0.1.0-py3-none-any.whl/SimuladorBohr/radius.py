"""
SimuladorBohr - radius.py
-----------------

Funciones para calcular los radios orbitales en el modelo de Bohr.
"""

from .constants import A_0

def orbit_radius(n: int, Z: int = 1) -> float:
    """
    Calcula el radio de la órbita n para un átomo con número atómico Z.
    r_n = A_0 * (n^2 / Z)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1.")
    return A_0 * (n**2 / Z)

def summary(Z: int = 1, max_n: int = 5):
    """Devuelve un diccionario con {n: r_n} para los primeros niveles."""
    return {n: orbit_radius(n, Z) for n in range(1, max_n+1)}

if __name__ == "__main__":
    for n, r in summary(Z=1, max_n=5).items():
        print(f"n={n}: r = {r:.3e} m")

