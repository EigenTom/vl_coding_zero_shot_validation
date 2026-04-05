# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
import matplotlib.lines as mlines

# ===================
# Part 2: Data Preparation
# ===================
# Simulated data for website traffic over months
months = np.linspace(1, 12, 12)  # 12 months
traffic = np.array([1000, 1500, 1800, 2200, 2500, 2700, 3000, 3200, 3400, 3500, 3600, 3800])
traffic_pred = traffic + np.random.normal(0, 200, len(traffic))
conversion_rate = np.linspace(0.02, 0.06, 12)
conversion_rate_pred = conversion_rate + np.random.uniform(-0.005, 0.005, len(conversion_rate))

# Extracted variables
traffic_label = "Actual Traffic"
traffic_pred_label = "Predicted Traffic"
conversion_rate_label = "Actual Conversion Rate"
conversion_rate_pred_label = "Predicted Conversion Rate"

traffic_ylabel = "Website Traffic"

conversion_rate_xlabel = "Months"
conversion_rate_ylabel = "Conversion Rate"
legend_labels = ["Actual", "Predicted"]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
traffic_ylim = [0, 4000]
traffic_xlim = [1, 12]
traffic_yticks = [0, 1000, 2000, 3000, 4000]
traffic_xticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
conversion_rate_ylim = [0, 0.07]
conversion_rate_xlim = [1, 12]
conversion_rate_yticks = [0.00, 0.02, 0.04, 0.06]
conversion_rate_xticks = traffic_xticks

legend_loc = "lower center"
legend_bbox_to_anchor = (0.5, -0.2)
legend_ncol = 2
legend_frameon = False

# Create figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

# Plot Traffic
ax1.plot(months, traffic, "o-", color="#d62728", label=traffic_label)
ax1.fill_between(months, traffic, color="#f2d0d0", alpha=0.5)
ax1.plot(months, traffic_pred, "s-", color="#9467bd", label=traffic_pred_label)
ax1.fill_between(months, traffic_pred, color="#e1daf5", alpha=0.5)
ax1.set_ylim(traffic_ylim)
ax1.set_xlim(traffic_xlim)
ax1.set_yticks(traffic_yticks)
ax1.set_xticks(traffic_xticks)
ax1.set_ylabel(traffic_ylabel)
ax1.tick_params(axis="both", which="both", length=0)

# Plot Conversion Rate
ax2.plot(months, conversion_rate, "o-", color="#d62728", label=conversion_rate_label)
ax2.fill_between(months, conversion_rate, color="#f2d0d0", alpha=0.5)
ax2.plot(months, conversion_rate_pred, "s-", color="#9467bd", label=conversion_rate_pred_label)
ax2.fill_between(months, conversion_rate_pred, color="#e1daf5", alpha=0.5)
ax2.set_ylim(conversion_rate_ylim)
ax2.set_xlim(conversion_rate_xlim)
ax2.set_yticks(conversion_rate_yticks)
ax2.set_xticks(conversion_rate_xticks)
ax2.set_xlabel(conversion_rate_xlabel)
ax2.set_ylabel(conversion_rate_ylabel)
ax2.tick_params(axis="both", which="both", length=0)

# Create custom legend
red_line = mlines.Line2D(
    [], [], color="#d62728", marker="o", markersize=6, label=legend_labels[0]
)
purple_line = mlines.Line2D(
    [], [], color="#9467bd", marker="s", markersize=6, label=legend_labels[1]
)
plt.legend(
    handles=[red_line, purple_line],
    loc=legend_loc,
    bbox_to_anchor=legend_bbox_to_anchor,
    ncol=legend_ncol,
    frameon=legend_frameon,
)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("area_8.pdf", bbox_inches="tight")