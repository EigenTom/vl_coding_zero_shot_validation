
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Simulated data for cumulative goals scored by four soccer teams over a 38-game season
import numpy as np; np.random.seed(0)
x = np.linspace(1, 38, 38)
y1 = np.cumsum(np.random.poisson(1.7, 38)) # Team A
y2 = np.cumsum(np.random.poisson(1.9, 38)) # Team B
y3 = np.cumsum(np.random.poisson(1.2, 38)) # Team C
y4 = np.cumsum(np.random.poisson(1.6, 38)) # Team D

# Labels and Plot Types
label_TeamA = "AWS Data Center"
label_TeamB = "Google Cloud Data Center"
label_TeamC = "Microsoft Azure Data Center"
label_TeamD = "IBM Cloud Data Center"

# Axes Limits and Labels
xlabel_value = "Weeks"
ylabel_value = "Cumulative Data Transfer (TB)"
zoomed_in_axes = [0.20, 0.5, 0.25, 0.25]
xlim_values = [33, 38]
ylim_values = [y1[32], max(y1[37], y2[37], y3[37], y4[37]) + 2]
xticks_values = [33, 35, 37]
yticks_values = list(range(int(ylim_values[0]), int(ylim_values[1])+5, 5))
title = "Data Transfer Comparison Over 38 Weeks"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the main figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the curves with distinct styles
ax.plot(x, y1, "r-", label=label_TeamA)
ax.plot(x, y2, "g--", label=label_TeamB)
ax.plot(x, y3, "b-.", label=label_TeamC)
ax.plot(x, y4, "m:", label=label_TeamD)

# Set labels and title
ax.set_xlabel(xlabel_value)
ax.set_ylabel(ylabel_value)
ax.set_title(title)

# Create the inset with the zoomed-in view
ax_inset = fig.add_axes(zoomed_in_axes)  # Adjust the position to align with the right side of the main plot
ax_inset.plot(x, y1, "r-")
ax_inset.plot(x, y2, "g--")
ax_inset.plot(x, y3, "b-.")
ax_inset.plot(x, y4, "m:")
ax_inset.set_xlim(xlim_values)
ax_inset.set_ylim(ylim_values)
ax_inset.set_xticks(xticks_values)
ax_inset.set_yticks(yticks_values)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add the legend to the main axis, outside the plot area
ax.legend(loc="lower right")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('PIP_18.pdf', bbox_inches='tight')
