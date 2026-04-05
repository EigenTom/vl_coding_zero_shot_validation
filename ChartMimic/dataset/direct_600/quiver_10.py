
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import numpy as np

import matplotlib.lines as mlines
import matplotlib.patches as mpatches


# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Define the vector field function
def vector_field(X, Y):
    U = -Y
    V = X
    return U, V


def modified_vector_field(X, Y):
    U = -1 - X**2 + Y
    V = 1 + X - Y**2
    return U, V


# Create a grid of points
x = np.linspace(0, 0.8, 10)
y = np.linspace(0, 0.8, 10)
X, Y = np.meshgrid(x, y)

# Compute the vector field
U, V = vector_field(X, Y)

# Compute the modified vector field
U_mod, V_mod = modified_vector_field(X, Y)

# Plot the curves as inverse functions with slightly different denominators for variation
x = np.linspace(0.2, 0.5, 100)
xlabel = "Technology X$_1$"
ylabel = "Technology X$_2$"
patch_labels = ["True Tech Field", "Model Learned Tech Field"]
line_labels = ["Tech Train Sample", "Tech Test Sample", "Model Train", "Model Test"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, color="#8e44ad", alpha=0.6)
plt.quiver(X, Y, U_mod, V_mod, color="#3498db", alpha=0.6)

plt.plot(x, 0.09 / (x**1.2), color="#e74c3c", linestyle='-', linewidth=2)
plt.plot(x, 0.08 / (x**1.2 + 0.04), color="#e67e22", linestyle='--', linewidth=2)
plt.plot(x, 0.075 / (x**1 + 0.04), color="#2ecc71", linestyle='-.', linewidth=2)
plt.plot(x, 0.12 / (x**1 + 0.05), color="#34495e", linestyle=':', linewidth=2)

# Add labels and legend
plt.xlabel(xlabel, fontsize=16, style="italic")
plt.ylabel(ylabel, fontsize=16, style="italic")

red_patch = mpatches.Patch(color="#8e44ad", label=patch_labels[0], alpha=0.6)
blue_patch = mpatches.Patch(color="#3498db", label=patch_labels[1], alpha=0.6)

# Create legend for curves
train_line = mlines.Line2D([], [], color="#e74c3c", label=line_labels[0], linestyle='-')
test_line = mlines.Line2D([], [], color="#e67e22", label=line_labels[1], linestyle='--')
sindy_train_line = mlines.Line2D([], [], color="#2ecc71", label=line_labels[2], linestyle='-.')
sindy_test_line = mlines.Line2D([], [], color="#34495e", label=line_labels[3], linestyle=':')

# Combine all legend handles
handles = [red_patch, blue_patch, train_line, test_line, sindy_train_line, sindy_test_line]

# Add the legend to the plot with specified location
plt.legend(handles=handles, loc="lower left")

# ===================
# Part 4: Saving Output
# ===================
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('quiver_10.pdf', bbox_inches='tight')
