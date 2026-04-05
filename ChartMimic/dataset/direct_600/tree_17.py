
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [40, 25, 15, 10, 5, 5]
labels = [
    "Procter & Gamble\n40%",
    "Unilever\n25%",
    "Nestle\n15%",
    "PepsiCo\n10%",
    "Coca-Cola\n5%",
    "Others\n5%"
]
title = "Market Share of Global FMCG Companies"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#4A90E2", "#50E3C2", "#F5A623", "#9013FE", "#B8E986", "#D0021B"]
# Create a figure with the specified size
fig = plt.figure(figsize=(6, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={"fontsize": 12, "color": "white"},
    ec="white",
)

# Set the title
plt.title(title, fontsize=18)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_17.pdf', bbox_inches='tight')
