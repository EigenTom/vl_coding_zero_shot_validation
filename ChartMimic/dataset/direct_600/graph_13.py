
# ===================
# Part 1: Importing Libraries
# ===================
import networkx as nx
import matplotlib.pyplot as plt

# ===================
# Part 2: Data Preparation
# ===================
# Create a directed graph for hospital departments
G = nx.DiGraph()
# Adding nodes representing departments
G.add_nodes_from([("Frontend", {"type": "module"}), 
                  ("Backend", {"type": "module"}), 
                  ("Database", {"type": "module"})])

# Adding edges representing interactions
G.add_edges_from([("Frontend", "Backend"), ("Backend", "Database"), ("Database", "Frontend")])

# Adding self-loops representing internal activities
self_loops = [("Frontend", "Frontend"), ("Backend", "Backend"), ("Database", "Database")]
G.add_edges_from(self_loops)

# Positioning nodes in a circular layout
pos = nx.circular_layout(G)

labels = ["Inter-module Communication", "Internal Module Activities"]

# ===================
# Part 3: Plot Configuration and Rendering
# ===================
plt.figure(figsize=(10, 8))

# Draw nodes and edges with base settings
nx.draw(G, pos, with_labels=True, node_color="violet", node_size=3000, edge_color="gray", linewidths=1.5, font_size=12, font_weight='bold')

# Highlight self-loops with a different style
nx.draw_networkx_edges(G, pos, edgelist=self_loops, edge_color="green", style="dashed", arrowstyle="<|-", arrowsize=20, width=2)

# Adding title and legend
plt.title("Interactions Between Software Modules", fontsize=16)
edge_legend = plt.Line2D([], [], linestyle="solid", color="gray", label=labels[0])
self_loop_legend = plt.Line2D([], [], linestyle="dashed", color="green", label=labels[1])
plt.legend(handles=[edge_legend, self_loop_legend])

# ===================
# Part 4: Saving Output
# ===================
# Displaying the plot with tight layout to minimize white space
plt.tight_layout()
plt.savefig("graph_13.pdf", bbox_inches="tight")
