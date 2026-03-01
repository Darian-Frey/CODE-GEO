import math
import random

def simulate_fuzzball_core(mass_solar):
    # Constants
    G = 6.67430e-11
    c = 299792458
    M_sun = 1.989e30
    PLANCK_LENGTH = 1.616e-35
    PLANCK_MASS = 2.176e-8
    
    # 1. Standard Schwarzschild Radius (The Classical 'Shell')
    M = mass_solar * M_sun
    r_s = (2 * G * M) / (c**2)
    
    # 2. CODE-GEO Information Core Radius (The 'Fuzzball' center)
    # R_core = (M/M_p)^(1/3) * L_p
    r_core = math.pow(M / PLANCK_MASS, 1/3) * PLANCK_LENGTH
    
    print(f"--- Project CODE-GEO: Fuzzball Core Simulation ---")
    print(f"Target: {mass_solar} Solar Mass Black Hole")
    print(f"Classical Singularity: 0.000 m (Infinite Density)")
    print(f"CODE-GEO Core Radius:  {r_core:.2e} meters")
    print("-" * 50)
    print(f"{'Time (Planck)':<15} | {'Horizon Jitter (Planck Lengths)':<30}")
    print("-" * 50)
    
    # 3. Simulate Horizon Fuzziness (Stochastic Jitter)
    # The horizon isn't fixed; it 'vibrates' due to the Information core
    for t in range(5):
        jitter = random.uniform(-1.0, 1.0) # Jitter in Planck units
        print(f"{t:<15} | {jitter:<30.4f}")

if __name__ == "__main__":
    # Simulate for a stellar-mass black hole (e.g., 10 Solar Masses)
    simulate_fuzzball_core(10.0)
