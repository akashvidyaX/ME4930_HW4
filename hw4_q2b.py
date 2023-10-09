import numpy as np
import sympy as sp

def skew_symmetric(v):
    return sp.Matrix([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

theta_sym = sp.Symbol('theta')

# Step 1: Define given vectors and compute skew-symmetric matrix
omega_hat_given = sp.Matrix([2/3, 2/3, 1/3])
v1_sym = sp.Matrix([1, 0, 1])
v2_given_sym = sp.Matrix([0, 1, 1])

# Construct the skew-symmetric matrix for omega_hat
K_sym = skew_symmetric(omega_hat_given)

# Step 2: Compute v2 using Rodrigues' rotation formula
v2_sym_formula = (sp.eye(3) + sp.sin(theta_sym) * K_sym + (1 - sp.cos(theta_sym)) * K_sym @ K_sym) @ v1_sym

# Set up equations based on the components of v2
equations = [sp.Eq(v2_sym_formula[i], v2_given_sym[i]) for i in range(3)]

# Solve the equations for theta
theta_solutions = sp.solve(equations, theta_sym)
theta_solutions
print(K_sym)
print(theta_solutions)
