import math

def simulate_evaporation(mass_solar):
    # Constants
    G = 6.67430e-11
    hbar = 1.05457e-34
    c = 299792458
    M_sun = 1.989e30
    
    M = mass_solar * M_sun
    
    # 1. Hawking Temperature (The 'Clock Speed' of evaporation)
    # T = (hbar * c^3) / (8 * pi * G * M * k_b) 
    # We simplify to find the Power (P)
    power = (hbar * math.pow(c, 6)) / (15360 * math.pi * math.pow(G, 2) * math.pow(M, 2))
    
    # 2. Total Evaporation Time (t_evap) in Years
    # t = 5120 * pi * G^2 * M^3 / (hbar * c^4)
    t_sec = (5120 * math.pi * math.pow(G, 2) * math.pow(M, 3)) / (hbar * math.pow(c, 4))
    t_years = t_sec / (365.25 * 24 * 3600)
    
    # 3. Code Recovery Rate (Bits per second)
    # Based on Bekenstein-Hawking entropy S = A/4
    # dS/dt represents the information leakage rate
    bit_leakage = power / (1.38e-23 * 1e-10) # Simplified informational flux
    
    print(f"--- Project CODE-GEO: Evaporation Analysis ---")
    print(f"Mass: {mass_solar} Solar Masses")
    print(f"Initial Power Output: {power:.2e} Watts")
    print(f"Information Leakage:  {bit_leakage:.2e} Q-Bits/sec")
    print("-" * 50)
    print(f"Total Time to 'Full System Defrag' (Evaporation):")
    print(f"{t_years:.2e} Years")
    print("-" * 50)
    print("Note: As the core shrinks, the 'Fuzziness' increases,")
    print("accelerating the leakage exponentially.")

if __name__ == "__main__":
    simulate_evaporation(10.0)
