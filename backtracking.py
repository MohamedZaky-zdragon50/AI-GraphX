# Here you can make sure that the color is not with the neighbors

def is_valid_coloring(node, color, colors, graph):
    for neighbor in graph.get_neighbors(node):
        if colors.get(neighbor) == color:
            return False
    return True



def solve_coloring(graph, nodes, num_colors, colors, index=0):

    if index == len(nodes):
        return True


    node = nodes[index]


    for color in range(1, num_colors + 1):
        if is_valid_coloring(node, color, colors, graph):
            colors[node] = color

           # Go to the next node
            if solve_coloring(graph, nodes, num_colors, colors, index + 1):
                return True

            # Here, if you do not find a suitable color, you will delete the color of this node and try another color.
            del colors[node]

    return False


# This is the basic function that we will start from.
def color_graph(graph, num_colors):
    nodes = graph.get_nodes()
    colors = {}

    if solve_coloring(graph, nodes, num_colors, colors):
        return colors
    else:
        return None
