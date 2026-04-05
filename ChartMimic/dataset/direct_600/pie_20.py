# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
labels = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys & Games"]
sizes = [35, 20, 15, 10, 20]
colors = plt.cm.Paired(np.linspace(0.3, 1, len(sizes)))
explode = (0.1, 0, 0, 0, 0.1)  # Highlight the two largest segments

# Extracted variables
plot_title = "Distribution of Sales by Category"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
autopct_format = "%1.1f%%"
shadow_option = True
start_angle = 90
legend_location = "upper right"
legend_fontsize = 10
title_fontsize = 16
title_y_position = 1.05
# Plot
plt.figure(figsize=(8, 6))
plt.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct=autopct_format,
    shadow=shadow_option,  # Add shadow for depth
    startangle=start_angle
)
plt.axis("equal")

# Add legend
plt.legend(labels, loc=legend_location, fontsize=legend_fontsize)
plt.title(plot_title, fontsize=title_fontsize, y=title_y_position)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig('pie_20.pdf', bbox_inches='tight')