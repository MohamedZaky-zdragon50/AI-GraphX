import matplotlib.pyplot as plt
import networkx as nx

# First, I use networkx to create the graph.
def draw_colored_graph(graph, coloring, save_path=None):
    G = nx.Graph()

    # add nodes
    for node in graph.get_nodes():
        G.add_node(node)

    # add edges
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            G.add_edge(node, neighbor)

   # This is a list of the colors I will be using.
    color_map = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "orange",
        "cyan",
        "magenta",
    ]
    node_colors = []
    for node in G.nodes():
        color_index = coloring.get(node, 0) - 1# Here I am subtracting 1 for you because your color is usually from the first 1 and here the Index is from 0
        node_colors.append(color_map[color_index % len(color_map)])

    # draw the graph
    pos = nx.spring_layout(G)# (spring_layout) tries to leave spaces between each node and the next
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=800,
        font_color="white",
    )
    
    plt.show()