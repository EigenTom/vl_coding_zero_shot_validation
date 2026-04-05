# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting (let's simulate some wave data)
# Set a random seed for reproducibility
np.random.seed(42)
X = np.linspace(0, 2 * np.pi, 100)
Y = np.linspace(0, 2 * np.pi, 100)
X, Y = np.meshgrid(X, Y)
Z1 = np.sin(X) * np.cos(Y)
Z2 = np.sin(X / 2) * np.cos(Y / 2)

# Titles and labels
title1 = "Wave Pattern 1"
title2 = "Wave Pattern 2"
xlabel = "X-axis"
ylabel = "Y-axis"
zlabel = "Z-axis"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure with specified size
fig, axs = plt.subplots(1, 2, figsize=(14, 6), subplot_kw={"projection": "3d"})

# First subplot
axs[0].plot_surface(X, Y, Z1, cmap="coolwarm", edgecolor="none", alpha=0.80)
axs[0].set_title(title1)
axs[0].set_xlabel(xlabel)
axs[0].set_ylabel(ylabel)
axs[0].set_zlabel(zlabel)

# Second subplot
axs[1].plot_surface(X, Y, Z2, cmap="coolwarm", edgecolor="none", alpha=0.80)
axs[1].set_title(title2)
axs[1].set_xlabel(xlabel)
axs[1].set_ylabel(ylabel)
axs[1].set_zlabel(zlabel)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("3d_17.pdf", bbox_inches="tight")