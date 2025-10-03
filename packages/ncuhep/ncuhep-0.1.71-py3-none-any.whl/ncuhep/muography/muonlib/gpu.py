# muonlib/gpu.py

import math
import numpy as np

# CUDA optional guard
try:
    from numba import cuda
    from numba.cuda.cudadrv.devicearray import DeviceNDArray
    CUDA_OK = cuda.is_available()
except Exception:
    CUDA_OK = False

from .constants import (
    CM2_TO_M2, P1, P2, P3, P4, P5,
    # survival
    A_c3, A_c2, A_c1, A_c0, C_c2, C_c1, C_c0, E0_a, E0_b, E0_c,
    n_a1, n_b1, n_a2, n_b2, n_c2, n_x0, n_D,
    # scattering
    A_m_sigma, A_c_sigma, A_m_crit, A_c_crit,
    tau_m_sigma, tau_c_sigma, tau_m_crit, tau_c_crit,
    LN_E0_SIGMA_COEFFS, LN_E0_CRIT_COEFFS, n_sigma, n_crit, c_sigma, c_crit
)

# --------- Device helpers (GPU) ---------
if CUDA_OK:

    @cuda.jit(device=True, inline=True)
    def d_det_to_earth_z(nx, ny, nz, zenith_rad, azimuth_rad):
        return math.sin(zenith_rad) * ny + math.cos(zenith_rad) * nz

    @cuda.jit(device=True, inline=True)
    def d_earth_zenith_from_det_vec(nx, ny, nz, zenith_rad, azimuth_rad):
        zE = d_det_to_earth_z(nx, ny, nz, zenith_rad, azimuth_rad)
        if zE > 1.0: zE = 1.0
        elif zE < -1.0: zE = -1.0
        return math.acos(zE)

    @cuda.jit(device=True, inline=True)
    def d_poly6_horner(a,b,c,d,e,f,g, lx):
        return ((((((a*lx + b)*lx + c)*lx + d)*lx + e)*lx + f)*lx + g)

    @cuda.jit(device=True, inline=True)
    def d_lnE0_sigma_val(x):
        lx = math.log(1e-9) if x < 1e-9 else math.log(x)
        a,b,c,d,e,f,g = LN_E0_SIGMA_COEFFS
        return d_poly6_horner(a,b,c,d,e,f,g, lx)

    @cuda.jit(device=True, inline=True)
    def d_lnE0_crit_val(x):
        lx = math.log(1e-9) if x < 1e-9 else math.log(x)
        a,b,c,d,e,f,g = LN_E0_CRIT_COEFFS
        return d_poly6_horner(a,b,c,d,e,f,g, lx)

    @cuda.jit(device=True, inline=True)
    def d_n_sig(x):
        a,b,c = n_sigma
        return (a*x + b)*x + c

    @cuda.jit(device=True, inline=True)
    def d_n_cri(x):
        a,b,c = n_crit
        return (a*x + b)*x + c

    @cuda.jit(device=True, inline=True)
    def d_c_sig(x):
        a,b,c0 = c_sigma
        lx = math.log(1e-9) if x < 1e-9 else math.log(x)
        return (a*lx + b)*lx + c0

    @cuda.jit(device=True, inline=True)
    def d_c_cri(x):
        a,b,c0 = c_crit
        lx = math.log(1e-9) if x < 1e-9 else math.log(x)
        return (a*lx + b)*lx + c0

    @cuda.jit(device=True, inline=True)
    def d_tau_sigma(x): return tau_m_sigma * x + tau_c_sigma

    @cuda.jit(device=True, inline=True)
    def d_tau_crit(x):  return tau_m_crit  * x + tau_c_crit

    @cuda.jit(device=True, inline=True)
    def d_A_sigma(x):   return A_m_sigma * x + A_c_sigma

    @cuda.jit(device=True, inline=True)
    def d_A_crit(x):    return A_m_crit  * x + A_c_crit

    @cuda.jit(device=True, inline=True)
    def d_A_of_x(x):  return (((A_c3*x + A_c2)*x + A_c1)*x + A_c0)

    @cuda.jit(device=True, inline=True)
    def d_C_of_x(x):  return (C_c2*x + C_c1)*x + C_c0

    @cuda.jit(device=True, inline=True)
    def d_E0_of_x(x): return math.exp(E0_c) * math.pow(x + E0_b, E0_a)

    # --------- tanh approximation helpers ---------
    @cuda.jit(device=True, inline=True)
    def d_tanh_rational(x):
        if x > 8.0:
            return 1.0
        elif x < -8.0:
            return -1.0
        xx = x * x
        return (x * (27.0 + xx)) / (27.0 + 9.0 * xx)

    @cuda.jit(device=True, inline=True)
    def d_tanh_switch(x, use_approx):
        return d_tanh_rational(x) if use_approx else math.tanh(x)

    @cuda.jit(device=True, inline=True)
    def d_n_of_x(x, approx_tanh):
        p1 = n_a1*x + n_b1
        p2 = (n_a2*x + n_b2)*x + n_c2
        warg = (x - n_x0)/n_D
        w  = 0.5 * (1.0 + d_tanh_switch(warg, approx_tanh))
        return (1.0 - w)*p1 + w*p2

    @cuda.jit(device=True, inline=True)
    def d_P_S_from_x_m(E, x_m, approx_tanh):
        A = d_A_of_x(x_m); C = d_C_of_x(x_m); E0 = d_E0_of_x(x_m); n = d_n_of_x(x_m, approx_tanh)
        if E <= 0.0 or E0 <= 0.0: return 0.0
        lnE  = math.log(E); lnE0 = math.log(E0)
        if lnE <= lnE0: return 0.0
        d = lnE - lnE0
        if d < 1e-300: d = 1e-300
        val = (1.0 + C) * math.exp(-A / math.pow(d, n))
        if val < 0.0: return 0.0
        if val > 1.0: return 1.0
        return val

    @cuda.jit(device=True, inline=True)
    def d_Theta_sigma(E, x_m):
        if E <= 0.0: return 0.0
        lnE = math.log(E)
        arg = abs((lnE - d_lnE0_sigma_val(x_m)) / d_tau_sigma(x_m))
        return (1.0 / E) * math.exp(d_c_sig(x_m) + d_A_sigma(x_m) * math.exp(-math.pow(arg, d_n_sig(x_m))))

    @cuda.jit(device=True, inline=True)
    def d_Theta_crit(E, x_m):
        if E <= 0.0: return 0.0
        lnE = math.log(E)
        arg = abs((lnE - d_lnE0_crit_val(x_m)) / d_tau_crit(x_m))
        return (1.0 / E) * math.exp(d_c_cri(x_m) + d_A_crit(x_m) * math.exp(-math.pow(arg, d_n_cri(x_m))))

    @cuda.jit(device=True, inline=True)
    def d_slope_to_sph(theta_x, theta_y):
        tx = math.tan(theta_x); ty = math.tan(theta_y)
        r  = math.sqrt(tx*tx + ty*ty)
        return math.atan(r), math.atan2(ty, tx)

    @cuda.jit(device=True, inline=True)
    def d_J_source(theta_x, theta_y):
        cx = math.cos(theta_x); cy = math.cos(theta_y)
        if cx == 0.0 or cy == 0.0: return 0.0
        tx = math.tan(theta_x); ty = math.tan(theta_y)
        sec2x = 1.0/(cx*cx);  sec2y = 1.0/(cy*cy)
        denom = math.pow(1.0 + tx*tx + ty*ty, 1.5)
        return (sec2x * sec2y) / denom

    @cuda.jit(device=True, inline=True)
    def d_cos_theta_star(theta_rad):
        c = math.cos(theta_rad)
        if c > 1.0: c = 1.0
        elif c < -1.0: c = -1.0
        num = c*c + P1*P1 + P2*(math.pow(c, P3)) + P4*(math.pow(c, P5))
        den = 1.0 + P1*P1 + P2 + P4
        val = num / den
        if val < 0.0: val = 0.0
        return math.sqrt(val)

    @cuda.jit(device=True, inline=True)
    def d_dphi0_dE(theta_rad, E):
        if E <= 0.0: return 0.0
        cst   = d_cos_theta_star(theta_rad)
        x     = E
        core  = x * (1.0 + 3.64 / (x * math.pow(cst, 1.29)))
        spec  = 0.14 * math.pow(core, -2.7)
        dem_pi = 1.0 + 1.1 * x * cst / 115.0
        dem_K  = 1.0 + 1.1 * x * cst / 850.0
        return (spec * ((1.0 / dem_pi) + 0.054 / dem_K)) * CM2_TO_M2

    @cuda.jit(device=True, inline=True)
    def d_gauss_core(theta, sigma):
        s = 1.0e-16 if sigma < 1.0e-16 else sigma
        x = theta / s
        return math.exp(-0.5 * x * x)

    @cuda.jit(device=True, inline=True)
    def d_tail(theta, sigma, theta0):
        s = 1.0e-16 if sigma < 1.0e-16 else sigma
        G0 = math.exp(-0.5 * (theta0/s)*(theta0/s))
        return G0 * math.exp(-(theta - theta0)/s)

    @cuda.jit(device=True, inline=True)
    def d_blend(theta, theta0, sigma, approx_tanh):
        s = 1.0e-16 if sigma < 1.0e-16 else sigma
        u = (theta - theta0) / (5.0 * s)
        return 0.5 * (1.0 + d_tanh_switch(u, approx_tanh))

    @cuda.jit(device=True, inline=True)
    def d_M_unnorm_dev(theta, sigma, theta0, approx_tanh):
        G = d_gauss_core(theta, sigma)
        T = d_tail(theta, sigma, theta0)
        w = d_blend(theta, theta0, sigma, approx_tanh)
        return (1.0 - w)*G + w*T

    @cuda.jit(device=True, inline=True)
    def d_gamma_small_angle_from_dot_approx(dot_val):
        if dot_val > 1.0: dot_val = 1.0
        elif dot_val < -1.0: dot_val = -1.0
        val = 2.0 * (1.0 - dot_val)
        if val < 0.0: val = 0.0
        return math.sqrt(val)

    @cuda.jit(device=True, inline=True)
    def d_gamma_small_angle_from_dot(dot_val):
        if dot_val > 1.0: dot_val = 1.0
        elif dot_val < -1.0: dot_val = -1.0
        return math.acos(dot_val)

    # ---------- robust local tangent basis at destination ----------
    @cuda.jit(device=True, inline=True)
    def d_build_tangent_basis(nx, ny, nz):
        if abs(nz) < 0.999:
            ux = -ny; uy = nx; uz = 0.0
        else:
            ux = 0.0; uy = -nz; uz = ny
        normu = math.sqrt(ux*ux + uy*uy + uz*uz)
        if normu < 1e-20:
            dotx = nx
            ux = 1.0 - dotx * nx
            uy =      - dotx * ny
            uz =      - dotx * nz
            normu = math.sqrt(ux*ux + uy*uy + uz*uz)
            if normu < 1e-30:
                if abs(nx) > abs(ny): ux, uy, uz = -nz, 0.0, nx
                else:                  ux, uy, uz = 0.0, nz, -ny
                normu = math.sqrt(ux*ux + uy*uy + uz*uz)
        invu = 1.0 / normu
        ux *= invu; uy *= invu; uz *= invu
        vx = ny * uz - nz * uy
        vy = nz * ux - nx * uz
        vz = nx * uy - ny * ux
        return ux, uy, uz, vx, vy, vz

    @cuda.jit(device=True, inline=True)
    def d_subpixel_dir(nx, ny, nz, ux, uy, uz, vx, vy, vz, dthx, dthy, du, dv):
        px = nx + (du * dthx) * ux + (dv * dthy) * vx
        py = ny + (du * dthx) * uy + (dv * dthy) * vy
        pz = nz + (du * dthx) * uz + (dv * dthy) * vz
        normp2 = px*px + py*py + pz*pz
        if normp2 <= 0.0:
            return nx, ny, nz
        invn = 1.0 / math.sqrt(normp2)
        return px*invn, py*invn, pz*invn

    # ---------- adaptive patch integral using precomputed bases ----------
    @cuda.jit(device=True, inline=True)
    def d_patch_integral_adaptive_pre(nxD, nyD, nzD,
                                      uxD, uyD, uzD, vxD, vyD, vzD,
                                      dthx, dthy, sx, sy, sz, sigma, theta0,
                                      approx_gamma, approx_tanh,
                                      eps_patch, max_levels, use_adaptive):
        nx = nxD; ny = nyD; nz = nzD
        ux = uxD; uy = uyD; uz = uzD
        vx = vxD; vy = vyD; vz = vzD

        s = 1
        prev = 0.0
        val = 0.0
        levels = 0
        while True:
            acc = 0.0
            invs = 1.0 / s
            for iu in range(s):
                du = (iu + 0.5) * invs - 0.5
                for iv in range(s):
                    dv = (iv + 0.5) * invs - 0.5
                    px, py, pz = d_subpixel_dir(nx, ny, nz, ux, uy, uz, vx, vy, vz, dthx, dthy, du, dv)
                    dotv = px * sx + py * sy + pz * sz
                    gamma = d_gamma_small_angle_from_dot_approx(dotv) if approx_gamma else d_gamma_small_angle_from_dot(dotv)
                    acc += d_M_unnorm_dev(gamma, sigma, theta0, approx_tanh)
            val = (acc / (s * s)) * dthx * dthy

            if not use_adaptive:
                break
            if levels > 0:
                num = val - prev
                if num < 0.0: num = -num
                denom = val if val > 1e-30 else 1e-30
                if (num / denom) <= eps_patch:
                    break
            prev = val
            levels += 1
            if levels > max_levels:
                break
            s <<= 1
        return val

    # --------- Kernels (1D pixel kernels kept for single-energy path) ---------
    @cuda.jit
    def precompute_dest_bases_kernel(nxD, nyD, nzD, uxD, uyD, uzD, vxD, vyD, vzD):
        H = nxD.shape[0]; W = nxD.shape[1]
        idx0 = cuda.grid(1)
        stride = cuda.gridsize(1)
        n = H*W
        for idx in range(idx0, n, stride):
            j = idx // W; i = idx - j*W
            ux, uy, uz, vx, vy, vz = d_build_tangent_basis(nxD[j, i], nyD[j, i], nzD[j, i])
            uxD[j, i] = ux; uyD[j, i] = uy; uzD[j, i] = uz
            vxD[j, i] = vx; vyD[j, i] = vy; vzD[j, i] = vz

    @cuda.jit
    def precompute_source_fields_kernel(
        THX, THY, Xeff_m, E, ngrid_norm, det_zenith_rad, det_azimuth_rad, approx_tanh,
        thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm
    ):
        H = THX.shape[0]; W = THX.shape[1]
        idx0 = cuda.grid(1)
        stride = cuda.gridsize(1)
        n = H*W
        for idx in range(idx0, n, stride):
            j = idx // W; i = idx - j*W

            thS, phS = d_slope_to_sph(THX[j,i], THY[j,i])
            thetaS[j,i] = thS;  phiS[j,i] = phS
            s = math.sin(thS); c = math.cos(thS)
            sx = s * math.cos(phS); sy = s * math.sin(phS); sz = c
            nxS[j,i] = sx; nyS[j,i] = sy; nzS[j,i] = sz

            Jsrc[j,i] = d_J_source(THX[j,i], THY[j,i])

            thEarth = d_earth_zenith_from_det_vec(sx, sy, sz, det_zenith_rad, det_azimuth_rad)
            phi0[j,i] = d_dphi0_dE(thEarth, E)

            xeff = Xeff_m[j,i]
            Ps[j,i]    = d_P_S_from_x_m(E, xeff, approx_tanh)
            sg         = d_Theta_sigma(E, xeff)
            t0         = d_Theta_crit(E, xeff)
            sigma[j,i]  = sg
            theta0[j,i] = t0

            # normalization area
            tmax = t0 + 10.0*sg
            if tmax < 0.2: tmax = 0.2
            elif tmax > 2.0: tmax = 2.0
            two_pi = 2.0*math.pi
            npts = ngrid_norm if ngrid_norm > 2 else 2048
            area = 0.0
            prev_t = 0.0
            prev_v = two_pi * prev_t * d_M_unnorm_dev(prev_t, sg, t0, approx_tanh)
            for k2 in range(1, npts):
                t = (tmax * k2) / (npts - 1.0)
                v = two_pi * t * d_M_unnorm_dev(t, sg, t0, approx_tanh)
                area += 0.5 * (v + prev_v) * (t - prev_t)
                prev_t = t
                prev_v = v
            if area < 1e-300: area = 1e-300
            Anorm[j,i]  = area

    @cuda.jit
    def sanitize_fields_kernel(phi0, Ps, Jsrc, sigma, theta0, Anorm, min_sigma, min_anorm):
        H = phi0.shape[0]; W = phi0.shape[1]
        idx0 = cuda.grid(1)
        stride = cuda.gridsize(1)
        n = H*W
        for idx in range(idx0, n, stride):
            j = idx // W; i = idx - j*W

            p0 = phi0[j,i]; ps = Ps[j,i]; js = Jsrc[j,i]
            sg = sigma[j,i]; t0 = theta0[j,i]; an = Anorm[j,i]

            if not (p0 == p0): p0 = 0.0
            if not (ps == ps): ps = 0.0
            if not (js == js): js = 0.0
            if not (sg == sg): sg = min_sigma
            if not (t0 == t0): t0 = 0.0
            if not (an == an): an = min_anorm

            if p0 < 0.0: p0 = 0.0
            if ps < 0.0: ps = 0.0
            if js < 0.0: js = 0.0
            if sg < min_sigma: sg = min_sigma
            if an < min_anorm: an = min_anorm

            phi0[j,i] = p0; Ps[j,i] = ps; Jsrc[j,i] = js
            sigma[j,i] = sg; theta0[j,i] = t0; Anorm[j,i] = an

    # --------- New 2D (energy × pixel) kernels ---------

    @cuda.jit
    def precompute_geom_kernel(THX, THY, nxS, nyS, nzS, Jsrc, thetaS, phiS):
        """Energy-independent geometry per pixel."""
        H = THX.shape[0]; W = THX.shape[1]
        j = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
        i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
        if j >= H or i >= W: return

        thS, phS = d_slope_to_sph(THX[j,i], THY[j,i])
        thetaS[j,i] = thS; phiS[j,i] = phS
        s = math.sin(thS); c = math.cos(thS)
        sx = s * math.cos(phS); sy = s * math.sin(phS); sz = c
        nxS[j,i] = sx; nyS[j,i] = sy; nzS[j,i] = sz
        Jsrc[j,i] = d_J_source(THX[j,i], THY[j,i])

    @cuda.jit
    def precompute_energy_fields_kernel_2d(
        energies, Xeff_m, det_zenith_rad, det_azimuth_rad, approx_tanh,
        nxS, nyS, nzS, ngrid_norm,
        phi0K, PsK, sigmaK, theta0K, AnormK
    ):
        """
        2D launch over (k, pixel). Writes per-energy fields into (K,H,W) arrays.
        """
        K = energies.shape[0]
        H = nxS.shape[0]; W = nxS.shape[1]

        k = cuda.blockIdx.z * cuda.blockDim.z + cuda.threadIdx.z
        j = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
        i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
        if k >= K or j >= H or i >= W:
            return

        E = energies[k]
        sx = nxS[j,i]; sy = nyS[j,i]; sz = nzS[j,i]
        thEarth = d_earth_zenith_from_det_vec(sx, sy, sz, det_zenith_rad, det_azimuth_rad)
        phi0 = d_dphi0_dE(thEarth, E)

        xeff = Xeff_m[j,i]
        Ps   = d_P_S_from_x_m(E, xeff, approx_tanh)
        sg   = d_Theta_sigma(E, xeff)
        t0   = d_Theta_crit(E, xeff)

        # normalization area
        tmax = t0 + 10.0*sg
        if tmax < 0.2: tmax = 0.2
        elif tmax > 2.0: tmax = 2.0
        two_pi = 2.0*math.pi
        npts = ngrid_norm if ngrid_norm > 2 else 2048
        area = 0.0
        prev_t = 0.0
        prev_v = two_pi * prev_t * d_M_unnorm_dev(prev_t, sg, t0, approx_tanh)
        for kk in range(1, npts):
            t = (tmax * kk) / (npts - 1.0)
            v = two_pi * t * d_M_unnorm_dev(t, sg, t0, approx_tanh)
            area += 0.5 * (v + prev_v) * (t - prev_t)
            prev_t = t
            prev_v = v
        if area < 1e-300: area = 1e-300

        phi0K[k, j, i]   = phi0
        PsK[k, j, i]     = Ps
        sigmaK[k, j, i]  = sg
        theta0K[k, j, i] = t0
        AnormK[k, j, i]  = area

    @cuda.jit
    def sanitize_fields_kernel_3d(phi0K, PsK, sigmaK, theta0K, AnormK, min_sigma, min_anorm):
        K = phi0K.shape[0]
        H = phi0K.shape[1]; W = phi0K.shape[2]
        k = cuda.blockIdx.z * cuda.blockDim.z + cuda.threadIdx.z
        j = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
        i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
        if k >= K or j >= H or i >= W: return

        p0 = phi0K[k,j,i]; ps = PsK[k,j,i]
        sg = sigmaK[k,j,i]; t0 = theta0K[k,j,i]; an = AnormK[k,j,i]

        if not (p0 == p0): p0 = 0.0
        if not (ps == ps): ps = 0.0
        if not (sg == sg): sg = min_sigma
        if not (t0 == t0): t0 = 0.0
        if not (an == an): an = min_anorm
        if p0 < 0.0: p0 = 0.0
        if ps < 0.0: ps = 0.0
        if sg < min_sigma: sg = min_sigma
        if an < min_anorm: an = min_anorm

        phi0K[k,j,i] = p0; PsK[k,j,i] = ps
        sigmaK[k,j,i] = sg; theta0K[k,j,i] = t0; AnormK[k,j,i] = an

    @cuda.jit
    def splat_kernel_2d(
        nxD, nyD, nzD, uxD, uyD, uzD, vxD, vyD, vzD,
        nxS, nyS, nzS, Jsrc,
        phi0K, PsK, sigmaK, theta0K, AnormK,
        ZK,  # (K,H,W)
        dthx, dthy, five_sigma, min_rcut, rcut_floor,
        approx_gamma, approx_tanh,
        eps_patch, max_levels, subpixel_trigger_px
    ):
        K = phi0K.shape[0]
        H = nxD.shape[0]; W = nxD.shape[1]

        k = cuda.blockIdx.z * cuda.blockDim.z + cuda.threadIdx.z
        j_src = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y
        i_src = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
        if k >= K or j_src >= H or i_src >= W:
            return

        base_phi0 = phi0K[k, j_src, i_src]
        base_Ps   = PsK[k, j_src, i_src]
        base_J    = Jsrc[j_src, i_src]
        if base_phi0 <= 0.0 or base_Ps <= 0.0 or base_J <= 0.0:
            return

        s  = sigmaK[k, j_src, i_src]
        t0 = theta0K[k, j_src, i_src]
        A  = AnormK[k, j_src, i_src]
        if A <= 0.0:
            return

        pix_halfdiag = 0.5 * math.hypot(dthx, dthy)
        rcut_phys = five_sigma * s
        rcut = rcut_phys
        floor_px = rcut_floor * pix_halfdiag
        if rcut < floor_px: rcut = floor_px
        if rcut < min_rcut: rcut = min_rcut

        ixr = int(rcut / dthx) + 1
        jyr = int(rcut / dthy) + 1

        sx = nxS[j_src, i_src]; sy = nyS[j_src, i_src]; sz = nzS[j_src, i_src]
        base = base_phi0 * base_Ps * base_J

        j0 = j_src - jyr;  j0 = 0 if j0 < 0 else j0
        j1 = j_src + jyr;  j1 = (H-1) if j1 > H-1 else j1
        i0 = i_src - ixr;  i0 = 0 if i0 < 0 else i0
        i1 = i_src + ixr;  i1 = (W-1) if i1 > W-1 else i1

        use_adaptive_pixel = (rcut_phys < subpixel_trigger_px * pix_halfdiag)

        for jd in range(j0, j1+1):
            for id_ in range(i0, i1+1):
                patch = d_patch_integral_adaptive_pre(
                    nxD[jd, id_], nyD[jd, id_], nzD[jd, id_],
                    uxD[jd, id_], uyD[jd, id_], uzD[jd, id_],
                    vxD[jd, id_], vyD[jd, id_], vzD[jd, id_],
                    dthx, dthy,
                    sx, sy, sz, s, t0,
                    approx_gamma, approx_tanh,
                    eps_patch, max_levels,
                    use_adaptive_pixel
                )
                if patch <= 0.0:
                    continue
                contrib = base * (patch / A)
                cuda.atomic.add(ZK, (k, jd, id_), contrib)

# --------- helpers & GPU wrapper funcs ---------

def _is_device_array(x):
    return CUDA_OK and isinstance(x, DeviceNDArray)

def _to_device_if_host(arr, dtype):
    if _is_device_array(arr):
        return arr
    return cuda.to_device(np.ascontiguousarray(arr, dtype=dtype))

def _choose_launch_1d(n_items, threads_per_block, sm_count_guess=80, blocks_per_sm=8):
    min_blocks = int(sm_count_guess * blocks_per_sm)
    need_blocks = (n_items + threads_per_block - 1) // threads_per_block
    return max(min_blocks, need_blocks)

def _ceil_div(a, b):
    return (a + b - 1) // b

# --------- Existing single-energy wrappers (unchanged API) ---------

def precompute_source_fields_gpu(
    E_GeV, THX, THY, Xeff, ngrid_norm, det_zenith_rad, det_azimuth_rad,
    approx_tanh=False, threads_per_block=256, dtype=np.float64,
    return_device=False, sanitize_device=True
):
    if not CUDA_OK:
        raise RuntimeError("CUDA not available")
    H, W = THX.shape
    n = H*W
    blocks = _choose_launch_1d(n, threads_per_block)

    THX  = np.ascontiguousarray(THX,  dtype=dtype)
    THY  = np.ascontiguousarray(THY,  dtype=dtype)
    Xeff = np.ascontiguousarray(Xeff, dtype=dtype)

    d_THX   = cuda.to_device(THX)
    d_THY   = cuda.to_device(THY)
    d_Xeff  = cuda.to_device(Xeff)

    d_thetaS = cuda.device_array((H, W), dtype=dtype)
    d_phiS   = cuda.device_array((H, W), dtype=dtype)
    d_nxS    = cuda.device_array((H, W), dtype=dtype)
    d_nyS    = cuda.device_array((H, W), dtype=dtype)
    d_nzS    = cuda.device_array((H, W), dtype=dtype)
    d_Jsrc   = cuda.device_array((H, W), dtype=dtype)
    d_phi0   = cuda.device_array((H, W), dtype=dtype)
    d_Ps     = cuda.device_array((H, W), dtype=dtype)
    d_sigma  = cuda.device_array((H, W), dtype=dtype)
    d_theta0 = cuda.device_array((H, W), dtype=dtype)
    d_Anorm  = cuda.device_array((H, W), dtype=dtype)

    precompute_source_fields_kernel[blocks, threads_per_block](
        d_THX, d_THY, d_Xeff,
        dtype(E_GeV), int(ngrid_norm),
        dtype(det_zenith_rad), dtype(det_azimuth_rad), bool(approx_tanh),
        d_thetaS, d_phiS, d_nxS, d_nyS, d_nzS, d_Jsrc, d_phi0, d_Ps, d_sigma, d_theta0, d_Anorm
    )
    cuda.synchronize()

    if sanitize_device:
        sanitize_fields_kernel[blocks, threads_per_block](
            d_phi0, d_Ps, d_Jsrc, d_sigma, d_theta0, d_Anorm,
            dtype(1e-16), dtype(1e-300)
        )
        cuda.synchronize()

    if return_device:
        return (d_thetaS, d_phiS, d_nxS, d_nyS, d_nzS, d_Jsrc, d_phi0, d_Ps, d_sigma, d_theta0, d_Anorm)

    return (d_thetaS.copy_to_host(), d_phiS.copy_to_host(),
            d_nxS.copy_to_host(), d_nyS.copy_to_host(), d_nzS.copy_to_host(),
            d_Jsrc.copy_to_host(), d_phi0.copy_to_host(), d_Ps.copy_to_host(),
            d_sigma.copy_to_host(), d_theta0.copy_to_host(), d_Anorm.copy_to_host())

def splat_gpu(
    nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm,
    dthx, dthy, five_sigma, min_rcut, rcut_floor, approx_gamma, approx_tanh,
    threads_per_block=256, shards=None, dtype=np.float64,
    eps_patch=0.01, max_subdiv_levels=2, subpixel_trigger_px=3.0
):
    # Kept for single-energy code path (uses 1-D kernel in your original code).
    if not CUDA_OK:
        raise RuntimeError("CUDA not available")
    H, W = nxD.shape
    n_pix = H*W
    blocks = _choose_launch_1d(n_pix, threads_per_block)

    d_nxD = _to_device_if_host(nxD, dtype); d_nyD = _to_device_if_host(nyD, dtype); d_nzD = _to_device_if_host(nzD, dtype)
    d_nxS = _to_device_if_host(nxS, dtype); d_nyS = _to_device_if_host(nyS, dtype); d_nzS = _to_device_if_host(nzS, dtype)
    d_Jsrc  = _to_device_if_host(Jsrc,  dtype)
    d_phi0  = _to_device_if_host(phi0,  dtype)
    d_Ps    = _to_device_if_host(Ps,    dtype)
    d_sigma = _to_device_if_host(sigma, dtype)
    d_theta0= _to_device_if_host(theta0,dtype)
    d_Anorm = _to_device_if_host(Anorm, dtype)

    # Precompute destination bases once
    d_uxD = cuda.device_array((H, W), dtype=dtype)
    d_uyD = cuda.device_array((H, W), dtype=dtype)
    d_uzD = cuda.device_array((H, W), dtype=dtype)
    d_vxD = cuda.device_array((H, W), dtype=dtype)
    d_vyD = cuda.device_array((H, W), dtype=dtype)
    d_vzD = cuda.device_array((H, W), dtype=dtype)
    precompute_dest_bases_kernel[blocks, threads_per_block](d_nxD, d_nyD, d_nzD, d_uxD, d_uyD, d_uzD, d_vxD, d_vyD, d_vzD)
    cuda.synchronize()

    # Accumulator (no shards in this path)
    d_Z = cuda.to_device(np.zeros((H, W), dtype=dtype))

    # Reuse 1-D per-pixel loop by “broadcasting” via outer loop on host if needed.
    # For simplicity, just launch the original 1-D kernel equivalents was omitted here.

    # We’ll do a simple device-side scatter using the 2D kernel with K=1 for code reuse:
    d_phi0K  = cuda.to_device(d_phi0.copy_to_host()[None, ...])
    d_PsK    = cuda.to_device(d_Ps.copy_to_host()[None, ...])
    d_sigmaK = cuda.to_device(d_sigma.copy_to_host()[None, ...])
    d_theta0K= cuda.to_device(d_theta0.copy_to_host()[None, ...])
    d_AnormK = cuda.to_device(d_Anorm.copy_to_host()[None, ...])
    d_ZK     = cuda.to_device(np.zeros((1, H, W), dtype=dtype))

    # Grid
    bx, by, bz = 16, 16, 1
    gx = _ceil_div(W, bx); gy = _ceil_div(H, by); gz = 1
    splat_kernel_2d[(gx, gy, gz), (bx, by, bz)](
        d_nxD, d_nyD, d_nzD, d_uxD, d_uyD, d_uzD, d_vxD, d_vyD, d_vzD,
        d_nxS, d_nyS, d_nzS, d_Jsrc,
        d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK,
        d_ZK,
        dtype(dthx), dtype(dthy), dtype(five_sigma), dtype(min_rcut), dtype(rcut_floor),
        bool(approx_gamma), bool(approx_tanh),
        dtype(eps_patch), int(max_subdiv_levels), dtype(subpixel_trigger_px)
    )
    cuda.synchronize()

    Z = d_ZK.copy_to_host()[0]
    return Z

# --------- New 2D wrappers ---------

def precompute_multi_gpu_geom(THX, THY, dtype=np.float64):
    """Return device geom buffers: nxS,nyS,nzS,Jsrc,thetaS,phiS."""
    if not CUDA_OK:
        raise RuntimeError("CUDA not available")
    H, W = THX.shape
    d_THX = cuda.to_device(np.ascontiguousarray(THX, dtype=dtype))
    d_THY = cuda.to_device(np.ascontiguousarray(THY, dtype=dtype))
    d_nxS = cuda.device_array((H, W), dtype=dtype)
    d_nyS = cuda.device_array((H, W), dtype=dtype)
    d_nzS = cuda.device_array((H, W), dtype=dtype)
    d_Jsrc= cuda.device_array((H, W), dtype=dtype)
    d_thetaS = cuda.device_array((H, W), dtype=dtype)
    d_phiS   = cuda.device_array((H, W), dtype=dtype)

    bx, by = 16, 16
    gx = _ceil_div(W, bx); gy = _ceil_div(H, by)
    precompute_geom_kernel[(gx, gy), (bx, by)](d_THX, d_THY, d_nxS, d_nyS, d_nzS, d_Jsrc, d_thetaS, d_phiS)
    cuda.synchronize()
    return d_nxS, d_nyS, d_nzS, d_Jsrc, d_thetaS, d_phiS, d_THX, d_THY

def precompute_multi_gpu_energy(
    energies, Xeff, det_zenith_rad, det_azimuth_rad, approx_tanh, ngrid_norm,
    d_nxS, d_nyS, d_nzS, dtype=np.float64
):
    """
    energies: (K,) host array (dtype), returns device 3D arrays (K,H,W).
    """
    if not CUDA_OK:
        raise RuntimeError("CUDA not available")
    H, W = d_nxS.shape
    energies = np.ascontiguousarray(energies, dtype=dtype)
    d_E = cuda.to_device(energies)
    d_X = _to_device_if_host(Xeff, dtype)

    d_phi0K  = cuda.device_array((energies.size, H, W), dtype=dtype)
    d_PsK    = cuda.device_array((energies.size, H, W), dtype=dtype)
    d_sigmaK = cuda.device_array((energies.size, H, W), dtype=dtype)
    d_theta0K= cuda.device_array((energies.size, H, W), dtype=dtype)
    d_AnormK = cuda.device_array((energies.size, H, W), dtype=dtype)

    bx, by, bz = 16, 8, 2  # small 3D tiles
    gx = _ceil_div(W, bx); gy = _ceil_div(H, by); gz = _ceil_div(energies.size, bz)

    precompute_energy_fields_kernel_2d[(gx, gy, gz), (bx, by, bz)](
        d_E, d_X, dtype(det_zenith_rad), dtype(det_azimuth_rad), bool(approx_tanh),
        d_nxS, d_nyS, d_nzS, int(ngrid_norm),
        d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK
    )
    cuda.synchronize()

    # sanitize
    sanitize_fields_kernel_3d[(gx, gy, gz), (bx, by, bz)](
        d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK, dtype(1e-16), dtype(1e-300)
    )
    cuda.synchronize()

    return d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK

def splat_gpu_2d(
    energies,                 # (K,) host array (dtype)
    nxD, nyD, nzD,            # (H,W) host or device
    d_nxS, d_nyS, d_nzS,      # (H,W) device
    d_Jsrc,                   # (H,W) device
    d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK,  # (K,H,W) device
    dthx, dthy, five_sigma, min_rcut, rcut_floor,
    approx_gamma, approx_tanh,
    dtype=np.float64, eps_patch=0.01, max_subdiv_levels=2, subpixel_trigger_px=10.0
):
    if not CUDA_OK:
        raise RuntimeError("CUDA not available")
    H, W = nxD.shape
    K = energies.size

    d_nxD = _to_device_if_host(nxD, dtype); d_nyD = _to_device_if_host(nyD, dtype); d_nzD = _to_device_if_host(nzD, dtype)

    # Precompute destination bases once
    n_pix = H*W
    tpb = 256
    blocks = _choose_launch_1d(n_pix, tpb)
    d_uxD = cuda.device_array((H, W), dtype=dtype)
    d_uyD = cuda.device_array((H, W), dtype=dtype)
    d_uzD = cuda.device_array((H, W), dtype=dtype)
    d_vxD = cuda.device_array((H, W), dtype=dtype)
    d_vyD = cuda.device_array((H, W), dtype=dtype)
    d_vzD = cuda.device_array((H, W), dtype=dtype)
    precompute_dest_bases_kernel[blocks, tpb](d_nxD, d_nyD, d_nzD, d_uxD, d_uyD, d_uzD, d_vxD, d_vyD, d_vzD)
    cuda.synchronize()

    d_ZK = cuda.to_device(np.zeros((K, H, W), dtype=dtype))

    bx, by, bz = 16, 8, 2
    gx = _ceil_div(W, bx); gy = _ceil_div(H, by); gz = _ceil_div(K, bz)

    splat_kernel_2d[(gx, gy, gz), (bx, by, bz)](
        d_nxD, d_nyD, d_nzD, d_uxD, d_uyD, d_uzD, d_vxD, d_vyD, d_vzD,
        d_nxS, d_nyS, d_nzS, d_Jsrc,
        d_phi0K, d_PsK, d_sigmaK, d_theta0K, d_AnormK,
        d_ZK,
        dtype(dthx), dtype(dthy), dtype(five_sigma), dtype(min_rcut), dtype(rcut_floor),
        bool(approx_gamma), bool(approx_tanh),
        dtype(eps_patch), int(max_subdiv_levels), dtype(subpixel_trigger_px)
    )
    cuda.synchronize()

    return d_ZK.copy_to_host()

# --------- shard chooser (kept; not used by 2D path directly) ---------

def choose_shards(H, W, dtype=np.float64, user_shards=None, safety_frac=0.5,
                  min_shards=2, max_shards_cap=32, default_if_unknown=4):
    if not CUDA_OK:
        return default_if_unknown if user_shards is None else int(user_shards)
    if user_shards is not None and user_shards >= 1:
        return int(user_shards)
    try:
        dev = cuda.get_current_device()
        sm_count = getattr(dev, "MULTIPROCESSOR_COUNT", 8)
        free_bytes, _total_bytes = cuda.current_context().get_memory_info()
        bytes_per_val = np.dtype(dtype).itemsize
        max_by_mem = int((safety_frac * free_bytes) // max(1, H*W*bytes_per_val))
        if max_by_mem < min_shards:
            max_by_mem = min_shards
        shard_guess = max(min_shards, min(max_by_mem, max_shards_cap, max(4, sm_count // 2)))
        return int(shard_guess)
    except Exception:
        return int(default_if_unknown)

def choose_energy_tile_size(H, W, dtype=np.float64, *,
                            per_energy_arrays=6,   # phi0, Ps, sigma, theta0, Anorm, Z
                            safety_frac=0.6,
                            min_tile=1,
                            max_tile=1_000_000):
    """
    Pick how many energies to process at once ("tile size") based on free VRAM.

    Assumes all geometry-sized arrays (nxD, bases, nxS, Jsrc, etc.) are already
    allocated on device; we only budget the *incremental* memory needed per energy.

    Memory model per energy:
      per_energy_arrays * H * W * itemsize
      (default per_energy_arrays=6 for: phi0, Ps, sigma, theta0, Anorm, output Z_slice)

    Returns an integer >= min_tile (and <= max_tile).
    """
    if not CUDA_OK:
        return min_tile

    try:
        free_bytes, _total_bytes = cuda.current_context().get_memory_info()
        bytes_per_val = np.dtype(dtype).itemsize
        per_energy_bytes = per_energy_arrays * H * W * bytes_per_val
        if per_energy_bytes <= 0:
            return min_tile

        # leave a safety margin so we don’t OOM when kernels allocate temps
        budget = int(safety_frac * free_bytes)

        T = budget // max(1, per_energy_bytes)
        if T < min_tile:
            T = min_tile
        if T > max_tile:
            T = max_tile
        return int(T)
    except Exception:
        # If anything goes wrong reading memory, fall back to a conservative tile
        return int(min_tile)
