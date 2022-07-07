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
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.plot(ypoints, color = 'r') # plt.plot(ypoints, c = '#4CAF50')
plt.show()
plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Line
plt.plot(ypoints, linestyle = 'dotted') # Or plt.plot(ypoints, ls = ':')
plt.show()
# plt.plot(ypoints, linestyle = 'dashed')

# Multiple Lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()

# Labels for a Plot
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
