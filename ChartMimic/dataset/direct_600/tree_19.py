
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [30, 25, 20, 10, 8, 7]  # Representing the proportion of each brand
labels = [
    "Sony\n30%",
    "Apple\n25%",
    "Bose\n20%",
    "Sennheiser\n10%",
    "JBL\n8%",
    "Beats\n7%",
]
title = "Market Share of Global Headphone Brands"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#8B4513", "#FFD700", "#D2B48C", "#90EE90", "#FFDAB9", "#FFDEAD"]
# Create a figure with the specified size
fig = plt.figure(figsize=(8, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.85,
    text_kwargs={"fontsize": 14, "color": "black"},
    pad=True,
    ec="white"
)

# Add a title
plt.title(title, fontsize=18)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_19.pdf', bbox_inches='tight')
