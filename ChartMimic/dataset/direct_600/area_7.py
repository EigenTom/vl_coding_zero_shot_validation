# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting (Production Volume of Different Fruits over Years)
years = [2015, 2016, 2017, 2018, 2019]
apple_production = [50, 55, 53, 58, 60]
banana_production = [80, 78, 85, 90, 95]
cherry_production = [30, 32, 31, 35, 37]
date_production = [40, 42, 45, 48, 50]

# Labels for legend
label_apple = "Apple Production"
label_banana = "Banana Production"
label_cherry = "Cherry Production"
label_date = "Date Production"

# Horizontal line value
axhline_value = 70

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot limits
xlim_values = (2015, 2019)
ylim_values = (20, 100)

# Axis labels
xlabel_values = ["2015", "2016", "2017", "2018", "2019"]
ylabel_values = [20, 40, 60, 80, 100]

# Axis ticks
xticks_values = years
yticks_values = [20, 40, 60, 80, 100]

# Plotting the data
plt.figure(figsize=(10, 6))  # Adjusting figure size to match original image dimensions
plt.plot(
    years,
    apple_production,
    "s-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#e41a1c",
    markeredgecolor="#d73027",
    markersize=10,
    color="#d73027",
    label=label_apple,
)
plt.plot(
    years,
    banana_production,
    "o-",
    clip_on=False,
    zorder=10,
    markerfacecolor="#377eb8",
    markeredgecolor="#2166ac",
    markersize=10,
    color="#2166ac",
    label=label_banana,
)
plt.plot(
    years,
    cherry_production,
    "^--",
    clip_on=False,
    zorder=10,
    markerfacecolor="#4daf4a",
    markeredgecolor="#1b7837",
    markersize=10,
    color="#1b7837",
    label=label_cherry,
)
plt.plot(
    years,
    date_production,
    "d-.",
    clip_on=False,
    zorder=10,
    markerfacecolor="#ff7f00",
    markeredgecolor="#d95f02",
    markersize=10,
    color="#d95f02",
    label=label_date,
)

# Filling the area under the curves
plt.fill_between(years, apple_production, banana_production, color="#e41a1c", alpha=0.2)
plt.fill_between(years, banana_production, cherry_production, color="#377eb8", alpha=0.2)
plt.fill_between(years, cherry_production, date_production, color="#4daf4a", alpha=0.2)
plt.fill_between(years, date_production, color="#ff7f00", alpha=0.2)

# Adding a horizontal dashed line at y=axhline_value
plt.axhline(axhline_value, color="black", linestyle="dotted")

# Setting the x-axis、y-axis limits
plt.xlim(*xlim_values)
plt.ylim(*ylim_values)

# Setting the x-axis tick labels
plt.xticks(xticks_values, xlabel_values)
plt.yticks(yticks_values, ylabel_values)

# Adding a legend at the bottom
plt.legend(loc="upper left", ncol=1, bbox_to_anchor=(1, 1), frameon=False)
plt.gca().tick_params(axis="both", which="both", length=0)

# Adding grid lines for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("area_7.pdf", bbox_inches="tight")