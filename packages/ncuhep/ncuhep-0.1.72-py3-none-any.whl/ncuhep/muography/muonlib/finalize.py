import json
import datetime
import numpy as np
import matplotlib.pyplot as plt

# ---- Small array flip helpers ----
def _flip_cols(Z):
    return Z[:, ::-1] if Z.ndim == 2 else Z[:, :, ::-1]

def _flip_rows(Z):
    return Z[::-1, :] if Z.ndim == 2 else Z[:, ::-1, :]

def _delta_sign(a, axis='x'):
    if axis == 'x':       # across columns
        return a[0, 1] - a[0, 0] if a.shape[1] > 1 else 1.0
    if axis == 'x_down':  # down rows
        return a[1, 0] - a[0, 0] if a.shape[0] > 1 else 1.0
    if axis == 'y_across':
        return a[0, 1] - a[0, 0] if a.shape[1] > 1 else 1.0
    if axis == 'y':
        return a[1, 0] - a[0, 0] if a.shape[0] > 1 else 1.0
    raise ValueError("bad axis")

def _ensure_xy_ascending(THX_mrad, THY_mrad, Z_like):
    X = np.asarray(THX_mrad); Y = np.asarray(THY_mrad); Z = Z_like
    xdx = _delta_sign(X, 'x'); xdy = _delta_sign(X, 'x_down')
    ydx = _delta_sign(Y, 'y_across'); ydy = _delta_sign(Y, 'y')
    swapped = (xdx == 0 and xdy != 0 and ydx != 0 and ydy == 0)
    if swapped:
        X = X.T; Y = Y.T
        Z = Z.T if Z.ndim == 2 else Z.transpose(0, 2, 1)

    if X[0, 0] > X[0, -1]:
        X = X[:, ::-1].copy(); Z = _flip_cols(Z).copy()
    if Y[0, 0] > Y[-1, 0]:
        Y = Y[::-1, :].copy(); Z = _flip_rows(Z).copy()
    return X, Y, Z

def _crop_window(THX_mrad, THY_mrad, Z_like, half_angle_deg):
    A_mrad = np.radians(half_angle_deg) * 1e3
    x = THX_mrad[0, :]; y = THY_mrad[:, 0]
    ix = np.where((x >= -A_mrad) & (x <= A_mrad))[0]
    iy = np.where((y >= -A_mrad) & (y <= A_mrad))[0]
    if ix.size == 0 or iy.size == 0:
        return (THX_mrad[:0, :0], THY_mrad[:0, :0],
                Z_like[:0, :0] if Z_like.ndim == 2 else Z_like[:, :0, :0])
    iy0, iy1 = iy.min(), iy.max() + 1
    ix0, ix1 = ix.min(), ix.max() + 1
    THXc = THX_mrad[iy0:iy1, ix0:ix1]
    THYc = THY_mrad[iy0:iy1, ix0:ix1]
    Zc   = Z_like[iy0:iy1, ix0:ix1] if Z_like.ndim == 2 else Z_like[:, iy0:iy1, ix0:ix1]
    return THXc, THYc, Zc

def _resample_bilinear(THX_mrad, THY_mrad, Z2d, x_new, y_new):
    x_src = THX_mrad[0, :]; y_src = THY_mrad[:, 0]
    dx = x_src[1] - x_src[0] if x_src.size > 1 else 1.0
    dy = y_src[1] - y_src[0] if y_src.size > 1 else 1.0
    fx = (x_new - x_src[0]) / dx; fy = (y_new - y_src[0]) / dy
    fx = np.clip(fx, 0, x_src.size - 1 - 1e-9)
    fy = np.clip(fy, 0, y_src.size - 1 - 1e-9)
    ix = np.floor(fx).astype(np.int64); iy = np.floor(fy).astype(np.int64)
    tx = fx - ix; ty = fy - iy

    Z00 = Z2d[iy[:, None],     ix[None, :]]
    Z10 = Z2d[iy[:, None] + 1, ix[None, :]]
    Z01 = Z2d[iy[:, None],     ix[None, :] + 1]
    Z11 = Z2d[iy[:, None] + 1, ix[None, :] + 1]

    wx0 = (1.0 - tx)[None, :]; wx1 = tx[None, :]
    wy0 = (1.0 - ty)[:, None]; wy1 = ty[:, None]
    return (Z00 * wx0 * wy0 + Z01 * wx1 * wy0 + Z10 * wx0 * wy1 + Z11 * wx1 * wy1)

def _resample_stack(THX_mrad, THY_mrad, Z_stack, x_new, y_new):
    out = np.empty((Z_stack.shape[0], y_new.size, x_new.size), dtype=Z_stack.dtype)
    for k in range(Z_stack.shape[0]):
        out[k] = _resample_bilinear(THX_mrad, THY_mrad, Z_stack[k], x_new, y_new)
    return out

def finalize_map(THX_mrad, THY_mrad, Z, crop_half_angle_deg=13.0, target_mrad_step=1.0):
    xdx = _delta_sign(THX_mrad, 'x');  xdy = _delta_sign(THX_mrad, 'x_down')
    ydx = _delta_sign(THY_mrad, 'y_across'); ydy = _delta_sign(THY_mrad, 'y')

    THX_n, THY_n, Z_n = _ensure_xy_ascending(THX_mrad, THY_mrad, Z)
    THX_c, THY_c, Z_c = _crop_window(THX_n, THY_n, Z_n, crop_half_angle_deg)
    if THX_c.size == 0: return THX_c, THY_c, Z_c

    A_mrad = np.radians(crop_half_angle_deg) * 1e3
    x_new = np.arange(-A_mrad, A_mrad + 1e-12, target_mrad_step, dtype=np.float64)
    y_new = np.arange(-A_mrad, A_mrad + 1e-12, target_mrad_step, dtype=np.float64)

    if THX_c.shape[0] < 2 or THX_c.shape[1] < 2:
        Xg, Yg = np.meshgrid(x_new, y_new, indexing="xy")
        Zr = np.full_like(Xg, Z_c.mean(), dtype=Z_c.dtype)
    else:
        Zr = _resample_bilinear(THX_c, THY_c, Z_c, x_new, y_new)
        Xg, Yg = np.meshgrid(x_new, y_new, indexing="xy")

    xdxg = _delta_sign(Xg, 'x');   xdyg = _delta_sign(Xg, 'x_down')
    ydxg = _delta_sign(Yg, 'y_across'); ydyg = _delta_sign(Yg, 'y')

    if ((xdx == 0) ^ (xdxg == 0)) and ((xdy == 0) ^ (xdyg == 0)) and ((ydx == 0) ^ (ydxg == 0)) and ((ydy == 0) ^ (ydyg == 0)):
        Xg = Xg.T; Yg = Yg.T; Zr = Zr.T

    xdxg = _delta_sign(Xg, 'x');   xdyg = _delta_sign(Xg, 'x_down')
    ydxg = _delta_sign(Yg, 'y_across'); ydyg = _delta_sign(Yg, 'y')

    if not (xdx == 0 and xdxg == 0) and (xdx != 0 and xdxg != 0) and (np.sign(xdx) != np.sign(xdxg)):
        Xg = Xg[:, ::-1]; Yg = Yg[:, ::-1]; Zr = Zr[:, ::-1]
    if not (xdy == 0 and xdyg == 0) and (xdy != 0 and xdyg != 0) and (np.sign(xdy) != np.sign(xdyg)):
        Xg = Xg[::-1, :]; Yg = Yg[::-1, :]; Zr = Zr[::-1, :]
    if not (ydx == 0 and ydxg == 0) and (ydx != 0 and ydxg != 0) and (np.sign(ydx) != np.sign(ydxg)):
        Xg = Xg[:, ::-1]; Yg = Yg[:, ::-1]; Zr = Zr[:, ::-1]
    if not (ydy == 0 and ydyg == 0) and (ydy != 0 and ydyg != 0) and (np.sign(ydy) != np.sign(ydyg)):
        Xg = Xg[::-1, :]; Yg = Yg[::-1, :]; Zr = Zr[::-1, :]

    return Xg, Yg, Zr

def finalize_stack(THX_mrad, THY_mrad, Z_stack, crop_half_angle_deg=13.0, target_mrad_step=1.0):
    xdx = _delta_sign(THX_mrad, 'x');  xdy = _delta_sign(THX_mrad, 'x_down')
    ydx = _delta_sign(THY_mrad, 'y_across'); ydy = _delta_sign(THY_mrad, 'y')

    THX_n, THY_n, Z_n = _ensure_xy_ascending(THX_mrad, THY_mrad, Z_stack)
    THX_c, THY_c, Z_c = _crop_window(THX_n, THY_n, Z_n, crop_half_angle_deg)
    if THX_c.size == 0: return THX_c, THY_c, Z_c

    A_mrad = np.radians(crop_half_angle_deg) * 1e3
    x_new = np.arange(-A_mrad, A_mrad + 1e-12, target_mrad_step, dtype=np.float64)
    y_new = np.arange(-A_mrad, A_mrad + 1e-12, target_mrad_step, dtype=np.float64)

    if THX_c.shape[0] < 2 or THX_c.shape[1] < 2:
        Xg, Yg = np.meshgrid(x_new, y_new, indexing="xy")
        Zr = np.full((Z_c.shape[0], y_new.size, x_new.size), Z_c.mean(), dtype=Z_c.dtype)
    else:
        Zr = _resample_stack(THX_c, THY_c, Z_c, x_new, y_new)
        Xg, Yg = np.meshgrid(x_new, y_new, indexing="xy")

    xdxg = _delta_sign(Xg, 'x');   xdyg = _delta_sign(Xg, 'x_down')
    ydxg = _delta_sign(Yg, 'y_across'); ydyg = _delta_sign(Yg, 'y')

    if ((xdx == 0) ^ (xdxg == 0)) and ((xdy == 0) ^ (xdyg == 0)) and ((ydx == 0) ^ (ydxg == 0)) and ((ydy == 0) ^ (ydyg == 0)):
        Xg = Xg.T; Yg = Yg.T; Zr = Zr.transpose(0, 2, 1)

    xdxg = _delta_sign(Xg, 'x');   xdyg = _delta_sign(Xg, 'x_down')
    ydxg = _delta_sign(Yg, 'y_across'); ydyg = _delta_sign(Yg, 'y')

    if not (xdx == 0 and xdxg == 0) and (xdx != 0 and xdxg != 0) and (np.sign(xdx) != np.sign(xdxg)):
        Xg = Xg[:, ::-1]; Yg = Yg[:, ::-1]; Zr = Zr[:, :, ::-1]
    if not (xdy == 0 and xdyg == 0) and (xdy != 0 and xdyg != 0) and (np.sign(xdy) != np.sign(xdyg)):
        Xg = Xg[::-1, :]; Yg = Yg[::-1, :]; Zr = Zr[:, ::-1, :]
    if not (ydx == 0 and ydxg == 0) and (ydx != 0 and ydxg != 0) and (np.sign(ydx) != np.sign(ydxg)):
        Xg = Xg[:, ::-1]; Yg = Yg[:, ::-1]; Zr = Zr[:, :, ::-1]
    if not (ydy == 0 and ydyg == 0) and (ydy != 0 and ydyg != 0) and (np.sign(ydy) != np.sign(ydyg)):
        Xg = Xg[::-1, :]; Yg = Yg[::-1, :]; Zr = Zr[:, ::-1, :]

    return Xg, Yg, Zr

def _extent_from_axes(THX_mrad: np.ndarray, THY_mrad: np.ndarray):
    return [THX_mrad.min(), THX_mrad.max(), THY_mrad.min(), THY_mrad.max()]

# ---- Plot helpers ----
def plot_single_map(THX_mrad, THY_mrad, Z, title="dΦ_D/dE", plot_grid=False):
    extent = _extent_from_axes(THX_mrad, THY_mrad)
    plt.figure(figsize=(6.6,5.6))
    im = plt.imshow(Z.T, extent=extent, aspect="equal")
    plt.xlabel(r"$\theta_x$ (mrad)"); plt.ylabel(r"$\theta_y$ (mrad)")
    plt.title(title)
    c = plt.colorbar(im); c.set_label(r"m$^{-2}$ s$^{-1}$ sr$^{-1}$ GeV$^{-1}$")
    plt.tight_layout()

    if plot_grid:
        plt.figure(figsize=(6.6, 5.6))
        im = plt.imshow(THX_mrad.T, extent=extent, aspect="equal")
        plt.xlabel(r"$\theta_x$ (mrad)"); plt.ylabel(r"$\theta_y$ (mrad)")
        plt.title(r"$\theta_x$ grid"); c = plt.colorbar(im); c.set_label(r"mrad")
        plt.tight_layout()

        plt.figure(figsize=(6.6, 5.6))
        im = plt.imshow(THY_mrad.T, extent=extent, aspect="equal")
        plt.xlabel(r"$\theta_x$ (mrad)"); plt.ylabel(r"$\theta_y$ (mrad)")
        plt.title(r"$\theta_y$ grid"); c = plt.colorbar(im); c.set_label(r"mrad")
        plt.tight_layout()

def plot_energy_stack(energies, THX_mrad, THY_mrad, Z_stack, plot_grid=False):
    nb = len(energies)
    ncols = int(np.ceil(np.sqrt(nb))); nrows = int(np.ceil(nb / ncols))
    extent = _extent_from_axes(THX_mrad, THY_mrad)
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.6*ncols, 3.2*nrows), squeeze=False)
    vmin = np.min(Z_stack); vmax = np.max(Z_stack)
    for ax in axes.ravel(): ax.axis("off")
    for k in range(nb):
        r = k // ncols; c = k % ncols
        ax = axes[r, c]; ax.axis("on")
        im = ax.imshow(Z_stack[k].T, extent=extent, aspect="equal", vmin=vmin, vmax=vmax)
        ax.set_title(rf"$E={energies[k]:.3g}$ GeV")
        ax.set_xlabel(r"$\theta_x$ (mrad)"); ax.set_ylabel(r"$\theta_y$ (mrad)")
    fig.subplots_adjust(right=0.88, wspace=0.25, hspace=0.35)
    cax = fig.add_axes([0.90, 0.15, 0.02, 0.7])
    fig.colorbar(im, cax=cax, label=r"m$^{-2}$ s$^{-1}$ sr$^{-1}$ GeV$^{-1}$")
    fig.suptitle(r"$d\Phi_D/dE$ maps", y=0.99)
    plt.tight_layout(rect=[0,0,0.88,0.97])

def _energy_bin_widths_from_centers(energies: np.ndarray) -> np.ndarray:
    E = np.asarray(energies, dtype=float)
    if E.ndim != 1 or E.size < 2: raise ValueError("energies must be 1D with length >= 2")
    edges = np.empty(E.size + 1, dtype=float)
    edges[1:-1] = 0.5 * (E[:-1] + E[1:])
    edges[0]  = E[0]  - (edges[1]  - E[0])
    edges[-1] = E[-1] + (E[-1] - edges[-2])
    if edges[0] <= 0: edges[0] = max(1e-12, 0.5 * E[0])
    return np.diff(edges)

def plot_integrated_spectrum(energies, THX_mrad, THY_mrad, Z_stack):
    THX_rad = THX_mrad / 1e3; THY_rad = THY_mrad / 1e3
    cx = np.cos(THX_rad); cy = np.cos(THY_rad)
    tx = np.tan(THX_rad); ty = np.tan(THY_rad)
    Jdet = (1.0/(cx*cx) * 1.0/(cy*cy)) / np.power(1.0 + tx*tx + ty*ty, 1.5)
    dthx = abs(THX_rad[0,1] - THX_rad[0,0]) if THX_rad.shape[1] > 1 else 1.0
    dthy = abs(THY_rad[1,0] - THY_rad[0,0]) if THY_rad.shape[0] > 1 else 1.0
    if dthx == 0.0: dthx = abs(THX_rad[1,0] - THX_rad[0,0]) if THX_rad.shape[0] > 1 else 1.0
    if dthy == 0.0: dthy = abs(THY_rad[0,1] - THY_rad[0,0]) if THY_rad.shape[1] > 1 else 1.0
    Phi = np.array([np.sum(Z_stack[k] * Jdet) * dthx * dthy for k in range(Z_stack.shape[0])])
    plt.figure(figsize=(6.0,4.4))
    plt.loglog(energies, Phi, marker="o")
    plt.xlabel("E (GeV)"); plt.ylabel(r"$\Phi(E)$  [m$^{-2}$ s$^{-1}$ GeV$^{-1}$]")
    plt.title("Integrated flux over FOV")
    plt.grid(True, which="both", ls=":")
    plt.tight_layout()

def plot_sum_or_integrated_map(energies, THX_mrad, THY_mrad, Z_stack, integrate_over_energy=False, title=None):
    if Z_stack.ndim != 3: raise ValueError("Z_stack must be (nbins, H, W).")
    if Z_stack.shape[0] != energies.size: raise ValueError("Z_stack[0] must equal len(energies).")
    if integrate_over_energy:
        widths = _energy_bin_widths_from_centers(energies)
        Z_plot = (Z_stack * widths[:, None, None]).sum(axis=0)
        cbar_label = r"m$^{-2}$ s$^{-1}$ sr$^{-1}$"
        default_title = r"$\int dE\, d\Phi_D/dE$"
    else:
        Z_plot = Z_stack.sum(axis=0)
        cbar_label = r"m$^{-2}$ s$^{-1}$ sr$^{-1}$ GeV$^{-1}$"
        default_title = r"$\sum_i (d\Phi_D/dE)(E_i)$"
    extent = _extent_from_axes(THX_mrad, THY_mrad)
    plt.figure(figsize=(6.8, 5.6))
    im = plt.imshow(Z_plot.T, extent=extent, aspect="equal")
    plt.xlabel(r"$\theta_x$ (mrad)"); plt.ylabel(r"$\theta_y$ (mrad)")
    plt.title(title if title is not None else default_title)
    c = plt.colorbar(im); c.set_label(cbar_label)
    plt.tight_layout()
    return Z_plot

def export_finalized_maps_npz(
    out_path: str,
    THX_mrad: np.ndarray,
    THY_mrad: np.ndarray,
    Z: np.ndarray,
    *,
    energies_GeV: np.ndarray | None = None,
    energy_edges_GeV: np.ndarray | None = None,
    crop_half_angle_deg: float | None = None,
    target_mrad_step: float | None = None,
    extra_meta: dict | None = None,
    include_unweighted: bool = True,
):
    THX_mrad = np.asarray(THX_mrad, dtype=np.float64)
    THY_mrad = np.asarray(THY_mrad, dtype=np.float64)
    Z        = np.asarray(Z,        dtype=np.float64)
    if THX_mrad.shape != THY_mrad.shape:
        raise ValueError("THX_mrad and THY_mrad must have the same shape (H, W).")
    H, W = THX_mrad.shape
    def _safe_step(v): return float(v[1] - v[0]) if v.size > 1 else np.nan
    x_axis = THX_mrad[0, :]; y_axis = THY_mrad[:, 0]
    dx_mrad = _safe_step(x_axis); dy_mrad = _safe_step(y_axis)
    window_x = (float(x_axis.min()), float(x_axis.max()))
    window_y = (float(y_axis.min()), float(y_axis.max()))
    meta = dict(
        created_utc_iso = datetime.datetime.utcnow().isoformat() + "Z",
        grid_shape      = [int(H), int(W)],
        angles_units    = "mrad",
        values_units    = dict(Z="m^-2 s^-1 sr^-1 GeV^-1", Z_dE="m^-2 s^-1 sr^-1"),
        processing      = dict(
            stage="finalized (axes normalized, crop, bilinear resample)",
            plotting_recommendation="imshow(..., origin='upper', extent=[xmin,xmax,ymin,ymax], aspect='equal')",
            crop_half_angle_deg = None if crop_half_angle_deg is None else float(crop_half_angle_deg),
            target_mrad_step    = None if target_mrad_step    is None else float(target_mrad_step),
            realized_pixel_mrad = dict(dx=float(dx_mrad), dy=float(dy_mrad)),
            realized_window_mrad= dict(x=list(window_x), y=list(window_y)),
        ),
    )
    if extra_meta:
        for k, v in extra_meta.items():
            try: json.dumps({k: v}); meta[k] = v
            except Exception: meta[k] = str(v)
    energies = None; edges = None; dE = None; Z_dE = None
    if energies_GeV is not None:
        energies = np.asarray(energies_GeV, dtype=np.float64)
        if energies.ndim != 1: raise ValueError("energies_GeV must be 1D.")
        if energies.size >= 2:
            edges = np.empty(energies.size + 1, dtype=np.float64)
            edges[1:-1] = 0.5 * (energies[:-1] + energies[1:])
            edges[0]    = energies[0]  - (edges[1]  - energies[0])
            edges[-1]   = energies[-1] + (energies[-1] - edges[-2])
            if edges[0] <= 0: edges[0] = max(1e-12, 0.5 * energies[0])
            dE = np.diff(edges)
        elif energies.size == 1 and energy_edges_GeV is not None and len(energy_edges_GeV) == 2:
            edges = np.asarray(energy_edges_GeV, dtype=np.float64); dE = np.diff(edges)
    if energy_edges_GeV is not None and edges is None:
        edges = np.asarray(energy_edges_GeV, dtype=np.float64)
        if edges.ndim != 1 or edges.size < 2:
            raise ValueError("energy_edges_GeV must be 1D with length >= 2.")
        dE = np.diff(edges)
        if energies is None: energies = 0.5 * (edges[:-1] + edges[1:])
    if dE is not None:
        if Z.ndim == 3:
            if Z.shape[0] != dE.size: raise ValueError("Z stack length != #energy bins.")
            Z_dE = Z * dE[:, None, None]
        elif Z.ndim == 2:
            if dE.size != 1: raise ValueError("2D Z requires exactly one ΔE.")
            Z_dE = Z * float(dE[0])
    payload = dict(THX_mrad=THX_mrad, THY_mrad=THY_mrad, meta_json=json.dumps(meta))
    if include_unweighted: payload["Z"] = Z
    if energies is not None: payload["energies_GeV"] = energies
    if edges is not None:
        payload["energy_edges_GeV"] = edges; payload["dE_GeV"] = dE
    if Z_dE is not None: payload["Z_dE"] = Z_dE
    np.savez_compressed(out_path, **payload)
    print(f"[INFO] Saved '{out_path}'")
