# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(24)

# Generate sample sales data
spring_sales = np.random.normal(loc=300, scale=50, size=1000)  # in units
summer_sales = np.random.normal(loc=500, scale=60, size=1000)  # in units
winter_sales = np.random.normal(loc=400, scale=70, size=1000)  # in units

labels = ["Spring Sales", "Summer Sales", "Winter Sales"]
avxlabel = "Average Spring Sales"
xlabel = "Sales Volume"
ylabel = "Density"
title = "Seasonal Sales Data Density Distributions"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
grid_linestyle = "-"
grid_linewidth = 0.5
grid_alpha = 0.7
line_linestyle = "--"
line_linewidth = 2
fill_alpha = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

# Plot the density plots
for data, color, label in zip(
    [spring_sales, summer_sales, winter_sales],
    ["blue", "orange", "green"],
    labels,
):
    density = gaussian_kde(data)
    xs = np.linspace(min(data) - 20, max(data) + 20, 200)
    density.covariance_factor = lambda: 0.25  # Adjust for smoother curves
    density._compute_covariance()
    plt.plot(
        xs,
        density(xs),
        color=color,
        label=label,
        linestyle=line_linestyle,  # dashed line
        linewidth=line_linewidth  # slightly thinner lines
    )
    plt.fill_between(xs, density(xs), color=color, alpha=fill_alpha)  # stronger fill for shade

# Plot a vertical line indicating the average spring sales
plt.axvline(x=np.mean(spring_sales), color="red", linestyle=line_linestyle, linewidth=line_linewidth, label=avxlabel)

# Set labels and title
ax.set_xlim(min(min(spring_sales), min(summer_sales), min(winter_sales)) - 20,
            max(max(spring_sales), max(summer_sales), max(winter_sales)) + 20)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Show grid with a thicker linestyle
plt.grid(True, linestyle=grid_linestyle, linewidth=grid_linewidth, alpha=grid_alpha)

# Add legend
plt.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("density_16.pdf", bbox_inches="tight")