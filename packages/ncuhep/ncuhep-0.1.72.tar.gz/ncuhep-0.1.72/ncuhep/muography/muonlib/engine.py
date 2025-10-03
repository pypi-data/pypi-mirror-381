# muonlib/engine.py  (aka muon_forward_model.py)
import math
import time
import json
import logging
import numpy as np

from .profiling import Profiler, _print_profile
from .angles import grid_steps
from .cpu import (
    angles_from_grid,
    unit_vectors_from_angles,
    precompute_source_fields,
    splat_cpu_vec,  # CPU path unchanged here
)
from .gpu import (
    CUDA_OK,
    precompute_source_fields_gpu,
    splat_gpu,
    choose_energy_tile_size,   # Adaptive tiling helper (GPU)
)
from .utils import prepare_xeff_and_warn, enforce_energy_single, enforce_energy_range
from .finalize import finalize_map as _finalize_map, finalize_stack as _finalize_stack
from .finalize import (
    export_finalized_maps_npz as _export_npz,
    plot_single_map as _plot_single_map,
    plot_energy_stack as _plot_energy_stack,
    plot_integrated_spectrum as _plot_integrated_spectrum,
    plot_sum_or_integrated_map as _plot_sum_or_integrated_map,
)

# ---------------- logging setup ----------------
_LOGGER_NAME = "muonlib.engine"
_logger = logging.getLogger(_LOGGER_NAME)
if not _logger.handlers:
    _logger.setLevel(logging.INFO)
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    _logger.addHandler(_h)
    _logger.propagate = False


def _normalize_precision(p):
    s = str(p).strip().lower()
    if s in ("fp32", "float32", "f32", "32"):
        return "fp32"
    return "fp64"


class MuonForwardModel:
    """
    Forward model for muon maps/stacks with CPU/GPU precompute + scatter.

    GPU knobs (Method A):
      * eps_patch: per-destination pixel adaptive refinement tolerance (relative)
      * max_subdiv_levels: max refinement levels (s = 1,2,4,...,2^L)
      * subpixel_trigger_px: trigger adaptive only if 5*sigma < subpixel_trigger_px * pixel_halfdiag

    Energy tiling:
      * energy_tile_size: if int, use this many energies per tile; if None (default), choose
        adaptively based on VRAM via gpu.choose_energy_tile_size().
    """

    def __init__(
        self,
        *,
        npz_path: str,
        rho_gcm3: float = 2.65,
        precompute_on_gpu: bool = True,
        approx_gamma: bool = False,
        approx_tanh: bool = False,
        five_sigma: float = 5.0,
        ngrid_norm: int = 2048,
        threads_per_block: int = 256,
        min_rcut_rad: float = 1e-5,
        rcut_floor: float = 0.75,
        shards: int | None = None,
        crop_half_angle_deg: float = 13.0,
        target_mrad_step: float = 1.0,
        thickness_source: str = "det",
        precision: str = "fp64",
        log_level: int = logging.INFO,
        eps_patch: float = 0.01,
        max_subdiv_levels: int = 2,
        subpixel_trigger_px: float = 10.0,
        # export finalize knob
        finalize_on_export: bool = False,
        # NEW: user-specified energy tiling (None => adaptive)
        energy_tile_size: int | None = None,
    ):
        self.npz_path = npz_path
        self.rho_gcm3 = float(rho_gcm3)

        self.precompute_on_gpu = bool(precompute_on_gpu)
        self.approx_gamma = bool(approx_gamma)
        self.approx_tanh = bool(approx_tanh)

        self.five_sigma = float(five_sigma)
        self.ngrid_norm = int(ngrid_norm)
        self.threads_per_block = int(threads_per_block)
        self.min_rcut_rad = float(min_rcut_rad)
        self.rcut_floor = float(rcut_floor)
        self.shards = None if shards is None else int(shards)

        self.crop_half_angle_deg = float(crop_half_angle_deg)
        self.target_mrad_step = float(target_mrad_step)

        self.thickness_source = "mc" if str(thickness_source).lower() == "mc" else "det"

        # precision / dtype
        self.precision = _normalize_precision(precision)
        self._dtype = np.float32 if self.precision == "fp32" else np.float64

        # GPU SSAA knobs
        self.eps_patch = float(eps_patch)
        self.max_subdiv_levels = int(max_subdiv_levels)
        self.subpixel_trigger_px = float(subpixel_trigger_px)

        # export finalize knob
        self.finalize_on_export = bool(finalize_on_export)

        # NEW: user tiling preference
        self.energy_tile_size = None if energy_tile_size is None else int(energy_tile_size)

        self._THX = None
        self._THY = None
        self._L = None

        self.logger = logging.getLogger(_LOGGER_NAME)
        self.set_log_level(log_level)

        self._det_zenith_rad = 0.0
        self._det_azimuth_rad = 0.0

    # --------- logging control ----------
    def set_log_level(self, level: int):
        self.logger.setLevel(level)

    # --------- user knobs ----------
    def set_npz(self, path: str):
        self.npz_path = str(path)
        self._THX = self._THY = self._L = None

    def set_compute(
        self,
        *,
        precompute_on_gpu=None,
        approx_gamma=None,
        approx_tanh=None,
        threads_per_block=None,
        min_rcut_rad=None,
        rcut_floor=None,
        shards=None,
        five_sigma=None,
        ngrid_norm=None,
        precision=None,
        eps_patch=None, max_subdiv_levels=None, subpixel_trigger_px=None,
        # NEW: user tiling override
        energy_tile_size=None,
    ):
        if precompute_on_gpu is not None:
            self.precompute_on_gpu = bool(precompute_on_gpu)
        if approx_gamma is not None:
            self.approx_gamma = bool(approx_gamma)
        if approx_tanh is not None:
            self.approx_tanh = bool(approx_tanh)
        if threads_per_block is not None:
            self.threads_per_block = int(threads_per_block)
        if min_rcut_rad is not None:
            self.min_rcut_rad = float(min_rcut_rad)
        if rcut_floor is not None:
            self.rcut_floor = float(rcut_floor)
        if shards is not None:
            self.shards = int(shards)
        if five_sigma is not None:
            self.five_sigma = float(five_sigma)
        if ngrid_norm is not None:
            self.ngrid_norm = int(ngrid_norm)
        if precision is not None:
            self.precision = _normalize_precision(precision)
            self._dtype = np.float32 if self.precision == "fp32" else np.float64
            self._THX = self._THY = self._L = None

        if eps_patch is not None:
            self.eps_patch = float(eps_patch)
        if max_subdiv_levels is not None:
            self.max_subdiv_levels = int(max_subdiv_levels)
        if subpixel_trigger_px is not None:
            self.subpixel_trigger_px = float(subpixel_trigger_px)

        # NEW: set tiling preference
        if energy_tile_size is not None:
            self.energy_tile_size = None if energy_tile_size in (None, "None") else int(energy_tile_size)

    def set_finalize(self, *, crop_half_angle_deg=None, target_mrad_step=None):
        if crop_half_angle_deg is not None:
            self.crop_half_angle_deg = float(crop_half_angle_deg)
        if target_mrad_step is not None:
            self.target_mrad_step = float(target_mrad_step)

    def set_thickness_source(self, source: str):
        self.thickness_source = "mc" if str(source).lower() == "mc" else "det"
        self._THX = self._THY = self._L = None  # force reload

    # --------- NPZ loader ----------
    def _load_npz(self):
        if self._THX is not None:
            return self._THX, self._THY, self._L

        data = np.load(self.npz_path, allow_pickle=True)

        THX_det = data.get("THX_rad_det", None)
        THY_det = data.get("THY_rad_det", None)
        L_det   = data.get("L_det", None)

        THX_mc = data.get("THX_rad_mc", None)
        THY_mc = data.get("THY_rad_mc", None)
        L_mc   = data.get("L_mc_mean", None)

        if THX_det is not None and THY_det is not None and L_det is not None:
            if self.thickness_source == "mc" and (THX_mc is not None and THY_mc is not None and L_mc is not None):
                THX = np.ascontiguousarray(THX_mc, dtype=self._dtype)
                THY = np.ascontiguousarray(THY_mc, dtype=self._dtype)
                L   = np.ascontiguousarray(L_mc,   dtype=self._dtype)
                self.logger.info("Using MC coarse thickness from NPZ.")
            else:
                if self.thickness_source == "mc":
                    self.logger.warning("Requested MC thickness, but NPZ has no MC coarse maps. Falling back to deterministic.")
                THX = np.ascontiguousarray(THX_det, dtype=self._dtype)
                THY = np.ascontiguousarray(THY_det, dtype=self._dtype)
                L   = np.ascontiguousarray(L_det,   dtype=self._dtype)
                self.logger.info("Using deterministic coarse thickness from NPZ.")
        else:
            self.logger.warning("NPZ appears to be in legacy format. Using THX_rad/THY_rad/L.")
            THX = np.ascontiguousarray(data["THX_rad"], dtype=self._dtype)
            THY = np.ascontiguousarray(data["THY_rad"], dtype=self._dtype)
            L   = np.ascontiguousarray(data["L"],       dtype=self._dtype)

        # detector angles from meta
        zenith_deg = 0.0
        azimuth_deg = 0.0
        if "meta_json" in data:
            try:
                mj = json.loads(str(data["meta_json"]))
                zenith_deg = float(mj.get("angle_deg", 0.0))
                azimuth_deg = float(mj.get("det_azimuth_deg", mj.get("azimuth_deg", 0.0)))
            except Exception:
                pass
        elif "meta" in data:
            try:
                md = data["meta"].item() if hasattr(data["meta"], "item") else dict(data["meta"])
                zenith_deg = float(md.get("angle_deg", 0.0))
                azimuth_deg = float(md.get("det_azimuth_deg", md.get("azimuth_deg", 0.0)))
            except Exception:
                pass
        self._det_zenith_rad = math.radians(zenith_deg)
        self._det_azimuth_rad = math.radians(azimuth_deg)

        self._THX, self._THY, self._L = THX, THY, L
        return THX, THY, L

    # --------- forward: single energy ----------
    def forward_single(
        self,
        *,
        E_GeV: float,
        return_diag: bool = False,
        profile: bool = False,
        force_cpu: bool = False,
        debug: bool = False,
    ):
        prof = Profiler()
        with prof.section("io:load_npz"):
            THX, THY, L = self._load_npz()
            THX, THY, L = THX.T, THY.T, L.T  # ensure (H,W)

        with prof.section("guard:energy"):
            E_use = enforce_energy_single(float(E_GeV), logger=self.logger)

        with prof.section("grid:steps"):
            dthx, dthy = grid_steps(THX, THY)

        with prof.section("angles_from_grid"):
            THD, PHD = angles_from_grid(THX, THY)

        with prof.section("detector_unit_vectors"):
            nxD, nyD, nzD = unit_vectors_from_angles(THD, PHD)

        with prof.section("xeff_prepare"):
            Xeff = prepare_xeff_and_warn(L, self.rho_gcm3, logger=self.logger)

        use_gpu_pre = (not force_cpu) and self.precompute_on_gpu and CUDA_OK
        use_gpu_splat = (not force_cpu) and CUDA_OK

        did_gpu_pre = False
        if use_gpu_pre:
            try:
                t0 = time.perf_counter()
                gpu_fields = precompute_source_fields_gpu(
                    E_use, THX, THY, Xeff, self.ngrid_norm,
                    getattr(self, "_det_zenith_rad", 0.0),
                    getattr(self, "_det_azimuth_rad", 0.0),
                    approx_tanh=self.approx_tanh,
                    threads_per_block=self.threads_per_block,
                    dtype=self._dtype,
                    return_device=True,
                    sanitize_device=True
                )
                (thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm) = gpu_fields
                prof.add("precompute:gpu", time.perf_counter() - t0)
                did_gpu_pre = True
            except Exception as e:
                if debug:
                    self.logger.warning("GPU precompute failed → CPU. %s", e)

        if not did_gpu_pre:
            with prof.section("precompute:cpu"):
                (thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps,
                 sigma, theta0, Anorm) = precompute_source_fields(
                    E_use, THX, THY, Xeff, self.ngrid_norm,
                    getattr(self, "_det_zenith_rad", 0.0),
                    getattr(self, "_det_azimuth_rad", 0.0),
                    approx_tanh=self.approx_tanh,
                )
            with prof.section("sanitize_fields"):
                for arr in (phi0, Ps, Jsrc):
                    np.nan_to_num(arr, copy=False, nan=self._dtype(0.0), posinf=self._dtype(0.0), neginf=self._dtype(0.0))
                    arr[arr < self._dtype(0.0)] = self._dtype(0.0)
                for arr, minv in ((sigma, self._dtype(1e-16)), (Anorm, self._dtype(1e-300))):
                    np.nan_to_num(arr, copy=False, nan=minv, posinf=minv, neginf=minv)
                    arr[arr < minv] = minv
                np.nan_to_num(theta0, copy=False, nan=self._dtype(0.0), posinf=self._dtype(0.0), neginf=self._dtype(0.0))

        H, W = THX.shape
        Z = np.zeros((H, W), dtype=self._dtype)

        used_gpu = False
        if use_gpu_splat:
            try:
                with prof.section("gpu:scatter"):
                    Z = splat_gpu(
                        nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm,
                        self._dtype(dthx), self._dtype(dthy),
                        self._dtype(self.five_sigma), self._dtype(self.min_rcut_rad), self._dtype(self.rcut_floor),
                        self.approx_gamma, self.approx_tanh,
                        threads_per_block=self.threads_per_block, shards=self.shards, dtype=self._dtype,
                        eps_patch=self.eps_patch,
                        max_subdiv_levels=self.max_subdiv_levels,
                        subpixel_trigger_px=self.subpixel_trigger_px,
                    )
                used_gpu = True
            except Exception as e:
                if debug:
                    self.logger.warning("GPU scatter failed → CPU. %s", e)

        if not used_gpu:
            with prof.section("cpu:splat_vec"):
                Z = splat_cpu_vec(
                    nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps,
                    sigma, theta0, Anorm, self._dtype(dthx), self._dtype(dthy),
                    self._dtype(self.five_sigma), self._dtype(self.min_rcut_rad), self._dtype(self.rcut_floor),
                    approx_tanh=self.approx_tanh,
                )

        THX, THY, Z = THX.T, THY.T, Z.T  # back to (H,W)

        if profile:
            _print_profile(f"MuonForwardModel::forward_single(E={E_GeV:g} GeV)", prof)

        return (THX * self._dtype(1e3), THY * self._dtype(1e3), Z)

    # --------- forward: multi-energy ----------
    def forward_multi(
        self,
        *,
        E_min: float,
        E_max: float,
        nbins: int,
        mode: str = "linear",
        return_diag: bool = False,
        show_progress: bool = True,
        profile: bool = False,
        force_cpu: bool = False,
        debug: bool = False,
    ):
        prof = Profiler()
        with prof.section("io:load_npz"):
            THX, THY, L = self._load_npz()
            THX, THY, L = THX.T, THY.T, L.T  # ensure (H,W)

        with prof.section("guard:energy_range"):
            Emin, Emax = enforce_energy_range(float(E_min), float(E_max), logger=self.logger)
            if mode.lower() == "linear":
                energies = np.linspace(Emin, Emax, int(nbins), dtype=self._dtype)
            else:
                energies = np.exp(np.linspace(np.log(Emin), np.log(Emax), int(nbins), dtype=self._dtype)).astype(self._dtype, copy=False)

        H, W = THX.shape
        with prof.section("grid:steps"):
            dthx, dthy = grid_steps(THX, THY)
        with prof.section("angles_from_grid"):
            THD, PHD = angles_from_grid(THX, THY)
        with prof.section("detector_unit_vectors"):
            nxD, nyD, nzD = unit_vectors_from_angles(THD, PHD)
        with prof.section("xeff_prepare"):
            Xeff = prepare_xeff_and_warn(L, self.rho_gcm3, logger=self.logger)

        # Decide energy tiling (T energies per tile)
        if (self.energy_tile_size is not None) and self.energy_tile_size > 0:
            # Manual override
            T = min(int(self.energy_tile_size), int(energies.size))
            self.logger.info(f"Energy tiling (manual): T={T} energies/tile (K={energies.size}).")
        else:
            # Adaptive (GPU only)
            T = 1
            if (not force_cpu) and CUDA_OK:
                T = choose_energy_tile_size(
                    H, W, dtype=self._dtype,
                    per_energy_arrays=6,  # phi0, Ps, sigma, theta0, Anorm, Z
                    safety_frac=0.6,
                    min_tile=1,
                    max_tile=int(energies.size),
                )
            self.logger.info(f"Energy tiling (adaptive): T={T} energies/tile (K={energies.size}).")

        Z_stack = np.empty((energies.size, H, W), dtype=self._dtype)
        diags = [] if return_diag else None

        use_gpu_pre = (not force_cpu) and self.precompute_on_gpu and CUDA_OK
        use_gpu_splat = (not force_cpu) and CUDA_OK
        perbin_prof = dict(precompute_cpu=0.0, precompute_gpu=0.0, gpu_kernel=0.0, cpu_splat=0.0)

        # Tile the energy loop (inner loop per-energy; ready for batched kernels)
        tile_iter = range(0, energies.size, max(1, T))
        if show_progress:
            try:
                from tqdm import trange
                tile_iter = trange(0, energies.size, max(1, T), desc="Energy tiles", unit="tile", leave=True)
            except Exception:
                pass

        for k0 in tile_iter:
            k1 = min(k0 + max(1, T), energies.size)

            for k in range(k0, k1):
                Ek = float(energies[k])
                did_gpu_pre = False

                if use_gpu_pre:
                    try:
                        t0 = time.perf_counter()
                        gpu_fields = precompute_source_fields_gpu(
                            Ek, THX, THY, Xeff, self.ngrid_norm,
                            getattr(self, "_det_zenith_rad", 0.0),
                            getattr(self, "_det_azimuth_rad", 0.0),
                            approx_tanh=self.approx_tanh,
                            threads_per_block=self.threads_per_block,
                            dtype=self._dtype,
                            return_device=True,
                            sanitize_device=True
                        )
                        (thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm) = gpu_fields
                        perbin_prof["precompute_gpu"] += (time.perf_counter() - t0)
                        did_gpu_pre = True
                    except Exception as e:
                        if debug:
                            self.logger.warning("GPU precompute (bin %d) → CPU. %s", k, e)

                if not did_gpu_pre:
                    t1 = time.perf_counter()
                    (thetaS, phiS, nxS, nyS, nzS, Jsrc, phi0, Ps,
                     sigma, theta0, Anorm) = precompute_source_fields(
                        Ek, THX, THY, Xeff, self.ngrid_norm,
                        getattr(self, "_det_zenith_rad", 0.0),
                        getattr(self, "_det_azimuth_rad", 0.0),
                        approx_tanh=self.approx_tanh,
                    )
                    for arr in (phi0, Ps, Jsrc):
                        np.nan_to_num(arr, copy=False, nan=self._dtype(0.0), posinf=self._dtype(0.0), neginf=self._dtype(0.0))
                        arr[arr < self._dtype(0.0)] = self._dtype(0.0)
                    for arr, minv in ((sigma, self._dtype(1e-16)), (Anorm, self._dtype(1e-300))):
                        np.nan_to_num(arr, copy=False, nan=minv, posinf=minv, neginf=minv)
                        arr[arr < minv] = minv
                    np.nan_to_num(theta0, copy=False, nan=self._dtype(0.0), posinf=self._dtype(0.0), neginf=self._dtype(0.0))
                    perbin_prof["precompute_cpu"] += (time.perf_counter() - t1)

                if use_gpu_splat:
                    try:
                        t4 = time.perf_counter()
                        Z_stack[k] = splat_gpu(
                            nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps, sigma, theta0, Anorm,
                            self._dtype(dthx), self._dtype(dthy),
                            self._dtype(self.five_sigma), self._dtype(self.min_rcut_rad), self._dtype(self.rcut_floor),
                            self.approx_gamma, self.approx_tanh,
                            threads_per_block=self.threads_per_block, shards=self.shards, dtype=self._dtype,
                            eps_patch=self.eps_patch,
                            max_subdiv_levels=self.max_subdiv_levels,
                            subpixel_trigger_px=self.subpixel_trigger_px,
                        )
                        perbin_prof["gpu_kernel"] += (time.perf_counter() - t4)
                    except Exception as e:
                        if debug:
                            self.logger.warning("CUDA scatter bin %d → CPU. %s", k, e)
                        t7 = time.perf_counter()
                        Z_stack[k] = splat_cpu_vec(
                            nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps,
                            sigma, theta0, Anorm, self._dtype(dthx), self._dtype(dthy),
                            self._dtype(self.five_sigma), self._dtype(self.min_rcut_rad), self._dtype(self.rcut_floor),
                            approx_tanh=self.approx_tanh,
                        )
                        perbin_prof["cpu_splat"] += (time.perf_counter() - t7)
                else:
                    t7 = time.perf_counter()
                    Z_stack[k] = splat_cpu_vec(
                        nxD, nyD, nzD, nxS, nyS, nzS, Jsrc, phi0, Ps,
                        sigma, theta0, Anorm, self._dtype(dthx), self._dtype(dthy),
                        self._dtype(self.five_sigma), self._dtype(self.min_rcut_rad), self._dtype(self.rcut_floor),
                        approx_tanh=self.approx_tanh,
                    )
                    perbin_prof["cpu_splat"] += (time.perf_counter() - t7)

                if return_diag:
                    diags.append(dict(
                        E=Ek,
                        Ps_min=float(np.min(Ps).copy_to_host() if CUDA_OK and hasattr(Ps, 'copy_to_host') else np.min(Ps)),
                        Ps_max=float(np.max(Ps).copy_to_host() if CUDA_OK and hasattr(Ps, 'copy_to_host') else np.max(Ps)),
                        sigma_min=float(np.min(sigma).copy_to_host() if CUDA_OK and hasattr(sigma, 'copy_to_host') else np.min(sigma)),
                        sigma_max=float(np.max(sigma).copy_to_host() if CUDA_OK and hasattr(sigma, 'copy_to_host') else np.max(sigma)),
                    ))

        for k, v in perbin_prof.items():
            prof.add(f"bins:{k}_sum", v)
            prof.add(f"bins:{k}_avg", v / max(1, energies.size))

        THX, THY, Z_stack = THX.T, THY.T, Z_stack.transpose((0, 2, 1))  # back to (H,W)
        out = ((energies.astype(self._dtype, copy=False),
                THX * self._dtype(1e3), THY * self._dtype(1e3), Z_stack, diags)
               if return_diag else
               (energies.astype(self._dtype, copy=False),
                THX * self._dtype(1e3), THY * self._dtype(1e3), Z_stack))

        if profile:
            _print_profile(
                f"MuonForwardModel::forward_multi({energies.size} bins, {E_min:g}–{E_max:g} GeV, mode={mode})",
                prof,
            )
        return out

    # ---- delegate finalize/plot/export ----
    def finalize_single(self, THX_mrad, THY_mrad, Z, *, crop_half_angle_deg=None, target_mrad_step=None):
        return _finalize_map(
            THX_mrad, THY_mrad, Z,
            crop_half_angle_deg=self.crop_half_angle_deg if crop_half_angle_deg is None else crop_half_angle_deg,
            target_mrad_step=self.target_mrad_step if target_mrad_step is None else target_mrad_step,
        )

    def finalize_stack(self, THX_mrad, THY_mrad, Z_stack, *, crop_half_angle_deg=None, target_mrad_step=None):
        return _finalize_stack(
            THX_mrad, THY_mrad, Z_stack,
            crop_half_angle_deg=self.crop_half_angle_deg if crop_half_angle_deg is None else crop_half_angle_deg,
            target_mrad_step=self.target_mrad_step if target_mrad_step is None else target_mrad_step,
        )

    def export_npz(self, out_path, THX_mrad, THY_mrad, Z, *,
                   energies_GeV=None, energy_edges_GeV=None,
                   crop_half_angle_deg=None, target_mrad_step=None,
                   extra_meta=None, include_unweighted=True,
                   finalize: bool | None = None):
        """
        Export either a single map (Z: HxW) or an energy stack (Z: BxHxW or HxWxB).

        If Z is 3D, we expect the leading dim to be bins (B,H,W). If it's (H,W,B),
        we'll transpose to (B,H,W) before finalizing/exporting.
        """
        finalize_flag = self.finalize_on_export if finalize is None else bool(finalize)

        # Normalize stack layout if needed
        if Z.ndim == 3:
            # Accept both (B,H,W) and (H,W,B): detect by matching THX/THY shapes
            H, W = THX_mrad.shape
            if Z.shape[1:] == (H, W):
                Z_stack = Z
            elif Z.shape[:2] == (H, W):
                Z_stack = np.transpose(Z, (2, 0, 1))  # (H,W,B) -> (B,H,W)
            else:
                raise ValueError(f"export_npz: Z shape {Z.shape} not compatible with THX/THY {(H, W)}")

            # Require energies for a stack
            if energies_GeV is None and energy_edges_GeV is None:
                raise ValueError("export_npz: exporting a stack requires energies_GeV or energy_edges_GeV")

            if finalize_flag:
                THX_mrad, THY_mrad, Z_stack = self.finalize_stack(
                    THX_mrad, THY_mrad, Z_stack,
                    crop_half_angle_deg=crop_half_angle_deg,
                    target_mrad_step=target_mrad_step
                )
            return _export_npz(
                out_path, THX_mrad, THY_mrad, Z_stack,
                energies_GeV=energies_GeV, energy_edges_GeV=energy_edges_GeV,
                crop_half_angle_deg=self.crop_half_angle_deg if crop_half_angle_deg is None else crop_half_angle_deg,
                target_mrad_step=self.target_mrad_step if target_mrad_step is None else target_mrad_step,
                extra_meta=extra_meta, include_unweighted=include_unweighted,
            )

        elif Z.ndim == 2:
            # Single map
            if finalize_flag:
                THX_mrad, THY_mrad, Z = self.finalize_single(
                    THX_mrad, THY_mrad, Z,
                    crop_half_angle_deg=crop_half_angle_deg,
                    target_mrad_step=target_mrad_step
                )
            return _export_npz(
                out_path, THX_mrad, THY_mrad, Z,
                energies_GeV=energies_GeV, energy_edges_GeV=energy_edges_GeV,
                crop_half_angle_deg=self.crop_half_angle_deg if crop_half_angle_deg is None else crop_half_angle_deg,
                target_mrad_step=self.target_mrad_step if target_mrad_step is None else target_mrad_step,
                extra_meta=extra_meta, include_unweighted=include_unweighted,
            )

        else:
            raise ValueError(f"export_npz: Z must be 2D or 3D, got ndim={Z.ndim}")

    def plot_single(self, THX_mrad, THY_mrad, Z, title="dΦ_D/dE", finalize=True, plot_grid=True):
        if finalize:
            THX_mrad, THY_mrad, Z = self.finalize_single(THX_mrad, THY_mrad, Z)
        return _plot_single_map(THX_mrad, THY_mrad, Z, title=title, plot_grid=plot_grid)

    def plot_stack(self, energies, THX_mrad, THY_mrad, Z_stack, finalize=True, plot_grid=True):
        if finalize:
            THX_mrad, THY_mrad, Z_stack = self.finalize_stack(THX_mrad, THY_mrad, Z_stack)
        return _plot_energy_stack(energies, THX_mrad, THY_mrad, Z_stack, plot_grid=plot_grid)

    def plot_integrated_spectrum(self, energies, THX_mrad, THY_mrad, Z_stack):
        return _plot_integrated_spectrum(energies, THX_mrad, THY_mrad, Z_stack)

    def plot_sum_or_integrated_map(self, energies, THX_mrad, THY_mrad, Z_stack, *,
                                   integrate_over_energy=False, title=None, finalize=True):
        if finalize:
            THX_mrad, THY_mrad, Z_stack = self.finalize_stack(THX_mrad, THY_mrad, Z_stack)
        return _plot_sum_or_integrated_map(
            energies, THX_mrad, THY_mrad, Z_stack,
            integrate_over_energy=integrate_over_energy, title=title
        )
