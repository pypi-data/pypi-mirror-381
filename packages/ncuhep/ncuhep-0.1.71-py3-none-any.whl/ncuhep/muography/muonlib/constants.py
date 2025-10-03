# Simulation limits / guards
L_MIN_FIT_M        = 40.0
L_MAX_FIT_M        = 1000.0
E_MIN_ALLOWED_GEV  = 22.4
E_MAX_FLUX_FIT_GEV = 4000.0
E_MAX_GEANT4_GEV   = 10000.0

# Units / physical constants
RHO0_G_CM3 = 2.65
CM2_TO_M2  = 1.0e4

# Survival (A, C, E0, n) coefficients
A_c3, A_c2, A_c1, A_c0 = 2.8221e-11, 1.2763e-7, 8.0243e-5, -5.4220e-4
C_c2, C_c1, C_c0       = 5.9205e-8, -6.7653e-6, 1.2987e-5
E0_a, E0_b, E0_c       = 1.1266, 1.0015, -1.2611
n_a1, n_b1             = -3.4521e-2, 11.066
n_a2, n_b2, n_c2       = 1.0492e-6, -1.4736e-3, 1.9579
n_x0, n_D              = -124.70, 200.0

# Scattering master coefficients
A_m_sigma, A_c_sigma = -5.3808e-4, 1.7001
A_m_crit,  A_c_crit  = -6.9970e-4, 1.8271

tau_m_sigma, tau_c_sigma = 1.5252e-4, 0.35566
tau_m_crit,  tau_c_crit  = 3.5246e-4, 0.29311

LN_E0_SIGMA_COEFFS = (2.6114e-3, -7.4551e-2, 0.88019, -5.4858, 18.985, -33.427, 24.807)
LN_E0_CRIT_COEFFS  = (2.2684e-3, -6.35752e-2, 0.74026, -4.5275, 15.302, -25.810, 18.023)

n_sigma = (-5.6105e-7, 6.0565e-4, 0.62974)
n_crit  = (-6.2242e-8, 3.0192e-4, 0.53446)

c_sigma = (0.055067, 0.079360, -2.2735)
c_crit  = (0.015468, 0.32582, -1.3413)

# Atmospheric flux params
P1, P2, P3, P4, P5 = 0.102573, -0.068287, 0.958633, 0.0407253, 0.817285
