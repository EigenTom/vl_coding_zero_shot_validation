# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================

np.random.seed(0)
vehicle_types = ["Cars", "Trucks", "Motorcycles"]

x_positions = np.linspace(0, 20, 6)
cars_energy_output = np.random.uniform(50, 100, 6)
trucks_energy_output = np.random.uniform(30, 80, 6)
motorcycles_energy_output = np.random.uniform(40, 90, 6)

cars_error = [np.random.uniform(5, 10, 6), np.random.uniform(5, 10, 6)]
trucks_error = [np.random.uniform(3, 6, 6), np.random.uniform(3, 6, 6)]
motorcycles_error = np.random.uniform(4, 8, 6)

vertical_line_position = 10

titles = ["Cars Energy Output", "Trucks Energy Output", "Motorcycles Energy Output"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create a figure with three subplots and shared x-axis
fig, (ax0, ax1, ax2) = plt.subplots(figsize=(6, 9), nrows=3, sharex=True)
cars_colors = plt.get_cmap("YlOrRd")(np.linspace(0.2, 0.8, 6))
trucks_colors = plt.get_cmap("Greens")(np.linspace(0.2, 0.8, 6))
motorcycles_color = "#33a02c"
# First subplot with symmetric vertical error bars
for i in range(len(x_positions)):
    ax0.errorbar(
        x_positions[i],
        cars_energy_output[i],
        yerr=[[cars_error[0][i]], [cars_error[1][i]]],
        fmt="o",
        color=cars_colors[i],
        capsize=4,
    )
    ax0.text(x_positions[i] - 0.5, cars_energy_output[i], f"{cars_energy_output[i]:.2f}", fontsize=8, ha="right")
ax0.set_title(titles[0])
ax0.axhline(y=75, linestyle="--", color="#FFA500")
ax0.yaxis.grid(True)
ax0.xaxis.grid(False)

# Second subplot with symmetric horizontal error bars
for i in range(len(x_positions)):
    ax1.errorbar(
        x_positions[i],
        trucks_energy_output[i],
        xerr=[[trucks_error[0][i]], [trucks_error[1][i]]],
        fmt="o",
        color=trucks_colors[i],
        capsize=4,
    )
    ax1.text(x_positions[i] + 0.5, trucks_energy_output[i] + 0.1, f"{trucks_energy_output[i]:.2f}", fontsize=8, ha="left")
ax1.set_title(titles[1])
ax1.axvline(x=vertical_line_position, linestyle="--", color="#1E90FF")
ax1.xaxis.grid(True)
ax1.yaxis.grid(False)

# Third subplot with symmetric vertical error bars
ax2.errorbar(x_positions, motorcycles_energy_output, yerr=motorcycles_error, fmt="*", color=motorcycles_color, capsize=4)
ax2.set_title(titles[2])
ax2.legend([vehicle_types[2]],loc="upper left")
ax2.yaxis.grid(True)
ax2.xaxis.grid(False)

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and display the plot
plt.tight_layout()
plt.savefig("errorpoint_19.pdf", bbox_inches="tight")