
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

# Add nodes with their respective colors and labels
nodes = {
    0: ("Emergency", "lightcoral"),
    1: ("Radiology", "dodgerblue"),
    2: ("Surgery", "lightgreen"),
    3: ("ICU", "gold"),
    4: ("Ward", "violet"),
    5: ("Pharmacy", "orange"),
    6: ("Discharge", "darkred"),
}
for node, (label, color) in nodes.items():
    G.add_node(node, label=label, color=color)

# Add edges with labels 
edges = [
    (0, 1, "to Radiology"), 
    (1, 2, "to Surgery"), 
    (2, 3, "to ICU"),
    (3, 4, "to Ward"),
    (4, 5, "to Pharmacy"),
    (5, 6, "to Discharge")
]
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Define node positions in a circular layout
pos = nx.circular_layout(G)

title = "Hospital Patient Workflow"


# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 10))

# Draw nodes with color attribute
node_colors = [G.nodes[node]["color"] for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=7000, ax=ax)

# Draw edges with arrows
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, ax=ax)

# Draw node labels
node_labels = {node: G.nodes[node]["label"] for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12, font_color="white", font_weight="bold", ax=ax)

# Draw edges with labels
edge_labels = {(u, v): G[u][v]["label"] for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

# Add a title
plt.title(title, size=15, fontweight="bold")

# Remove axis
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_7.pdf", bbox_inches="tight")
