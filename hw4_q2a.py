import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
np.set_printoptions(suppress=True)

# Define the omega_hat variables
omega_1, omega_2, omega_3 = symbols('omega_1 omega_2 omega_3')

# Given rotation matrix
R_given = np.array([[0, 0, 1], [0, -1, 0], [1, 0, 0]])

# Rotation matrix R based on the given formula
R_formula = np.array([
    [2*omega_1**2 - 1, 2*omega_1*omega_2, 2*omega_1*omega_3],
    [2*omega_1*omega_2, 2*omega_2**2 - 1, 2*omega_2*omega_3],
    [2*omega_1*omega_3, 2*omega_2*omega_3, 2*omega_3**2 - 1]
])

# Set up the equations
equations = [Eq(R_formula[i, j], R_given[i, j]) for i in range(3) for j in range(3)]

# Solve for omega_hat components
omega_hat_solutions = solve(equations, (omega_1, omega_2, omega_3))
print(omega_hat_solutions)


#VERFICATION USING PREVIOUS CODE:


# Function to compute the skew-symmetric matrix from a vector
def skew_symmetric(v):
    return np.array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])

# Function to compute the rotation matrix from exponential coordinates
def matrix_exponential(omega_theta):
    theta = np.linalg.norm(omega_theta)
    if theta == 0:
        return np.eye(3)
    omega_hat = omega_theta / theta
    omega_skew = skew_symmetric(omega_hat)
    R = np.eye(3) + np.sin(theta) * omega_skew + (1 - np.cos(theta)) * np.dot(omega_skew, omega_skew)
    return R

# Define omega_theta values
omega_theta_1 = np.pi * np.array([-np.sqrt(2)/2, 0, -np.sqrt(2)/2])
omega_theta_2 = np.pi * np.array([np.sqrt(2)/2, 0, np.sqrt(2)/2])

# Compute R for the two omega_hat solutions
R_from_omega_theta_1 = matrix_exponential(omega_theta_1)
R_from_omega_theta_2 = matrix_exponential(omega_theta_2)

print(R_from_omega_theta_1)
print(R_from_omega_theta_2)



