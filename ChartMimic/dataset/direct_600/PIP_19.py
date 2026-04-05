
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
# Data for late-night pharmacy brands
import numpy as np; np.random.seed(42)
pharmacy_brands = {
    "NightCare": np.random.normal(loc=(500, 700), scale=100, size=(50, 2)),
    "24HourMeds": np.random.normal(loc=(600, 600), scale=100, size=(30, 2)),
    "MediExpress": np.random.normal(loc=(700, 900), scale=100, size=(40, 2)),
    "AllNightPharma": np.random.normal(loc=(800, 500), scale=100, size=(60, 2)),
    "QuickHealth": np.random.normal(loc=(600, 400), scale=100, size=(70, 2)),
    "PharmaGo": np.random.normal(loc=(400, 800), scale=100, size=(45, 2)),
}

# Colors for pharmacy brands
colors = {
    "NightCare": "red",
    "24HourMeds": "blue",
    "MediExpress": "green",
    "AllNightPharma": "purple",
    "QuickHealth": "orange",
    "PharmaGo": "yellow",
}
title ="Pharmacy Brand Performance Across Various Service Metrics"
xlabel = "Service Time (Minutes)"
ylabel = "Customer Satisfaction Score"
# Inset plot configuration
insetaxes = [0.2, 0.6, 0.3, 0.3]
insetxlim = [500, 700]  # Focus on NightCare and 24HourMeds
insetylim = [600, 800]
insetxticks = [500.0, 600.0, 700.0]
insetyticks = [600.0, 700.0, 800.0]

# Arrow and annotation configuration
arrowstart = (500, 750)  # Arrow start for NightCare
arrowend = (0.38, 0.7)  # Relative inset arrow end
annotaterecx = [500, 700]  # Annotation range for X
annotaterecy = [600, 800]  # Annotation range for Y

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the scatter plot
fig, ax = plt.subplots(figsize=(10, 8))
for team, data in pharmacy_brands.items():
    ax.scatter(data[:, 0], data[:, 1], c=colors[team], label=team, alpha=0.6, edgecolors='w', s=100)

# Enclosing rectangle for annotation
rect = plt.Rectangle((annotaterecx[0], annotaterecy[0]), annotaterecx[1] - annotaterecx[0], annotaterecy[1] - annotaterecy[0], 
                     linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Create the inset with zoomed-in view
ax_inset = fig.add_axes(insetaxes)
for team, data in pharmacy_brands.items():
    ax_inset.scatter(data[:, 0], data[:, 1], c=colors[team], alpha=0.6, edgecolors='w', s=40)
ax_inset.set_xlim(insetxlim)
ax_inset.set_ylim(insetylim)
ax_inset.set_xticks(insetxticks)
ax_inset.set_yticks(insetyticks)
ax_inset.spines["bottom"].set_color("black")  # Add black border to the inset
ax_inset.spines["left"].set_color("black")
ax_inset.spines["top"].set_color("black")
ax_inset.spines["right"].set_color("black")

ax.annotate(
    "",
    xy=arrowstart,
    xytext=arrowend,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=1),
)

# Adding titles and labels
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.legend()

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig('PIP_19.pdf', bbox_inches='tight')
