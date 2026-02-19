# CODE-GEO: Simulation Suite 🖥️

This directory contains the computational proofs and visualizers for the **Unified Code-Geometric Framework**. Each tool is designed to validate a specific scale of the theory, from Planck-scale horizon jitters to galactic rotation curves.

---

## 🛠️ Tools & Usage

### 1. `echo_simulator.py` (Python 3)
**Scale:** Quantum / Black Hole Scrambling  
Calculates the specific temporal echo delay for black hole remnants based on mass and spin.
- **Key Logic:** Scrambling time $\tau \propto \ln(S)$.
- **Run:** `python3 echo_simulator.py`
- **Output:** Predicted delay in milliseconds (e.g., 2.816 ms for GW250114).

### 2. `m31_rotation.py` (Python 3)
**Scale:** Galactic / Dark Matter Replacement  
Compares Newtonian gravity against CODE-GEO Entropic Drag for the Andromeda Galaxy (M31).
- **Key Logic:** $\delta \Phi \sim \sqrt{G M a_0} \ln(r)$.
- **Run:** `python3 m31_rotation.py`
- **Output:** Comparative velocity table (km/s) across radial distances.

### 3. `fuzzball_core.py` (Python 3)
**Scale:** Planckian / Singularity Resolution  
Calculates the physical dimensions of the non-singular Information Core and simulates horizon jitter.
- **Key Logic:** $R_{core} \propto (M/M_p)^{1/3}$.
- **Run:** `python3 fuzzball_core.py`
- **Output:** Core radius in meters and stochastic Planck-length jitter log.

### 4. `evaporation_timer.py` (Python 3)
**Scale:** Cosmic / Information Recovery  
Estimates the Hawking evaporation timeline and the information "leakage" rate of the core.
- **Key Logic:** Bit-rate leakage via horizon computational bandwidth.
- **Run:** `python3 evaporation_timer.py`
- **Output:** Total de-fragmentation time (years) and Q-Bits/sec recovery rate.

### 5. `core_visualizer.cpp` (C++/SFML)
**Scale:** Visual / HUD Interface  
A real-time, retro-wireframe visualizer of the Information Core sitting inside the Schwarzschild radius.
- **Dependencies:** `libsfml-dev`
- **Compile:** `g++ core_visualizer.cpp -o visualizer -lsfml-graphics -lsfml-window -lsfml-system`
- **Run:** `./visualizer`
- **Features:** Green scanline HUD, red jittering core, and JMC-standard telemetry.

---

## 🧩 Dependencies
- **Python 3.x** (standard math libraries)
- **C++11 or higher**
- **SFML 2.5+** (for visualizer)

*Note: All simulations use constants calibrated for the February 2026 CODE-GEO baseline.*
