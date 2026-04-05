# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(4)
categories = np.arange(1, 6, 1)
data = {
    "Sector A": np.random.randint(200, 300, size=(categories.size)),
    "Sector B": np.random.randint(150, 250, size=(categories.size)),
    "Sector C": np.random.randint(100, 200, size=(categories.size)),
    "Sector D": np.random.randint(50, 150, size=(categories.size)),
}

# Extracted variables
legend_labels = list(data.keys())
xlabel_value = "Category"
ylabel_value = "Value"
title_value = "Values by Category"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (1, 5)
ylim_values = (0, 900)
legend_loc = "upper right"
legend_reverse = False
legend_frameon = True
legend_ncol = 1
legend_bbox_to_anchor = (1.1, 1.15)
title_y_position = 1.05
colors = ["#FFD700", "#ADFF2F", "#6495ED", "#DC143C"]
fig, ax = plt.subplots(figsize=(12, 6))
ax.stackplot(
    categories,
    data.values(),
    labels=legend_labels,
    alpha=0.85,
    colors=colors,
)
ax.legend(
    loc=legend_loc,
    reverse=legend_reverse,
    frameon=legend_frameon,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
)
ax.set_xlim(*xlim_values)
ax.set_ylim(*ylim_values)
ax.set_title(title_value, y=title_y_position, fontsize=18)
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.grid(True, linestyle='--', color='grey', alpha=0.7)
ax.tick_params(axis="both", which="major", length=5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_19.pdf", bbox_inches="tight")
