# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Create societal data
years = np.linspace(2000, 2020, 100)  # Years from 2000 to 2020
tech_adoption = np.exp(-0.003 * (years - 2010) ** 2)  # Tech adoption rate peaks around year 2010
internet_use = 0.9 * np.exp(-0.004 * (years - 2015) ** 2)  # Internet use peaks around year 2015

# Text variables
xlabel_text = "Year"
ylabel_text = "Proportion"
title_text = "Technology Adoption and Internet Use Over the Years"
legend_tech_adoption = 'Tech Adoption Rate'
legend_internet_use = 'Internet Use Rate'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
legend_location = 'upper right'
# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.fill_between(years, tech_adoption, color="purple", edgecolor="#800080", alpha=0.6, label=legend_tech_adoption)
ax.fill_between(years, internet_use, color="orange", edgecolor="#ffa500", alpha=0.6, label=legend_internet_use)

# Customize the plot
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.tick_params(left=True, labelleft=True, bottom=True, labelbottom=True)
ax.set_xlabel(xlabel_text)
ax.set_ylabel(ylabel_text)
ax.set_title(title_text)
ax.set_ylim(0, 1)

# Add legend
ax.legend(loc=legend_location)

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("density_13.pdf", bbox_inches="tight")