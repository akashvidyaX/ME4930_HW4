import sympy as sp
import numpy as np
# Define the symbolic variables
gamma_rpy_sym, beta_rpy_sym, alpha_rpy_sym = sp.symbols('gamma_rpy beta_rpy alpha_rpy')

# Symbolic rotation matrices for roll-pitch-yaw angles
Rot_x_sym = sp.Matrix([
    [1, 0, 0],
    [0, sp.cos(gamma_rpy_sym), -sp.sin(gamma_rpy_sym)],
    [0, sp.sin(gamma_rpy_sym), sp.cos(gamma_rpy_sym)]
])

Rot_y_sym = sp.Matrix([
    [sp.cos(beta_rpy_sym), 0, sp.sin(beta_rpy_sym)],
    [0, 1, 0],
    [-sp.sin(beta_rpy_sym), 0, sp.cos(beta_rpy_sym)]
])

Rot_z_sym = sp.Matrix([
    [sp.cos(alpha_rpy_sym), -sp.sin(alpha_rpy_sym), 0],
    [sp.sin(alpha_rpy_sym), sp.cos(alpha_rpy_sym), 0],
    [0, 0, 1]
])

# Compute the symbolic rotation matrix R_rpy
R_rpy_sym = Rot_z_sym * Rot_y_sym * Rot_x_sym

print(R_rpy_sym)