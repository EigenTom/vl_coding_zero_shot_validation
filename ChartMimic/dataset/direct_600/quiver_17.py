
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Define a vector field function that represents population movement
def vector_field(X, Y):
    # Example function to mimic population movement
    U = np.cos(X) - np.sin(Y)
    V = np.sin(X) + np.cos(Y)
    return U, V

# Create a grid of points
x = np.linspace(-20.0, 20.0, 10)
y = np.linspace(-20.0, 20.0, 10)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = vector_field(X, Y)
xlabel = "X Coordinate (km)"
ylabel = "Y Coordinate (km)"
title = "Ocean Current Vector Field"
colorbar_title = "Current Speed (m/s)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))

# Use colors to represent the strength of the movement
colors = np.sqrt(U**2 + V**2)
quiver = ax.quiver(X, Y, U, V, colors, cmap="YlGn")

# Add the color bar
cbar = fig.colorbar(quiver, ax=ax)
cbar.set_label(colorbar_title)

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
ax.grid(True, linestyle="--", alpha=0.7)

# Adjust the aspect ratio to be equal for correct geographical representation
ax.set_aspect("equal")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout for better spacing
plt.tight_layout()

# Save and display the plot
plt.savefig('quiver_17.pdf', bbox_inches='tight')
