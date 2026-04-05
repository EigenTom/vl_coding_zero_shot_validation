
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = [
    "SMARTPHONES",
    "TABLETS",
    "WEARABLES",
    "SMART TVS",
    "SMART SPEAKERS"
]  # Capitalized category labels
means = [0.65, 0.32, 0.38, 0.35, 0.45]  # Increased mean values to show upward trend
errors = [0.04, 0.03, 0.02, 0.05, 0.04]  # Adjusted error margins
downerrors = [0.03, 0.02, 0.03, 0.03, 0.04]
legendtitles = ["Mean","Projected market share"]
texttitle ="Baseline"
title = "Projected Increase in Smart Device Market Share"
ylabel = "Projected Share of Global Market (Fraction)"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusting figure size to match new image dimensions
ax.errorbar(
    categories,
    means,
    yerr=[errors, downerrors],
    fmt="s",
    color="green",
    ecolor="darkgreen",
    capsize=5,
    markerfacecolor='lightgreen',
    markeredgewidth=2,
    markeredgecolor='darkgreen'
)

# Adding a legend with both "Mean" and "Dataset mean"
dataset_mean = 0.22
mean_line = ax.errorbar(
    [], [], yerr=[], fmt="o", color="green", ecolor="darkgreen", capsize=5
)
dataset_mean_line = ax.axhline(
    y=dataset_mean, color="gray", linestyle="--", linewidth=1
)
ax.legend(
    [dataset_mean_line, mean_line],
    legendtitles,
    loc="upper right",
    fancybox=True,
    framealpha=1,
    shadow=True,
    borderpad=1,
)
# Adding a horizontal line for dataset mean and text annotation with a white background
ax.text(
    0.95,
    dataset_mean,
    texttitle,
    va="center",
    ha="right",
    backgroundcolor="white",
    transform=ax.get_yaxis_transform(),
)

# Setting labels and a title
ax.set_ylabel(ylabel)
ax.set_title(title)
plt.xticks(rotation=30)
plt.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorpoint_17.pdf", bbox_inches="tight")
