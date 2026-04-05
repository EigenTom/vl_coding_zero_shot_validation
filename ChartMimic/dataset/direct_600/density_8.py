# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(2)
# Generate data for the plot
x = np.linspace(0, 15, 600)  # Simulate time progression
# Generate air quality index data with some variations
y = [
    np.random.uniform(50, 150) + np.cos(x - i)*np.random.uniform(5, 25) 
    for index, i in enumerate(np.linspace(0, 15, 7))
]

# Extracted variables
cbar_label = "Air Quality Index"
title_text = "Air Quality Index Fluctuations Over Time"
xlabel_text = "Time (hours)"
ylabel_text = "Air Quality Index"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size to match the preferred dimensions
fig, ax = plt.subplots(figsize=(12, 7))

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap="viridis", norm=plt.Normalize(vmin=50, vmax=175))
cbar = plt.colorbar(sm, ax=ax, label=cbar_label)
cbar.set_label(cbar_label, rotation=270, labelpad=20)

# Plotting the data
for i in range(7):
    plt.fill_between(x, y[i], color=plt.cm.viridis(i / 7), alpha=0.6)

plt.ylim(30, 175)
plt.title(title_text)
plt.xlabel(xlabel_text)
plt.ylabel(ylabel_text)

# Customize spines to enhance visual appeal
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(True)
plt.gca().spines["left"].set_visible(False)
plt.gca().set_yticks([])

# ===================
# Part 4: Saving Output
# ===================
# Display plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_8.pdf", bbox_inches="tight")