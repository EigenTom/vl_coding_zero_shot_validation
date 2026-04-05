
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(42)
transportation_modes = {
    "cars": np.random.normal(loc=(600, 800), scale=100, size=(50, 2)),  # NightCare
    "buses": np.random.normal(loc=(700, 700), scale=100, size=(30, 2)),  # 24HourMeds
    "bikes": np.random.normal(loc=(800, 900), scale=100, size=(40, 2)),  # MediExpress
    "trains": np.random.normal(loc=(900, 600), scale=100, size=(60, 2)),  # AllNightPharma
    "planes": np.random.normal(loc=(1000, 500), scale=100, size=(70, 2)),  # QuickHealth
}

# Define colors and markers for each pharmacy brand, keeping variable names unchanged
colors = {
    "cars": "red",      # NightCare
    "buses": "blue",    # 24HourMeds
    "bikes": "green",   # MediExpress
    "trains": "purple", # AllNightPharma
    "planes": "orange", # QuickHealth
}

markers = {
    "cars": "s",      # NightCare
    "buses": "o",     # 24HourMeds
    "bikes": "^",     # MediExpress
    "trains": "d",    # AllNightPharma
    "planes": "p",    # QuickHealth
}

insetaxes=[0.15, 0.15, 0.2, 0.2]
insetxlim=[600, 900]
insetylim=[500, 1000]
insetxticks=[600, 750, 900]
insetyticks=[500, 750, 1000]
arrowstart=(600,400)  # MediExpress focus
arrowend=(0.35, 0.3)
annotaterecx = [600, 900]
annotaterecy = [500, 1000]
title = "Transportation Mode Efficiency"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 10))

for mode, data in transportation_modes.items():
    ax.scatter(data[:, 0], data[:, 1], c=colors[mode], marker=markers[mode], label=mode, alpha=0.7)

# Draw annotation rectangle around specific region   
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[1], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[1]], [annotaterecy[0], annotaterecy[0]], color="black", lw=1)
ax.plot([annotaterecx[0], annotaterecx[0]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)
ax.plot([annotaterecx[1], annotaterecx[1]], [annotaterecy[0], annotaterecy[1]], color="black", lw=1)

# Create the inset with a zoomed-in view of a specific region
ax_inset = fig.add_axes(insetaxes)
for mode, data in transportation_modes.items():
    ax_inset.scatter(data[:, 0], data[:, 1], c=colors[mode], marker=markers[mode], alpha=0.7)
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

# Add annotation to indicate the inset region
ax.annotate("", xy=arrowstart, xytext=arrowend, textcoords="axes fraction", arrowprops=dict(facecolor="black", lw=0.1))

# Add titles and labels
ax.set_title(title)
ax.set_xlabel("Feature X")
ax.set_ylabel("Feature Y")
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('PIP_20.pdf', bbox_inches='tight')

