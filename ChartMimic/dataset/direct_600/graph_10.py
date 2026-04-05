
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
# Create a random graph representing a social network
G = nx.random_geometric_graph(25, 0.3)

# Position the nodes using the Kamada-Kawai layout algorithm for a spread-out structure
pos = nx.kamada_kawai_layout(G)

# Randomly select some edges to color as 'strong friendships'
edges = list(G.edges())
strong_friendships = np.random.choice(
    len(edges), size=int(len(edges) * 0.3), replace=False
)  # Highlighting 20% of the edges
strong_friendships = [edges[i] for i in strong_friendships]
title="Social Network OF Family Tree"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig = plt.subplots(figsize=(10, 10))

# Draw the nodes with a softer color
nx.draw_networkx_nodes(G, pos, node_size=300, node_color='#ffcccb', edgecolors='#2b2d42', linewidths=0.5)

# Draw the edges with a light transparency
nx.draw_networkx_edges(G, pos, edge_color='#a8dadc', alpha=0.5)

# Draw the selected 'strong friendship' edges with a distinct color
nx.draw_networkx_edges(G, pos, edgelist=strong_friendships, edge_color='#1d3557', width=2)

# Add a title
plt.title(title, fontsize=16)

# Add a legend
strong_patch = plt.Line2D([], [], color='#40E0D0', linewidth=2, linestyle='-', label='Strong Friendships')
all_patch = plt.Line2D([], [], color='#a8dadc', linewidth=2, linestyle='-', alpha=0.5, label='Friendships')
plt.legend(handles=[strong_patch, all_patch])

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_10.pdf", bbox_inches="tight")
