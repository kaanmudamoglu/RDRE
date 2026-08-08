# Validation Report: Supersonic Aerodynamics of a Flat Plate

## 1.Objective
The objective of this study is to validate a custom-built Python gas dynamics library through comparison with CFD simulations performed in OpenFOAM.

The selected validation case is a flat plate at angle of attack in a supersonic flow. This case was chosen because it contains both oblique shock and Prandtl-Meyer expansion waves, allowing direct comparison between analytical shock-expansion theory and numerical CFD result.

The free stream conditions are:

- Air as perfect gas
- Free stram Mach Number $Ma = 3$
- Atmospheric Pressure
- Temperature $T = 300K$
- Ratio of spesific heats $\gamma = 1.4$
- Angle of Attack $\alpha = 20\degree$

The study follows the workflow
1. Analytical solution using custom Python tools.
2. CFD simulation using OpenFOAM.
3. Comparison of theoretical and numerical results.
4. Assessment of the validity of the inviscid assumptions used in shock-expansion theory.

## Analytical Background

The analytical solution is based on shock-expansion theory for thin plates in supersonic flow. The free stream is named as Region 1. The supersonic flow generates a Prandtl-Meyer shock on the upper surface and an oblique shock on the lower surface which are Region 2 and Region 3 respectively.
