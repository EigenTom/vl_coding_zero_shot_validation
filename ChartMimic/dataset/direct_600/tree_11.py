
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import squarify

# ===================
# Part 2: Data Preparation
# ===================
# Data
sizes = [0.22, 0.18, 0.15, 0.20, 0.10, 0.15]
labels = [
    "Smartwatches\n22%",
    "Fitness Trackers\n18%",
    "Smart Glasses\n15%",
    "VR Headsets\n20%",
    "Smart Clothing\n10%",
    "Other\n15%",
]


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#8ecae6", "#219ebc", "#023047", "#ffb703", "#fb8500", "#8e4a49"]
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
plt.savefig('tree_11.pdf', bbox_inches='tight')
