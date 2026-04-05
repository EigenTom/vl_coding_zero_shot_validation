# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data for plotting
categories = ["Electric Cars", "Hybrid Cars", "Sedan", "SUV", "Sports Cars"]
average_speeds = [120.5, 110.2, 95.6, 85.3, 140.7]  # Average speed (km/h)
errors = [5.0, 4.3, 3.8, 6.1, 4.9]  # Speed variance (km/h)
world_mean = [105.4]  # Global average speed (km/h)
xlabel = "Average Speed (km/h)"
label = "Global Average Speed"
plot_title = 'Average Speed by Car Type'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plotting the data
plt.figure(figsize=(10, 7))  # Adjusting figure size for better readability
plt.errorbar(
    average_speeds,
    categories,
    xerr=errors,
    fmt="*",
    color="#2a9d8f",
    ecolor="#1B998B",
    capsize=3,
    elinewidth=2,
    markeredgewidth=2,
    label="Car Type Mean",
)
plt.axvline(world_mean[0], color="#2a9d8f", linestyle="--", linewidth=3, label=label)

# Customizing the plot
plt.xlabel(xlabel)
plt.title(plot_title)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# ===================
# Part 4: Saving Output
# ===================
# Adjusting the layout and saving the figure
plt.tight_layout()
plt.savefig("errorpoint_12.pdf", bbox_inches="tight")