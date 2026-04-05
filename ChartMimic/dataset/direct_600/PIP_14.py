# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Sample financial data (stock prices and economic indicators)
import numpy as np; np.random.seed(0)
stock_prices_A = np.random.normal(100, 20, 10)  # Stock prices for Company A
stock_prices_B = np.random.normal(50, 10, 10)  # Stock prices for Company B
bond_prices_A = np.random.normal(150, 30, 10)  # Bond prices for Company A
bond_prices_B = np.random.normal(80, 15, 10)  # Bond prices for Company B
prices_A_total = np.concatenate([stock_prices_A, bond_prices_A])
prices_B_total = np.concatenate([stock_prices_B, bond_prices_B])

inflation_rates_X = np.random.normal(105, 10, 5)  # Inflation rates for Region X
inflation_rates_Y = np.random.normal(55, 5, 5)  # Inflation rates for Region Y

interest_rates_X = np.random.normal(90, 7, 5)  # Interest rates for Region X
interest_rates_Y = np.random.normal(60, 8, 5)  # Interest rates for Region Y

xlabel = "AI Model Accuracy Improvement (%)"
ylabel = "Training Time Reduction (hours)"
ax1xlim = [50, 200]
ax1ylim = [30, 120]
diffline1 = [[0, 0], [50, 200], [30, 120]]
diffline2 = [[0, 0], [60, 100], [40, 80]]
annotaterecx1 = [60, 100]
annotaterecy1 = [40, 80]
ax2xlim = [60, 100]
ax2ylim = [40, 80]
plotup1 = [60, 80]
plotdown1 = [60, 40]

label = ["Neural Networks (Accuracy)", "Decision Trees (Training Time)", "Support Vector Machines (Efficiency)"]
label2 = ["Overfitting Risk Zone", "Efficient Training Zone"]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Scatter plots
ax1.scatter(prices_A_total, prices_B_total, marker="^", color="green", label=label[0])
ax1.scatter(inflation_rates_X, inflation_rates_Y, marker="o", color="blue", label=label[1])
ax1.scatter(interest_rates_X, interest_rates_Y, marker="s", color="brown", label=label[2])

# Shaded regions
ax1.fill_betweenx(y=[0, ax1ylim[1]], x1=ax1xlim[0], x2=0, color="red", alpha=0.2, label=label2[0])
ax1.fill_betweenx(y=[0, ax1ylim[0]], x1=0, x2=ax1xlim[1], color="green", alpha=0.2, label=label2[1])

# Axis limits and aspect ratio
ax1.set_xlim(ax1xlim)
ax1.set_ylim(ax1ylim)
ax1.plot(diffline1[1], diffline1[0], color="black", lw=1, linestyle='--')
ax1.plot(diffline1[0], diffline1[2], color="black", lw=1, linestyle='--')

ax1.plot([annotaterecx1[0], annotaterecx1[1]], [annotaterecy1[1], annotaterecy1[1]], color="black", lw=1, linestyle='--')
ax1.plot([annotaterecx1[0], annotaterecx1[1]], [annotaterecy1[0], annotaterecy1[0]], color="black", lw=1, linestyle='--')
ax1.plot([annotaterecx1[0], annotaterecx1[0]], [annotaterecy1[0], annotaterecy1[1]], color="black", lw=1, linestyle='--')
ax1.plot([annotaterecx1[1], annotaterecx1[1]], [annotaterecy1[0], annotaterecy1[1]], color="black", lw=1, linestyle='--')

ax1.set_xlabel(xlabel, fontsize=12)
ax1.set_ylabel(ylabel, fontsize=12)
ax1.grid(True, which="both", linestyle="--", lw=0.5)
ax1.legend(loc="upper right")

# Scatter plots for the second axis
ax2.scatter(prices_A_total, prices_B_total, marker="^", color="green")
ax2.scatter(inflation_rates_X, inflation_rates_Y, marker="o", color="blue")
ax2.scatter(interest_rates_X, interest_rates_Y, marker="s", color="brown")

# Shaded regions
ax2.fill_betweenx(y=[ax2ylim[1], 0], x1=ax2xlim[0], x2=0, color="red", alpha=0.2)
ax2.fill_betweenx(y=[0, ax2ylim[0]], x1=0, x2=ax2xlim[1], color="green", alpha=0.2)

# Axis limits and aspect ratio
ax2.set_xlim(ax2xlim)
ax2.set_ylim(ax2ylim)
ax2.plot(diffline2[1], diffline2[0], color="black", lw=1, linestyle='--')
ax2.plot(diffline2[0], diffline2[2], color="black", lw=1, linestyle='--')
ax2.grid(True, which="both", linestyle="--", lw=0.5)

# Coordinates of the main plot corners
ax1_plot_up = ax1.transData.transform_point(plotup1)
ax1_plot_down = ax1.transData.transform_point(plotdown1)

# Coordinates of the inset corners
ax2_up = ax2.transData.transform_point(plotup1)
ax2_down = ax2.transData.transform_point(plotdown1)

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
plt.savefig('PIP_14.pdf', bbox_inches='tight')