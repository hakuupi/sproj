import matplotlib.pyplot as plt
import numpy as np

data = [(0.78, 0.62), (0.88, 0.48), (0.81, 0.68), (0.72, 0.71), (0.60, 0.79),  (0.44, 0.89), (0.25, 0.96), (0.05, 0.97), (-0.14, 0.94), (-0.32, 0.87),  (-0.47, 0.77), (-0.59, 0.65), (-0.68, 0.50), (-0.73, 0.34), (-0.75, 0.17),  (-0.74, -0.01), (-0.69, -0.18), (-0.62, -0.34), (-0.52, -0.48), (-0.39, -0.60),  (-0.24, -0.70), (-0.06, -0.77), (0.12, -0.81), (0.29, -0.83), (0.45, -0.81),  (0.61, -0.76), (0.75, -0.69), (0.88, -0.58), (0.98, -0.44), (1.06, -0.28),  (1.11, -0.11), (1.13, 0.07), (1.11, 0.25), (1.05, 0.42), (0.95, 0.57)]

# separate x and y coordinates
x_coords = [pt[0] for pt in data]
y_coords = [pt[1] for pt in data]


# plot the data points
fig, ax = plt.subplots()
ax.scatter(x_coords, y_coords)




# Define the first circle-like topology: a single large circle
r = 1
theta = np.linspace(0, 2*np.pi, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot(x, y, color='red')

# Define the second circle-like topology: two concentric circles
r1 = 0.8
r2 = 1.1
theta = np.linspace(0, 2*np.pi, 100)
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)
ax.plot(x1, y1, color='blue')
ax.plot(x2, y2, color='blue')

# Set the axis limits and display the plot
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)



plt.show()
