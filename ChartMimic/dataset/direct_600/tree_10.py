
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [0.35, 0.25, 0.15, 0.10, 0.08, 0.07]
labels = [
    "Dogs\n35%",
    "Cats\n25%",
    "Fish\n15%",
    "Birds\n10%",
    "Small Mammals\n8%",
    "Other\n7%",
]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#FFD700", "#FF4500", "#32CD32", "#1E90FF", "#8A2BE2", "#D2691E"]
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    text_kwargs={"fontsize": 18, "color": "white"},
    pad=0.25,
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
# Show plot
plt.savefig('tree_10.pdf', bbox_inches='tight')
