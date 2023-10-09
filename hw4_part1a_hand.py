####################SUPPORTING HAND CALCULATIONS###############################

import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)


# Define the x_a and y_a directions
x_a = np.array([0, 0, 1])
y_a = np.array([-1, 0, 0])

# Compute the z_a direction using cross product
z_a = np.cross(x_a, y_a)
print(z_a)

# Define the rotation matrix R_sa
R_sa = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0]])

print(R_sa)

# Compute the rotation angle theta using the trace of R_sa
rotation_angle = np.arccos((np.trace(R_sa) - 1) / 2)

rot_angle_degree = np.degrees(rotation_angle)


w = np.array([
    (R_sa[2, 1] - R_sa[1, 2]) / (2 * np.sin(rotation_angle)),
    (R_sa[0, 2] - R_sa[2, 0]) / (2 * np.sin(rotation_angle)),
    (R_sa[1, 0] - R_sa[0, 1]) / (2 * np.sin(rotation_angle))
])


print("Rotation Axis (w):", w)

exp_coordinates = w * rotation_angle
print("Rotation Angle (rads):", rotation_angle)
print("Rotation Angle (degrees):", rot_angle_degree)
print("Exponential Coordinates (w.theta):", exp_coordinates)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, w[0], w[1], w[2], color='r', label='Rotation Axis')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X_s')
ax.set_ylabel('Y_s')
ax.set_zlabel('Z_s')
ax.legend()
plt.title('Rotation Axis in {s} frame')
plt.show()
