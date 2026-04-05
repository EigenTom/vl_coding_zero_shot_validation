
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Generate some economic data
public_sector = [
    300,
    500,
    800,
    1200,
    1500,
    2000,
    2500,
    3000,
    3500,
    3800,
    4000,
]  # Government Cloud Adoption (in TB)
private_sector = [
    1000,
    1300,
    1600,
    1800,
    2000,
    2400,
    2800,
    3200,
    3500,
    3700,
    3900,
]  # Enterprise Cloud Adoption (in TB)
bins = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
labels = ["Government Cloud", "Enterprise Cloud"]
xmainlabel = "Cloud Adoption Time Frame (Years)"
xmainlim = [-0.1, 1.1]
xmainticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
ymainlabel = "Data Usage (in TB)"
ymainlim = [0, 10000]
ymainticks = [0, 1000, 2000, 3000, 4000, 5000,6000,7000,8000,9000,10000]

xinsetlim = [0.35, 1.0]
xinsetticks = [0.4, 0.6, 0.8, 1.0]
yinsetlim = [0, 4500]
yinsetticks = [0, 1000,2000, 3000, 4000]

# Coordinates for lines connecting the plots (main and inset)
mainplotline = [(0.435, 2500), (1.1, 0)]
maininsetline = [(0.4, 0), (1.0, 0)]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create main plot with adjusted bar widths and white borders
fig, ax_main = plt.subplots(figsize=(10, 6))
bar_width = 0.05  # Slightly less than the bin width to create a gap
ax_main.bar(
    bins,
    public_sector,
    width=bar_width,
    color="#4CAF50",  # Green for Public Sector
    align="center",
    label=labels[0],
    edgecolor="white",
)
ax_main.bar(
    bins,
    private_sector,
    width=bar_width,
    color="#2196F3",  # Blue for Private Sector
    align="center",
    bottom=public_sector,
    label=labels[1],
    edgecolor="white",
)
ax_main.set_xlabel(xmainlabel)
ax_main.set_xlim(xmainlim)
ax_main.set_xticks(xmainticks)
ax_main.set_ylabel(ymainlabel)
ax_main.set_ylim(ymainlim)
ax_main.set_yticks(ymainticks)
ax_main.legend(loc="upper right", prop={"size": 16})
ax_main.grid()

# Inset plot configuration
ax_inset = fig.add_axes([0.15, 0.45, 0.3, 0.4])
ax_inset.bar(
    bins[4:],
    public_sector[4:],
    width=bar_width,
    color="#4CAF50",
    align="center",
    edgecolor="white",
)
ax_inset.bar(
    bins[4:],
    private_sector[4:],
    width=bar_width,
    color="#2196F3",
    align="center",
    bottom=public_sector[4:],
    edgecolor="white",
)
ax_inset.set_xlim(xinsetlim)  # Zoom in on the right part of the data
ax_inset.set_xticks(xinsetticks)
ax_inset.set_ylim(yinsetlim)
ax_inset.set_yticks(yinsetticks)
ax_inset.grid()

# Adding lines to connect the plots.
# Coordinates of the main plot corners
main_plot_left = ax_main.transData.transform_point(mainplotline[0])
main_plot_right = ax_main.transData.transform_point(mainplotline[1])

# Coordinates of the inset corners
inset_left = ax_inset.transData.transform_point(maininsetline[0])
inset_right = ax_inset.transData.transform_point(maininsetline[1])

# Transform to figure coordinates for annotation
main_plot_left = fig.transFigure.inverted().transform(main_plot_left)
main_plot_right = fig.transFigure.inverted().transform(main_plot_right)
inset_left = fig.transFigure.inverted().transform(inset_left)
inset_right = fig.transFigure.inverted().transform(inset_right)

# Draw lines connecting corners
fig.add_artist(
    plt.Line2D(
        (main_plot_left[0], inset_left[0]),
        (main_plot_left[1], inset_left[1]),
        color="gray",
    )
)
fig.add_artist(
    plt.Line2D(
        (main_plot_right[0], inset_right[0]),
        (main_plot_right[1], inset_right[1]),
        color="gray",
    )
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('PIP_16.pdf', bbox_inches='tight')
