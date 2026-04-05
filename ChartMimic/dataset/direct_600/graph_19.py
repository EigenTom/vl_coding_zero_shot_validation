
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Creating a house-like graph structure to resemble an art gallery layout
G = nx.house_graph()
# explicitly set positions (e.g., art pieces positions in a gallery)
pos = {0: (0, 0), 1: (2, 0), 2: (0.5, 3), 3: (1, 1), 4: (0.5, 2.0)}
labels = {
    0: "Main Data Center (Seattle)", 
    1: "Backup Data Center (Chicago)", 
    2: "Edge Server (New York)", 
    3: "Edge Server (San Francisco)", 
    4: "Client Device (Los Angeles)"
}

# Set the plot title and subtitle
title = "Cloud Computing Infrastructure Layout"
suptitle = "Data Flow and Connectivity between Key Network Components"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 10))

# Nodes configuration
nx.draw_networkx_nodes(G, pos, node_size=200, nodelist=[4], node_color="chocolate", edgecolors="black", linewidths=2)
nx.draw_networkx_nodes(G, pos, node_size=300, nodelist=[0, 1, 2, 3], node_color="darkseagreen", edgecolors="black", linewidths=2)

# Edges configuration
nx.draw_networkx_edges(G, pos, alpha=0.6, width=4, edge_color="gray", style="dashed")

# Adding text annotations - Labels for art pieces

nx.draw_networkx_labels(G, pos, labels=labels, font_size=14, font_color="black", font_family="sans-serif")

# Title and axis configurations
plt.title(title, fontsize=24, fontweight="bold")
plt.suptitle(suptitle, fontsize=16, style="italic")
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_19.pdf", bbox_inches="tight")
