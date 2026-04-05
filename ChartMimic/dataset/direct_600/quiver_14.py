
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
def vector_field(X, Y):
    # Simulating a rotating wind pattern
    U = -Y
    V = X
    return U, V

# Create a grid of points
x = np.linspace(-100.0, 100.0, 15)
y = np.linspace(-100.0, 100.0, 15)
X, Y = np.meshgrid(x, y)

# Compute the vector field for magnetic forces
U, V = vector_field(X, Y)
magnitude = np.sqrt(U**2 + V**2)

xlabel = "X Position (m)"
ylabel = "Y Position (m)"
title = "Magnetic Field Around a Dipole"
cbar_label = 'Wind Speed (units)'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
quiver = ax.quiver(X, Y, U, V, magnitude, cmap='coolwarm', scale=5)

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
ax.grid(True, linestyle="--", alpha=0.5)

# Add color bar to show magnitude
cbar = plt.colorbar(quiver, ax=ax)
cbar.set_label(cbar_label)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('quiver_14.pdf', bbox_inches='tight')
