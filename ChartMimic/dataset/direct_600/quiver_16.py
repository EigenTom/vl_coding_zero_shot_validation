
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Define the vector field function for wind flow
def wind_field(X, Y):
    # Simulate wind flow from southwest to northeast
    U = np.sin(2 * np.pi * (Y - X) / 5)
    V = np.cos(2 * np.pi * (Y - X) / 5)
    return U, V

# Create a finer grid of points for electric field
x = np.linspace(-10.0, 10.0, 50)
y = np.linspace(-10.0, 10.0, 50)
X, Y = np.meshgrid(x, y)

# Compute the electric field
U, V = wind_field(X, Y)
xlabel = "X Coordinate (m)"
ylabel = "Y Coordinate (m)"
title = "Electric Field Around a Charge"
colorbar_title = "Electric Field Strength (N/C)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(7, 6))

# Use a more contrasting color scheme
colors = np.sqrt(U**2 + V**2)
quiver = ax.quiver(X, Y, U, V, colors, cmap="PuBuGn")

# Add a color bar to show the wind speed
cbar = fig.colorbar(quiver, ax=ax)
cbar.set_label(colorbar_title)

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
ax.grid(True, linestyle="--", alpha=0.7)

# Adjust the aspect ratio
ax.set_aspect("equal")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout
plt.tight_layout()

# Display the plot
plt.savefig('quiver_16.pdf', bbox_inches='tight')
