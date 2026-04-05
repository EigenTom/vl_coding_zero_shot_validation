# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Updated days
days = np.linspace(0, 100, 50)

# Generate different trends for each line
daily_oil_price = np.sin(days * 0.1) + 1.0  # Sinusoidal trend (oil price fluctuations)
global_oil_demand = np.array(days) ** 2 * 0.0001 + 0.5  # Quadratic growth (global oil demand)
random_price_changes = np.random.normal(
    loc=1.5, scale=0.2, size=len(days)
)  # Random noise (daily price changes)
fossil_fuel_consumption = np.exp(0.01 * days)  # Exponential growth (fossil fuel consumption)

# Simulate standard deviations for error
std_dev = 0.1
daily_oil_price_std = np.full_like(daily_oil_price, std_dev)
global_oil_demand_std = np.full_like(global_oil_demand, std_dev)
random_price_changes_std = np.full_like(random_price_changes, std_dev)
fossil_fuel_consumption_std = np.full_like(fossil_fuel_consumption, std_dev)

# Labels and configuration
xlabel = "Days"
ylabel = "Energy Metrics"
line_labels = ["Daily Oil Price", "Global Oil Demand"]
xticks = np.linspace(0, 200, 9)
yticks = np.arange(0, 9, 1)
axesinset = [0.2, 0.65, 0.3, 0.2]
insetxlim = [25, 75]
insetylim = [1, 2]
insetxticks = [25, 50, 75]
insetyticks = [1, 1.5, 2]
arrowstart = (50, 3.5)
arrowend = (0.274, 0.22)
annotaterecx = [25, 75]
annotaterecy = [1, 2]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with a single plot
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the third line on the main plot
ax.plot(
    days, random_price_changes, "*--", color="yellow", label=line_labels[0]
)
ax.fill_between(
    days,
    random_price_changes - random_price_changes_std,
    random_price_changes + random_price_changes_std,
    color="blue",
    alpha=0.2,
)

# Plot the fourth line on the main plot
ax.plot(
    days, fossil_fuel_consumption, "^-", color="green", label=line_labels[1]
)
ax.fill_between(
    days,
    fossil_fuel_consumption - fossil_fuel_consumption_std,
    fossil_fuel_consumption + fossil_fuel_consumption_std,
    color="orange",
    alpha=0.2,
)

# Set labels, ticks, legend and grid for the main plot
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.legend(loc="upper left", shadow=True, frameon=True, framealpha=0.9)
ax.grid(
    True, which="both", axis="both", color="lightgray", linestyle="--", linewidth=0.5
)
ax.set_facecolor("#f9f9f9")

# Draw a rectangle on the main plot to indicate the area of zoom-in
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[1], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[0], annotaterecy[0]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[0]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[1], annotaterecx[1]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(
    axesinset
)  # Adjust the position to align with the right side of the main plot

# Plot the third line on the inset
ax_inset.plot(
    days, random_price_changes, "*--", color="yellow", label=line_labels[0]
)
ax_inset.fill_between(
    days,
    random_price_changes - random_price_changes_std,
    random_price_changes + random_price_changes_std,
    color="blue",
    alpha=0.2,
)

# Plot the fourth line on the inset
ax_inset.plot(
    days, fossil_fuel_consumption, "^-", color="green", label=line_labels[1]
)
ax_inset.fill_between(
    days,
    fossil_fuel_consumption - fossil_fuel_consumption_std,
    fossil_fuel_consumption + fossil_fuel_consumption_std,
    color="orange",
    alpha=0.2,
)

# Set limits, ticks and border color for the inset
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add an arrow from the rectangle on the main plot to the inset
ax.annotate(
    "",
    xy=arrowstart,  # Arrow start point (on the main plot)
    xytext=arrowend,  # Arrow end point (on the inset)
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1),
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig("PIP_11.pdf", bbox_inches="tight")