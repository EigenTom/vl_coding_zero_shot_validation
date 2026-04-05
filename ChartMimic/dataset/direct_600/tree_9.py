
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [0.30, 0.25, 0.15, 0.10, 0.12, 0.08]
labels = [
    "Nestle\n30%",
    "PepsiCo\n25%",
    "Coca-Cola\n15%",
    "Unilever\n10%",
    "Danone\n12%",
    "Others\n8%",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#56b1bf", "#59c3c3", "#74d3ae", "#a1de93", "#f2e394", "#f2ae73"]
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    text_kwargs={"fontsize": 18, "color": "black"},
    pad=0.25,
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Save plot
plt.savefig('tree_9.pdf', bbox_inches='tight')
