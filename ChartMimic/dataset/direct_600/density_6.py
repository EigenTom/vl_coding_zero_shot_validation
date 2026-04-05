# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(24)  # Using a different seed for varied data
# Generate data for the plot
x = np.linspace(0, 14, 800)  # Time in weeks
# Simulated temperature data for seven different cities
y = [
    np.random.uniform(0.5, 1.5)
    * np.sin(0.3 * (x - i))
    for index, i in enumerate(np.linspace(0, 6, 7))
]

# Extracted text variables
cbar_label = "City"
xlabel_text = "Weeks"
ylabel_text = "Temperature Change"
title_text = "Temperature Change of Different Cities Over Weeks"
legend_labels = [f"City {i+1}" for i in range(7)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Set the figure size
fig, ax = plt.subplots(figsize=(12, 5))

# Create a colorbar
sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(vmin=0, vmax=6))
cbar = plt.colorbar(sm, ax=ax, label=cbar_label)
cbar.set_label(cbar_label, rotation=270, labelpad=20)

# Plot each city's temperature trend
for i in range(7):
    plt.plot(
        x, y[i], color=plt.cm.coolwarm(i / 7), alpha=0.8, label=legend_labels[i]
    )

plt.ylim(-2, 2)
plt.xlabel(xlabel_text)
plt.ylabel(ylabel_text)
plt.title(title_text)

# Remove top and right plot borders and set major grid lines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.grid(True, which='major', axis='both', linestyle='--', linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_6.pdf", bbox_inches="tight")