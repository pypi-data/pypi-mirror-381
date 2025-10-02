"""
SimuladorBohr - plotting.py
---------------------------

Funciones de visualización del modelo de Bohr:
niveles de energía y órbitas electrónicas.
"""

import matplotlib.pyplot as plt
import numpy as np
from .energy import energy_ev
from .radius import orbit_radius

def plot_energy_levels(Z=1, max_n=6, show=True):
    """Grafica los niveles de energía en eV."""
    ns = list(range(1, max_n+1))
    energies = [energy_ev(n, Z) for n in ns]

    fig, ax = plt.subplots()
    for n, E in zip(ns, energies):
        ax.hlines(E, 0, 1, colors='b', linewidth=2)
        ax.text(1.05, E, f"n={n}, {E:.2f} eV", va="center")
    ax.set_xlim(0, 1.3)
    ax.set_ylabel("Energía (eV)")
    ax.set_title(f"Niveles de energía (Z={Z})")
    ax.invert_yaxis()
    ax.get_xaxis().set_visible(False)

    if show:
        plt.show()
    return fig, ax

def plot_orbits(Z=1, ns=(1,2,3), show=True):
    """Grafica órbitas electrónicas para un conjunto de niveles n."""
    radii = [orbit_radius(n, Z) for n in ns]
    theta = np.linspace(0, 2*np.pi, 400)

    fig, ax = plt.subplots()
    for n, r in zip(ns, radii):
        ax.plot(r*np.cos(theta), r*np.sin(theta), label=f"n={n}, r={r:.2e} m")
    ax.scatter([0],[0], c="red", s=30, label="Núcleo")
    ax.set_aspect("equal", "box")
    ax.legend()
    ax.set_title(f"Órbitas electrónicas (Z={Z})")

    if show:
        plt.show()
    return fig, ax
