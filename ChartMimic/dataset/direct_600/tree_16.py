
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [35, 30, 20, 8, 5, 2]
labels = ["Cloud Computing", "Cybersecurity", "Artificial Intelligence", "Blockchain", "Data Privacy", "Quantum Computing"]
title = "Tech Industry Focus Areas Distribution"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#4A90E2", "#50E3C2", "#B8E986", "#7ED321", "#417505", "#BD10E0"]
# Create a figure with the specified size
fig = plt.figure(figsize=(10, 6))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.7,
    text_kwargs={"fontsize": 12, "color": "white"},
    ec="black",  # edge color
)

# Add title
plt.title(title, fontsize=18)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig('tree_16.pdf', bbox_inches='tight')