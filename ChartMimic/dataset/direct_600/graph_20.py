
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
# Create a random graph with 12 nodes and a 0.3 probability for edge creation
random.seed(20)
np.random.seed(42)  # For reproducibility
G = nx.erdos_renyi_graph(15, 0.2)
weights = {edge: np.random.randint(1, 10) for edge in G.edges()}
nx.set_edge_attributes(G, weights, "weight")

# Use a spring layout for node positions
pos = nx.spring_layout(G, seed=42)

# Labels for nodes
labels = {i: f"Node {i}" for i in G.nodes()}

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, "weight")

title = "Cloud Infrastructure and Data Flow Network"

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 10))

# Draw nodes with a modern color scheme
nx.draw(G, pos, node_size=800, node_color="skyblue", edge_color="gray", with_labels=False)

# Draw the labels for the nodes
nx.draw_networkx_labels(G, pos, labels=labels, font_color="black", font_size=12, font_weight="bold")

# Draw the edges with varying widths based on weights
nx.draw_networkx_edges(G, pos, width=[weights[edge] * 0.8 for edge in G.edges()], edge_color="teal")

# Draw edge labels with weights
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=10)

# Add a title and configure layout
plt.title(title, size=20)
plt.tight_layout()

# ===================
# Part 4: Saving Output
# ===================
# Save the plot
plt.savefig("graph_20.pdf", bbox_inches="tight")
