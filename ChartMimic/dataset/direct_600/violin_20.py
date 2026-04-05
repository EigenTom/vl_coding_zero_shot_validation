
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Simulate new data representing technology performance metrics
tech_data1 = np.clip(np.random.normal(0.75, 0.07, 200), 0, 1)  # Blockchain System
tech_data2 = np.clip(np.random.normal(0.80, 0.09, 200), 0, 1)  # Cloud Computing
tech_data3 = np.clip(np.random.normal(0.70, 0.12, 200), 0, 1)  # Edge Computing
tech_data4 = np.clip(np.random.normal(0.60, 0.14, 200), 0, 1)  # IoT Platform
tech_data5 = np.clip(np.random.normal(0.66, 0.17, 200), 0, 1)  # 5G Network

# Simulated metrics for Pearson R and Error Rate (EER)
pearson_r = [0.30, 0.27, 0.23, 0.21, 0.17]
eer = [3.5, 5.5, 9.0, 13.0, 16.5]

data = [tech_data1, tech_data2, tech_data3, tech_data4, tech_data5]
categories = ["Blockchain", "Cloud", "Edge Computing", "IoT", "5G"]
ylabel = "Technology Performance Score"
ylim = [0, 1.06]
xlabel = "Technology Type"
textlabels = ["Pearson Correlation", "Error Rate (%)"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 6))

# Create violin plots
violin_parts = ax.violinplot(data, showmeans=False, showmedians=True, showextrema=False)

# Customize the appearance
ax.set_ylabel(ylabel)
ax.set_xticks(np.arange(1, len(categories) + 1))
ax.set_xticklabels(categories)
ax.set_ylim(ylim)
ax.set_xlabel(xlabel)

# Define a technology-oriented color palette
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

for i, (pc, d) in enumerate(zip(violin_parts["bodies"], data)):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor("black")
    pc.set_alpha(0.75)

    # Calculate the quartiles and median
    quartile1, median, quartile3 = np.percentile(d, [25, 50, 75])
    iqr = quartile3 - quartile1

    # Calculate whiskers
    lower_whisker = np.min(d[d >= quartile1 - 1.5 * iqr])
    upper_whisker = np.max(d[d <= quartile3 + 1.5 * iqr])

    # Annotate statistics
    ax.vlines(i + 1, quartile1, quartile3, color="k", linestyle="-", lw=4)
    ax.scatter(i + 1, median, color="w", s=40, zorder=3)
    ax.vlines(i + 1, lower_whisker, upper_whisker, color="k", linestyle="-", lw=1)
    ax.text(i + 1 + 0.3, np.median(data[i]), f"{median:.2f}", ha="left", va="center", color="black", rotation=45)

    # Annotate with Pearson R and EER values
    ax.text(i + 1, 0.14, f"{pearson_r[i]:.2f}", ha="center", va="center", color="green", fontsize=10)
    ax.text(i + 1, 0.08, f"{eer[i]:.2f}", ha="center", va="center", color="blue", fontsize=10)

ax.text(5.6, 0.14, textlabels[0], ha="left", va="center", color="green", fontsize=10)
ax.text(5.6, 0.08, textlabels[1], ha="left", va="center", color="blue", fontsize=10)

# Make the other parts of the violin plots invisible
for partname in ("cbars", "cmins", "cmaxes", "cmedians"):
    vp = violin_parts.get(partname)
    if vp:
        vp.set_visible(False)

# Add grid for better readability
ax.grid(True, linestyle='--', which='both', color='grey', alpha=0.5)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig('violin_20.pdf', bbox_inches='tight')

