# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(42)
# Data for the plot representing sales growth in different regions
years = np.array([2017, 2018, 2019, 2020, 2021, 2022])
region_x = np.array([200, 210, 220, 230, 240, 250]) + np.random.normal(0, 5, 6)  # Adding noise
region_y = np.array([180, 190, 198, 210, 220, 230]) + np.random.normal(0, 5, 6)
region_z = np.array([160, 170, 178, 190, 200, 210]) + np.random.normal(0, 5, 6)
region_w = np.array([140, 150, 158, 170, 180, 190]) + np.random.normal(0, 5, 6)
benchmark = np.linspace(200, 200, len(years))  # Benchmark line

# Extracted variables
fill_label_region_x = "Region X"
fill_label_region_y = "Region Y"
fill_label_region_z = "Region Z"
fill_label_region_w = "Region W"
plot_label_benchmark = "Benchmark"
title_text = "Sales Growth Over Time by Region"
xlabel_text = "Year"
ylabel_text = "Sales (in thousands)"
legend_title = "Regions"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
xlim_values = (min(years), max(years))
ylim_values = (130, 260)
xticks_values = years
yticks_values = np.arange(130, 261, 20)
legend_loc = "upper left"
legend_bbox_to_anchor = (1.05, 1)
legend_ncol = 1
# Create the plot with a business-appropriate color scheme
plt.figure(figsize=(10, 6))
plt.fill_between(years, region_x, color="purple", alpha=0.3, label=fill_label_region_x)
plt.fill_between(years, region_y, color="cyan", alpha=0.3, label=fill_label_region_y)
plt.fill_between(years, region_z, color="magenta", alpha=0.3, label=fill_label_region_z)
plt.fill_between(years, region_w, color="yellow", alpha=0.3, label=fill_label_region_w)
plt.plot(
    years, benchmark, color="black", linestyle="--", linewidth=2, label=plot_label_benchmark
)

# Add a title and labels with enhanced formatting
plt.title(title_text, fontsize=14, y=1.1)
plt.xlabel(xlabel_text, fontsize=12)
plt.ylabel(ylabel_text, fontsize=12)
plt.xticks(xticks_values)
plt.yticks(yticks_values)
plt.gca().tick_params(axis="both", which="both", length=0)

# Setting the limits explicitly to prevent cut-offs
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Adding a legend with a title
plt.legend(
    title=legend_title,
    frameon=False,
    framealpha=0.8,
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout to ensure no clipping
plt.tight_layout()
plt.savefig("area_12.pdf", bbox_inches="tight")