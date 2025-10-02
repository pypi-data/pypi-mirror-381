# src/SimuladorBohr/constants.py

"""
Módulo: constants
Constantes físicas fundamentales para el modelo de Bohr.

Todas las constantes están en unidades del SI.
Fuente recomendada: CODATA 2018/2022.
"""

import math

# Constantes físicas
PI = math.pi                          # Número pi
EPSILON_0 = 8.8541878128e-12          # Permisividad eléctrica del vacío [F/m]
H = 6.62607015e-34                    # Constante de Planck [J·s]
HBAR = H / (2 * PI)                   # Constante de Planck reducida [J·s]
E_CHARGE = 1.602176634e-19            # Carga elemental [C]
M_E = 9.1093837015e-31                # Masa del electrón [kg]
C = 299792458                         # Velocidad de la luz en el vacío [m/s]
N_A = 6.02214076e23                   # Número de Avogadro [1/mol]
R_INF = 10973731.568160               # Constante de Rydberg [1/m]

# Derivadas útiles
A_0 = (HBAR**2) * (4 * PI * EPSILON_0) / (M_E * E_CHARGE**2)  # Radio de Bohr [m]

if __name__ == "__main__":
    print("Constantes definidas:")
    print(f"Radio de Bohr a0 = {A_0:.3e} m")
    print(f"Constante de Planck h = {H:.3e} J·s")
    print(f"Constante reducida ħ = {HBAR:.3e} J·s")
    print(f"Carga del electrón e = {E_CHARGE:.3e} C")
