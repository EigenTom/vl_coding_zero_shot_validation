
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for Law domain
categories = [
    "Football",
    "Basketball",
    "Tennis",
    "Cricket",
    "Swimming",
    "Athletics",
]
unique_speaker_mean = [100, 80, 30, 150, 60, 50]  # Example mean values for participants
unique_shouter_mean = [1000, 500, 200, 1200, 400, 300]  # Example mean values for audience
unique_speaker_error = [10, 15, 9, 12, 10, 12]  # Example error values for participants
unique_shouter_error = [120, 120, 80, 100, 90, 70]  # Example error values for audience
labels = ["Participant count mean", "Audience count mean"]
ylabel = "Number of Participants"
axlabel = "Average Audience Count"
title = "Analysis of Unique Speaker and Shouter Counts in Law Domains"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Error bars and markers
ax.errorbar(
    categories,
    unique_speaker_mean,
    yerr=unique_speaker_error,
    fmt="o",
    color="orange",
    marker="^",
    markersize=8,
    label=labels[0],
)
ax.errorbar(
    categories,
    unique_shouter_mean,
    yerr=unique_shouter_error,
    fmt="o",
    color="purple",
    marker="o",
    markersize=8,
    label=labels[1],
)

# Customization
ax.set_ylabel(ylabel)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.axhline(
    y=sum(unique_shouter_mean) / len(unique_shouter_mean),
    color="grey",
    linestyle="--",
    linewidth=1.5,
    label=axlabel,
)

# Title and Grid
ax.set_title(title)
ax.grid(True, linestyle='--', linewidth=0.5)

# Legend
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("errorpoint_15.pdf", bbox_inches="tight")
