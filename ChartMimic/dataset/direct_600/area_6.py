# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
years = [2013, 2014, 2015, 2016, 2017]
revenue = [55, 60, 65, 70, 75]  # Annual Revenue in USD million
expenses = [45, 50, 55, 58, 60]  # Annual Expenses in USD million
profit = [10, 15, 10, 12, 15]  # Annual Profit in USD million

# Labels for legend
label_revenue = "Annual Revenue"
label_expenses = "Annual Expenses"
label_profit = "Annual Profit"

# Title and labels
plot_title = "Financial Overview Over the Years"
xlabel_text = "Years"
ylabel_text = "Million USD"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot limits
xlim_values = (2013, 2017)
ylim_values = (0, 80)

# Axis labels
xlabel_values = ["2013", "2014", "2015", "2016", "2017"]
ylabel_values = [0, 20, 40, 60, 80]

# Axis ticks
xticks_values = years
yticks_values = [0, 20, 40, 60, 80]

# Plotting the data
title_fontsize = 16
label_fontsize = 14
title_pad = 20
plt.figure(figsize=(12, 8))  # Adjusting figure size to fit better
plt.plot(
    years,
    revenue,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#3498db",
    markeredgecolor="#2980b9",
    markersize=10,
    color="#2980b9",
    label=label_revenue,
)
plt.plot(
    years,
    expenses,
    "s-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#e74c3c",
    markeredgecolor="#c0392b",
    markersize=10,
    color="#c0392b",
    label=label_expenses,
)
plt.plot(
    years,
    profit,
    "d-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#2ecc71",
    markeredgecolor="#27ae60",
    markersize=10,
    color="#27ae60",
    label=label_profit,
)

# Filling the area under the curves
plt.fill_between(years, revenue, expenses, color="#3498db", alpha=0.4)
plt.fill_between(years, expenses, profit, color="#e74c3c", alpha=0.4)
plt.fill_between(years, profit, 0, color="#2ecc71", alpha=0.4)

# Setting the x-axis and y-axis limits
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Setting the x-axis and y-axis tick labels
plt.xticks(xticks_values, xlabel_values)
plt.yticks(yticks_values, ylabel_values)

# Adding a legend
plt.legend(loc="upper left", frameon=False)
plt.gca().tick_params(axis="both", which="both", length=0)

# Adding title and labels
plt.title(plot_title, fontsize=title_fontsize, pad=title_pad)
plt.xlabel(xlabel_text, fontsize=label_fontsize)
plt.ylabel(ylabel_text, fontsize=label_fontsize)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_6.pdf", bbox_inches="tight")