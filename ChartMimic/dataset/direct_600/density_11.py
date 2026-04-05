# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np


# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(1)
# Generating new data representing some different measurements
data1 = np.random.normal(loc=20, scale=5, size=1000)
data2 = np.random.normal(loc=25, scale=6, size=1000)

# Extracted strings
title_text = 'Density Distribution of Voltage Measurements'
xlabel_text = 'Voltage (V)'
ylabel_text = 'Density'
legend_label1 = 'True Distribution 1'
legend_label2 = 'True Distribution 2'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))  # Adjusted for better readability

# Adding a line for the true distribution (assuming normal for illustration)
x = np.linspace(min(data1.min(), data2.min()), max(data1.max(), data2.max()), 300)
data1_pdf = (1/(np.sqrt(2 * np.pi) * 5)) * np.exp(-(x-20)**2 / (2 * 5**2))
data2_pdf = (1/(np.sqrt(2 * np.pi) * 6)) * np.exp(-(x-25)**2 / (2 * 6**2))
ax.plot(x, data1_pdf, linestyle='--', linewidth=2, label=legend_label1)
ax.plot(x, data2_pdf, linestyle='--', linewidth=2, label=legend_label2)

# Customize the plot
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.tick_params(left=True, labelleft=True, bottom=True, labelbottom=True)

# Add title and labels
ax.set_title(title_text, fontsize=18)
ax.set_xlabel(xlabel_text, fontsize=16)
ax.set_ylabel(ylabel_text, fontsize=16)
ax.legend(loc='upper right')

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_11.pdf", bbox_inches="tight")