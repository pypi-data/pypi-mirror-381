"""
Módulo para cálculos de transiciones electrónicas en el modelo de Bohr.
Incluye funciones para energía, frecuencia y longitud de onda de fotones emitidos/absorbidos.
"""

from .energy import energy_joule
from .constants import H, C, E_CHARGE

def transition_energy_joule(n_i: int, n_f: int, Z: int = 1) -> float:
    return energy_joule(n_f, Z) - energy_joule(n_i, Z)

def transition_energy_ev(n_i: int, n_f: int, Z: int = 1) -> float:
    return abs(transition_energy_joule(n_i, n_f, Z)) / E_CHARGE

def frequency(n_i: int, n_f: int, Z: int = 1) -> float:
    return abs(transition_energy_joule(n_i, n_f, Z)) / H

def wavelength(n_i: int, n_f: int, Z: int = 1) -> float:
    return C / frequency(n_i, n_f, Z)

