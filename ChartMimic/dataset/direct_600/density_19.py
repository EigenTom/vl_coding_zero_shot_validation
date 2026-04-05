# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(43)
# Sample data
eng_scores = np.random.normal(loc=65, scale=8, size=1000)
hist_scores = np.random.normal(loc=80, scale=15, size=1000)

# Compute density for each dataset
density_eng = gaussian_kde(eng_scores)
density_hist = gaussian_kde(hist_scores)
xs = np.linspace(20, 130, 300)
ys_eng = density_eng(xs)
ys_hist = density_hist(xs)

# Labels and texts
labels = ["English", "History"]
xlabel = "Score"
ylabel = "Density"
title = "Distribution of Test Scores in English and History"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim = (20, 130)
grid_style = ":"

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Fill between x for density regions
plt.fill_between(xs, ys_eng, color="green", alpha=0.3, label=labels[0])
plt.fill_between(xs, ys_hist, color="red", alpha=0.3, label=labels[1])

# Set labels and title (if any)
ax.set_xlim(xlim)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
plt.grid(True, linestyle=grid_style)

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_19.pdf", bbox_inches="tight")