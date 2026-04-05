# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# AI Algorithms
import numpy as np; np.random.seed(0)
x_guards = np.random.normal(70, 10, 10)  # Model Accuracy (Algorithm A)
y_guards = np.random.normal(90, 15, 10)  # Processing Speed (Algorithm A)

# Machine Learning
x_forwards = np.random.normal(80, 12, 10)  # Model Accuracy (Algorithm B)
y_forwards = np.random.normal(100, 18, 10)  # Processing Speed (Algorithm B)

# Deep Learning
x_centers = np.random.normal(85, 14, 10)  # Model Accuracy (Algorithm C)
y_centers = np.random.normal(95, 20, 10)  # Processing Speed (Algorithm C)

# Axis labels and limits
xlabel = "Model Accuracy Increase (%)"
ylabel = "Processing Speed Increase (ms)"
ax1xlim = [50, 100]
ax1ylim = [70, 130]
ax2xlim = [60, 90]
ax2ylim = [80, 120]
diffline1 = [[0, 0], [50, 100], [70, 130]]
diffline2 = [[0, 0], [60, 90], [80, 120]]
title1 = "Overall AI Algorithm Performance Improvement"
title2 = "Zoom-in View"
label = ["Model Accuracy", "Processing Speed", "Deep Learning"]
plot_up1 = [60, 80]
plot_down1 = [60, 120]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plots
ax1.scatter(x_guards, y_guards, marker="o", color="blue", label="Solar Energy")
ax1.scatter(x_forwards, y_forwards, marker="s", color="red", label="Wind Energy")
ax1.scatter(x_centers, y_centers, marker="^", color="green", label="Hydro Energy")

# Shaded regions
ax1.fill_betweenx(y=[0, ax1ylim[1]], x1=0, x2=ax1xlim[1], color="lightblue", alpha=0.2)

# Axis limits and aspect ratio
ax1.set_xlim(ax1xlim)
ax1.set_ylim(ax1ylim)
ax1.plot(diffline1[1], diffline1[0], color="black", lw=1, linestyle="--")
ax1.plot(diffline1[0], diffline1[2], color="black", lw=1, linestyle="--")

ax1.set_xlabel(xlabel)
ax1.set_ylabel(ylabel)
ax1.legend(loc="upper right")
ax1.grid(True, which="both", linestyle="--", lw=0.5)
ax1.set_title(title1)

# Scatter plots for zoom-in view
ax2.scatter(x_guards, y_guards, marker="o", color="red", label=label[0])
ax2.scatter(x_forwards, y_forwards, marker="s", color="blue", label=label[1])
ax2.scatter(x_centers, y_centers, marker="^", color="green", label=label[2])

# Shaded regions
ax2.fill_betweenx(y=[0, ax2ylim[1]], x1=40, x2=ax2xlim[1], color="lightgreen", alpha=0.2)

# Axis limits and aspect ratio
ax2.set_xlim(ax2xlim)
ax2.set_ylim(ax2ylim)
ax2.plot(diffline2[1], diffline2[0], color="black", lw=1, linestyle="--")
ax2.plot(diffline2[0], diffline2[2], color="black", lw=1, linestyle="--")
ax2.grid(True, which="both", linestyle="--", lw=0.5)
ax2.set_title(title2)

# Coordinates of the main plot corners


# Coordinates of the inset corners
ax1_plot_up = ax1.transData.transform_point(plot_up1)
ax1_plot_down = ax1.transData.transform_point(plot_down1)
ax2_plot_up = ax2.transData.transform_point(plot_up1)
ax2_plot_down = ax2.transData.transform_point(plot_down1)

# Transform to figure coordinates for annotation
main_plot_up = fig.transFigure.inverted().transform(ax1_plot_up)
main_plot_down = fig.transFigure.inverted().transform(ax1_plot_down)
inset_up = fig.transFigure.inverted().transform(ax2_plot_up)
inset_down = fig.transFigure.inverted().transform(ax2_plot_down)

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
plt.savefig('PIP_13.pdf', bbox_inches='tight')