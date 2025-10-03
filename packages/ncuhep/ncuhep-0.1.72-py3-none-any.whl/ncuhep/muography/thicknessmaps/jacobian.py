# jacobian.py
import numpy as np
from numba import njit

@njit(cache=True, fastmath=True)
def jacobian_slope(theta_x, theta_y):
    cx = np.cos(theta_x); cy = np.cos(theta_y)
    tx = np.tan(theta_x); ty = np.tan(theta_y)
    sec2x = 1.0/(cx*cx); sec2y = 1.0/(cy*cy)
    return (sec2x*sec2y) / np.power(1.0 + tx*tx + ty*ty, 1.5)

def jacobian_array(THX, THY):
    return jacobian_slope(THX, THY)
