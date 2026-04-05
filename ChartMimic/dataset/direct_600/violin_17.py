
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt


# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(1)
# New data representing engagement rates for different marketing campaigns
data_OnlineStore = np.random.normal(0.70, 0.10, 200)
data_PhysicalStore = np.random.normal(0.55, 0.12, 200)
data_TelephoneSupport = np.random.normal(0.65, 0.08, 200)

xticklabels = ["Online Store", "Physical Store", "Telephone Support"]
ylabel = "Customer Satisfaction Scores"
title = "Customer Satisfaction Across Sales Channels"
ylim = [0.2, 1.0]
xticks = [1, 2, 3]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(6, 6))

# Create violin plots with transparency
violin_parts1 = ax.violinplot(data_OnlineStore, positions=[1], showmeans=True)
violin_parts2 = ax.violinplot(data_PhysicalStore, positions=[2], showmeans=True)
violin_parts3 = ax.violinplot(data_TelephoneSupport, positions=[3], showmeans=True)

# Customize colors
violin_parts1["bodies"][0].set_facecolor("#e41a1c")  
violin_parts1["bodies"][0].set_alpha(0.6)

violin_parts2["bodies"][0].set_facecolor("#377eb8")  
violin_parts2["bodies"][0].set_alpha(0.6)

violin_parts3["bodies"][0].set_facecolor("#4daf4a") 
violin_parts3["bodies"][0].set_alpha(0.6)

# Customize mean line colors
for partname in ("cmeans", "cmaxes", "cmins", "cbars"):
    vp = violin_parts1[partname]
    vp.set_edgecolor("#d62728")  # Red
    vp.set_linewidth(1.5)

    vp = violin_parts2[partname]
    vp.set_edgecolor("#d62728")  # Red
    vp.set_linewidth(1.5)

    vp = violin_parts3[partname]
    vp.set_edgecolor("#d62728")  # Red
    vp.set_linewidth(1.5)

# Set x-axis and y-axis labels
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_ylabel(ylabel)
ax.set_title(title)

# Add grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Set y-axis limits
ax.set_ylim(ylim)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('violin_17.pdf', bbox_inches='tight')
