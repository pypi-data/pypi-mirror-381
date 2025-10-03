# grf.py
import numpy as np
import numpy.fft as _fft

def gaussian_random_field(shape, dx, dy, sigma, corr_len_m, rng):
    """
    Gaussian random field with optional Gaussian correlation.
    Falls back to white noise if the frequency response is ~1.
    """
    H, W = shape
    if sigma <= 0.0:
        return np.zeros(shape, dtype=float)

    if corr_len_m is None or corr_len_m <= 0.0:
        return rng.normal(0.0, sigma, size=shape)

    l2 = float(corr_len_m) ** 2
    kx_max = np.pi / float(dx)
    ky_max = np.pi / float(dy)
    Kmax2  = kx_max * kx_max + ky_max * ky_max
    delta = 1.0 - np.exp(-0.5 * l2 * Kmax2)

    if delta < 1e-6:
        return rng.normal(0.0, sigma, size=shape)

    wn = rng.normal(0.0, 1.0, size=shape)

    kx = 2.0 * np.pi * _fft.fftfreq(W, d=dx)
    ky = 2.0 * np.pi * _fft.fftfreq(H, d=dy)
    KX, KY = np.meshgrid(kx, ky, indexing="xy")
    K2 = KX * KX + KY * KY

    Hk = np.exp(-0.5 * l2 * K2)

    WN = _fft.fft2(wn)
    F  = WN * Hk
    field = _fft.ifft2(F).real

    s = field.std()
    if s > 0.0:
        field *= (sigma / s)
    else:
        field = rng.normal(0.0, sigma, size=shape)

    return field
