
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
import numpy as np; np.random.seed(0)
# Data
x = ["AWS", "Azure", "Google Cloud", "IBM Cloud"]
y1 = [45, 60, 35, 50]  # Year 1 usage (in %)
y2 = [50, 62, 38, 52]  # Year 2 usage (in %)
y3 = [55, 64, 40, 54]  # Year 3 usage (in %)
y4 = [58, 65, 42, 55]  # Year 4 usage (in %)
labels= ["Year 1", "Year 2", "Year 3", "Year 4"]
insertax1=[0.6, 0.2, 0.1, 0.3]
insertylim1=[30, 40]
insertxlim1=[1.5, 2.5]
insertax2=[0.88, 0.7, 0.1, 0.2]
insertylim2=[45, 65]
insertxlim2=[2.5, 3.5]
xlabel="Cloud Provider"
ylabel="Usage Percentage"
title="Cloud Provider Usage Over Time"
insetaxes=[0.6, 0.5, 0.1, 0.3]
arrowend1 = [0.65, 0.4]
arrowend2 = [0.93, 0.7]
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
# Plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, "r-*", label=labels[0])
ax.plot(x, y2, "b-v", label=labels[1])
ax.plot(x, y3, "g--o", label=labels[2])
ax.plot(x, y4, "y-.s", label=labels[3])

# Create the first inset with the zoomed-in view
ax_inset1 = fig.add_axes(insetaxes)
ax_inset1.plot(x, y1, "r-*")
ax_inset1.plot(x, y2, "b-v")
ax_inset1.plot(x, y3, "g--o")
ax_inset1.plot(x, y4, "y-.s")
ax_inset1.spines["bottom"].set_color("black")
ax_inset1.spines["left"].set_color("black")
ax_inset1.spines["top"].set_color("black")
ax_inset1.spines["right"].set_color("black")
ax_inset1.set_ylim(insertylim1)
ax_inset1.set_xlim(insertxlim1)

# Create the second inset with the zoomed-in view
ax_inset2 = fig.add_axes(insertax2)
ax_inset2.plot(x, y1, "r-*")
ax_inset2.plot(x, y2, "b-v")
ax_inset2.plot(x, y3, "g--o")
ax_inset2.plot(x, y4, "y-.s")
ax_inset2.spines["bottom"].set_color("black")
ax_inset2.spines["left"].set_color("black")
ax_inset2.spines["top"].set_color("black")
ax_inset2.spines["right"].set_color("black")
ax_inset2.set_ylim(insertylim2)
ax_inset2.set_xlim(insertxlim2)

# Customizing the plot
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(title)
ax.legend(loc="lower right")
ax.grid(True)
ax.annotate(
    "",
    xy=(x[2], y3[2]),
    xytext=arrowend1,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1, shrink=0.01),
)
ax.annotate(
    "",
    xy=(x[3], y3[3]),
    xytext=arrowend2,
    textcoords="axes fraction",
    arrowprops=dict(facecolor="black", lw=0.1, shrink=0.01),
)

# ===================
# Part 4: Saving Output
# ===================
# Show plot
plt.tight_layout()
plt.savefig('PIP_15.pdf', bbox_inches='tight')
