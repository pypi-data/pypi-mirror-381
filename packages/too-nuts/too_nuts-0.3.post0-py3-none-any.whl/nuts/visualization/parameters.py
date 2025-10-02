""" Parameters for visuals, mostly sky maps.

.. autosummary::
   :toctree:
   :recursive:

"""

import numpy as np

# North Galactic Pole
alphaG = 192.85948 * np.pi / 180.0
deltaG = 27.12825 * np.pi / 180.0

# North Celestial Pole
lNCP = 122.93192 * np.pi / 180.0

## Precision of the equatorial grid
# num_D = 99.0
# num_A = 199.0
# Precision of the equatorial grid
num_D = 299.0
num_A = 399.0

one_year = 3600.0 * 24.0 * 365.0

# Right ascension and declination grids
Phi_tab = np.arange(0, 2.0 * np.pi + 2.0 * np.pi / num_A, 2.0 * np.pi / num_A)
CosTheta_tab = np.arange(-1.0, 1.0 + 2.0 / num_D, 2.0 / num_D)
Theta_tab_calc = np.zeros(len(CosTheta_tab))
Theta_tab_calc[1:] = np.arccos(CosTheta_tab[:-1])[::-1]
Dec_tab = np.pi / 2.0 - Theta_tab_calc
Alpha_tab, Delta_tab = np.meshgrid(Phi_tab, Dec_tab)
dOmega = 2.0 / num_D * 2.0 * np.pi / num_A  # solid angle bin
