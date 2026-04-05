# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
months = np.arange(1, 13)
rainfall_data = {
    "City A": np.random.uniform(50, 200, size=12),
    "City B": np.random.uniform(30, 150, size=12),
    "City C": np.random.uniform(20, 100, size=12),
    "City D": np.random.uniform(10, 80, size=12),
    "City E": np.random.uniform(5, 50, size=12),
}

# Extracted variables
legend_labels = list(rainfall_data.keys())
xlabel_value = "Month"
ylabel_value = "Rainfall (mm)"
title_value = "Monthly Rainfall in Different Cities"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (1, 12)
ylim_values = (0, 600)
legend_loc = "upper left"
legend_reverse = True
legend_frameon = True
legend_ncol = 1
legend_bbox_to_anchor = (1, 1)
title_y_position = 1.05
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"]
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(
    months,
    rainfall_data.values(),
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
ax.set_title(title_value, y=title_y_position)
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.tick_params(axis="both", which="both", length=0)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_17.pdf", bbox_inches="tight")
