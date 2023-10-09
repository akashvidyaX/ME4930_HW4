import numpy as np
import matplotlib.pyplot as plt

def matrix_exponential(omega_theta):
    """
    Compute the matrix exponential and visualize the frame and rotation axis.
    
    Args:
    - omega_theta (numpy.ndarray): 3x1 exponential coordinates of rotation.
    
    Returns:
    - numpy.ndarray: 3x3 rotation matrix.
    """
    
    # Extract rotation axis and angle from omega_theta
    theta = np.linalg.norm(omega_theta)
    omega = omega_theta / theta
    
    # Compute the skew-symmetric matrix K
    K = np.array([[0, -omega[2], omega[1]],
                  [omega[2], 0, -omega[0]],
                  [-omega[1], omega[0], 0]])
    
    # Compute the rotation matrix using Rodrigues' formula
    R = np.eye(3) + np.sin(theta) * K + (1 - np.cos(theta)) * np.dot(K, K)
    
    # Visualization
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, R[0, 0], R[1, 0], R[2, 0], color='r', label='X axis')
    ax.quiver(0, 0, 0, R[0, 1], R[1, 1], R[2, 1], color='g', label='Y axis')
    ax.quiver(0, 0, 0, R[0, 2], R[1, 2], R[2, 2], color='b', label='Z axis')
    ax.quiver(0, 0, 0, omega[0], omega[1], omega[2], color='y', linewidth=1.5, label='Rotation Axis')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X_s')
    ax.set_ylabel('Y_s')
    ax.set_zlabel('Z_s')
    ax.legend()
    plt.title('Frame and Rotation Axis in {s} frame')
    plt.show()
    
    return R

# Test the function with omega.theta = [1,2,0]
omega_theta = np.array([1, 2, 0])
theta = np.linalg.norm(omega_theta)
omega = omega_theta / theta
K = np.array([[0, -omega[2], omega[1]],
                  [omega[2], 0, -omega[0]],
                  [-omega[1], omega[0], 0]])
    
R_test = matrix_exponential(omega_theta)
print(omega)
print(theta)
print(K)
print(R_test)
