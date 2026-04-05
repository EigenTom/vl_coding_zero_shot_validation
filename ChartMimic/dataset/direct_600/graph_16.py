
# ===================
# Part 1: Importing Libraries
# ===================
import matplotlib.pyplot as plt
import networkx as nx

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph representing an educational curriculum
G = nx.DiGraph()

# Add nodes representing different business departments
modules = {0: "Sales", 1: "Marketing", 2: "Product Development",
               3: "R&D", 4: "Finance", 5: "Human Resources",
               6: "IT Support", 7: "Customer Service", 8: "Operations",
               9: "Legal", 10: "Compliance", 11: "Supply Chain"}

G.add_nodes_from(modules.keys())

# Add edges with weights representing communication flow or collaboration (weight = frequency/importance)
edges = [(0, 1, 3), (1, 2, 4), (1, 9, 2), (2, 3, 4), (3, 4, 3),
         (3, 5, 2), (4, 7, 2), (5, 6, 1), (6, 10, 4), (7, 8, 3),
         (8, 10, 4), (10, 11, 2)]

G.add_weighted_edges_from(edges)

# Adjust node positions using spring layout for better visualization
pos = nx.spring_layout(G, seed=42)
title ="Marking units and their collaboration relationships"

# Labels for nodes and edges
node_labels = modules
edge_labels = {(start, end): f"{weight}" for start, end, weight in edges}

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(14, 10))

# Draw nodes with varying sizes and colors
node_size = [800 + 200 * (i % 3) for i in range(len(modules))]
node_color = ["lightblue" if i % 3 == 0 else "green" if i % 3 == 1 else "red" for i in range(len(modules))]

nx.draw(G, pos, node_size=node_size, node_color=node_color, with_labels=False, arrows=True)

# Draw labels for nodes and edges
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Adjust plot parameters for better visualization
plt.title(title, fontsize=15)
plt.axis('off')

# ===================
# Part 4: Saving Output
# ===================
# Show the plot
plt.tight_layout()
plt.savefig("graph_16.pdf", bbox_inches="tight")
