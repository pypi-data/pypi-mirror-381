# SimuladorBohr

SimuladorBohr es una librería en Python para realizar cálculos y visualización del modelo atómico de Bohr.  
Incluye funciones para niveles de energía, radios orbitales, transiciones electrónicas y representaciones gráficas.

## Autores
Daniel Felipe Ramirez – dfrc5528@gmail.com

Santiago Criollo Bermudez – santicriollo@hotmail.com

Alexei Duran – amidamarulas@gmail.com

## Propósito

El objetivo de esta librería es proporcionar una herramienta educativa y de apoyo para el estudio del modelo atómico de Bohr.  
Permite calcular energías en diferentes unidades, radios de órbitas electrónicas, características de transiciones y generar gráficas ilustrativas.

## Instalación

Clonar el repositorio e instalar en modo editable:

```bash
git clone https://github.com/amidamarulas/SimuladorBohr.git
cd SimuladorBohr
pip install -e .
```

Instalación de libreria

```bash
pip install SimuladorBohr
```

## Uso básico

Importar las funciones principales del paquete:

```bash
from SimuladorBohr.energy import energy_ev
from SimuladorBohr.radius import orbit_radius
from SimuladorBohr.transitions import wavelength
```

## Ejemplos

Calculo de la energía de un nivel

```bash
from SimuladorBohr.energy import energy_ev
print("Energía n=1:", energy_ev(1), "eV")
```

Radio de la órbita

from SimuladorBohr.radius import orbit_radius
print("Radio de la órbita n=2:", orbit_radius(2), "m")

```bash
from SimuladorBohr.radius import orbit_radius
print("Radio de la órbita n=2:", orbit_radius(2), "m")
```

Longitud de onda de una transición
```bash
from SimuladorBohr.transitions import wavelength
print("Transición 3 → 2:", wavelength(3,2)*1e9, "nm")
```

Ejemplo completo
```bash
from SimuladorBohr.energy import energy_ev
from SimuladorBohr.radius import orbit_radius
from SimuladorBohr.transitions import transition_energy_ev, wavelength, frequency
from SimuladorBohr.plotting import plot_energy_levels, plot_orbits

Z = 1  # Hidrógeno
for n in range(1,5):
    print(f"n={n}: E = {energy_ev(n, Z):.3f} eV, r = {orbit_radius(n):.2e} m")

dE = transition_energy_ev(3,2,Z)
lam = wavelength(3,2,Z)
nu = frequency(3,2,Z)
print(f"ΔE = {dE:.3f} eV, λ = {lam*1e9:.2f} nm, ν = {nu:.2e} Hz")

plot_energy_levels(Z, max_n=6)
plot_orbits(Z, ns=[1,2,3])
```