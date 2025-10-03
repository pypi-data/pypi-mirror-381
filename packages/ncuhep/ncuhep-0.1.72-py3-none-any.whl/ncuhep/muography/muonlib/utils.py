# muonlib/utils.py
from .constants import (
    RHO0_G_CM3,
    L_MIN_FIT_M, L_MAX_FIT_M,
    E_MIN_ALLOWED_GEV, E_MAX_FLUX_FIT_GEV, E_MAX_GEANT4_GEV,
)
import logging
import numpy as np
from typing import Optional

# Fallback/module logger (used only if caller doesn't pass one)
_LOGGER_NAME = "muonlib.utils"
_logger = logging.getLogger(_LOGGER_NAME)
if not _logger.handlers:
    _logger.setLevel(logging.INFO)
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    _logger.addHandler(_h)
    _logger.propagate = False


def prepare_xeff_and_warn(L_m: np.ndarray, rho_gcm3: float, *, logger: Optional[logging.Logger] = None):
    """
    Compute effective thickness Xeff and clamp to [L_MIN_FIT_M, L_MAX_FIT_M].
    Warnings are emitted via the provided logger (or module logger if None).
    """
    log = logger or _logger
    rho_scale = rho_gcm3 / RHO0_G_CM3
    Xeff = L_m * rho_scale

    below = (Xeff < L_MIN_FIT_M)
    above = (Xeff > L_MAX_FIT_M)
    n_below = int(below.sum())
    n_above = int(above.sum())

    if n_below > 0:
        log.warning(
            "Path length below fit domain: clamped %d pixels to %.6g m.",
            n_below, L_MIN_FIT_M
        )
        Xeff = np.where(below, L_MIN_FIT_M, Xeff)

    if n_above > 0:
        log.warning(
            "Path length above fit domain: clamped %d pixels to %.6g m.",
            n_above, L_MAX_FIT_M
        )
        Xeff = np.where(above, L_MAX_FIT_M, Xeff)

    return Xeff


def enforce_energy_single(E: float, *, logger: Optional[logging.Logger] = None) -> float:
    """
    Clamp a single energy to the supported domain, logging warnings if needed.
    """
    log = logger or _logger
    E0 = float(E)
    if E0 < E_MIN_ALLOWED_GEV:
        log.warning(
            "Energy below fit domain: requested E=%.6g GeV. Raised to %.6g GeV.",
            E0, E_MIN_ALLOWED_GEV
        )
        E0 = E_MIN_ALLOWED_GEV

    E_cap = min(E_MAX_FLUX_FIT_GEV, E_MAX_GEANT4_GEV)
    if E0 > E_cap:
        log.warning(
            "Energy above fit domain: requested E=%.6g GeV. Capped to %.6g GeV.",
            E0, E_cap
        )
        E0 = E_cap
    return E0


def enforce_energy_range(E_min: float, E_max: float, *, logger: Optional[logging.Logger] = None):
    """
    Clamp an energy range to the supported domain, logging warnings if needed.
    """
    log = logger or _logger
    emin = float(E_min)
    emax = float(E_max)

    if emin < E_MIN_ALLOWED_GEV:
        log.warning(
            "Start energy below fit domain: %.6g → %.6g.",
            emin, E_MIN_ALLOWED_GEV
        )
        emin = E_MIN_ALLOWED_GEV

    overall_cap = min(E_MAX_FLUX_FIT_GEV, E_MAX_GEANT4_GEV)
    if emax > overall_cap:
        log.warning(
            "End energy above fit domain: %.6g → %.6g.",
            emax, overall_cap
        )
        emax = overall_cap

    if emax <= emin:
        raise ValueError(f"E_max ({emax}) must be > E_min ({emin}).")

    return emin, emax
