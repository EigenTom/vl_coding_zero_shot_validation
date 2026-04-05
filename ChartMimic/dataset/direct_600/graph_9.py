# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)  # Ensuring reproducibility
# Create a random graph to represent a communication network
G = nx.random_geometric_graph(50, 0.2)

# Position nodes using the Kamada-Kawai layout to achieve a more spread-out layout
pos = nx.kamada_kawai_layout(G)

# Node type assignment: 50% base stations (blue), rest mobile devices (orange)
node_colors = []
for node in G.nodes():
    if np.random.rand() > 0.5:
        node_colors.append('blue')  # Base station
    else:
        node_colors.append('orange')  # Mobile device

# Edges: Mark 30% of the edges as experiencing packet loss (dashed lines, highlighted)
edges = list(G.edges())
num_packet_loss = int(len(edges) * 0.3)
packet_loss_edges = np.random.choice(len(edges), size=num_packet_loss, replace=False)
packet_loss_edges = [edges[i] for i in packet_loss_edges]

title = "Communication Network"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 10))

# Draw the nodes with respective colors
nx.draw_networkx_nodes(G, pos, node_size=100, node_color=node_colors, ax=ax)

# Draw all edges
nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray", alpha=0.5)

# Draw packet loss edges with a different style (dashed)
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=packet_loss_edges, style='dashed', edge_color="red")

# Add a legend
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='Mobile Device'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Base Station'),
    plt.Line2D([0], [0], color='gray', lw=2, alpha=0.5, label='Regular Connection'),
    plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2, label='Packet Loss')
]

ax.legend(handles=legend_elements, loc='upper right')

# Remove axis
plt.axis("off")

# Add a title
plt.title(title)

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_9.pdf", bbox_inches="tight")