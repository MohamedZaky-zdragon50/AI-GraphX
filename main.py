from graph import Graph
from backtracking import color_graph
from genetic import genetic_color
from visualizer import draw_colored_graph
import time
from plot_fitness import show_fitness_plot


# Function to compute the chromatic number (minimum number of colors needed to color the graph)
def chromatic_number(graph):
    # Try increasing number of colors until a valid coloring is found (using backtracking)
    n = 1
    while True:
        coloring = color_graph(graph, n)
        if coloring:
            return n, coloring
        n += 1


# Function to print information about the graph (number of nodes, edges, degrees, connectivity)
def print_graph_info(graph):
    print("\nGraph Info:")
    nodes = graph.get_nodes()
    print(f"Number of nodes: {len(nodes)}")
    edges = set()
    for node in nodes:
        for neighbor in graph.get_neighbors(node):
            if (neighbor, node) not in edges:
                edges.add((node, neighbor))
    print(f"Number of edges: {len(edges)}")
    print("Degrees:")
    for node in nodes:
        print(f"  Node {node}: {len(graph.get_neighbors(node))}")
    # Check if connected (simple BFS)
    if nodes:
        visited = set()
        queue = [nodes[0]]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                queue.extend(
                    [n for n in graph.get_neighbors(current) if n not in visited]
                )
        print(f"Connected: {'Yes' if len(visited) == len(nodes) else 'No'}")


# Function to load a graph from a text file
def load_graph_from_file(filename):
    g = Graph()
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        num_nodes = int(lines[0])
        node_names = lines[1 : num_nodes + 1]
        for node in node_names:
            g.add_node(node)
        num_edges = int(lines[num_nodes + 1])
        edge_lines = lines[num_nodes + 2 : num_nodes + 2 + num_edges]
        for line in edge_lines:
            node1, node2 = line.split()
            g.add_edge(node1, node2)
    return g


# Main program logic
def main():
    # Interactive input for graph creation
    g = Graph()
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    node_names = []
    for i in range(num_nodes):
        node = input(f"Enter name for node {i + 1}: ")
        g.add_node(node)
        node_names.append(node)
    num_edges = int(input("\nEnter the number of edges in the graph: "))
    for i in range(num_edges):
        print(f"\nEdge {i + 1}:")
        node1 = input("Enter first node: ")
        node2 = input("Enter second node: ")
        g.add_edge(node1, node2)

    # Calculate and display the chromatic number
    print("\nCalculating chromatic number (minimum colors needed)...")
    min_colors, min_coloring = chromatic_number(g)
    print(f"Chromatic number: {min_colors}")
    print("Example optimal coloring:")
    for node, color in min_coloring.items():
        print(f"Node {node} has color {color}")

    # Ask the user for the number of colors to use
    num_colors = int(input("\nEnter the number of colors to use: "))
    print("\n1. Backtracking")
    print("2. Genetic Algorithm")
    choice = input("Choose the solving method (1 or 2): ")

    # Solve the coloring problem using the selected method
    start = time.time()
    if choice == "1":
        # Use backtracking algorithm
        coloring = color_graph(g, num_colors)
        method = "Backtracking"
    elif choice == "2":
        # Ask for genetic algorithm parameters
        population_size = int(input("Enter population size (default 50): ") or "50")
        generations = int(input("Enter number of generations (default 100): ") or "100")
        coloring, fitness_progress = genetic_color(
            g,
            num_colors,
            population_size=population_size,
            generations=generations,
            return_progress=True
        )
        # Show fitness plot
        show_fitness_plot(fitness_progress)

        method = "Genetic Algorithm"
    else:
        print("Invalid choice.")
        return
    elapsed = time.time() - start

    # Show the result and draw the graph
    if coloring:
        print(f"\nResult using {method} (in {elapsed:.4f} seconds):")
        for node, color in coloring.items():
            print(f"Node {node} has color {color}")
        # هنا برسم ال graph
        draw_colored_graph(g, coloring)
    else:
        print("\nNo valid coloring found with the given number of colors.")


# Entry point of the program
if __name__ == "__main__":
    main()
