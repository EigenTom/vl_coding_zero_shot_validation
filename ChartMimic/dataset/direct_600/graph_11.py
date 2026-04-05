
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a new graph representing a hypothetical legal network
G = nx.Graph()

# Add nodes representing different legal entities
# Add nodes representing different components in a cloud computing system
nodes = [("Data Center", {"type": "Infrastructure"}),
         ("Cloud Provider", {"type": "Service Provider"}),
         ("Enterprise User", {"type": "User"}),
         ("Individual User", {"type": "User"}),
         ("Regulatory Authority", {"type": "Government"})]
G.add_nodes_from(nodes)

# Add edges representing interactions
edges = [("Data Center", "Cloud Provider"),
         ("Cloud Provider", "Enterprise User"),
         ("Cloud Provider", "Individual User"),
         ("Data Center", "Regulatory Authority"),
         ("Regulatory Authority", "Enterprise User"),
         ("Regulatory Authority", "Individual User")]
G.add_edges_from(edges)

# Define positions for nodes explicitly
pos = {"Data Center": (1, 2), "Cloud Provider": (1, 1), "Enterprise User": (0, 0), "Individual User": (2, 0), "Regulatory Authority": (1, 3)}
title="Hypothetical Legal Network"
# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 10))

# Node color mapping based on entity type
color_map = {"Infrastructure": "rosybrown", "Service Provider": "lemonchiffon", "User": "gold", "Government": "aqua"}
# Draw nodes with colors based on their type
node_colors = [color_map[G.nodes[node]["type"]] for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=4000, edgecolors='black')

# Draw edges with alpha for transparency and consistent width
nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.7, width=2.5)

# Add labels to nodes
labels = {node: node for node in G.nodes}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=14, font_color="black")

# Create legend for node colors
import matplotlib.patches as mpatches
legend_elements = [mpatches.Patch(color=color, label=label) for label, color in color_map.items()]
plt.legend(handles=legend_elements, loc='upper left', frameon=False, fontsize=12)

# Title and axis settings
plt.title(title, fontsize=20, fontweight='bold')
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_11.pdf", bbox_inches="tight")

