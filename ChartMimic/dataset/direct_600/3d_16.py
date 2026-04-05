# ===================
# Part 1: Importing Libraries
# ===================
import numpy as np
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================

# Generate data for different types of food consumption (fruits, vegetables, grains)
np.random.seed(42)

# Fruit consumption data
fruits = np.random.normal(loc=150, scale=25, size=50)  # mean consumption around 150 grams

# Vegetable consumption data
veggies = np.random.uniform(low=75, high=200, size=50)  # randomly between 75 and 200 grams

# Grain consumption data
grains = np.random.normal(loc=250, scale=30, size=50)  # mean consumption around 250 grams

# Second set of data for variations in different conditions
fruits2 = np.random.normal(loc=160, scale=20, size=50)
veggies2 = np.random.uniform(low=80, high=190, size=50)
grains2 = np.random.normal(loc=240, scale=35, size=50)

labels = ["Consumption Set 1", "Consumption Set 2"]
xlabel = "Fruit Consumption (grams)"
ylabel = "Vegetable Consumption (grams)"
zlabel = "Grain Consumption (grams)"
title = "3D Food Consumption Patterns"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw={"projection": "3d"})

# Configure the plot limits
ax.set_xlim3d([100, 200])
ax.set_ylim3d([50, 250])
ax.set_zlim3d([150, 400])

# Set the viewing angle
ax.view_init(elev=25, azim=60)
ax.dist = 10

# Scatter plot for the first set of data
ax.scatter3D(fruits, veggies, grains, color="green", marker='o', label=labels[0])

# Scatter plot for the second set of data
ax.scatter3D(fruits2, veggies2, grains2, color="orange", marker='^', label=labels[1])

# Modify axis labels and title
ax.set_xlabel(xlabel, fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)
ax.set_zlabel(zlabel, fontsize=12)
ax.set_title(title, fontsize=15)

# Legend for the plot
plt.legend(loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("3d_16.pdf", bbox_inches="tight")

