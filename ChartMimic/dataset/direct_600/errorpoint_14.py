
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data (example values, replace with actual data)
categories = [
    "Artificial Intelligence",
    "Cybersecurity",
    "Blockchain",
    "Quantum Computing",
    "Cloud Computing",
    "Internet of Things",
]
unique_speaker_mean = [50, 45, 40, 38, 48, 42]  # Replace with actual mean values for unique speakers
unique_shouter_mean = [20, 18, 15, 17, 22, 19]  # Replace with actual mean values for unique shouters
unique_speaker_error = [5, 4, 3, 4.5, 4, 3.5]  # Replace with actual error values for unique speakers
unique_shouter_error = [2, 2.5, 2, 2.25, 2.5, 2.75]  # Replace with actual error values for unique shouters
labels = ["Unique speaker count mean", "Unique shouter count mean"]
ylabel = "Number of Unique Speakers"
axlabel = "Average Unique Shouter Count"
title = "Average Number of Unique Speakers and Shouters in Different Tech Fields"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(
    figsize=(12, 8)
)  # Adjust the size to match the original image's dimensions
ax.errorbar(
    categories,
    unique_speaker_mean,
    yerr=unique_speaker_error,
    fmt="^",
    color="navy",
    label=labels[0],
    capsize=10,
    markersize=8,
    elinewidth=2,
    markeredgewidth=2,
)
ax.errorbar(
    categories,
    unique_shouter_mean,
    yerr=unique_shouter_error,
    fmt="*",
    color="olivedrab",
    label=labels[1],
    capsize=10,
    markersize=8,
    elinewidth=2,
    markeredgewidth=2,
)

# Customization
ax.set_ylabel(ylabel)
ax.set_xticklabels(categories, rotation=45, ha="right")
ax.axhline(
    y=sum(unique_shouter_mean) / len(unique_shouter_mean),
    color="grey",
    linestyle="--",
    linewidth=2,
    label=axlabel,
)
ax.legend()
ax.set_title(title)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig("errorpoint_14.pdf", bbox_inches="tight")
