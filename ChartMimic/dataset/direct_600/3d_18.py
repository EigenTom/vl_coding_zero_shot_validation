# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Set a random seed for reproducibility
np.random.seed(0)
# Define the data for the societal metrics surface plots
x = np.linspace(-50, 50, 200)  # Increased resolution
y = np.linspace(-50, 50, 200)  # Increased resolution
x, y = np.meshgrid(x, y)
z1 = 0.005 * (x**2 + y**2)  # A concave shape representing Social Index
z2 = 0.01 * (x * y)  # A saddle shape representing Economic Index
z3 = np.sin(0.1 * np.sqrt(x**2 + y**2))  # A wave pattern for Health Index
z4 = np.log(x**2 + y**2 + 1)  # Logarithmic growth for Combined Index

# Extracted text variables
title_social_index = "Social Index"
title_economic_index = "Economic Index"
title_health_index = "Health Index"
title_combined_index = "Combined Index"
x_label = "X Axis"
y_label = "Y Axis"
z_label_social = "Social Value"
z_label_economic = "Economic Value"
z_label_health = "Health Value"
z_label_combined = "Combined Value"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
font_size = 12
title_pad = 10

# Create a figure with specified size to match the original image's dimensions
fig = plt.figure(figsize=(14, 10))

# Plot the first subplot
ax1 = fig.add_subplot(141, projection="3d", facecolor="white")  # Set background to white
surf1 = ax1.plot_surface(x, y, z1, cmap="plasma", edgecolor='none')
ax1.set_title(title_social_index, fontsize=font_size, pad=title_pad)
ax1.set_xlabel(x_label, fontsize=font_size)  # Increased font size
ax1.set_ylabel(y_label, fontsize=font_size)  # Increased font size
ax1.set_zlabel(z_label_social, fontsize=font_size)  # Increased font size

# Plot the second subplot
ax2 = fig.add_subplot(142, projection="3d", facecolor="white")
surf2 = ax2.plot_surface(x, y, z2, cmap="inferno", edgecolor='none')
ax2.set_title(title_economic_index, fontsize=font_size, pad=title_pad)
ax2.set_xlabel(x_label, fontsize=font_size)
ax2.set_ylabel(y_label, fontsize=font_size)
ax2.set_zlabel(z_label_economic, fontsize=font_size)

# Plot the third subplot
ax3 = fig.add_subplot(143, projection="3d", facecolor="white")
surf3 = ax3.plot_surface(x, y, z3, cmap="magma", edgecolor='none')
ax3.set_title(title_health_index, fontsize=font_size, pad=title_pad)
ax3.set_xlabel(x_label, fontsize=font_size)
ax3.set_ylabel(y_label, fontsize=font_size)
ax3.set_zlabel(z_label_health, fontsize=font_size)

# Plot the fourth subplot
ax4 = fig.add_subplot(144, projection="3d", facecolor="white")
surf4 = ax4.plot_surface(x, y, z4, cmap="cividis", edgecolor='none')
ax4.set_title(title_combined_index, fontsize=font_size, pad=title_pad)
ax4.set_xlabel(x_label, fontsize=font_size)
ax4.set_ylabel(y_label, fontsize=font_size)
ax4.set_zlabel(z_label_combined, fontsize=font_size)

# Make sure all subplots have a consistent view initialization
for ax in [ax1, ax2, ax3, ax4]:
    ax.view_init(30, 45)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and spacing
plt.tight_layout()

# Save the plot to a file
plt.savefig("3d_18.pdf", bbox_inches="tight")