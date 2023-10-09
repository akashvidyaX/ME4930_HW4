import numpy as np

# Given roll-pitch-yaw angles
gamma_rpy = np.radians(30)
beta_rpy = np.radians(60)
alpha_rpy = np.radians(45)

# Calculating the first set of ZYZ Euler angles
alpha_zyz1 = np.arctan2(
    (np.sin(alpha_rpy) * np.sin(beta_rpy) * np.cos(gamma_rpy) - np.cos(alpha_rpy) * np.sin(gamma_rpy)),
    (np.cos(alpha_rpy) * np.sin(beta_rpy) * np.cos(gamma_rpy) + np.sin(alpha_rpy) * np.sin(gamma_rpy))
)
beta_zyz1 = np.arctan2(
    np.sqrt(np.sin(gamma_rpy)**2 + np.sin(beta_rpy)**2 * np.cos(gamma_rpy)**2),
    np.cos(beta_rpy) * np.cos(gamma_rpy)
)
gamma_zyz1 = np.arctan2(
    np.cos(beta_rpy) * np.sin(gamma_rpy),
    np.sin(beta_rpy)
)

# Calculating the second set of ZYZ Euler angles
alpha_zyz2 = np.arctan2(
    (np.sin(alpha_rpy) * np.sin(beta_rpy) * np.cos(gamma_rpy) - np.cos(alpha_rpy) * np.sin(gamma_rpy)),
    (-np.cos(alpha_rpy) * np.sin(beta_rpy) * np.cos(gamma_rpy) - np.sin(alpha_rpy) * np.sin(gamma_rpy))
)
beta_zyz2 = np.arctan2(
    -np.sqrt(np.sin(gamma_rpy)**2 + np.sin(beta_rpy)**2 * np.cos(gamma_rpy)**2),
    np.cos(beta_rpy) * np.cos(gamma_rpy)
)
gamma_zyz2 = np.arctan2(
    np.cos(beta_rpy) * np.sin(gamma_rpy),
    -np.sin(beta_rpy)
)

print(np.degrees([alpha_zyz1, beta_zyz1, gamma_zyz1]), np.degrees([alpha_zyz2, beta_zyz2, gamma_zyz2]))
