# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Sample data for online marketing campaigns
newsletter_campaign = np.random.normal(loc=11, scale=1.2, size=1500)
social_media_campaign = np.random.normal(loc=16, scale=1.0, size=1500)
podcast_marketing = np.random.normal(loc=13, scale=1.5, size=1500)
labels = ["Newsletter Campaign", "Social Media Campaign", "Podcast Marketing"]
avxlabel = "Optimal Threshold"
xlabel = "Campaign Effectiveness"
ylabel = "Density"
title = "Density Plot of Marketing Campaign Effectiveness"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(9, 6))

# Plot the density plots
for data, color, label in zip(
    [newsletter_campaign, social_media_campaign, podcast_marketing],
    ["#2ca02c", "#1f77b4", "#9467bd"],  # Using a set of visually appealing colors
    labels,
):
    density = gaussian_kde(data)
    xs = np.linspace(7.0, 19.0, 200)
    density.covariance_factor = lambda: 0.5
    density._compute_covariance()
    plt.fill_between(xs, density(xs), color=color, alpha=0.3, label=label)

# Plot the optimal threshold line
plt.axvline(x=14.0, color="orange", linestyle="--", label=avxlabel)

# Set labels and title (if any)
ax.set_xlim(7.0, 22.0)
ax.set_xticks([7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0])
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid
plt.grid(True, linestyle="--")

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("density_18.pdf", bbox_inches="tight")