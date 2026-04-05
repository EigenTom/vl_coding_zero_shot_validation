
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [30, 25, 20, 15, 10]
labels = [
    "Twinings\n30%",
    "Lipton\n25%",
    "Dilmah\n20%",
    "Tazo\n15%",
    "Tetley\n10%"
]
title = "Market Share of Global Black Tea Brands"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#8FBC8F", "#FFD700", "#D2B48C", "#6B8E23", "#CD853F"]
# Create a figure with the specified size
fig = plt.figure(figsize=(8, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={"fontsize": 14, "color": "black"},
    pad=True,
    ec="black",
)

# Set title
plt.title(title, fontsize=16)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_18.pdf', bbox_inches='tight')

