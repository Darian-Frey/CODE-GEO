"""
CODE-GEO V3 Consistency Audit
Script: linearized_dispersion.py
Role: Verifies the 'Slow-Light' Refractive Index of the 2.0 Rs Shell.
Reference: docs/REASONING_LOG.md
"""
import math

C = 299792458.0
G = 6.67430e-11
M_SOLAR = 1.9891e30
M_REMNANT = 62.7 * M_SOLAR
RS = (2 * G * M_REMNANT) / (C**2)  # ~185.233 km

F_KERR = 284.60
F_ECHO = 355.11
DF_OBSERVED = F_ECHO - F_KERR # 70.51 Hz

def verify_refractive_index():
    t_crossing_vacuum = RS / C
    
    # In CODE-GEO, the echo delay (2.816ms) and the spectral gap (70.51Hz)
    # must be consistent with the Refractive Index 'n'.
    
    # 1. n from Time Delay: t_delay = n * (RS / C)
    # Note: Using RS as shell thickness (2Rs - 1Rs)
    n_delay = 0.002816 / t_crossing_vacuum
    
    # 2. n from Spectral Gap: df = (1 / 4t) * (1 / n)
    n_spectral = (1 / (4 * t_crossing_vacuum)) / DF_OBSERVED
    
    print(f"--- REFRACTIVE INDEX AUDIT (V3.2) ---")
    print(f"n (from Delay):    {n_delay:.4f}")
    print(f"n (from Spectrum): {n_spectral:.4f}")
    print(f"---------------------------------------------")
    
    variance = abs(n_delay - n_spectral)
    print(f"Index Variance:    {variance:.4f}")
    print(f"---------------------------------------------")
    print(f"RESULT: {'STABLE' if variance < 0.2 else 'UNSTABLE'}")
    print(f"Conclusion: Shell acts as a medium with n ≈ {n_delay:.2f}")

if __name__ == "__main__":
    verify_refractive_index()
