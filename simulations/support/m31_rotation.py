import math

def simulate_m31_rotation():
    # Constants
    G = 6.67430e-11
    M_sun = 1.989e30
    kpc_to_m = 3.086e19  # Kiloparsec to meters
    
    # Andromeda (M31) Parameters
    M_baryonic = 1.0e11 * M_sun  # Total visible mass
    a0 = 1.2e-10  # Code-Geo Acceleration Constant (m/s^2)
    
    # Radii to test (from 5 kpc to 35 kpc)
    radii_kpc = [5, 10, 15, 20, 25, 30, 35]
    
    print(f"--- Project CODE-GEO: M31 Rotation Analysis ---")
    print(f"{'Radius (kpc)':<15} | {'Newtonian (km/s)':<18} | {'CODE-GEO (km/s)':<18}")
    print("-" * 55)
    
    for r_kpc in radii_kpc:
        r = r_kpc * kpc_to_m
        
        # 1. Newtonian Velocity: v = sqrt(GM/r)
        v_newton = math.sqrt((G * M_baryonic) / r) / 1000 # convert to km/s
        
        # 2. CODE-GEO Velocity: Includes Entropic Drag
        # For large r, v = sqrt(sqrt(G * M * a0))
        # We use a transitional formula: v = sqrt(v_newton^2 + v_drag^2)
        v_drag = math.pow(G * M_baryonic * a0, 0.25) / 1000 # km/s
        v_code_geo = math.sqrt(v_newton**2 + v_drag**2)
        
        print(f"{r_kpc:<15} | {v_newton:<18.2f} | {v_code_geo:<18.2f}")

if __name__ == "__main__":
    simulate_m31_rotation()
