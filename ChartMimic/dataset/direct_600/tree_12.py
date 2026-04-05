
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [25.6, 21.3, 14.1, 12.0, 11.5, 8.5, 7.0]
labels = [
    "Pfizer\n25.6%",
    "Roche\n21.3%",
    "Johnson & Johnson\n14.1%",
    "Merck\n12.0%",
    "Novartis\n11.5%",
    "Sanofi\n8.5%",
    "Others\n7.0%",
]

title = 'Pharmaceutical companies'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]
# Create a figure with the specified size
fig = plt.figure(figsize=(14, 10))

# Create a treemap
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={"fontsize": 18},
    ec="white",
)

# Add title
plt.title(title, fontsize=22)

# Remove axes
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('tree_12.pdf', bbox_inches='tight')
