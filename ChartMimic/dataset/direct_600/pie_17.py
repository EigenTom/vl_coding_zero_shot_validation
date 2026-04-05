# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
sizes = [35.4, 24.5, 15.3, 13.7, 8.6, 2.5]  # Example new data of market share percentages
labels = ["Company A", "Company B", "Company C", "Company D", "Company E", "Others"]


# Plot configuration
title = "Market Share Distribution among Companies"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
explode = (0.1, 0, 0, 0, 0, 0.2)  # add explode parameter to separate slices
title_pad = 20
autopct_format = "%1.1f%%"
startangle = 90
wedgeprops = dict(edgecolor="w")
# Plot
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    sizes,
    colors=["#FF6347", "#FF7F50", "#FFD700", "#ADFF2F", "#32CD32", "#00FA9A"],
    autopct=autopct_format,
    startangle=startangle,
    wedgeprops=wedgeprops,
    explode=explode,
    labels=labels
)
ax.set_title(title, pad=title_pad)  # Set the title with padding

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('pie_17.pdf', bbox_inches='tight')