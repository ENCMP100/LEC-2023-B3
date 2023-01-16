"""
Created on Sun Jan 15 20:19:50 2023

@author: ranaweer
"""

import numpy as np
import matplotlib.pyplot as plt

# Plotting a graph
# ================
theta = np.arange(0, 2 * np.pi, 0.1) # angle in radians
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)

plt.plot(theta, sin_theta, color='r', label='sin')
plt.plot(theta, cos_theta, color='b', label='blue')
plt.xlabel('angle (radians)')
plt.ylabel('function value')
plt.title('Trigonometric Functions')
plt.grid(visible=True, color='c') #cyan color
plt.legend()



 




