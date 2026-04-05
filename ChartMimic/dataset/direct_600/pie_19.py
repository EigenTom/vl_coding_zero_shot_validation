# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
# Data for new pie chart
categories = ['Reading', 'Exercising', 'Working', 'Entertainment', 'Others']
percentages = [20, 15, 40, 15, 10]


# Extracted text variables
chart_title = "Daily Activity Breakdown"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = plt.cm.Paired(np.linspace(0, 1, 5))  # Different colormap for visual diversity
explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # Smaller explosion for subtler separation
autopct_format = "%1.1f%%"
legend_location = "best"
legend_bbox_to_anchor = (0, 0.8)
# Plot
fig, ax = plt.subplots(figsize=(10, 10))  # Adjust figure size for better visualization
patches, texts, autotexts = ax.pie(
    percentages,
    colors=colors,
    autopct=autopct_format,
    startangle=90,
    wedgeprops=dict(edgecolor="black"),
    explode=explode,
    pctdistance=0.75  # Adjust percentage labels position for better clarity
)

# Optional: creating a donut chart by adding a center circle
donut_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(donut_circle)

# Ensure pie is drawn as a circle
ax.axis("equal")

plt.title(chart_title, fontsize=22)
plt.legend(patches, categories, loc=legend_location, bbox_to_anchor=legend_bbox_to_anchor)

# ===================
# Part 4: Saving Output
# ===================
# Display the plot and save with an updated filename
plt.tight_layout()
plt.savefig('pie_19.pdf', bbox_inches='tight')