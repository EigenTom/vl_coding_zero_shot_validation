
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
# Setting a random seed for reproducibility
import numpy as np; np.random.seed(0)
# Generate mean scores for 5 games for 2 teams
mean_scores_team1 = np.linspace(650, 750, 5)
mean_scores_team2 = np.linspace(520, 670, 5)
# Smaller standard deviations for realistic revenue clustering
standard_deviations = [50] * 5

# Generate data for Team1 and Team2
team1_scores = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_scores_team1, standard_deviations)
]
team2_scores = [
    np.random.normal(loc=mean, scale=std, size=50)
    for mean, std in zip(mean_scores_team2, standard_deviations)
]
positions_team1 = np.array(range(1, len(team1_scores) + 1)) - 0.2
positions_team2 = np.array(range(1, len(team2_scores) + 1)) + 0.2
legend_labels = ["Company1", "Company2"]
xlabel="Quarter"
ylabel="Revenue ($ in millions)"
xticks=[1, 2, 3, 4, 5]
xtickslabels = ["Q1", "Q2", "Q3", "Q4", "Q5"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure and axis with specified dimensions
fig, ax = plt.subplots(figsize=(8, 7))

# Violin plot width
violin_width = 0.35

# Create the violin plot with adjusted positions
parts_team1 = ax.violinplot(
    team1_scores, positions=positions_team1, widths=violin_width, showmeans=False, showmedians=True
)
parts_team2 = ax.violinplot(
    team2_scores, positions=positions_team2, widths=violin_width, showmeans=False, showmedians=True
)

# Customizing the colors of the violin plot
for pc in parts_team1["bodies"]:
    pc.set_facecolor("palevioletred")  # Team1 color
    pc.set_edgecolor("black")
    pc.set_alpha(0.7)

for pc in parts_team2["bodies"]:
    pc.set_facecolor("aquamarine")  # Team2 color
    pc.set_edgecolor("black")
    pc.set_alpha(0.7)

# Customizing the median lines and removing caps
for partname in ("cbars", "cmins", "cmaxes", "cmedians"):
    vp = parts_team1[partname]
    vp.set_edgecolor("black")
    vp.set_linewidth(1)
    if partname in ("cmins", "cmaxes", "cmedians"):
        vp.set_visible(False)  # Hide caps

    vp = parts_team2[partname]
    vp.set_edgecolor("black")
    vp.set_linewidth(1)
    if partname in ("cmins", "cmaxes", "cmedians"):
        vp.set_visible(False)  # Hide caps

# Adding statistics annotations for both teams
for i in range(len(team1_scores)):
    # Team1 statistics
    quartile1, median, quartile3 = np.percentile(team1_scores[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(team1_scores[i][team1_scores[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(team1_scores[i][team1_scores[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions_team1[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(
        median,
        positions_team1[i] - 0.025,
        positions_team1[i] + 0.025,
        color="white",
        linestyle="-",
        lw=1,
        zorder=3,
    )
    ax.vlines(
        positions_team1[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1
    )

    # Team2 statistics
    quartile1, median, quartile3 = np.percentile(team2_scores[i], [25, 50, 75])
    iqr = quartile3 - quartile1
    lower_whisker = np.min(team2_scores[i][team2_scores[i] >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(team2_scores[i][team2_scores[i] <= quartile3 + 1.5 * iqr])
    ax.vlines(positions_team2[i], quartile1, quartile3, color="black", linestyle="-", lw=4)
    ax.hlines(
        median,
        positions_team2[i] - 0.025,
        positions_team2[i] + 0.025,
        color="white",
        linestyle="-",
        lw=1,
        zorder=3,
    )
    ax.vlines(
        positions_team2[i], lower_whisker, upper_whisker, color="black", linestyle="-", lw=1
    )

# Change the border color to grey
for spine in ax.spines.values():
    spine.set_edgecolor("grey")

# Remove small ticks beside the numbers on the x and y axes
ax.tick_params(axis="both", which="both", length=0)

# Adding the corrected legend
ax.legend(
    [parts_team1["bodies"][0], parts_team2["bodies"][0]],
    legend_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 1.1),
    ncol=2,
)

# Setting the title and labels
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)

# Setting the x-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xtickslabels)

# Enabling y-axis grid lines
ax.yaxis.grid(
    True, linestyle="-", linewidth=0.7, color="grey", zorder=0
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust figure size to match original image's dimensions
fig.set_size_inches(7, 5)  # Width, Height in inches

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.savefig('violin_12.pdf', bbox_inches='tight')
