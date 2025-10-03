"""
muonlib: forward muography modeling with CPU (Numba) and optional GPU (Numba CUDA).

Primary API:
    - MuonForwardModel

Useful helpers re-exported:
    - finalize_map, finalize_stack
    - export_finalized_maps_npz
    - plot_single_map, plot_energy_stack, plot_sum_or_integrated_map, plot_integrated_spectrum
"""

from .engine import MuonForwardModel

# Finalization / plotting / export helpers
from .finalize import (
    finalize_map, finalize_stack,
    export_finalized_maps_npz,
    plot_single_map, plot_energy_stack,
    plot_sum_or_integrated_map, plot_integrated_spectrum
)

# Optional: expose profiler utils
from .profiling import Profiler, Section, _print_profile

__all__ = [
    "MuonForwardModel",
    "finalize_map", "finalize_stack",
    "export_finalized_maps_npz",
    "plot_single_map", "plot_energy_stack",
    "plot_sum_or_integrated_map", "plot_integrated_spectrum",
    "Profiler", "Section", "_print_profile",
]
