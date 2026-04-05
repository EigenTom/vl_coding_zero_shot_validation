# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(24)  # Different seed for new data
# Generate data for the plot
x = np.linspace(0, 15, 1000)  # Time in months
# Simulated efficacy data for nine different treatments with different parameters
y = [
    np.random.uniform(0.6, 1.4) * np.sin(0.2 * x * (index + 1)) * np.exp(-0.05 * (x - i) ** 2 / np.linspace(0.3, 0.9, 9)[index])
    for index, i in enumerate(np.linspace(1, 11, 9))
]

# Extracted variables
cbar_label = "Dosage Variation"
xlabel_text = 'Months'
ylabel_text = 'Efficacy'
title_text = 'Efficacy of Different Treatments Over Time'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(12, 5))

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap="plasma", norm=plt.Normalize(vmin=0, vmax=8))
cbar = plt.colorbar(sm, ax=ax, label=cbar_label)
cbar.set_label(cbar_label, rotation=270, labelpad=15)

# Plot each treatment's efficacy trend
for i in range(9):
    plt.plot(x, y[i], color=plt.cm.plasma(i / 9), alpha=0.7, linewidth=2, label=f'Treatment {i+1}')

plt.ylim(-1.5, 1.5)
plt.xlabel(xlabel_text)
plt.ylabel(ylabel_text)
plt.title(title_text)

# Remove top and right plot borders
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(True)
plt.gca().spines["left"].set_visible(True)
plt.gca().set_yticks([])

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_7.pdf", bbox_inches="tight")