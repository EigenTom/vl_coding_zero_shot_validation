# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
# Climate change data for temperature and CO2 levels
# CO2 levels for different regions
import numpy as np; np.random.seed(0)
co2_region_a = np.random.normal(400, 10, 10)  # CO2 levels (Region A)
temp_region_a = np.random.normal(1.5, 0.3, 10)  # Temperature increase (Region A)
co2_region_b = np.random.normal(500, 20, 10)  # CO2 levels (Region B)
temp_region_b = np.random.normal(2.0, 0.4, 10)  # Temperature increase (Region B)
co2_region_ab = np.concatenate([co2_region_a, co2_region_b])
temp_region_ab = np.concatenate([temp_region_a, temp_region_b])

# CO2 levels for smaller regions
co2_region_c = np.random.normal(450, 15, 5)  # CO2 levels (Region C)
temp_region_c = np.random.normal(1.8, 0.2, 5)  # Temperature increase (Region C)
co2_region_d = np.random.normal(420, 12, 5)  # CO2 levels (Region D)
temp_region_d = np.random.normal(1.6, 0.3, 5)  # Temperature increase (Region D)

# Labels and plot limits
xlabel = "CO2 Levels (ppm)"
ylabel = "Temperature Increase (°C)"
ax1xlim = [380, 550]
ax1ylim = [1.0, 2.5]
main_diff_line = [[1.0, 1.0], [380, 550], [1.0, 2.5]]
inset_diff_line = [[1.0, 1.0], [400, 500], [1.2, 2.0]]
annotation_rect_x = [400, 500]
annotation_rect_y = [1.2, 2.0]
ax2xlim = [400, 500]
ax2ylim = [1.2, 2.0]
main_plot_upper = [400, 2.0]
main_plot_lower = [400, 1.2]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# Scatter plots
ax1.scatter(co2_region_ab, temp_region_ab, marker="^", color="#1f77b4", label='Region A & B')
ax1.scatter(co2_region_c, temp_region_c, marker="o", color="#ff7f0e", label='Region C')
ax1.scatter(co2_region_d, temp_region_d, marker="s", color="#2ca02c", label='Region D')

# Shaded regions
ax1.fill_betweenx(y=[1.5, ax1ylim[1]], x1=ax1xlim[0], x2=450, color="red", alpha=0.2)
ax1.fill_betweenx(y=[1.5, ax1ylim[0]], x1=450, x2=ax1xlim[1], color="green", alpha=0.2)

# Axis limits and aspect ratio
ax1.set_xlim(ax1xlim)
ax1.set_ylim(ax1ylim)
ax1.plot(main_diff_line[1], main_diff_line[0], color="black", lw=0.5)
ax1.plot(main_diff_line[0], main_diff_line[2], color="black", lw=0.5)

ax1.plot([annotation_rect_x[0], annotation_rect_x[1]], [annotation_rect_y[1], annotation_rect_y[1]], color="black", lw=0.5)
ax1.plot([annotation_rect_x[0], annotation_rect_x[1]], [annotation_rect_y[0], annotation_rect_y[0]], color="black", lw=0.5)
ax1.plot([annotation_rect_x[0], annotation_rect_x[0]], [annotation_rect_y[0], annotation_rect_y[1]], color="black", lw=0.5)
ax1.plot([annotation_rect_x[1], annotation_rect_x[1]], [annotation_rect_y[0], annotation_rect_y[1]], color="black", lw=0.5)

ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.legend(loc="upper right")
ax1.grid(True, which="both", linestyle="--", lw=0.5)

# Scatter plots
ax2.scatter(co2_region_ab, temp_region_ab, marker="^", color="#1f77b4")
ax2.scatter(co2_region_c, temp_region_c, marker="o", color="#ff7f0e")
ax2.scatter(co2_region_d, temp_region_d, marker="s", color="#2ca02c")

# Shaded regions
ax2.fill_betweenx(y=[ax2ylim[1], 1.5], x1=ax2xlim[0], x2=450, color="red", alpha=0.2)
ax2.fill_betweenx(y=[1.5, ax2ylim[0]], x1=450, x2=ax2xlim[1], color="green", alpha=0.2)

# Axis limits and aspect ratio
ax2.set_xlim(ax2xlim)
ax2.set_ylim(ax2ylim)
ax2.plot(inset_diff_line[1], inset_diff_line[0], color="black", lw=0.5)
ax2.plot(inset_diff_line[0], inset_diff_line[2], color="black", lw=0.5)
ax2.grid(True, which="both", linestyle="--", lw=0.5)

# Coordinates of the main plot corners
ax1_plot_up = ax1.transData.transform_point(main_plot_upper)
ax1_plot_down = ax1.transData.transform_point(main_plot_lower)

# Coordinates of the inset corners
ax2_up = ax2.transData.transform_point(main_plot_upper)
ax2_down = ax2.transData.transform_point(main_plot_lower)

# Transform to figure coordinates for annotation
main_plot_up = fig.transFigure.inverted().transform(ax1_plot_up)
main_plot_down = fig.transFigure.inverted().transform(ax1_plot_down)
inset_up = fig.transFigure.inverted().transform(ax2_up)
inset_down = fig.transFigure.inverted().transform(ax2_down)

# Draw lines connecting corners
fig.add_artist(
    plt.Line2D(
        (main_plot_up[0], inset_up[0]), (main_plot_up[1], inset_up[1]), color="gray"
    )
)
fig.add_artist(
    plt.Line2D(
        (main_plot_down[0], inset_down[0]),
        (main_plot_down[1], inset_down[1]),
        color="gray",
    )
)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('PIP_12.pdf', bbox_inches='tight')