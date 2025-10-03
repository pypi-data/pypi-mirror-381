import numpy as np
from numba import njit
from .constants import P1, P2, P3, P4, P5, CM2_TO_M2

@njit(cache=True, fastmath=True)
def cos_theta_star(theta_rad):
    c = np.cos(theta_rad)
    if c > 1.0: c = 1.0
    elif c < -1.0: c = -1.0
    num = c*c + P1*P1 + P2*(c**P3) + P4*(c**P5)
    den = 1.0 + P1*P1 + P2 + P4
    val = num / den
    if val < 0.0: val = 0.0
    return np.sqrt(val)

@njit(cache=True, fastmath=True)
def dphi0_dE(theta_rad, E_GeV):
    if E_GeV <= 0.0: return 0.0
    cst   = cos_theta_star(theta_rad)
    x     = E_GeV
    core  = x * (1.0 + 3.64 / (x * (cst**1.29)))
    spec  = 0.14 * (core ** (-2.7))
    dem_pi = 1.0 + 1.1 * x * cst / 115.0
    dem_K  = 1.0 + 1.1 * x * cst / 850.0
    return (spec * ((1.0 / dem_pi) + 0.054 / dem_K)) * CM2_TO_M2
