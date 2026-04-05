
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
subjects_1 = ["Data Science", "Cybersecurity", "Cloud Computing"]
out_start_1 = [8.5, 7.9, 8.0]
out_group_bias_1 = [-2.5, -3.0, -2.8]
in_start_1 = [7.8, 7.5, 7.2]
in_group_bias_1 = [+1.5, +2.3, +1.8]
ax1_labels = ["Out-group bias\n(Cybersecurity)", "In-group bias\n(Cybersecurity)"]

subjects_2 = ["Artificial Intelligence", "Machine Learning", "Blockchain"]
out_start_2 = [9.0, 8.8, 7.9]
out_group_bias_2 = [-3.0, -2.5, -3.2]
in_start_2 = [8.2, 8.4, 7.5]
in_group_bias_2 = [+1.2, +2.0, +1.5]
ax2_labels = ["Out-group bias\n(Machine Learning)", "In-group bias\n(Machine Learning)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Set the y-axis offsets to be in the middle of each grid
offset = 0.5

# First subplot (subjects_1)
for i, subject in enumerate(subjects_1):
    # Out-group bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(out_start_1[i], i + offset * 3 / 2),
        xytext=(out_start_1[i] + out_group_bias_1[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="dodgerblue"),
    )
    ax1.scatter(
        [out_start_1[i], out_start_1[i] + out_group_bias_1[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{out_group_bias_1[i]:.2f}",
        (out_start_1[i] + out_group_bias_1[i], i + offset * 1.75),
        color="dodgerblue",
        ha="right",
        va="center",
    )

    # In-group bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(in_start_1[i], i + offset / 2),
        xytext=(in_start_1[i] + in_group_bias_1[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="gray"),
    )
    ax1.scatter(
        [in_start_1[i], in_start_1[i] + in_group_bias_1[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{in_group_bias_1[i]:.2f}",
        (in_start_1[i] + in_group_bias_1[i], i + offset * 0.75),
        color="gray",
        ha="left",
        va="center",
    )

# Second subplot (subjects_2)
for i, subject in enumerate(subjects_2):
    ax2.annotate(
        "",
        xy=(out_start_2[i], i + offset * 3 / 2),
        xytext=(out_start_2[i] + out_group_bias_2[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="dodgerblue"),
    )
    ax2.scatter(
        [out_start_2[i], out_start_2[i] + out_group_bias_2[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{out_group_bias_2[i]:.2f}",
        (out_start_2[i] + out_group_bias_2[i], i + offset * 1.75),
        color="dodgerblue",
        ha="right",
        va="center",
    )

    ax2.annotate(
        "",
        xy=(in_start_2[i], i + offset / 2),
        xytext=(in_start_2[i] + in_group_bias_2[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="gray"),
    )
    ax2.scatter(
        [in_start_2[i], in_start_2[i] + in_group_bias_2[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{in_group_bias_2[i]:.2f}",
        (in_start_2[i] + in_group_bias_2[i], i + offset * 0.75),
        color="gray",
        ha="left",
        va="center",
    )

# Set y-axis limits
ax1.set_ylim(0, len(subjects_1))
ax2.set_ylim(0, len(subjects_2))

# Set x-axis limits uniformly
ax1.set_xlim(2, 12)
ax2.set_xlim(2, 12)

# Adjust the y-axis tick positions
ax1.set_yticks([i + offset for i in range(len(subjects_1))])
ax1.set_yticklabels(subjects_1)
ax2.set_yticks([i + offset for i in range(len(subjects_2))])
ax2.set_yticklabels(subjects_2)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# Offset grid lines on the y-axis
ax1.set_yticks([i for i in range(len(subjects_1))], minor=True)
ax2.set_yticks([i for i in range(len(subjects_2))], minor=True)
ax1.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="black")
ax2.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="black")

# Add x-axis grid lines and set gap is 1
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))
ax2.xaxis.set_major_locator(plt.MultipleLocator(1))
ax1.grid(axis="x", linestyle="--", linewidth=0.5)
ax2.grid(axis="x", linestyle="--", linewidth=0.5)

# Create arrow-shaped legend entries with a line that aligns with the arrowhead
dodgerblue_arrow = mlines.Line2D(
    [],
    [],
    color="dodgerblue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
gray_arrow = mlines.Line2D(
    [],
    [],
    color="gray",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[dodgerblue_arrow, gray_arrow], bbox_to_anchor=(0.45, 0), ncol=2)

dodgerblue_arrow = mlines.Line2D(
    [],
    [],
    color="dodgerblue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
gray_arrow = mlines.Line2D(
    [],
    [],
    color="gray",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[dodgerblue_arrow, gray_arrow], bbox_to_anchor=(0.85, 0), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_6.pdf', bbox_inches='tight')

