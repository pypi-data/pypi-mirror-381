# binning.py
import numpy as np
from .jacobian import jacobian_array

def _conservative_rebin_jacobian(THX_f, THY_f, Q_f, fine_step_mrad, coarse_step_mrad):
    r_exact = coarse_step_mrad / fine_step_mrad
    r = int(round(r_exact))
    if r <= 0:
        raise ValueError("coarse_step_mrad must be >= fine_step_mrad.")
    if abs(r_exact - r) > 1e-3:
        return None  # -> use general path

    Hf, Wf = Q_f.shape
    Hy = (Hf // r) * r
    Wx = (Wf // r) * r

    trim_y = Hf - Hy
    trim_x = Wf - Wx
    top = trim_y // 2
    left = trim_x // 2
    bottom = Hf - (trim_y - top)
    right = Wf - (trim_x - left)

    THX_f_t = THX_f[top:bottom, left:right]
    THY_f_t = THY_f[top:bottom, left:right]
    Q_f_t   = Q_f[top:bottom, left:right]
    J_f_t   = jacobian_array(THX_f_t, THY_f_t)

    Ny_c = THX_f_t.shape[0] // r
    Nx_c = THX_f_t.shape[1] // r

    def blockify(A): return A.reshape(Ny_c, r, Nx_c, r).transpose(0, 2, 1, 3)

    Q_blk = blockify(Q_f_t)
    J_blk = blockify(J_f_t)

    num = (Q_blk * J_blk).sum(axis=(2, 3))
    den = J_blk.sum(axis=(2, 3))
    Q_c = np.where(den > 0.0, num / den, 0.0)

    theta_x_f = THX_f[0, :]
    theta_y_f = THY_f[:, 0]
    theta_x_f_t = theta_x_f[left:right]
    theta_y_f_t = theta_y_f[top:bottom]
    dxf = (theta_x_f_t[1] - theta_x_f_t[0]) if theta_x_f_t.size > 1 else fine_step_mrad*1e-3
    dyf = (theta_y_f_t[1] - theta_y_f_t[0]) if theta_y_f_t.size > 1 else fine_step_mrad*1e-3

    theta_x_c = theta_x_f_t[0] + (np.arange(Nx_c) * r + 0.5*(r-1)) * dxf
    theta_y_c = theta_y_f_t[0] + (np.arange(Ny_c) * r + 0.5*(r-1)) * dyf
    THX_c, THY_c = np.meshgrid(theta_x_c, theta_y_c, indexing="xy")

    step = float(coarse_step_mrad) * 1e-3
    THX_c = np.round(THX_c / step) * step
    THY_c = np.round(THY_c / step) * step

    return THX_c, THY_c, Q_c

def _bin_results_by_jacobian_general(THX_rad, THY_rad, Q, result_step_mrad):
    step = float(result_step_mrad) * 1e-3  # rad

    x = THX_rad.ravel()
    y = THY_rad.ravel()
    J = jacobian_array(THX_rad, THY_rad).ravel()
    Qf = Q.ravel()

    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()

    kx_min = int(np.ceil((x_min - 0.5*step) / step))
    kx_max = int(np.floor((x_max + 0.5*step) / step))
    ky_min = int(np.ceil((y_min - 0.5*step) / step))
    ky_max = int(np.floor((y_max + 0.5*step) / step))

    x_cent = (np.arange(kx_min, kx_max + 1, dtype=np.int64) * step).astype(np.float64)
    y_cent = (np.arange(ky_min, ky_max + 1, dtype=np.int64) * step).astype(np.float64)

    x_edges = np.concatenate([x_cent - 0.5*step, [x_cent[-1] + 0.5*step]])
    y_edges = np.concatenate([y_cent - 0.5*step, [y_cent[-1] + 0.5*step]])

    H_w  = np.histogram2d(y, x, bins=[y_edges, x_edges], weights=J)[0]
    H_Qw = np.histogram2d(y, x, bins=[y_edges, x_edges], weights=J*Qf)[0]
    tiny = 1e-300
    Q_bin = H_Qw / np.maximum(H_w, tiny)

    THX_c, THY_c = np.meshgrid(x_cent, y_cent, indexing="xy")
    return THX_c, THY_c, Q_bin

def bin_results_jacobian(THX_rad, THY_rad, Q, fine_step_mrad, result_step_mrad,
                         sigma=None, P=None):
    """
    Returns coarse (THX, THY, Q, sigma?, P?), all in radians.
    Integer ratio → conservative block rebin; else → histogram2d.
    For sigma (std): Var = E[σ^2+μ^2]-μ_bin^2.
    """
    out = _conservative_rebin_jacobian(THX_rad, THY_rad, Q, fine_step_mrad, result_step_mrad)
    if out is not None:
        THX_c, THY_c, Q_c = out
        sigma_c = None; P_c = None
        if sigma is not None:
            s_out = _conservative_rebin_jacobian(THX_rad, THY_rad, sigma*sigma + Q*Q, fine_step_mrad, result_step_mrad)
            if s_out is not None:
                _, _, m2 = s_out
                var = np.maximum(m2 - Q_c*Q_c, 0.0)
                sigma_c = np.sqrt(var)
        if P is not None:
            p_out = _conservative_rebin_jacobian(THX_rad, THY_rad, P, fine_step_mrad, result_step_mrad)
            if p_out is not None:
                _, _, P_c = p_out
        return THX_c, THY_c, Q_c, sigma_c, P_c

    THX_c, THY_c, Q_c = _bin_results_by_jacobian_general(THX_rad, THY_rad, Q, result_step_mrad)
    sigma_c = None; P_c = None
    if sigma is not None:
        _, _, m2 = _bin_results_by_jacobian_general(THX_rad, THY_rad, sigma*sigma + Q*Q, result_step_mrad)
        var = np.maximum(m2 - Q_c*Q_c, 0.0)
        sigma_c = np.sqrt(var)
    if P is not None:
        _, _, P_c = _bin_results_by_jacobian_general(THX_rad, THY_rad, P, result_step_mrad)
    return THX_c, THY_c, Q_c, sigma_c, P_c
