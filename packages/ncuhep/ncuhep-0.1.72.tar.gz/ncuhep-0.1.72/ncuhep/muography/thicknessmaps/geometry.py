# geometry.py
import numpy as np
from numba import njit

@njit(cache=True)
def projection2cart(r, theta_x_rad, theta_y_rad):
    x_ = np.tan(theta_x_rad)
    y_ = np.tan(theta_y_rad)
    c = r / np.sqrt(1.0 + x_**2 + y_**2)
    return x_ * c, y_ * c, c

@njit(cache=True)
def det2earth(x, y, z, zenith_rad, azimuth_rad):
    # azimuth: clockwise from North (0°=North, 90°=East)
    ca = np.cos(azimuth_rad); sa = np.sin(azimuth_rad)
    cz = np.cos(zenith_rad);  sz = np.sin(zenith_rad)
    x_ = ca * x - sa * cz * y + sa * sz * z
    y_ = sa * x + ca * cz * y - ca * sz * z
    z_ = sz * y + cz * z
    return x_, y_, z_

@njit(cache=True, fastmath=True)
def earth_dir_from_detector_angles(theta_x_rad, theta_y_rad, zenith_rad, azimuth_rad):
    xd, yd, zd = projection2cart(1.0, theta_x_rad, theta_y_rad)
    xe, ye, ze = det2earth(xd, yd, zd, zenith_rad, azimuth_rad)
    return xe, ye, ze  # ENU
