
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Data for the plot
regions_1 = ["North America", "Latin America", "Middle East"]
market_penetration_1 = [28, 42, 58]  # Updated EV adoption rates in percentage
market_penetration_change_1 = [5, 9, 14]  # Updated change in EV adoption rates
customer_loyalty_1 = [72, 78, 70]  # Updated satisfaction with charging infrastructure
customer_loyalty_change_1 = [9, 7, 12]  # Updated change in satisfaction with charging infrastructure
ax1_labels = ["Market Share\nChange (%)", "Satisfaction with Features\nChange (%)"]

regions_2 = ["South Asia", "Sub-Saharan Africa", "Oceania"]
market_penetration_2 = [22, 17, 35]  # Updated EV adoption rates in percentage
market_penetration_change_2 = [3, 2, 8]  # Updated change in EV adoption rates
customer_loyalty_2 = [52, 48, 65]  # Updated satisfaction with charging infrastructure
customer_loyalty_change_2 = [9, 4, 10]  # Updated change in satisfaction with charging infrastructure
ax2_labels = ["Market Share\nChange (%)", "Satisfaction with Features\nChange (%)"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Set the y-axis offsets to be in the middle of each grid
offset = 0.5

# First subplot (regions_1)
for i, region in enumerate(regions_1):
    # Market Penetration change line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(market_penetration_1[i], i + offset * 3 / 2),
        xytext=(market_penetration_1[i] + market_penetration_change_1[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="orange"),
    )
    ax1.scatter(
        [market_penetration_1[i], market_penetration_1[i] + market_penetration_change_1[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=25,
    )
    ax1.annotate(
        f"{market_penetration_change_1[i]:.2f}",
        (market_penetration_1[i] + market_penetration_change_1[i], i + offset * 1.75),
        color="orange",
        ha="right",
        va="center",
    )

    # Customer Loyalty change line with arrow and black dots at start and end
    ax1.annotate(
        "",
        xy=(customer_loyalty_1[i], i + offset / 2),
        xytext=(customer_loyalty_1[i] + customer_loyalty_change_1[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="blue"),
    )
    ax1.scatter(
        [customer_loyalty_1[i], customer_loyalty_1[i] + customer_loyalty_change_1[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=25,
    )
    ax1.annotate(
        f"{customer_loyalty_change_1[i]:.2f}",
        (customer_loyalty_1[i] + customer_loyalty_change_1[i], i + offset * 0.75),
        color="blue",
        ha="left",
        va="center",
    )

# Second subplot (regions_2)
for i, region in enumerate(regions_2):
    ax2.annotate(
        "",
        xy=(market_penetration_2[i], i + offset * 3 / 2),
        xytext=(market_penetration_2[i] + market_penetration_change_2[i], i + offset * 3 / 2),
        arrowprops=dict(arrowstyle="<-", color="orange"),
    )
    ax2.scatter(
        [market_penetration_2[i], market_penetration_2[i] + market_penetration_change_2[i]],
        [i + offset * 3 / 2, i + offset * 3 / 2],
        color="black",
        s=25,
    )
    ax2.annotate(
        f"{market_penetration_change_2[i]:.2f}",
        (market_penetration_2[i] + market_penetration_change_2[i], i + offset * 1.75),
        color="orange",
        ha="right",
        va="center",
    )

    ax2.annotate(
        "",
        xy=(customer_loyalty_2[i], i + offset / 2),
        xytext=(customer_loyalty_2[i] + customer_loyalty_change_2[i], i + offset / 2),
        arrowprops=dict(arrowstyle="<-", color="blue"),
    )
    ax2.scatter(
        [customer_loyalty_2[i], customer_loyalty_2[i] + customer_loyalty_change_2[i]],
        [i + offset / 2, i + offset / 2],
        color="black",
        s=25,
    )
    ax2.annotate(
        f"{customer_loyalty_change_2[i]:.2f}",
        (customer_loyalty_2[i] + customer_loyalty_change_2[i], i + offset * 0.75),
        color="blue",
        ha="left",
        va="center",
    )

# set y-axis limits
ax1.set_ylim(0, len(regions_1))
ax2.set_ylim(0, len(regions_2))

# Set x-axis limits uniformly
ax1.set_xlim(0, 100)
ax2.set_xlim(0, 100)

# Adjust the y-axis tick positions
ax1.set_yticks([i + offset for i in range(len(regions_1))])
ax1.set_yticklabels(regions_1)
ax2.set_yticks([i + offset for i in range(len(regions_2))])
ax2.set_yticklabels(regions_2)
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position("right")

# Offset grid lines on the y-axis
ax1.set_yticks([i for i in range(len(regions_1))], minor=True)
ax2.set_yticks([i for i in range(len(regions_2))], minor=True)
ax1.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="grey")
ax2.yaxis.grid(True, which="minor", linewidth=0.5, alpha=0.7, color="grey")

# add x-axis grid lines and set gap is 10
ax1.xaxis.set_major_locator(plt.MultipleLocator(10))
ax2.xaxis.set_major_locator(plt.MultipleLocator(10))
ax1.grid(axis="x", linestyle="--", linewidth=0.5)
ax2.grid(axis="x", linestyle="--", linewidth=0.5)

# Create arrow-shaped legend entries with a line that aligns with the arrowhead
orange_arrow = mlines.Line2D(
    [],
    [],
    color="orange",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="blue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax1_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[orange_arrow, blue_arrow], bbox_to_anchor=(0.45, 0), ncol=2)

orange_arrow = mlines.Line2D(
    [],
    [],
    color="orange",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[0],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
blue_arrow = mlines.Line2D(
    [],
    [],
    color="blue",
    marker=">",
    linestyle="-",
    markersize=8,
    label=ax2_labels[1],
    linewidth=2,
    markeredgewidth=2,
    markevery=(1, 1),
)
fig.legend(handles=[orange_arrow, blue_arrow], bbox_to_anchor=(0.85, 0), ncol=2)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_9.pdf', bbox_inches='tight')

