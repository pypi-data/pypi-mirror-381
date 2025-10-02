"""
SimuladorBohr - energy.py
-----------------

Funciones para calcular las energías de los niveles electrónicos
en el modelo atómico de Bohr.
"""

from .constants import H, E_CHARGE, M_E, EPSILON_0

def energy_joule(n: int, Z: int = 1) -> float:
    """
    Calcula la energía del nivel n en julios (J).
    E_n = - (M_E * e^4 * Z^2) / (8 * ε0^2 * h^2 * n^2)
    """
    if n < 1:
        raise ValueError("El número cuántico principal n debe ser >= 1.")
    return - (M_E * E_CHARGE**4 * Z**2) / (8 * EPSILON_0**2 * H**2 * n**2)

def energy_ev(n: int, Z: int = 1) -> float:
    """Calcula la energía del nivel n en electronvoltios (eV)."""
    return energy_joule(n, Z) / E_CHARGE

def summary(Z: int = 1, max_n: int = 5):
    """
    Genera un diccionario con {n: (E_J, E_eV)} para los primeros niveles.
    """
    return {n: (energy_joule(n, Z), energy_ev(n, Z)) for n in range(1, max_n+1)}

if __name__ == "__main__":
    for n, (EJ, EV) in summary(Z=1, max_n=5).items():
        print(f"n={n}: {EJ:.3e} J  |  {EV:.3f} eV")
