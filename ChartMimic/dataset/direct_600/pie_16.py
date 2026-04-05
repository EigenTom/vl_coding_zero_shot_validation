# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Data to plot
fruits = ["Apples", "Bananas", "Grapes", "Cherries", "Peaches", "Plums"]
sizes = [10, 22, 15, 12, 30, 11]

explode = (0.1, 0, 0, 0, 0, 0)  # explode the first slice

# Plot configuration variables
title_text = "Different Fruits Share in Market (in %)"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
colors = ["#ff9999","#66b3ff","#99ff99","#ffcc99","#c2c2f0","#ffb3e6"]
title_pad = 20
title_fontsize = 18
legend_loc = "center left"
legend_bbox_to_anchor = (1, 0, 0.5, 1)
autopct_format = "%1.1f%%"
startangle = 90
wedgeprops = dict(edgecolor="k")

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(
    sizes,
    colors=colors,
    autopct=autopct_format,
    startangle=startangle,
    wedgeprops=wedgeprops,
    explode=explode
)

# Adding a title and legend
ax.set_title(title_text, pad=title_pad, fontsize=title_fontsize)
ax.legend(fruits, loc=legend_loc, bbox_to_anchor=legend_bbox_to_anchor)

# ===================
# Part 4: Saving Output
# ===================
# Show plot with tight layout
plt.tight_layout()
plt.savefig('pie_16.pdf', bbox_inches='tight')