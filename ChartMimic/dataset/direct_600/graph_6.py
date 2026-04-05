
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a simple directed graph to represent species interaction
G = nx.DiGraph()

# Add nodes representing different species
species = ["Tree", "Bird", "Bug", "Fungi", "Shrub", "Fox", "Deer", "Wolf"]
G.add_nodes_from(species)

# Add edges representing interactions with weights indicating interaction strength
interactions = [
    ("Tree", "Bird", 1), ("Tree", "Bug", 2), ("Bird", "Tree", 1),
    ("Bug", "Fungi", 3), ("Shrub", "Bug", 2), ("Fox", "Deer", 4),
    ("Wolf", "Fox", 3), ("Deer", "Shrub", 2), ("Fungi", "Tree", 1)
]
G.add_weighted_edges_from(interactions)

pos = nx.spring_layout(G, seed=42)  # Fixed layout for reproducibility

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, "weight")

title = "Species Interaction Network in an Ecosystem"
legend = ["Interaction Strength"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 10))

# Draw nodes with different colors and sizes based on their importance
node_sizes = [G.degree(node) * 300 for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="lightgreen", edgecolors='black')

# Draw edges with varying thickness based on weight
edge_weights = [G[u][v]['weight'] for u,v in G.edges()]
nx.draw_networkx_edges(G, pos, width=edge_weights, edge_color='brown', arrowstyle='-|>', arrowsize=12)

# Add labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=10)

# Add title and legend
plt.title(title, fontsize=16)
plt.legend(legend, loc="upper right")

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig("graph_6.pdf", bbox_inches="tight")
