class Graph:
    def __init__(self):
        self.map = {}

    def add_node(self, node):
        if node not in self.map:
            self.map[node] = [] #Here I put the node as the key and make it an empty list

    def add_edge(self, first_node, second_node):
        # Here I make sure that the nodes are present with me or not
        if first_node not in self.map:
            self.add_node(first_node)
        if second_node not in self.map:
            self.add_node(second_node)
       # After I make sure they exist, I add each node to the other's list.
        if second_node not in self.map[first_node]:
            self.map[first_node].append(second_node)
        if first_node not in self.map[second_node]:
            self.map[second_node].append(first_node)

    def get_nodes(self):
        return list(self.map.keys())

    def get_neighbors(self, node):
        return self.map.get(node, [])#Here I used (get) so that when it doesn't find the node it prints an empty list instead of giving an error.

    def print_graph(self):
        for node in self.map:
            print(node, "->", self.map[node])#But here it prints what is there, so it is not necessary to use get
