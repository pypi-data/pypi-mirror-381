import math
import numpy as np
from numba import njit

@njit(cache=True, fastmath=True)
def slope_to_sph(theta_x, theta_y):
    tx = np.tan(theta_x); ty = np.tan(theta_y)
    r  = np.sqrt(tx*tx + ty*ty)
    return np.arctan(r), np.arctan2(ty, tx)

@njit(cache=True, fastmath=True)
def det_to_earth_z(nx, ny, nz, zenith_rad, azimuth_rad):
    # (azimuth is not used in this simplified rotation: tilt about x-axis toward +y)
    z_ = math.sin(zenith_rad) * ny + math.cos(zenith_rad) * nz
    return z_

@njit(cache=True, fastmath=True)
def earth_zenith_from_det_vec(nx, ny, nz, zenith_rad, azimuth_rad):
    zE = det_to_earth_z(nx, ny, nz, zenith_rad, azimuth_rad)
    if zE > 1.0: zE = 1.0
    elif zE < -1.0: zE = -1.0
    return math.acos(zE)  # θ_Earth

@njit(cache=True, fastmath=True)
def J_source(theta_x, theta_y):
    cx = np.cos(theta_x); cy = np.cos(theta_y)
    if cx == 0.0 or cy == 0.0: return 0.0
    tx = np.tan(theta_x); ty = np.tan(theta_y)
    sec2x = 1.0/(cx*cx);  sec2y = 1.0/(cy*cy)
    return (sec2x * sec2y) / np.power(1.0 + tx*tx + ty*ty, 1.5)

def grid_steps(THX: np.ndarray, THY: np.ndarray):
    dthx = float(np.median(np.diff(THX[0, :]))) if THX.shape[1] > 1 else 1.0
    dthy = float(np.median(np.diff(THY[:, 0]))) if THY.shape[0] > 1 else 1.0
    return abs(dthx), abs(dthy)
