# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Data
np.random.seed(0)  # Ensuring reproducibility
n_aug = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
savings = np.array([300, 450, 600, 400, 700, 800, 1200, 1500, 1000, 900, 800, 950])
expenses = np.array([200, 300, 400, 300, 350, 600, 800, 1000, 750, 700, 650, 600])

# Calculate cumulative values for stacked area chart
cumulative_savings = savings
cumulative_expenses = cumulative_savings + expenses

# Positions for the bars on the x-axis
ind = np.arange(len(n_aug))

# Variables for plot configuration
savings_label = "Savings"
expenses_label = "Expenses"
xlabel_text = "Month"
ylabel_text = "Dollars ($)"
title_text = "Monthly Financial Summary"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (0, 11)
ylim_values = (0, 3000)
yticks_values = list(range(0, 3500, 500))
legend_location = "upper left"
legend_fontsize = 10
legend_frameon = True
legend_shadow = False
legend_facecolor = "#f9f9f9"
legend_ncol = 2
legend_bbox_to_anchor = (0.1, 1.0)
# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Adjusted for better aspect ratio
ax.fill_between(
    n_aug, 0, cumulative_savings, label=savings_label, color="#34bfa3", alpha=0.7
)
ax.fill_between(
    n_aug,
    cumulative_savings,
    cumulative_expenses,
    label=expenses_label,
    color="#fa9e57",
    alpha=0.7,
)

# Enhancing the plot with additional visuals
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.set_yticks(yticks_values)
# Setting the x-axis and y-axis limits dynamically
ax.set_ylim(*ylim_values)  # Ensure all data fits well
ax.set_xlim(*xlim_values)
# Labels, Title and Grid
ax.set_xlabel(xlabel_text, fontsize=14)
ax.set_ylabel(ylabel_text, fontsize=14)
ax.set_title(title_text, fontsize=18, y=1.02)
ax.tick_params(axis="both", which="both", color="gray")
# Custom legend
ax.legend(
    loc=legend_location,
    fontsize=legend_fontsize,
    frameon=legend_frameon,
    shadow=legend_shadow,
    facecolor=legend_facecolor,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
)

# Grid
ax.grid(True, linestyle="--", alpha=0.5, which="both")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig("area_15.pdf", bbox_inches="tight")
