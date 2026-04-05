# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
# Reproducibility
np.random.seed(2)
# Simulated conference attendance data
attendance1 = np.random.normal(loc=250, scale=60, size=1000)
attendance2 = np.random.normal(loc=450, scale=80, size=1000)
attendance3 = np.random.normal(loc=550, scale=100, size=1000)

# Compute density for each dataset
density1 = gaussian_kde(attendance1)
density2 = gaussian_kde(attendance2)
density3 = gaussian_kde(attendance3)
xs = np.linspace(50, 750, 400)
ys1 = density1(xs)
ys2 = density2(xs)
ys3 = density3(xs)

# Labels
labels = ["Session 1", "Session 2", "Session 3"]
xlabel = "Attendance"
ylabel = "Density"
title = "Density Plot of Conference Attendance"
peak_annotation = "Peak: {}"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
grid_style = "--"
# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Fill between x for density regions with optimization
plt.fill_between(xs, ys1, color="lightcoral", alpha=0.5, label=labels[0])
plt.fill_between(xs, ys2, color="lightseagreen", alpha=0.5, label=labels[1])
plt.fill_between(xs, ys3, color="lightsalmon", alpha=0.5, label=labels[2])

# Plot lines for densities
plt.plot(xs, ys1, color="maroon", linestyle="-.", linewidth=2)
plt.plot(xs, ys2, color="darkcyan", linestyle="-.", linewidth=2)
plt.plot(xs, ys3, color="peru", linestyle="-.", linewidth=2)

# Set labels and title (if any)
ax.set_xlim(50, 750)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Annotations for peaks
peak1 = xs[np.argmax(ys1)]
peak2 = xs[np.argmax(ys2)]
peak3 = xs[np.argmax(ys3)]
plt.annotate(peak_annotation.format(int(peak1)), xy=(peak1, max(ys1)), xytext=(peak1+50, max(ys1)-0.0006),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(peak_annotation.format(int(peak2)), xy=(peak2, max(ys2)), xytext=(peak2+50, max(ys2)+0.0006),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(peak_annotation.format(int(peak3)), xy=(peak3, max(ys3)), xytext=(peak3+50, max(ys3)-0.0006),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Show grid
plt.grid(True, linestyle=grid_style)

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_20.pdf", bbox_inches="tight")