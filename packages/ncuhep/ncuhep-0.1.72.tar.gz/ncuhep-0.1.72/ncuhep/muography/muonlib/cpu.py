import math
import numpy as np
from numba import njit, prange

from .angles import slope_to_sph, earth_zenith_from_det_vec, J_source
from .models import P_S_from_x_m, Theta_sigma, Theta_crit
from .flux import dphi0_dE

# ---------------- fast tanh approx ----------------
@njit(inline='always', cache=True, fastmath=True)
def _tanh_rational(x):
    # Stable, cheap: tanh(x) ~ x * (27 + x^2) / (27 + 9 x^2)
    # Clamp for large |x| to avoid loss of significance
    if x > 8.0:
        return 1.0
    elif x < -8.0:
        return -1.0
    xx = x * x
    return (x * (27.0 + xx)) / (27.0 + 9.0 * xx)

@njit(inline='always', cache=True, fastmath=True)
def _blend(theta, theta0, sigma, approx_tanh):
    s = 1.0e-16 if sigma < 1.0e-16 else sigma
    u = (theta - theta0) / (5.0 * s)
    t = _tanh_rational(u) if approx_tanh else math.tanh(u)
    return 0.5 * (1.0 + t)

@njit(inline='always', cache=True, fastmath=True)
def _gauss_core(theta, sigma):
    s = 1.0e-16 if sigma < 1.0e-16 else sigma
    x = theta / s
    return math.exp(-0.5 * x * x)

@njit(inline='always', cache=True, fastmath=True)
def _tail(theta, sigma, theta0):
    s = 1.0e-16 if sigma < 1.0e-16 else sigma
    G0 = math.exp(-0.5 * (theta0/s) * (theta0/s))
    return G0 * math.exp(-(theta - theta0) / s)

@njit(inline='always', cache=True, fastmath=True)
def _M_unnorm(theta, sigma, theta0, approx_tanh):
    G = _gauss_core(theta, sigma)
    T = _tail(theta, sigma, theta0)
    w = _blend(theta, theta0, sigma, approx_tanh)
    return (1.0 - w) * G + w * T

@njit(cache=True, fastmath=True)
def _norm_area_2pi_theta_local(sigma, theta0, ngrid_norm, approx_tanh):
    # Trapezoid integrate 2π ∫ theta * M(theta) dtheta, with safeguards (full area)
    sg = sigma
    t0 = theta0
    tmax = t0 + 10.0 * sg
    if tmax < 0.2:
        tmax = 0.2
    elif tmax > 2.0:
        tmax = 2.0

    two_pi = 2.0 * math.pi
    npts = ngrid_norm if ngrid_norm > 2 else 2048
    area = 0.0
    prev_t = 0.0
    prev_v = two_pi * prev_t * _M_unnorm(prev_t, sg, t0, approx_tanh)
    for k in range(1, npts):
        t = (tmax * k) / (npts - 1.0)
        v = two_pi * t * _M_unnorm(t, sg, t0, approx_tanh)
        area += 0.5 * (v + prev_v) * (t - prev_t)
        prev_t = t
        prev_v = v
    if area < 1e-300:
        area = 1e-300
    return area

@njit(cache=True, fastmath=True)
def _cut_area_2pi_theta_local(sigma, theta0, rcut, ngrid_norm, approx_tanh):
    """2π ∫_0^{rcut} θ M(θ) dθ via trapezoid, consistent with kernels."""
    two_pi = 2.0 * math.pi
    npts = ngrid_norm if ngrid_norm > 2 else 2048
    area = 0.0
    prev_t = 0.0
    prev_v = two_pi * prev_t * _M_unnorm(prev_t, sigma, theta0, approx_tanh)
    for k in range(1, npts):
        t = (rcut * k) / (npts - 1.0)
        v = two_pi * t * _M_unnorm(t, sigma, theta0, approx_tanh)
        area += 0.5 * (v + prev_v) * (t - prev_t)
        prev_t = t
        prev_v = v
    if area < 1e-300:
        area = 1e-300
    return area

# ---------------- vector/angle helpers ----------------
@njit(parallel=True, cache=True, fastmath=True)
def angles_from_grid(THX, THY):
    H, W = THX.shape
    TH = np.empty_like(THX)
    PH = np.empty_like(THX)
    for j in prange(H):
        for i in range(W):
            th, ph = slope_to_sph(THX[j, i], THY[j, i])
            TH[j, i] = th
            PH[j, i] = ph
    return TH, PH

@njit(parallel=True, cache=True, fastmath=True)
def unit_vectors_from_angles(TH, PH):
    H, W = TH.shape
    nx = np.empty_like(TH)
    ny = np.empty_like(TH)
    nz = np.empty_like(TH)
    for j in prange(H):
        for i in range(W):
            th = TH[j, i]; ph = PH[j, i]
            s = np.sin(th); c = np.cos(th)
            nx[j, i] = s * np.cos(ph)
            ny[j, i] = s * np.sin(ph)
            nz[j, i] = c
    return nx, ny, nz

# ---------------- precompute fields (CPU) ----------------
@njit(parallel=True, cache=True, fastmath=True)
def precompute_source_fields(E_GeV, THX, THY, Xeff_m, ngrid_norm,
                             det_zenith_rad, det_azimuth_rad, approx_tanh=False):
    H, W = THX.shape
    thetaS = np.empty_like(THX); phiS   = np.empty_like(THX)
    nxS    = np.empty_like(THX); nyS    = np.empty_like(THX); nzS = np.empty_like(THX)
    Jsrc   = np.empty_like(THX); phi0   = np.empty_like(THX)
    Ps     = np.empty_like(THX); sigma  = np.empty_like(THX); theta0 = np.empty_like(THX)
    Anorm  = np.empty_like(THX)

    for j in prange(H):
        for i in range(W):
            thS, phS = slope_to_sph(THX[j, i], THY[j, i])
            thetaS[j, i] = thS; phiS[j, i] = phS
            s = np.sin(thS); c = np.cos(thS)
            nx = s * np.cos(phS); ny = s * np.sin(phS); nz = c
            nxS[j, i] = nx; nyS[j, i] = ny; nzS[j, i] = nz

            Jsrc[j, i] = J_source(THX[j, i], THY[j, i])

            thEarth = earth_zenith_from_det_vec(nx, ny, nz, det_zenith_rad, det_azimuth_rad)
            phi0[j, i] = dphi0_dE(thEarth, E_GeV)

            x_eff_m     = Xeff_m[j, i]
            Ps[j, i]    = P_S_from_x_m(E_GeV, x_eff_m)
            sg          = Theta_sigma(E_GeV, x_eff_m)
            t0          = Theta_crit(E_GeV, x_eff_m)
            sigma[j, i]  = sg
            theta0[j, i] = t0
            # Local area to honor approx_tanh choice:
            Anorm[j, i]  = _norm_area_2pi_theta_local(sg, t0, ngrid_norm, approx_tanh)

    return thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm

# ---------------- splat (CPU, fast approximate) ----------------
@njit(parallel=True, cache=True, fastmath=True)
def splat_cpu_vec(
    nxD, nyD, nzD,
    nxS, nyS, nzS,
    Jsrc, phi0, Ps, sigma, theta0, Anorm,
    dthx, dthy, five_sigma, min_rcut, rcut_floor,
    approx_tanh=False
):
    H, W = nxD.shape
    Z = np.zeros((H, W), dtype=nxD.dtype)
    for js in prange(H):
        for is_ in range(W):
            base_phi0 = phi0[js, is_]; base_Ps = Ps[js, is_]; base_J = Jsrc[js, is_]
            if base_phi0 <= 0.0 or base_Ps <= 0.0 or base_J <= 0.0:
                continue

            s = sigma[js, is_]; t0 = theta0[js, is_]; A = Anorm[js, is_]
            if A <= 0.0:
                continue

            rcut_phys = five_sigma * s
            pix_halfdiag = 0.5 * math.hypot(dthx, dthy)
            rcut = rcut_phys
            floor_px = rcut_floor * pix_halfdiag
            if rcut < floor_px: rcut = floor_px
            if rcut < min_rcut: rcut = min_rcut

            ixr = int(rcut / dthx) + 1
            jyr = int(rcut / dthy) + 1

            sx = nxS[js, is_]; sy = nyS[js, is_]; sz = nzS[js, is_]
            base = base_phi0 * base_Ps * base_J

            j0 = js - jyr;  j0 = 0 if j0 < 0 else j0
            j1 = js + jyr;  j1 = (H - 1) if j1 > H - 1 else j1
            i0 = is_ - ixr; i0 = 0 if i0 < 0 else i0
            i1 = is_ + ixr; i1 = (W - 1) if i1 > W - 1 else i1

            for jd in range(j0, j1 + 1):
                for id_ in range(i0, i1 + 1):
                    dotv = nxD[jd, id_] * sx + nyD[jd, id_] * sy + nzD[jd, id_] * sz
                    val = 2.0 * (1.0 - dotv)
                    if val < 0.0:
                        val = 0.0
                    gamma = math.sqrt(val)
                    if gamma > rcut:
                        continue
                    sclip = 1.0e-16 if s < 1.0e-16 else s
                    x = gamma / sclip
                    G  = math.exp(-0.5 * x * x)
                    G0 = math.exp(-0.5 * (t0/sclip) * (t0/sclip))
                    T  = G0 * math.exp(-(gamma - t0)/sclip)
                    w  = _blend(gamma, t0, sclip, approx_tanh)
                    Munn = (1.0 - w) * G + w * T
                    Z[jd, id_] += base * (Munn / A) * dthx * dthy
    return Z

# ---------------- helpers for conservative CPU path ----------------
@njit(inline='always', cache=True, fastmath=True)
def _nxny_from_slopes(thx, thy):
    tx = math.tan(thx); ty = math.tan(thy)
    r = math.sqrt(tx*tx + ty*ty)
    th = math.atan(r)
    ph = math.atan2(ty, tx) if (tx != 0.0 or ty != 0.0) else 0.0
    s = math.sin(th); c = math.cos(th)
    return s * math.cos(ph), s * math.sin(ph), c

@njit(cache=True, fastmath=True)
def _supersample_pixel_gamma(
    thx_center, thy_center, dthx, dthy, ssaa,
    sx, sy, sz
):
    """
    Average gamma over a pixel by uniform ssaa x ssaa sub-samples.
    Returns the mean gamma; caller evaluates M at that representative gamma.
    """
    if ssaa <= 1:
        nx, ny, nz = _nxny_from_slopes(thx_center, thy_center)
        dotv = nx*sx + ny*sy + nz*sz
        val = 2.0 * (1.0 - dotv)
        if val < 0.0: val = 0.0
        return math.sqrt(val)

    inv = 1.0 / ssaa
    acc = 0.0
    for uy in range(ssaa):
        fy = (uy + 0.5) * inv - 0.5
        thy = thy_center + fy * dthy
        for ux in range(ssaa):
            fx = (ux + 0.5) * inv - 0.5
            thx = thx_center + fx * dthx
            nx, ny, nz = _nxny_from_slopes(thx, thy)
            dotv = nx*sx + ny*sy + nz*sz
            val = 2.0 * (1.0 - dotv)
            if val < 0.0: val = 0.0
            acc += math.sqrt(val)
    return acc * (inv * inv)

@njit(cache=True, fastmath=True)
def _pick_ssaa_for_pixel(s, dth_diag, tol, ssaa_min, ssaa_max):
    """
    Heuristic selector for supersampling level.
    Increases SSAA as 5*sigma shrinks relative to pixel diagonal.
    """
    five_s = 5.0 * s
    if five_s > 3.0 * dth_diag:
        return ssaa_min
    ratio = (3.0 * dth_diag) / max(1e-16, five_s)
    base = int(math.ceil(ssaa_min * ratio))
    if base < ssaa_min: base = ssaa_min
    if base > ssaa_max: base = ssaa_max
    return base

# ---------------- conservative CPU path ----------------
@njit(parallel=True, cache=True, fastmath=True)
def splat_cpu_conservative(
    THX, THY,               # detector slope-angle grids (H,W) [radians]
    nxD, nyD, nzD,          # destination unit vectors
    nxS, nyS, nzS,          # source unit vectors
    Jsrc, phi0, Ps, sigma, theta0, Anorm,
    dthx, dthy, five_sigma, min_rcut, rcut_floor,
    approx_tanh,
    ngrid_norm,             # for area integrals
    conserve_within_nsigma, # e.g., 5.0
    conservation_tol,       # e.g., 0.01 (1%)
    ssaa_min, ssaa_max
):
    H, W = nxD.shape
    Z = np.zeros((H, W), dtype=nxD.dtype)
    two_pi = 2.0 * math.pi
    pix_halfdiag = 0.5 * math.hypot(dthx, dthy)

    for js in prange(H):
        for is_ in range(W):
            base_phi0 = phi0[js, is_]; base_Ps = Ps[js, is_]; base_J = Jsrc[js, is_]
            if base_phi0 <= 0.0 or base_Ps <= 0.0 or base_J <= 0.0:
                continue

            s = sigma[js, is_]; t0 = theta0[js, is_]; A = Anorm[js, is_]
            if A <= 0.0:
                continue

            rcut_phys = five_sigma * s
            rcut_nsig = conserve_within_nsigma * s
            if rcut_nsig < rcut_phys:
                rcut_phys = rcut_nsig

            rcut = rcut_phys
            floor_px = rcut_floor * pix_halfdiag
            if rcut < floor_px: rcut = floor_px
            if rcut < min_rcut: rcut = min_rcut

            ixr = int(rcut / dthx) + 1
            jyr = int(rcut / dthy) + 1

            sx = nxS[js, is_]; sy = nyS[js, is_]; sz = nzS[js, is_]
            base = base_phi0 * base_Ps * base_J

            # continuous target area within rcut
            A_cut = _cut_area_2pi_theta_local(s, t0, rcut, ngrid_norm, approx_tanh)

            # PASS 1: measure discrete sum with adaptive SSAA per pixel
            S = 0.0
            j0 = js - jyr;  j0 = 0 if j0 < 0 else j0
            j1 = js + jyr;  j1 = (H - 1) if j1 > H - 1 else j1
            i0 = is_ - ixr; i0 = 0 if i0 < 0 else i0
            i1 = is_ + ixr; i1 = (W - 1) if i1 > W - 1 else i1

            for jd in range(j0, j1 + 1):
                for id_ in range(i0, i1 + 1):
                    thx_c = THX[jd, id_]; thy_c = THY[jd, id_]
                    ssaa = _pick_ssaa_for_pixel(s, pix_halfdiag, conservation_tol, ssaa_min, ssaa_max)
                    gamma_avg = _supersample_pixel_gamma(thx_c, thy_c, dthx, dthy, ssaa, sx, sy, sz)
                    if gamma_avg > rcut:
                        continue

                    sclip = 1.0e-16 if s < 1.0e-16 else s
                    x = gamma_avg / sclip
                    G  = math.exp(-0.5 * x * x)
                    G0 = math.exp(-0.5 * (t0/sclip) * (t0/sclip))
                    T  = G0 * math.exp(-(gamma_avg - t0)/sclip)
                    w  = _blend(gamma_avg, t0, sclip, approx_tanh)
                    Mmean = (1.0 - w) * G + w * T

                    S += Mmean * dthx * dthy

            if S <= 0.0:
                continue

            alpha = A_cut / S  # scale to match continuous target

            # PASS 2: write scaled contributions
            for jd in range(j0, j1 + 1):
                for id_ in range(i0, i1 + 1):
                    thx_c = THX[jd, id_]; thy_c = THY[jd, id_]
                    ssaa = _pick_ssaa_for_pixel(s, pix_halfdiag, conservation_tol, ssaa_min, ssaa_max)
                    gamma_avg = _supersample_pixel_gamma(thx_c, thy_c, dthx, dthy, ssaa, sx, sy, sz)
                    if gamma_avg > rcut:
                        continue

                    sclip = 1.0e-16 if s < 1.0e-16 else s
                    x = gamma_avg / sclip
                    G  = math.exp(-0.5 * x * x)
                    G0 = math.exp(-0.5 * (t0/sclip) * (t0/sclip))
                    T  = G0 * math.exp(-(gamma_avg - t0)/sclip)
                    w  = _blend(gamma_avg, t0, sclip, approx_tanh)
                    Mmean = (1.0 - w) * G + w * T

                    Z[jd, id_] += alpha * base * (Mmean / A) * dthx * dthy

    return Z
