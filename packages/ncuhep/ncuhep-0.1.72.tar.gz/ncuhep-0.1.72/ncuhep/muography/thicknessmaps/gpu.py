# gpu.py
import numpy as np

try:
    from numba import cuda
    CUDA_OK = cuda.is_available()
except Exception:
    cuda = None
    CUDA_OK = False

if CUDA_OK:
    from math import tan, sqrt, cos, sin, floor, fabs
    from numba import cuda

    @cuda.jit(device=True, inline=True)
    def _bilinear_sample_gpu(Z, x0, y0, dx, dy, x, y):
        fx = (x - x0) / dx; fy = (y - y0) / dy
        i = int(floor(fx));  j = int(floor(fy))
        nx_ = Z.shape[1]; ny_ = Z.shape[0]
        if i < 0: i = 0
        if j < 0: j = 0
        if i > nx_ - 2: i = nx_ - 2
        if j > ny_ - 2: j = ny_ - 2
        tx = fx - i; ty = fy - j
        z00 = Z[j, i];   z10 = Z[j, i+1]
        z01 = Z[j+1, i]; z11 = Z[j+1, i+1]
        return (1.0-tx)*(1.0-ty)*z00 + tx*(1.0-ty)*z10 + (1.0-tx)*ty*z01 + tx*ty*z11

    @cuda.jit(device=True, inline=True)
    def _projection2cart_gpu(r, tx, ty):
        x_ = tan(tx); y_ = tan(ty); c = r / sqrt(1.0 + x_*x_ + y_*y_)
        return x_ * c, y_ * c, c

    @cuda.jit(device=True, inline=True)
    def _det2earth_gpu(x, y, z, zenith_rad, azimuth_rad):
        ca = cos(azimuth_rad); sa = sin(azimuth_rad)
        cz = cos(zenith_rad);  sz = sin(zenith_rad)
        x_ = ca * x - sa * cz * y + sa * sz * z
        y_ = sa * x + ca * cz * y - ca * sz * z
        z_ = sz * y + cz * z
        return x_, y_, z_

    @cuda.jit(device=True, inline=True)
    def _earth_dir_from_detector_angles_gpu(tx, ty, zenith_rad, azimuth_rad):
        xd, yd, zd = _projection2cart_gpu(1.0, tx, ty)
        xe, ye, ze = _det2earth_gpu(xd, yd, zd, zenith_rad, azimuth_rad)
        return xe, ye, ze

    @cuda.jit(device=True)
    def _ray_length_gpu(Z, x0, y0, dx, dy,
                        x_min, x_max, y_min, y_max,
                        x_det, y_det, z_det,
                        nx, ny, nz,
                        s_max, ds_coarse, eps_bisect, max_bisect):
        s = 1e-6
        x = x_det + s*nx; y = y_det + s*ny; z = z_det + s*nz
        if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max): return 0.0
        h = _bilinear_sample_gpu(Z, x0, y0, dx, dy, x, y)
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

            h = _bilinear_sample_gpu(Z, x0, y0, dx, dy, x, y)
            f = z - h
            crossed = (f <= 0.0) != inside

            if crossed:
                s_left = s; s_right = s_next
                for _ in range(max_bisect):
                    s_mid = 0.5*(s_left + s_right)
                    xm = x_det + s_mid*nx; ym = y_det + s_mid*ny; zm = z_det + s_mid*nz
                    hm = _bilinear_sample_gpu(Z, x0, y0, dx, dy, xm, ym)
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

    @cuda.jit
    def compute_thickness_map_rotated_gpu(Z, x0, y0, dx, dy, z_det,
                                          zenith_rad, det_azimuth_rad,
                                          dem_cos, dem_sin,
                                          THX, THY,
                                          s_max, ds_coarse, eps_bisect, max_bisect,
                                          x_min, x_max, y_min, y_max,
                                          L):
        j, i = cuda.grid(2)
        H = THX.shape[0]; W = THX.shape[1]
        if j >= H or i >= W: return
        thx = THX[j, i]; thy = THY[j, i]
        nx_e, ny_e, nz = _earth_dir_from_detector_angles_gpu(thx, thy, zenith_rad, det_azimuth_rad)
        nx =  nx_e * dem_cos + ny_e * dem_sin
        ny = -nx_e * dem_sin + ny_e * dem_cos
        L[j, i] = _ray_length_gpu(
            Z, x0, y0, dx, dy,
            x_min, x_max, y_min, y_max,
            0.0, 0.0, z_det,
            nx, ny, nz,
            s_max, ds_coarse, eps_bisect, max_bisect
        )

def run_gpu_thickness(Z_host, THX_f, THY_f,
                      x0, y0, dx, dy, z0,
                      theta0, det_azimuth,
                      dem_cos, dem_sin,
                      s_max, ds_coarse, eps_bisect, max_bisect,
                      x_min, x_max, y_min, y_max,
                      gpu_block=(16, 16),
                      prof=None):
    """
    Host wrapper (if CUDA available). Returns L (H,W) ndarray.
    """
    if not CUDA_OK:
        raise RuntimeError("CUDA not available.")
    from numba import cuda as _cuda
    if prof is not None: sect = prof.section("gpu:HtoD"); sect.__enter__()
    Z_d   = _cuda.to_device(np.asarray(Z_host, dtype=np.float64))
    THX_d = _cuda.to_device(np.asarray(THX_f, dtype=np.float64))
    THY_d = _cuda.to_device(np.asarray(THY_f, dtype=np.float64))
    L_d   = _cuda.device_array(THX_d.shape, dtype=np.float64)
    if prof is not None: sect.__exit__(None, None, None)

    H, W = THX_d.shape
    by, bx = gpu_block
    grid = ((H + by - 1)//by, (W + bx - 1)//bx)

    if prof is not None: sectk = prof.section("gpu:kernel"); sectk.__enter__()
    compute_thickness_map_rotated_gpu[grid, (by, bx)](
        Z_d,
        np.float64(x0), np.float64(y0),
        np.float64(dx), np.float64(dy),
        np.float64(z0),
        np.float64(theta0), np.float64(det_azimuth),
        np.float64(dem_cos), np.float64(dem_sin),
        THX_d, THY_d,
        np.float64(s_max), np.float64(ds_coarse),
        np.float64(eps_bisect), np.int32(max_bisect),
        np.float64(x_min), np.float64(x_max),
        np.float64(y_min), np.float64(y_max),
        L_d
    )
    _cuda.synchronize()
    if prof is not None: sectk.__exit__(None, None, None)

    if prof is not None: sectd = prof.section("gpu:DtoH"); sectd.__enter__()
    out = L_d.copy_to_host()
    if prof is not None: sectd.__exit__(None, None, None)
    return out
