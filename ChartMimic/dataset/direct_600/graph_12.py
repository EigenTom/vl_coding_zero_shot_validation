
# ===================
# Part 1: Importing Libraries
# ===================
import networkx as nx
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph representing an organizational communication network
G = nx.DiGraph()

# Add nodes
G.add_nodes_from([1, 0, 2, 4,3])

# Add edges representing communication channels
communication_edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]

# Add self-loops representing personal tasks
self_loops = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# Combine all edges
G.add_edges_from(communication_edges + self_loops)

# Position nodes using a circular layout
pos = nx.circular_layout(G)

title = "Social Media Interaction Network"
annotation_text = 'Solid Lines: User Interaction\nDashed Lines: Moderation'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# Draw the graph with custom node and edge colors
nx.draw(G, pos, with_labels=True, node_color="darkcyan", edge_color="gray")

# Highlight the communication edges with solid lines
nx.draw_networkx_edges(G, pos, edgelist=communication_edges, edge_color="purple", style="solid", arrowstyle="->")

# Highlight the self-loops with dashed lines and different arrow style
nx.draw_networkx_edges(G, pos, edgelist=self_loops, edge_color="orange", style="dashed", arrowstyle="<|-")

# Add a title and legend to the plot
plt.title(title)
props = dict(boxstyle='round', facecolor='lightcoral', alpha=0.5)
plt.text(0.05, 0.95, annotation_text, 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', bbox=props)
# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_12.pdf", bbox_inches="tight")
