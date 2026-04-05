# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Generate data for the plot
x = np.linspace(0, 10, 100)  # Simulate x-axis values with fewer points
# Generate random data for 3 different categories
y = [np.random.uniform(1, 15) * np.sin(x - i) + np.random.uniform(-1, 1, 100) for i in range(3)]

# Labels and titles
cbar_label = "Random Value"
plot_title = "Sinusoidal Random Value Distribution"
x_label = "X-axis Values"
y_label = "Sinusoidal Random Values"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_loc = "upper right"
# Set the figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Create a colorbar with a different colormap
sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=plt.Normalize(vmin=1, vmax=15))
cbar = plt.colorbar(sm, ax=ax, label=cbar_label)
cbar.set_label(cbar_label, rotation=270, labelpad=15)

# Plotting the data
for i in range(3):
    plt.plot(x, y[i], color=plt.cm.coolwarm(i / 3), alpha=0.8, linewidth=2, label=f'Category {i+1}')

plt.ylim(-5, 20)
plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.legend(loc=legend_loc)

# Customize plot border and ticks
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_visible(True)
plt.gca().spines["left"].set_visible(True)
plt.gca().set_yticks(np.arange(-5, 21, 5))
plt.gca().set_xticks(np.arange(0, 11, 2))

# ===================
# Part 4: Saving Output
# ===================
# Display plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_9.pdf", bbox_inches="tight")