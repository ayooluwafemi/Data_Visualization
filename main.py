# Matplotlib is a low level graph plotting library in python that serves as a visualization utility
# import matplotlib

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()

# Plot with Markers
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple Points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

# Marker and Line
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
# plt.plot(ypoints, marker = '*')
plt.show()

# Format Strings
plt.plot(ypoints, 'o:r')
plt.show()

# Marker Size
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Color
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()