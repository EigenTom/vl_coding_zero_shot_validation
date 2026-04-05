
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Define the vector field function for wind patterns
def wind_vector_field(X, Y):
    # Hypothetical function representing wind patterns over farmland
    U = -2 * Y
    V = 2 * X
    return U, V

# Create a finer grid of points (representing a larger farmland)
x = np.linspace(-12.0, 12.0, 30)
y = np.linspace(-12.0, 12.0, 30)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = wind_vector_field(X, Y)
xlabel = "X Coordinate (km)"
ylabel = "Y Coordinate (km)"
title = "Temperature Distribution Over Agricultural Land"
cbar_label = 'Temperature'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
# Use a more agriculture-themed color scheme
colors = np.sqrt(U**2 + V**2)
quiver = ax.quiver(X, Y, U, V, colors, cmap="winter")

# Add several streamlines to the vector field plot for better visualization
strm = ax.streamplot(X, Y, U, V, color='teal', linewidth=0.5)

# Set labels and title
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_title(title, fontsize=14, pad=15)

# Show grid
ax.grid(True, linestyle="--", alpha=0.7)

# Add color bar
cbar = plt.colorbar(quiver, ax=ax)
cbar.set_label(cbar_label, rotation=270, labelpad=15)

# Adjust the aspect ratio
ax.set_aspect("equal")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Display the plot
plt.savefig('quiver_18.pdf', bbox_inches='tight')
