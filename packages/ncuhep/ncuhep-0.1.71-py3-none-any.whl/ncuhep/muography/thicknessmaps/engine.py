# engine.py
import time
import logging
import numpy as np

from .profiling import Profiler, print_profile
from .dem import compute_thickness_map_rotated_cpu, bilinear_sample
from .gpu import CUDA_OK, run_gpu_thickness
from .grf import gaussian_random_field
from .binning import bin_results_jacobian

# ---------------- logging setup ----------------
_LOGGER_NAME = "thicknessmaps"
_logger = logging.getLogger(_LOGGER_NAME)
if not _logger.handlers:
    _logger.setLevel(logging.INFO)
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    _logger.addHandler(_h)
    _logger.propagate = False


class ThicknessMap:
    """
    Compute thickness maps from a regular DEM, with tilt+azimuths.

    Design:
      • Fine grid is used only for computation; outputs are kept in coarse space.
      • Deterministic (non-MC) and MC results are stored SEPARATELY.
      • Coarse products are always produced/saved/plotted.
    """

    def __init__(self,
                 dem_path: str,
                 angle_deg: float,
                 angle_window_deg: float,
                 fine_step_mrad: float,
                 *,
                 det_azimuth_deg: float = 0.0,
                 dem_azimuth_deg: float = 0.0,
                 flip_x: bool = False,
                 flip_y: bool = False,
                 s_max: float = 5000.0,
                 eps_bisect: float = 0.02,
                 max_bisect: int = 96,
                 ds_coarse_scale: float = 0.1,
                 log_level: int = logging.INFO):
        self.dem_path = str(dem_path)
        self.angle_deg = float(angle_deg)
        self.angle_window_deg = float(angle_window_deg)
        self.fine_step_mrad = float(fine_step_mrad)
        self.det_azimuth_deg = float(det_azimuth_deg)
        self.dem_azimuth_deg = float(dem_azimuth_deg)
        self.flip_x = bool(flip_x)
        self.flip_y = bool(flip_y)
        self.s_max = float(s_max)
        self.eps_bisect = float(eps_bisect)
        self.max_bisect = int(max_bisect)
        self.ds_coarse_scale = float(ds_coarse_scale)

        # radians/precompute
        self.theta0 = np.deg2rad(self.angle_deg)
        self.det_azimuth = np.deg2rad(self.det_azimuth_deg)
        self.dem_azimuth = np.deg2rad(self.dem_azimuth_deg)
        self._dem_cos = np.cos(self.dem_azimuth)
        self._dem_sin = np.sin(self.dem_azimuth)

        # DEM/grid
        self.Zg = None
        self.x0g = self.x1g = self.y0g = self.y1g = None
        self.dx = self.dy = None
        self.z0 = None
        self.THX_f = self.THY_f = None  # fine slope grid (immutable after build)

        # ---- deterministic (non-MC) fine results (for computation only)
        self.L_fine = None

        # ---- deterministic coarse results (ALWAYS kept)
        self.THX_c = None; self.THY_c = None
        self.L_c = None
        self._result_step_mrad = None

        # ---- MC fine results (for computation only)
        self.L_mc_mean = None
        self.sigmaL_mc = None
        self.P_mc = None

        # ---- MC coarse results (kept separately)
        self.THX_c_mc = None; self.THY_c_mc = None
        self.L_c_mc = None
        self.sigmaL_c_mc = None
        self.P_c_mc = None
        self._result_step_mrad_mc = None

        self._warned_cuda = False
        self.logger = logging.getLogger(_LOGGER_NAME)
        self.set_log_level(log_level)
        self._prof = None

    # ----- logger control / profiler -----
    def set_log_level(self, level: int): self.logger.setLevel(level)
    def get_profile(self): return self._prof
    def print_profile(self, title="ThicknessMap run"):
        if self._prof is not None: print_profile(title, self._prof)

    # ---------------- DEM I/O ----------------
    def load_dem(self):
        t0 = time.perf_counter()
        dem = np.load(self.dem_path)["DEM"]
        Xr = dem[:, 0].copy(); Yr = dem[:, 1].copy(); Zr = dem[:, 2].copy()
        if self.flip_x: Xr = -Xr
        if self.flip_y: Yr = -Yr

        x_unique = np.unique(Xr); y_unique = np.unique(Yr)
        nx = x_unique.size; ny = y_unique.size
        if nx * ny != Zr.size:
            raise ValueError("DEM points do not form a complete regular grid.")

        order = np.lexsort((Xr, Yr))
        Zg = Zr[order].reshape(ny, nx)

        self.x0g, self.y0g = x_unique[0], y_unique[0]
        self.x1g, self.y1g = x_unique[-1], y_unique[-1]
        self.dx = (self.x1g - self.x0g) / (nx - 1) if nx > 1 else 1.0
        self.dy = (self.y1g - self.y0g) / (ny - 1) if ny > 1 else 1.0

        if not (self.x0g <= 0.0 <= self.x1g and self.y0g <= 0.0 <= self.y1g):
            raise ValueError(
                f"Detector (0,0) outside DEM bounds: "
                f"X:[{self.x0g:.2f},{self.x1g:.2f}]  Y:[{self.y0g:.2f},{self.y1g:.2f}]"
            )

        self.z0 = bilinear_sample(Zg, self.x0g, self.y0g, self.dx, self.dy, 0.0, 0.0)
        self.Zg = Zg
        t1 = time.perf_counter()
        self.logger.info(f"DEM loaded: shape={Zg.shape}, dx={self.dx:.3f} m, dy={self.dy:.3f} m, z0={self.z0:.3f} m ({t1-t0:.2f}s)")
        return self

    # ---------------- Grids ----------------
    def _make_centered_grid(self, step_mrad: float):
        half = int(np.floor(np.radians(self.angle_window_deg) * 1e3 / step_mrad))
        m = np.arange(-half, half + 1, dtype=np.float64) * step_mrad
        r = m * 1e-3  # radians
        THX, THY = np.meshgrid(r, r, indexing='xy')
        return THX, THY

    def build_fine_grid(self):
        if self.THX_f is not None and self.THY_f is not None:
            return self.THX_f, self.THY_f
        t0 = time.perf_counter()
        self.THX_f, self.THY_f = self._make_centered_grid(self.fine_step_mrad)
        t1 = time.perf_counter()
        self.logger.info(f"Slope grid built: shape={self.THX_f.shape}, step={self.fine_step_mrad:.3f} mrad ({t1-t0:.2f}s)")
        return self.THX_f, self.THY_f

    # ---------------- Compute (CPU/GPU + optional MC) ----------------
    def compute_thickness(self,
                          *,
                          calculate_sigma: bool = False,
                          accelerator: str = "cpu",
                          sigmaZ_m: float = 3.0,
                          mc_samples: int = 64,
                          mc_corr_len_m: float | None = 40.0,
                          mc_corr: float | None = None,     # alias
                          mc_seed: int | None = 123,
                          show_progress: bool = True,
                          gpu_block: tuple[int, int] = (16, 16),
                          profile: bool = False,
                          return_profile: bool = False,
                          result_step_mrad: float | None = None):
        """
        - calculate_sigma=False: compute deterministic fine L, then ALWAYS bin to coarse (step = result_step_mrad or fine_step_mrad).
        - calculate_sigma=True : ensure deterministic L exists and is binned; then run MC and bin MC to the SAME step.
        """
        # reset profiler for this run
        self._prof = Profiler(); prof = self._prof

        with prof.section("io:ensure_dem"):
            if self.Zg is None:
                with prof.section("io:load_dem"):
                    self.load_dem()
        with prof.section("grid:ensure"):
            if self.THX_f is None:
                with prof.section("grid:build_fine"):
                    self.build_fine_grid()

        # choose coarse step (always produce coarse)
        if result_step_mrad is None or result_step_mrad <= 0.0:
            result_step_mrad = self.fine_step_mrad  # default to fine step to guarantee coarse output

        use_gpu = (accelerator.lower() == "gpu") and CUDA_OK
        if (accelerator.lower() == "gpu") and not CUDA_OK and (not self._warned_cuda):
            self.logger.warning("CUDA not available; falling back to CPU.")
            self._warned_cuda = True

        ds_coarse = self.ds_coarse_scale * min(self.dx, self.dy)
        self.logger.debug(f"ds_coarse={ds_coarse:.3f} m, s_max={self.s_max:.1f} m")

        def _compute_L(Z):
            if use_gpu:
                with prof.section("gpu:thickness_kernel"):
                    return run_gpu_thickness(
                        Z, self.THX_f, self.THY_f,
                        self.x0g, self.y0g, self.dx, self.dy, self.z0,
                        self.theta0, self.det_azimuth,
                        self._dem_cos, self._dem_sin,
                        self.s_max, ds_coarse, self.eps_bisect, self.max_bisect,
                        self.x0g, self.x1g, self.y0g, self.y1g,
                        gpu_block=gpu_block, prof=prof
                    )
            else:
                with prof.section("cpu:thickness"):
                    return compute_thickness_map_rotated_cpu(
                        Z, self.x0g, self.y0g, self.dx, self.dy, self.z0,
                        self.theta0, self.det_azimuth,
                        self._dem_cos, self._dem_sin,
                        self.THX_f, self.THY_f,
                        self.s_max, ds_coarse, self.eps_bisect, self.max_bisect,
                        self.x0g, self.x1g, self.y0g, self.y1g
                    )

        mode = "GPU (CUDA)" if use_gpu else "CPU"

        # ------- deterministic branch: we always want L_c
        need_det_compute = (self.L_fine is None)
        if need_det_compute:
            self.logger.info(f"Compute L (deterministic) on {mode} …")
            t0 = time.perf_counter()
            self.L_fine = _compute_L(self.Zg)
            t1 = time.perf_counter()
            self.logger.info(f"Done: L computed in {t1 - t0:.2f}s")

        # (re)bin deterministic fine to coarse (always)
        self.logger.info(f"Binning deterministic result → coarse grid: step={result_step_mrad:.3f} mrad")
        t_bin0 = time.perf_counter()
        THX_c, THY_c, L_c, _, _ = bin_results_jacobian(
            self.THX_f, self.THY_f, self.L_fine,
            self.fine_step_mrad, result_step_mrad,
            sigma=None, P=None
        )
        self.THX_c, self.THY_c = THX_c, THY_c
        self.L_c = L_c
        self._result_step_mrad = float(result_step_mrad)
        t_bin1 = time.perf_counter()
        prof.add("post:bin_by_jacobian(det)", (t_bin1 - t_bin0))
        self.logger.info(f"Done binning in {t_bin1 - t_bin0:.2f}s; coarse shape={self.L_c.shape}")

        if calculate_sigma:
            # ------- MC run: produce separate MC fields and coarse products
            corr_len = float(mc_corr_len_m if mc_corr_len_m is not None else (mc_corr if mc_corr is not None else 0.0))
            self.logger.info(f"Compute MC on {mode}: sigmaZ={sigmaZ_m} m, samples={mc_samples}, corr_len={corr_len} m")
            rng = np.random.default_rng(mc_seed)
            H, W = self.THX_f.shape
            mean = np.zeros((H, W), dtype=np.float64)
            m2   = np.zeros((H, W), dtype=np.float64)
            hits = np.zeros((H, W), dtype=np.int64)

            try:
                from tqdm.auto import tqdm
                iterator = tqdm(range(mc_samples), desc="Monte-Carlo DEM", unit="realization") if show_progress else range(mc_samples)
            except Exception:
                iterator = range(mc_samples)

            t0_all = time.perf_counter()
            for m in iterator:
                with prof.section("mc:noise_gen"):
                    dZ = gaussian_random_field(self.Zg.shape, self.dx, self.dy, sigmaZ_m, corr_len, rng)
                    Zm = self.Zg + dZ
                with prof.section("mc:thickness"):
                    Lm = _compute_L(Zm)
                with prof.section("mc:accumulate"):
                    hits += (Lm > 0.0)
                    delta = Lm - mean
                    mean += delta / (m + 1)
                    m2   += delta * (Lm - mean)
            t1_all = time.perf_counter()
            with prof.section("mc:finalize"):
                var = m2 / max(mc_samples - 1, 1)
                std = np.sqrt(np.maximum(var, 0.0))
                p_hit = hits.astype(np.float64) / mc_samples

            # Store MC fine outputs (not exported/plot directly)
            self.L_mc_mean = mean
            self.sigmaL_mc = std
            self.P_mc = p_hit

            self.logger.info(f"Done: MC (samples={mc_samples}) in {t1_all - t0_all:.2f}s")

            # Bin MC to coarse at the SAME step
            self.logger.info(f"Binning MC mean → coarse grid: step={result_step_mrad:.3f} mrad (Jacobian-weighted)")
            t_bin0 = time.perf_counter()
            THX_c, THY_c, L_c, s_c, P_c = bin_results_jacobian(
                self.THX_f, self.THY_f, self.L_mc_mean,
                self.fine_step_mrad, result_step_mrad,
                sigma=self.sigmaL_mc, P=self.P_mc
            )
            self.THX_c_mc, self.THY_c_mc = THX_c, THY_c
            self.L_c_mc = L_c
            self.sigmaL_c_mc = s_c
            self.P_c_mc = P_c
            self._result_step_mrad_mc = float(result_step_mrad)
            t_bin1 = time.perf_counter()
            prof.add("post:bin_by_jacobian(mc)", (t_bin1 - t_bin0))
            self.logger.info(f"Done binning in {t_bin1 - t_bin0:.2f}s; coarse shape={self.L_c_mc.shape}")

        # print profile if asked
        if profile:
            self.print_profile("Thickness" + (" (Monte-Carlo)" if calculate_sigma else ""))

        if return_profile:
            return self, prof
        return self

    # ---------------- Orientation helpers ----------------
    @staticmethod
    def orient_xy(THX, THY, Z, *, transpose=False, flip_axis=None):
        X = THX; Y = THY; W = Z
        if transpose:
            X = X.T; Y = Y.T
            W = W.T if W.ndim == 2 else W.transpose(0, 2, 1)
        if flip_axis is not None:
            if flip_axis == 0:
                X = X[::-1, :]; Y = Y[::-1, :]
                W = W[::-1, :] if W.ndim == 2 else W[:, ::-1, :]
            elif flip_axis == 1:
                X = X[:, ::-1]; Y = Y[:, ::-1]
                W = W[:, ::-1] if W.ndim == 2 else W[:, :, ::-1]
        return X, Y, W

    # ---------------- Helpers to get coarse arrays ----------------
    def _coarse_det(self):
        return self.THX_c, self.THY_c, self.L_c

    def _coarse_mc(self):
        return self.THX_c_mc, self.THY_c_mc, self.L_c_mc, self.sigmaL_c_mc, self.P_c_mc

    # ---------------- Export (ALWAYS coarse; include MC if available) ----------------
    def export_npz(self,
                   out_path: str,
                   *,
                   extra_meta: dict | None = None):
        """
        Always exports coarse deterministic map.
        If MC coarse exists, also export MC coarse maps in the same file.
        Keys:
          - Deterministic: THX_rad_det, THY_rad_det, L_det
          - MC (if present): THX_rad_mc, THY_rad_mc, L_mc_mean, sigmaL_mc, P_mc
        """
        THX_det, THY_det, L_det = self._coarse_det()
        if L_det is None:
            raise RuntimeError("No coarse deterministic results to export. Run compute_thickness() first.")

        t0 = time.perf_counter()

        # Orient deterministic coarse to (xy) order
        THX_o_det, THY_o_det, L_o_det = self.orient_xy(THX_det, THY_det, L_det, transpose=True, flip_axis=1)
        payload = dict(
            THX_rad_det=THX_o_det,
            THY_rad_det=THY_o_det,
            THX_mrad_det=(THX_o_det * 1e3),
            THY_mrad_det=(THY_o_det * 1e3),
            L_det=L_o_det
        )

        # If MC coarse exists, export it too (with its own grid keys)
        THX_mc, THY_mc, L_mc, s_mc, P_mc = self._coarse_mc()
        if L_mc is not None:
            THX_o_mc, THY_o_mc, L_o_mc = self.orient_xy(THX_mc, THY_mc, L_mc, transpose=True, flip_axis=1)
            payload.update(
                THX_rad_mc=THX_o_mc,
                THY_rad_mc=THY_o_mc,
                THX_mrad_mc=(THX_o_mc * 1e3),
                THY_mrad_mc=(THY_o_mc * 1e3),
                L_mc_mean=L_o_mc
            )
            if s_mc is not None:
                _, _, s_o_mc = self.orient_xy(THX_mc, THY_mc, s_mc, transpose=True, flip_axis=1)
                payload["sigmaL_mc"] = s_o_mc
            if P_mc is not None:
                _, _, P_o_mc = self.orient_xy(THX_mc, THY_mc, P_mc, transpose=True, flip_axis=1)
                payload["P_mc"] = P_o_mc

        ds_coarse = self.ds_coarse_scale * min(self.dx, self.dy)
        meta = dict(
            angle_deg=float(self.angle_deg),
            det_azimuth_deg=float(self.det_azimuth_deg),
            dem_azimuth_deg=float(self.dem_azimuth_deg),
            window_deg=float(self.angle_window_deg),
            fine_mrad_step=float(self.fine_step_mrad),
            result_mrad_step_det=float(self._result_step_mrad) if self._result_step_mrad is not None else None,
            result_mrad_step_mc=float(self._result_step_mrad_mc) if self._result_step_mrad_mc is not None else None,
            s_max=float(self.s_max),
            ds_coarse=float(ds_coarse),
            eps_bisect=float(self.eps_bisect),
            max_bisect=int(self.max_bisect),
            dem_bounds=(float(self.x0g), float(self.x1g), float(self.y0g), float(self.y1g)),
            z0=float(self.z0),
            flips=dict(flip_x=bool(self.flip_x), flip_y=bool(self.flip_y)),
            notes="Coarse deterministic always included; MC coarse included if available."
        )
        if extra_meta:
            meta.update(extra_meta)
        payload["meta"] = meta

        np.savez(out_path, **payload)
        t1 = time.perf_counter()
        self.logger.info(f"Saved NPZ → {out_path} ({t1 - t0:.2f}s)")
        if self._prof is not None:
            self._prof.add("io:export_npz", (t1 - t0))
        return out_path

    # ---------------- Plot (ALWAYS coarse; plot both if MC exists) ----------------
    def plot(self, *, show=True):
        """
        Plots the coarse deterministic map; if MC coarse exists, plots it too.
        """
        import matplotlib.pyplot as plt
        t0 = time.perf_counter()

        # Deterministic coarse (required)
        THX_det, THY_det, L_det = self._coarse_det()
        if L_det is None:
            raise RuntimeError("Nothing to plot. Coarse deterministic map not available.")

        THX_o, THY_o, L_o = self.orient_xy(THX_det, THY_det, L_det, transpose=True, flip_axis=1)
        self.logger.info("Plotting deterministic coarse…")
        plt.figure()
        im = plt.imshow(L_o.T, aspect='equal')
        plt.colorbar(im, label="L_det (m)")
        plt.xlabel("Theta X (mrad)"); plt.ylabel("Theta Y (mrad)")
        plt.title("Thickness (deterministic, coarse)")

        # MC coarse (optional)
        THX_mc, THY_mc, L_mc, s_mc, P_mc = self._coarse_mc()
        if L_mc is not None:
            THX_o_mc, THY_o_mc, L_o_mc = self.orient_xy(THX_mc, THY_mc, L_mc, transpose=True, flip_axis=1)
            self.logger.info("Plotting MC coarse…")
            plt.figure()
            im = plt.imshow(L_o_mc.T, aspect='equal')
            plt.colorbar(im, label="E[L] (m)")
            plt.xlabel("Theta X (mrad)"); plt.ylabel("Theta Y (mrad)")
            plt.title("Thickness (MC mean, coarse)")

            if s_mc is not None:
                _, _, sL_o_mc = self.orient_xy(THX_mc, THY_mc, s_mc, transpose=True, flip_axis=1)
                plt.figure()
                im = plt.imshow(sL_o_mc.T, aspect='equal')
                plt.colorbar(im, label="σ_L (m)")
                plt.xlabel("Theta X (mrad)"); plt.ylabel("Theta Y (mrad)")
                plt.title("Thickness uncertainty (MC, coarse)")

            if P_mc is not None:
                _, _, P_o_mc = self.orient_xy(THX_mc, THY_mc, P_mc, transpose=True, flip_axis=1)
                plt.figure()
                im = plt.imshow(P_o_mc.T, aspect='equal', vmin=0, vmax=1)
                plt.colorbar(im, label="P(hit)")
                plt.xlabel("Theta X (mrad)"); plt.ylabel("Theta Y (mrad)")
                plt.title("Hit probability (MC, coarse)")

        plt.tight_layout()
        if show: plt.show()
        t1 = time.perf_counter()
        if self._prof is not None:
            self._prof.add("viz:plot", (t1 - t0))
