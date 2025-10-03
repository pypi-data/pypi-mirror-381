# dem.py
import numpy as np
from math import floor, fabs
from numba import njit, prange
from .geometry import earth_dir_from_detector_angles

@njit(cache=True, fastmath=True)
def bilinear_sample(Z, x0, y0, dx, dy, x, y):
    fx = (x - x0) / dx
    fy = (y - y0) / dy
    i = int(floor(fx));  j = int(floor(fy))
    if i < 0: i = 0
    if j < 0: j = 0
    nx_ = Z.shape[1]; ny_ = Z.shape[0]
    if i > nx_ - 2: i = nx_ - 2
    if j > ny_ - 2: j = ny_ - 2
    tx = fx - i; ty = fy - j
    z00 = Z[j, i];   z10 = Z[j, i+1]
    z01 = Z[j+1, i]; z11 = Z[j+1, i+1]
    return (1.0-tx)*(1.0-ty)*z00 + tx*(1.0-ty)*z10 + (1.0-tx)*ty*z01 + tx*ty*z11

@njit(cache=True, fastmath=True)
def cumulative_terrain_length(Z, x0, y0, dx, dy,
                              x_min, x_max, y_min, y_max,
                              x_det, y_det, z_det,
                              nx, ny, nz,
                              s_max, ds_coarse, eps_bisect, max_bisect):
    s = 1e-6
    x = x_det + s*nx; y = y_det + s*ny; z = z_det + s*nz
    if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max): return 0.0
    h = bilinear_sample(Z, x0, y0, dx, dy, x, y)
    f_prev = z - h
    inside = (f_prev <= 0.0)
    s_entry = s if inside else 0.0
    total = 0.0

    while s < s_max:
        s_next = s + ds_coarse
        if s_next > s_max: s_next = s_max
        x = x_det + s_next*nx; y = y_det + s_next*ny; z = z_det + s_next*nz

        if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max):
            if inside: total += (s_next - s_entry)
            break

        h = bilinear_sample(Z, x0, y0, dx, dy, x, y)
        f = z - h
        crossed = (f <= 0.0) != inside

        if crossed:
            s_left = s; s_right = s_next
            for _ in range(max_bisect):
                s_mid = 0.5*(s_left + s_right)
                xm = x_det + s_mid*nx; ym = y_det + s_mid*ny; zm = z_det + s_mid*nz
                hm = bilinear_sample(Z, x0, y0, dx, dy, xm, ym)
                fm = zm - hm
                if (fm <= 0.0) != inside: s_right = s_mid
                else:                      s_left = s_mid
                if (s_right - s_left) < 1e-4 or fabs(fm) < eps_bisect:
                    break
            s_cross = 0.5*(s_left + s_right)
            if inside:
                total += (s_cross - s_entry); inside = False
            else:
                s_entry = s_cross;          inside = True
            s = s_next
            continue

        s = s_next

    if inside and s >= s_max: total += (s_max - s_entry)
    return total

@njit(parallel=True, cache=True, fastmath=True)
def compute_thickness_map_rotated_cpu(Z, x0, y0, dx, dy, z_det,
                                      zenith_rad, det_azimuth_rad,
                                      dem_cos, dem_sin,
                                      THX, THY,
                                      s_max, ds_coarse, eps_bisect, max_bisect,
                                      x_min, x_max, y_min, y_max):
    H, W = THX.shape
    L = np.zeros((H, W), dtype=np.float64)
    for j in prange(H):
        for i in range(W):
            thx = THX[j, i]; thy = THY[j, i]
            nx_e, ny_e, nz = earth_dir_from_detector_angles(thx, thy, zenith_rad, det_azimuth_rad)
            nx =  nx_e * dem_cos + ny_e * dem_sin
            ny = -nx_e * dem_sin + ny_e * dem_cos
            L[j, i] = cumulative_terrain_length(
                Z, x0, y0, dx, dy,
                x_min, x_max, y_min, y_max,
                0.0, 0.0, z_det,
                nx, ny, nz,
                s_max, ds_coarse, eps_bisect, max_bisect
            )
    return L
