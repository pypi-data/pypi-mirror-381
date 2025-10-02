"""
SimuladorBohr
=============
Librería en Python para cálculos y visualización del modelo atómico de Bohr.

Incluye:
- Constantes físicas
- Energías electrónicas
- Radios orbitales
- Transiciones electrónicas
- Funciones de graficación
"""

# Constantes
from .constants import (
    PI, EPSILON_0, H, HBAR, E_CHARGE, M_E, C, N_A, R_INF, A_0
)

# Energías
from .energy import (
    energy_joule, energy_ev, summary
)

# Radios
from .radius import (
    orbit_radius
)

# Transiciones
from .transitions import (
    transition_energy_joule, transition_energy_ev, frequency, wavelength
)

# Gráficas
from .plotting import (
    plot_energy_levels, plot_orbits
)

__all__ = [
    # Constantes
    "PI", "EPSILON_0", "H", "HBAR", "E_CHARGE", "M_E", "C", "N_A", "R_INF", "A_0",
    # Energías
    "energy_joule", "energy_ev", "summary",
    # Radios
    "orbit_radius",
    # Transiciones
    "transition_energy_joule", "transition_energy_ev", "frequency", "wavelength",
    # Gráficas
    "plot_energy_levels", "plot_orbits"
]
