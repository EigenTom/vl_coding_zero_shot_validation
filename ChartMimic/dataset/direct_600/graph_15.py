
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

# Define nodes with component-related attributes
nodes = {
    0: ("Processor", "red"),
    1: ("Memory", "green"),
    2: ("Storage", "orange"),
    3: ("Network Interface", "blue"),
    4: ("GPU", "purple"),
    5: ("Power Supply", "black"),
    6: ("Cooling System", "lightblue"),
}
for node, (component, color) in nodes.items():
    G.add_node(node, component=component, color=color)

# Add edges with labels representing data flow
edges = [
    (0, 1, "Data Transfer"),
    (1, 2, "Data Read/Write"),
    (2, 3, "Network Transfer"),
    (3, 4, "Graphics Processing"),
    (4, 5, "Power Consumption"),
    (5, 6, "Heat Generation"),
]
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define node positions in a circular layout
pos = nx.circular_layout(G)

title = "Component Stations Communication Network"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 10))

# Draw nodes with color attribute
node_colors = [G.nodes[node]["color"] for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800, ax=ax)

# Draw edges with labels
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', arrowsize=20, width=2, edge_color='black', ax=ax)
edge_labels = {(u, v): G[u][v]["label"] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='darkred', font_size=10, ax=ax)

# Draw node labels indicating component conditions
node_labels = {node: G.nodes[node]["component"] for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color='black', ax=ax)

# Remove axis and add title
plt.axis("off")
plt.title( title, fontsize=16, fontweight='bold')

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_15.pdf", bbox_inches="tight")
