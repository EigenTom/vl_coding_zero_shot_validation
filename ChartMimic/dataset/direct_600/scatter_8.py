# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# Simulate some data for the scatter plot
n_points = 200
ar_x = np.random.normal(0.4, 0.05, n_points)
ar_y = np.random.normal(0.3, 0.05, n_points)
de_x = np.random.normal(-0.2, 0.05, n_points)
de_y = np.random.normal(0.1, 0.05, n_points)
fr_x = np.random.normal(-0.3, 0.05, n_points)
fr_y = np.random.normal(-0.1, 0.05, n_points)
he_x = np.random.normal(0.1, 0.05, n_points)
he_y = np.random.normal(0.2, 0.05, n_points)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the scatter plot
plt.figure(figsize=(8, 8))
plt.scatter(ar_x, ar_y, color="blue", alpha=0.5, label="ar")
plt.scatter(de_x, de_y, color="magenta", alpha=0.5, label="de")
plt.scatter(fr_x, fr_y, color="yellow", alpha=0.5, label="fr")
plt.scatter(he_x, he_y, color="green", alpha=0.5, label="he")
plt.tick_params(axis="both", length=0)
# Add labels and title
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(
    title="Legend", ncol=4, bbox_to_anchor=(0.5, 1.1), loc="upper center", frameon=False
)

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout
plt.tight_layout()
plt.savefig("scatter_8.pdf", bbox_inches="tight")
