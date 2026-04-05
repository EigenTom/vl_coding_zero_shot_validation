
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
# Updated for a new domain: Programming Languages Performance and Developer Preferences
languages = ["Python", "Java", "C++"]
performance_scores_lang = [9.0, 8.5, 7.0]
performance_bias_lang = [+3.2, +2.8, +2.0]
usability_scores_lang = [7.5, 6.5, 6.0]
usability_bias_lang = [-2.5, -2.8, -3.0]
lang_labels = ["Performance Bias", "Usability Bias"]

frameworks = ["Django", "Spring", "Qt"]
performance_scores_fw = [8.2, 7.8, 7.5]
performance_bias_fw = [+3.5, +3.0, +2.5]
usability_scores_fw = [7.0, 6.8, 6.5]
usability_bias_fw = [-3.0, -2.8, -2.5]
fw_labels = ["Performance Bias", "Usability Bias"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Set the y-axis offsets to be in the middle of each grid
offset = 0.5

# First subplot (languages)
for i, tech in enumerate(languages):
    # Creativity bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(performance_scores_lang[i], i + offset * 3 / 2),
        xytext=(performance_scores_lang[i] + performance_bias_lang[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<|-", linestyle="dotted", color="yellowgreen"),
    )
    ax1.scatter(
        [performance_scores_lang[i], performance_scores_lang[i] + performance_bias_lang[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{performance_bias_lang[i]:.2f}",
        (performance_scores_lang[i] + performance_bias_lang[i], i + offset * 1.75),
        color="yellowgreen",
        ha="left",
        va="center",
    )

    # Precision bias line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(usability_scores_lang[i], i + offset / 2),
        xytext=(usability_scores_lang[i] + usability_bias_lang[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<|-", linestyle="dashed", color="dodgerblue"),
    )
    ax1.scatter(
        [usability_scores_lang[i], usability_scores_lang[i] + usability_bias_lang[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax1.annotate(
        f"{usability_bias_lang[i]:.2f}",
        (usability_scores_lang[i] + usability_bias_lang[i], i + offset * 0.75),
        color="dodgerblue",
        ha="right",
        va="center",
    )

# Second subplot (frameworks)
for i, mov in enumerate(frameworks):
    ax2.annotate(
        "",
        xy=(performance_scores_fw[i], i + offset * 3 / 2),
        xytext=(performance_scores_fw[i] + performance_bias_fw[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<|-", linestyle="dotted", color="yellowgreen"),
    )
    ax2.scatter(
        [performance_scores_fw[i], performance_scores_fw[i] + performance_bias_fw[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{performance_bias_fw[i]:.2f}",
        (performance_scores_fw[i] + performance_bias_fw[i], i + offset * 1.75),
        color="yellowgreen",
        ha="left",
        va="center",
    )

    ax2.annotate(
        "",
        xy=(usability_scores_fw[i], i + offset / 2),
        xytext=(usability_scores_fw[i] + usability_bias_fw[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<|-", linestyle="dashed", color="dodgerblue"),
    )
    ax2.scatter(
        [usability_scores_fw[i], usability_scores_fw[i] + usability_bias_fw[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=10,
    )
    ax2.annotate(
        f"{usability_bias_fw[i]:.2f}",
        (usability_scores_fw[i] + usability_bias_fw[i], i + offset * 0.75),
        color="dodgerblue",
        ha="right",
        va="center",
    )

# Set y-axis limits
ax1.set_ylim(0, len(languages))
ax2.set_ylim(0, len(frameworks))

# Set x-axis limits uniformly
ax1.set_xlim(0, 12)
ax2.set_xlim(0, 12)

# Adjust the y-axis tick positions
ax1.set_yticks([i + offset for i in range(len(languages))])
ax1.set_yticklabels(languages)
ax2.set_yticks([i + offset for i in range(len(frameworks))])
ax2.set_yticklabels(frameworks)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# Offset grid lines on the y-axis
ax1.set_yticks([i for i in range(len(languages))], minor=True)
ax2.set_yticks([i for i in range(len(frameworks))], minor=True)
ax1.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="gray")
ax2.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="gray")

# add x-axis grid lines and set gap to 1
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))
ax2.xaxis.set_major_locator(plt.MultipleLocator(1))
ax1.grid(axis="x", linestyle="--", linewidth=0.5)
ax2.grid(axis="x", linestyle="--", linewidth=0.5)

# Create arrow-shaped legend entries with a line that aligns with the arrowhead
red_arrow = mlines.Line2D(
    [],
    [],
    color="yellowgreen",
    marker=">",
    linestyle="dotted",
    markersize=8,
    label=lang_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="dodgerblue",
    marker=">",
    linestyle="dashed",
    markersize=8,
    label=lang_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[red_arrow, blue_arrow], bbox_to_anchor=(0.45, 0), ncol=2)

red_arrow = mlines.Line2D(
    [],
    [],
    color="yellowgreen",
    marker=">",
    linestyle="dotted",
    markersize=8,
    label=fw_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="dodgerblue",
    marker=">",
    linestyle="dashed",
    markersize=8,
    label=fw_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[red_arrow, blue_arrow], bbox_to_anchor=(0.85, 0), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_8.pdf', bbox_inches='tight')
