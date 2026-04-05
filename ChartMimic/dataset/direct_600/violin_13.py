
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)

# Generate mean values for fuel efficiency (in MPG)
mean_values_electric = np.linspace(15, 25, 5)
mean_values_hybrid = np.linspace(20, 30, 5)

# Standard deviations
standard_deviations = [5] * 5

# Generate synthetic data for Electric Cars
data_electric = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_values_electric, standard_deviations)
]

# Generate synthetic data for Hybrid Cars
data_hybrid = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_values_hybrid, standard_deviations)
]

# Set positions for violins
positions_electric = np.array(range(1, len(data_electric) + 1)) - 0.2
positions_hybrid = np.array(range(1, len(data_hybrid) + 1)) + 0.2

# Labels and ticks
legend_labels = ["Iphone 13", "Iphone 13 Pro"]
xlabel = "Usage Patterns"
ylabel = "Battery Life (Hours)"
xticks = [1, 2, 3, 4, 5]
xtickslabels = ["Browsing", "Streaming", "Gaming", "Standby", "Video Call"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(8, 7))

violin_width = 0.35

# Create violin plots
parts_electric = ax.violinplot(
    data_electric, positions=positions_electric, widths=violin_width, showmeans=False, showmedians=True
)
parts_hybrid = ax.violinplot(
    data_hybrid, positions=positions_hybrid, widths=violin_width, showmeans=False, showmedians=True
)

# Customizing colors
for pc in parts_electric["bodies"]:
    pc.set_facecolor("cornsilk")
    pc.set_edgecolor("black")
    pc.set_alpha(1)

for pc in parts_hybrid["bodies"]:
    pc.set_facecolor("powderblue")
    pc.set_edgecolor("black")
    pc.set_alpha(1)

# Customizing median lines and removing caps
for partname in ("cbars", "cmins", "cmaxes", "cmedians"):
    vp_electric = parts_electric[partname]
    vp_hybrid = parts_hybrid[partname]
    vp_electric.set_edgecolor("black")
    vp_hybrid.set_edgecolor("black")
    vp_electric.set_linewidth(1)
    vp_hybrid.set_linewidth(1)
    if partname in ("cmins", "cmaxes", "cmedians"):
        vp_electric.set_visible(False)  # Hide caps
        vp_hybrid.set_visible(False)  # Hide caps

# Adding statistical annotations
for i in range(len(data_electric)):
    quartile1, median, quartile3 = np.percentile(data_electric[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(data_electric[i][data_electric[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(data_electric[i][data_electric[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions_electric[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(median, positions_electric[i] - 0.025, positions_electric[i] + 0.025, color="white", linestyle="-", lw=1, zorder=3)
    ax.vlines(positions_electric[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1)

    quartile1, median, quartile3 = np.percentile(data_hybrid[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(data_hybrid[i][data_hybrid[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(data_hybrid[i][data_hybrid[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions_hybrid[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(median, positions_hybrid[i] - 0.025, positions_hybrid[i] + 0.025, color="white", linestyle="-", lw=1, zorder=3)
    ax.vlines(positions_hybrid[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1)

# Customize borders
for spine in ax.spines.values():
    spine.set_edgecolor("grey")

# Remove ticks
ax.tick_params(axis="both", which="both", length=0)

# Adding legend
ax.legend(
    [parts_electric["bodies"][0], parts_hybrid["bodies"][0]],
    legend_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.1),
    ncol=2,
)

# Setting labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Setting x-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabels)

# Enabling y-axis grid lines
ax.yaxis.grid(
    True, linestyle="-", linewidth=0.7, color="grey", zorder=0
)

# ===================
# Part 4: Saving Output
# ===================
fig.set_size_inches(7, 5)

plt.tight_layout()
plt.savefig("violin_13.pdf", bbox_inches="tight")
