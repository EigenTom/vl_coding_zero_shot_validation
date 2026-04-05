# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

x = np.arange(len(months))  # Months
smartphone_sales = np.random.uniform(2, 5, len(months))
laptop_sales = np.random.uniform(3, 7, len(months))
wearable_sales = np.random.uniform(1, 4, len(months))
error_smartphone = [np.random.uniform(0.1, 0.5, len(months)), np.random.uniform(0.1, 0.5, len(months))]
error_laptop = [np.random.uniform(0.2, 1.0, len(months)), np.random.uniform(0.2, 1.0, len(months))]  # Symmetric horizontal error
error_wearable = np.random.uniform(0.1, 0.8, len(months))
chart_title = "Monthly Sales Performance of Tech Products with Error Bars"
highlight_month = 6  # July

ylabel = ["Smartphone Sales (Thousands)", "Laptop Sales (Thousands)", "Wearable Sales (Thousands)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with three subplots and shared x-axis
fig, (ax0, ax1, ax2) = plt.subplots(figsize=(8, 12), nrows=3, sharex=True)
colors_smartphone = plt.get_cmap("jet_r")(np.linspace(0.2, 0.8, len(months)))
colors_laptop = plt.get_cmap("tab20")(np.linspace(0.2, 0.8, len(months)))
color_wearable = "gold"

# First subplot with symmetric vertical error bars (Smartphone sales)
for i in range(len(x)):
    ax0.errorbar(
        x[i],
        smartphone_sales[i],
        yerr=[[error_smartphone[0][i]], [error_smartphone[1][i]]],
        fmt="o",
        color=colors_smartphone[i],
        capsize=4,
    )
    ax0.text(x[i] - 0.2, smartphone_sales[i] + 0.1, f"{smartphone_sales[i]:.2f}", fontsize=8, ha="right")
ax0.set_title(chart_title)
ax0.axhline(y=3.5, linestyle="--", color="#6b8e23")
ax0.set_ylabel(ylabel[0])
ax0.yaxis.grid(True)
ax0.xaxis.grid(False)

# Second subplot with symmetric horizontal error bars (Laptop sales)
for i in range(len(x)):
    ax1.errorbar(
        x[i],
        laptop_sales[i],
        xerr=[[error_laptop[0][i]], [error_laptop[1][i]]],
        fmt="o",
        color=colors_laptop[i],
        markersize=8,
    )
    ax1.text(x[i] + 0.1, laptop_sales[i] + 0.1, f"{laptop_sales[i]:.2f}", fontsize=8, ha="left")
ax1.axvline(x=highlight_month, linestyle="--", color="#d45500")
ax1.set_ylabel(ylabel[1])
ax1.yaxis.grid(True)
ax1.xaxis.grid(False)

# Third subplot with symmetric vertical error bars (Wearable sales)
ax2.errorbar(x, wearable_sales, yerr=error_wearable, fmt="*", color=color_wearable, capsize=2)
for i in range(len(x)):
    ax2.text(x[i], wearable_sales[i] + 0.1, f"{wearable_sales[i]:.2f}", fontsize=8, ha="center")
ax2.set_ylabel(ylabel[2])
ax2.yaxis.grid(True)
ax2.xaxis.grid(False)

# Set shared x-axis labels
plt.xticks(x, months)
ax2.set_xlabel("Month")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig("errorpoint_20.pdf", bbox_inches="tight")