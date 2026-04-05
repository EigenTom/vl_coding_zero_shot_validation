
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = [
    "Heatwaves",
    "Floods",
    "Droughts",
    "Wildfires",
    "Hurricanes",
]
means = [0.50, 0.40, 0.35, 0.30, 0.25]  # Example mean occurrence rates
errors = [0.05, 0.04, 0.03, 0.05, 0.04]  # Example upper error margins
downerrors = [0.03, 0.02, 0.02, 0.04, 0.03]  # Example lower error margins
legendtitles = ["Dataset Mean", "Mean Occurrence"]
texttitle = "Climate Phenomena Occurrence"
ylabel = "Occurrence Rate (Fraction of total events)"
title = "Cybersecurity Threat Incident Rates"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
fig, ax = plt.subplots(figsize=(10, 8))

# Adjusting color scheme and marker style
ax.errorbar(
    categories,
    means,
    yerr=[errors, downerrors],
    fmt="o",
    color="cyan",
    ecolor="cyan",
    capsize=5,
    markersize=8,
    markerfacecolor="purple",
    markeredgewidth=2,
)

# Adding a legend with both "Mean Occurrence" and "Dataset Mean"
dataset_mean = 0.29
mean_line = ax.errorbar(
    [], [], yerr=[], fmt="^", color="cyan", ecolor="cyan", capsize=5, markersize=8,
    markerfacecolor="purple", markeredgewidth=2
)
dataset_mean_line = ax.axhline(
    y=dataset_mean, color="teal", linestyle="--", linewidth=2
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
    fontsize=10,
    weight='bold'
)

# Setting labels and title
ax.set_ylabel(ylabel)
ax.set_title(title)
plt.xticks(rotation=45)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("errorpoint_16.pdf", bbox_inches="tight")
