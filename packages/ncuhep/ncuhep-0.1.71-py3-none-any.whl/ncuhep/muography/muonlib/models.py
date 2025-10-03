import math
import numpy as np
from numba import njit
from .constants import (
    # Survival
    A_c3, A_c2, A_c1, A_c0, C_c2, C_c1, C_c0, E0_a, E0_b, E0_c,
    n_a1, n_b1, n_a2, n_b2, n_c2, n_x0, n_D,
    # Scattering
    A_m_sigma, A_c_sigma, A_m_crit, A_c_crit,
    tau_m_sigma, tau_c_sigma, tau_m_crit, tau_c_crit,
    LN_E0_SIGMA_COEFFS, LN_E0_CRIT_COEFFS, n_sigma, n_crit, c_sigma, c_crit
)

# ---------- Survival S(E|x) ----------
@njit(cache=True, fastmath=True)
def _A_of_x(x):  return ((A_c3*x + A_c2)*x + A_c1)*x + A_c0

@njit(cache=True, fastmath=True)
def _C_of_x(x):  return (C_c2*x + C_c1)*x + C_c0

@njit(cache=True, fastmath=True)
def _E0_of_x(x): return np.exp(E0_c) * np.power(x + E0_b, E0_a)

@njit(cache=True, fastmath=True)
def _n_of_x(x):
    p1 = n_a1*x + n_b1
    p2 = (n_a2*x + n_b2)*x + n_c2
    w  = 0.5 * (1.0 + np.tanh((x - n_x0)/n_D))
    return (1.0 - w)*p1 + w*p2

@njit(cache=True, fastmath=True)
def P_S_from_x_m(E_GeV: float, x_m: float) -> float:
    A = _A_of_x(x_m); C = _C_of_x(x_m); E0 = _E0_of_x(x_m); n = _n_of_x(x_m)
    if E_GeV <= 0.0 or E0 <= 0.0: return 0.0
    lnE  = np.log(E_GeV); lnE0 = np.log(E0)
    if lnE <= lnE0: return 0.0
    d = lnE - lnE0
    if d < 1e-300: d = 1e-300
    val = (1.0 + C) * np.exp(-A / np.power(d, n))
    if val < 0.0: return 0.0
    if val > 1.0: return 1.0
    return val

# ---------- Scattering master form for σ and θ0 ----------
@njit(cache=True, fastmath=True)
def _poly6_horner(coeffs, lx):
    a,b,c,d,e,f,g = coeffs
    return ((((((a*lx + b)*lx + c)*lx + d)*lx + e)*lx + f)*lx + g)

@njit(cache=True, fastmath=True)
def _lnE0_sigma_val(x):
    lx = np.log(1e-9) if x < 1e-9 else np.log(x)
    return _poly6_horner(LN_E0_SIGMA_COEFFS, lx)

@njit(cache=True, fastmath=True)
def _lnE0_crit_val(x):
    lx = np.log(1e-9) if x < 1e-9 else np.log(x)
    return _poly6_horner(LN_E0_CRIT_COEFFS, lx)

@njit(cache=True, fastmath=True)
def _n_sig(x):
    a,b,c = n_sigma
    return (a*x + b)*x + c

@njit(cache=True, fastmath=True)
def _n_cri(x):
    a,b,c = n_crit
    return (a*x + b)*x + c

@njit(cache=True, fastmath=True)
def _c_sig(x):
    lx = np.log(1e-9) if x < 1e-9 else np.log(x)
    a,b,c0 = c_sigma
    return (a*lx + b)*lx + c0

@njit(cache=True, fastmath=True)
def _c_cri(x):
    lx = np.log(1e-9) if x < 1e-9 else np.log(x)
    a,b,c0 = c_crit
    return (a*lx + b)*lx + c0

@njit(cache=True, fastmath=True)
def _tau_sigma(x): return tau_m_sigma * x + tau_c_sigma

@njit(cache=True, fastmath=True)
def _tau_crit(x):  return tau_m_crit  * x + tau_c_crit

@njit(cache=True, fastmath=True)
def _A_sigma(x):   return A_m_sigma * x + A_c_sigma

@njit(cache=True, fastmath=True)
def _A_crit(x):    return A_m_crit  * x + A_c_crit

@njit(cache=True, fastmath=True)
def Theta_sigma(E, x_m):
    if E <= 0.0: return 0.0
    lnE = np.log(E)
    arg = np.abs((lnE - _lnE0_sigma_val(x_m)) / _tau_sigma(x_m))
    return (1.0 / E) * np.exp(_c_sig(x_m) + _A_sigma(x_m) * np.exp(-np.power(arg, _n_sig(x_m))))

@njit(cache=True, fastmath=True)
def Theta_crit(E, x_m):
    if E <= 0.0: return 0.0
    lnE = np.log(E)
    arg = np.abs((lnE - _lnE0_crit_val(x_m)) / _tau_crit(x_m))
    return (1.0 / E) * np.exp(_c_cri(x_m) + _A_crit(x_m) * np.exp(-np.power(arg, _n_cri(x_m))))

# ---------- Molière approx & normalization ----------
@njit(cache=True, fastmath=True)
def gauss_core(theta, sigma):
    s = 1e-16 if sigma < 1e-16 else sigma
    x = theta / s
    return np.exp(-0.5 * x * x)

@njit(cache=True, fastmath=True)
def tail(theta, sigma, theta0):
    s = 1e-16 if sigma < 1e-16 else sigma
    G0 = np.exp(-0.5 * (theta0/s)*(theta0/s))
    return G0 * np.exp(-(theta - theta0)/s)

@njit(cache=True, fastmath=True)
def blend(theta, theta0, sigma):
    s = 1e-16 if sigma < 1e-16 else sigma
    return 0.5 * (1.0 + np.tanh((theta - theta0) / (5.0*s)))

@njit(cache=True, fastmath=True)
def M_unnorm(theta, sigma, theta0):
    G = gauss_core(theta, sigma)
    T = tail(theta, sigma, theta0)
    w = blend(theta, theta0, sigma)
    return (1.0 - w)*G + w*T

@njit(cache=True, fastmath=True)
def norm_area_2pi_theta(sig, th0, ngrid=2048):
    tmax = th0 + 10.0*sig
    if tmax < 0.2: tmax = 0.2
    elif tmax > 2.0: tmax = 2.0
    two_pi = 2.0*np.pi
    npts = ngrid if ngrid > 2 else 2048
    area = 0.0
    prev_t = 0.0
    prev_v = two_pi * prev_t * M_unnorm(prev_t, sig, th0)
    for k in range(1, npts):
        t = (tmax * k) / (npts - 1)
        v = two_pi * t * M_unnorm(t, sig, th0)
        area += 0.5 * (v + prev_v) * (t - prev_t)
        prev_t = t
        prev_v = v
    if area < 1e-300: area = 1e-300
    return area, tmax
