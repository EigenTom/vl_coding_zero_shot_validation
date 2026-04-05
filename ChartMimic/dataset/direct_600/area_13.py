# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# ===================
# Part 2: Data Preparation
# ===================
# New Data for Different Domain (Sales Data)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_a = np.random.randint(20, 70, size=len(months))
product_b = np.random.randint(15, 55, size=len(months))
product_c = np.random.randint(10, 50, size=len(months))

# Calculate cumulative values for stacked area chart
cumulative_product_a = product_a
cumulative_product_b = cumulative_product_a + product_b
cumulative_product_c = cumulative_product_b + product_c

# Positions for the bars on the x-axis
ind = np.arange(len(months))

# Variables for plot configuration
product_a_label = "Product A Sales"
product_b_label = "Product B Sales"
product_c_label = "Product C Sales"
xlabel_text = "Months"
ylabel_text = "Sales"
title_text = "Monthly Sales Data"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (0, 11)
ylim_values = (0, max(cumulative_product_c) + 10)

yticks_values = range(0, max(cumulative_product_c) + 10, 20)
legend_location = "upper center"
legend_fontsize = 10
legend_frameon = True
legend_shadow = True
legend_facecolor = "#ffffff"
legend_ncol = 3
legend_bbox_to_anchor = (0.5, 1.15)
title_fontsize = 16
title_y = 1.2
xlabel_fontsize = 14
ylabel_fontsize = 14
tick_params_color = "gray"
grid_linestyle = "--"
grid_alpha = 0.5

# Plot
fig, ax = plt.subplots(figsize=(10, 5))  # Adjusted for better aspect ratio
ax.fill_between(
    months, 0, cumulative_product_a, label=product_a_label, color="#42A5F5", alpha=0.7
)
ax.fill_between(
    months,
    cumulative_product_a,
    cumulative_product_b,
    label=product_b_label,
    color="#AB47BC",
    alpha=0.7,
)
ax.fill_between(
    months,
    cumulative_product_b,
    cumulative_product_c,
    label=product_c_label,
    color="#26A69A",
    alpha=0.7,
)

# Enhancing the plot with additional visuals
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_yticks(yticks_values)
# Setting the x-axis and y-axis limits dynamically
ax.set_ylim(*ylim_values)  # Ensure all data fits well
ax.set_xlim(*xlim_values)
# Labels, Title and Grid
ax.set_xlabel(xlabel_text, fontsize=xlabel_fontsize)
ax.set_ylabel(ylabel_text, fontsize=ylabel_fontsize)
ax.set_title(title_text, fontsize=title_fontsize, y=title_y)
ax.tick_params(axis="both", which="both", color=tick_params_color)
# Custom legend
ax.legend(
    loc=legend_location,
    fontsize=legend_fontsize,
    frameon=legend_frameon,
    shadow=legend_shadow,
    facecolor=legend_facecolor,
    ncol=legend_ncol,
    bbox_to_anchor=legend_bbox_to_anchor,
)

# Grid
ax.grid(True, linestyle=grid_linestyle, alpha=grid_alpha, which="both")

# ===================
# Part 4: Saving Output
# ===================
# Adjusting layout to reduce white space
plt.tight_layout()
plt.savefig("area_13.pdf", bbox_inches="tight")