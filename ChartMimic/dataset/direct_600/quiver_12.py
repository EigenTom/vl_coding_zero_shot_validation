
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np

import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
# Define the wind field function for an agricultural domain
def wind_field(X, Y):
    # This is a simplified wind vector field 
    U = np.sin(np.pi * X) * np.cos(np.pi * Y)
    V = -np.cos(np.pi * X) * np.sin(np.pi * Y)
    return U, V


# Create a grid of points
x = np.linspace(-50.0, 50.0, 20)
y = np.linspace(-50.0, 50.0, 20)
X, Y = np.meshgrid(x, y)

# Compute the electric field
U, V = wind_field(X, Y)
xlabel = "X Position (m)"
ylabel = "Y Position (m)"
title = "Electric Field Distribution in Circuit"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(7, 6))
ax.quiver(X, Y, U, V, color="slateblue", scale=50, width=0.0025)

# Set labels and title
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_title(title, fontsize=14, fontweight='bold')

# Set background color and grid
ax.set_facecolor("beige")  # light green background
ax.grid(True, linestyle="--", alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('quiver_12.pdf', bbox_inches='tight')
