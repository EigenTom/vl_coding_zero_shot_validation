
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph
G = nx.DiGraph()

# Add nodes with their respective energy types and colors
nodes = {
    0: ("Main Power Plant", "navy"),
    1: ("Substation A", "lightblue"),
    2: ("Substation B", "lightgreen"),
    3: ("Residential Area A1", "orange"),
    4: ("Residential Area A2", "pink"),
    5: ("Industrial Area B1", "purple"),
    6: ("Industrial Area B2", "red"),
}
for node, (location, color) in nodes.items():
    G.add_node(node, location=location, color=color)

# Add edges with capacities representing energy transmission
edges = [(0, 1, "500MW"), (0, 2, "600MW"), (1, 3, "200MW"), 
         (1, 4, "250MW"), (2, 5, "300MW"), (2, 6, "350MW")]
for u, v, capacity in edges:
    G.add_edge(u, v, capacity=capacity)

# Set network title and legend
title = "Power Grid Transmission Network"
legendtitle = "Energy Distribution Nodes"
    
# Define node positions in a circular layout
pos = nx.circular_layout(G)

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 10))

# Draw nodes with color attribute and label them
node_colors = [G.nodes[node]["color"] for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
nx.draw_networkx_labels(G, pos, labels={node: G.nodes[node]["location"] for node in G.nodes}, font_size=10)

# Draw edges with capacity labels
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
edge_labels = {(u, v): G[u][v]["capacity"] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Add a title
plt.title(title, fontsize=18)

# Add legend manually
legend_labels = {color: energy_type for _, (energy_type, color) in nodes.items()}
for color in set(node_colors):
    ax.plot([], [], color=color, label=legend_labels[color], marker='o', markersize=10, linestyle='')

# Removing the axis
plt.axis("off")

# Adding legend to the plot
plt.legend(title=legendtitle, loc="upper left")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_17.pdf", bbox_inches="tight")
