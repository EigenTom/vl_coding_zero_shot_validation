
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
# ===================
# Part 2: Data Preparation
# ===================
np.random.seed(0)
random.seed(42)
# Create a random social network graph
G = nx.random_geometric_graph(30, 0.5)

# Position the nodes based on their connections using a layout algorithm
pos = nx.spring_layout(G)  # This layout algorithm mimics the force-directed placement

# Randomly select some edges to color blue
edges = list(G.edges())
highlighted_edges = np.random.choice(
    len(edges), size=int(len(edges) * 0.3), replace=False
)
highlighted_edges = [edges[i] for i in highlighted_edges]

title = "Power Grid Transmission Network"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
fig, ax = plt.subplots(figsize=(10, 10))

# Draw the nodes
nx.draw_networkx_nodes(G, pos, node_size=200, node_color="darkorange", ax=ax)

# Draw the edges
nx.draw_networkx_edges(G, pos, edgelist=edges, alpha=0.2, edge_color="indianred", ax=ax)

# Draw the highlighted edges in blue
nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, edge_color="blue", width=2, alpha=0.6, ax=ax)

# Title and axis settings
plt.title(title, fontsize=15)
plt.axis("off")

# ===================
# Part 4: Saving Output
# ===================
plt.tight_layout()
plt.savefig("graph_18.pdf", bbox_inches="tight")
