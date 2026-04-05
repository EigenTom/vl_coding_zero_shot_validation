
# ===================
# Part 1: Importing Libraries
# ===================
import networkx as nx
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph
G = nx.DiGraph()

# Add nodes representing different entities in the energy flow
nodes = ['Main Data Center', 'Edge Server in NY', 'Edge Server in LA', 'User in NY', 'User in LA']
for node in nodes:
    G.add_node(node)

# Define edges representing data flow between entities
edges = [
    ('Main Data Center', 'Edge Server in NY'),
    ('Main Data Center', 'Edge Server in LA'),
    ('Edge Server in NY', 'User in NY'),
    ('Edge Server in LA', 'User in LA'),
    ('Edge Server in NY', 'Edge Server in NY'),  # Self-loop for data caching or processing in NY
    ('Edge Server in LA', 'Edge Server in LA'),  # Self-loop for data caching or processing in LA
    ('Main Data Center', 'Main Data Center')     # Self-loop for system monitoring or feedback
]

# Add edges to the graph
G.add_edges_from(edges)

# Define positions for a clear layout
pos = nx.spring_layout(G, seed=42)

title = 'Data Transformation Flow Between Entities'

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(12, 10))

# Draw the graph with customized node colors and labels
node_colors = ['green' if 'Main Data Cente' in node else 'blue' if 'Edge Server in NY' in node else 'yellow' for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=3000, font_size=10, font_weight='bold', edge_color='gray')

# Draw edges with differentiated styles for self-loops
self_loops = [(u, v) for u, v in G.edges() if u == v]
other_edges = [(u, v) for u, v in G.edges() if u != v]

nx.draw_networkx_edges(G, pos, edgelist=other_edges, arrowstyle='-|>', arrowsize=20, width=2.0, edge_color='black')
nx.draw_networkx_edges(G, pos, edgelist=self_loops, arrowstyle='-|>', style='dashed', arrowsize=20, width=2.0, edge_color='red')

# Title and labels
plt.title(title, fontsize=15)
plt.axis('off')

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_14.pdf", bbox_inches="tight")
