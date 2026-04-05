
# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
def migration_vector_field(X, Y):
    # Simulate migration from rural (outer) to urban (center)
    U = -X * 0.5
    V = -Y * 0.5
    return U, V

# Create a grid of points
x = np.linspace(-100.0, 100.0, 20)
y = np.linspace(-100.0, 100.0, 20)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = migration_vector_field(X, Y)
xlabel = "Longitude"
ylabel = "Latitude"
title = "Ocean Currents: Global Water Movement"
annotation_text = "Movement Center"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the plot
fig, ax = plt.subplots(figsize=(7, 6))
quiver = ax.quiver(X, Y, U, V, color="royalblue", angles='xy', scale_units='xy', scale=0.5)

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Grid and aspect ratio
ax.grid(True, linestyle="--", alpha=0.5)
ax.set_aspect('equal')

# Add annotations
ax.annotate(annotation_text, xy=(1, 0), xytext=(1.5, 1.5),
             arrowprops=dict(color='Orange', shrink=0.05))

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('quiver_13.pdf', bbox_inches='tight')
