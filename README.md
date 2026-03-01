# Project CODE-GEO (V3.1)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18828511.svg)](https://doi.org/10.5281/zenodo.18828511)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Complexity-Originating Dimensional Emergence: A Unified Informational Bridge**

> "Spacetime is not a stage, but a quantum error-correcting output. Gravity is the cost of the computation."

## 🌌 Overview
Project CODE-GEO provides a formal mathematical bridge between **Planck-scale Quantum Information** and **Macroscopic Gravitational Wave Observations**. 

By re-contextualizing General Relativity as a manifestation of **Krylov Complexity growth**, we resolve the **Black Hole Information Paradox**. This framework replaces the classical singularity with a non-singular **Information Core** and a refractive **Fuzzy Shell** at $2.0 R_s$, ensuring unitary consistency during binary black hole mergers.

---

## 📂 Key Research Documents (Primary Audit)
For those conducting a technical review or "sanity check" of the framework, start here:

* **[Technical Whitepaper V3.1](manuscripts/TECHNICAL_WHITE_PAPER_V3.1.md)**: Formal mathematical coupling of alpha-Krylov complexity.
* **[PRD Style Abstract & Intro](manuscripts/CODE-GEO_PRD_Submission_V3.pdf)**: Formal academic framing of the Hilbert-Complexity Action.
* **[Technical Verification Report](manuscripts/CODE-GEO_Technical_Verification_V3.pdf)**: Hard data, spectral parameters, and empirical locks for GW250114.
* **[Executive Summary](docs/EXECUTIVE_SUMMARY.md)**: High-level briefing for the LSC Data Analysis Council.

---

## 🔬 Theoretical Framework

### 1. The Hilbert-Complexity Action
CODE-GEO extends the Einstein-Hilbert action by coupling the Ricci scalar to **Krylov Complexity Density** ($C_k$), representing the quantum circuit depth required to "compute" the local manifold.

![Hilbert-Complexity Action](assets/equations/action.svg)

* **$\alpha$ (Alpha)**: Coupling constant ($\approx 1.04 \times 10^{-71} \text{ m}^2$), derived from the Holographic Bound.
* **$C_k$**: Scaled as $L^{-4}$, ensuring the term remains suppressed in low-energy environments but dominates at the scrambling surface.

### 2. Nonlinear Activation (The Stealth Gate)
To satisfy high-precision Post-Newtonian constraints and Binary Pulsar data, CODE-GEO utilizes a **Nonlinear Gate** $(R_s/r)^6$. This ensures the "Information Shell" remains in a stealth state until extreme curvature thresholds are reached.

![Nonlinear Gate](assets/equations/gate.svg)

* **Inspiral Phase**: Complexity effects are suppressed by a factor of $10^{-6}$ (undetectable).
* **Merger/Ringdown**: The shell activates, creating a medium with a **refractive index $n \approx 4.56$**.

---

## 📡 Empirical Validation: Event GW250114
The primary falsifiable prediction of CODE-GEO V3.1 is the **2.816 ms echo** detected in the **GW250114** remnant ringdown.

### Predicted Signal Parameters:
* **Echo Delay ($\Delta t$):** 2.816 ms
* **Resonance Frequency ($f_{echo}$):** 355.11 Hz
* **Spectral Gap**: 70.5 Hz separation from the Kerr fundamental.
* **Geometric Lock:** The shell stabilizes at exactly **2.0 $R_s$** ($\sim$371 km for a 62.7 $M_{\odot}$ remnant).

---

## 💻 Simulation Suite
Run independent audits of the theoretical locks using the Python verification engine in the `simulations/` directory:

* `simulations/echo_simulator.py`: Primary engine for calculating 2.816 ms delays.
* `simulations/horizon_mod.py`: Calculates geometric lock and shell thickness.
* `simulations/adm_mass_audit.py`: Verifies negligible ADM mass addition ($\approx 10^{-39}$ kg).
* `simulations/support/m31_rotation.py`: Simulates galactic rotation curves as "Entropic Drag".

**Run Full Audit:**
```bash
python3 simulations/nonlinear_gate.py && python3 simulations/adm_mass_audit.py
