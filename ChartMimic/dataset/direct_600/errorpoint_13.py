
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
np.random.seed(1)
authors = [
    "Alice Johnson",
    "Michael Smith",
    "Emily Davis",
    "John Wilson",
    "Sophia Martinez",
    "James Brown",
    "Olivia Garcia",
    "William Lee",
    "Ava Thompson",
    "David Miller",
]
values = [
    15.5,  # Billion USD
    21.1,
    18.8,
    25.5,
    13.3,
    19.9,
    23.3,
    17.7,
    20.0,
    16.6,
]
errors = [
    [1.0, -0.8],  # Error margins in Billion USD
    [1.5, -1.2],
    [0.9, -0.7],
    [1.4, -1.1],
    [0.8, -0.6],
    [1.0, -0.8],
    [1.3, -1.0],
    [1.0, -0.7],
    [1.2, -0.9],
    [1.0, -0.8],
]
methods = [
    "Revenue Projections",
    "Market Analysis",
    "Historical Trends",
    "Machine Learning Models",
    "Expert Opinions",
    "Adjusted Estimates",
    "Hybrid Forecast",
    "Predictive Algorithms",
    "Competitive Analysis",
    "Economic Forecast",
]
xticks = np.arange(10.0, 30.0, 2.0)  # Adjusted for larger scale
xlim = [10.0, 30.0]
xvline = 20.0  # Industry average profit in Billion USD
xvspan = [19.0, 21.0]  # Range near industry average
xlabel = "Population Growth Rate (%)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Error bars with different positive and negative values
for i, (author, value, error) in enumerate(zip(authors, values, errors)):
    ax.errorbar(
        value,
        i,
        xerr=[[abs(error[1])], [error[0]]],
        fmt="o",
        color="black",
        ecolor="black",
        capsize=3,
    )
    ax.text(
        value,
        i - 0.15,
        r"$%.1f^{+%.2f} _{-%.2f}$" % (value, error[0], abs(error[1])),
        va="center",
        ha="center",
        fontsize=9,
    )

# Highlighted region with adjusted color and alpha
ax.axvspan(xvspan[0], xvspan[1], color="yellow", alpha=0.3)

# Text for methods with adjusted font size
for i, method in enumerate(methods):
    ax.text(30, i, method, va="center", ha="left", fontsize=11)

# Set labels and title
ax.set_yticks(range(len(authors)))
ax.set_yticklabels(authors)
ax.set_xlabel(xlabel, fontsize=12)
ax.set_xlim(xlim)
ax.invert_yaxis()  # Invert y-axis to match the original image
ax.axvline(x=xvline, linestyle="--", color="orange")
# Adjust x-axis ticks and labels
ax.set_xticks(xticks)
ax.set_xticklabels([f"{x:.1f}" for x in xticks])

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save/show the plot
plt.tight_layout()
plt.savefig("errorpoint_13.pdf", bbox_inches="tight")
