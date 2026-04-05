
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [30.0, 25.0, 15.0, 10.0, 8.0, 5.0, 4.0, 3.0]
labels = [
    "Apple\n30.0%",
    "Microsoft\n25.0%",
    "Google\n15.0%",
    "Amazon\n10.0%",
    "Samsung\n8.0%",
    "IBM\n5.0%",
    "Intel\n4.0%",
    "Facebook\n3.0%",
]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = [
    "#8c510a",
    "#d8b365",
    "#f6e8c3",
    "#c7eae5",
    "#5ab4ac",
    "#01665e",
    "#c2a5cf",
    "#762a83",
]
# Create a figure with the specified size
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(
    sizes=sizes, label=labels, color=colors, alpha=0.8, text_kwargs={"fontsize": 18}
)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout and save to file
plt.tight_layout()
plt.savefig("tree_6.pdf", bbox_inches="tight")
