# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# --------------------
# Part 2: Data Preparation
# --------------------
# Simulated Revenue Data for plotting

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
revenue_exp_apple = np.array([500000, 550000, 605000, 665500, 732050, 805255])  # Exponential growth for Apple
revenue_lin_apple = np.array([500000, 510000, 520000, 530000, 540000, 550000])  # Linear growth for Apple
revenue_exp_microsoft = np.array([1000000, 1100000, 1210000, 1331000, 1464100, 1610510])  # Exponential growth for Microsoft
revenue_lin_microsoft = np.array([1000000, 1030000, 1060000, 1090000, 1120000, 1150000])  # Linear growth for Microsoft 

labels = [
    "Apple | Exponential Growth",
    "Apple | Linear Growth",
    "Microsoft | Exponential Growth",
    "Microsoft | Linear Growth"
]
xlabel = "Year"
ylabel = "Revenue (USD)"
title = "Revenue Growth of Apple and Microsoft (2010-2020)"

# Labels and tick mark settings
xticks = years
yticks = np.linspace(0, 2000000, 5)
yticklabels = [f"${int(x):,}" for x in yticks]
inset_axes = [0.22, 0.67, 0.3, 0.25]
inset_ylim = [400000, 1000000]
yticks_inset = np.linspace(400000, 1000000, 4)
x_years = [f"{int(x)}" for x in years]


# --------------------
# Part 3: Plot Configuration and Rendering
# --------------------
# Create the main figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data with different styles and colors
ax.plot(years, revenue_exp_apple, "o-", label=labels[0], color="brown")
ax.plot(years, revenue_lin_apple, "x--", label=labels[1], color="brown")
ax.plot(years, revenue_exp_microsoft, "o-", label=labels[2], color="purple")
ax.plot(years, revenue_lin_microsoft, "x--", label=labels[3], color="purple")

# Set labels and title
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Adjust y-axis limits and ticks
ax.set_ylim([0, 400000])
ax.set_yticks(yticks)
ax.set_yticklabels(yticklabels)

# Add a legend
ax.legend()

# Create an inset axis for Apple data
ax_inset = fig.add_axes(inset_axes)
ax_inset.plot(years, revenue_exp_apple, "o-", color="brown")
ax_inset.plot(years, revenue_lin_apple, "x--", color="brown")

# Adjust y-axis limits for inset
ax_inset.set_ylim(inset_ylim)
ax_inset.set_xlim([2010, 2020])
ax_inset.set_yticks(yticks_inset)

# Change x-axis tick labels to years
ax.set_xticks(years)
ax.set_xticklabels(x_years)
ax_inset.set_xticks(years)
ax_inset.set_xticklabels(x_years)

# --------------------
# Part 4: Saving Output
# --------------------
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_17.pdf', bbox_inches='tight')