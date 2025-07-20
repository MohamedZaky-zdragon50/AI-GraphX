import random

# Make sure there are no neighbors of the same color
def is_valid_coloring(graph, coloring):
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            if coloring.get(node) == coloring.get(neighbor):
                return False
    return True

# The quality of the coloring is calculated (the higher the better)
def fitness(graph, coloring):
    score = 0
    for node in graph.get_nodes():
        for neighbor in graph.get_neighbors(node):
            if coloring.get(node) != coloring.get(neighbor):
                score += 1
    return score

# It generates random coloring
def generate_coloring(graph, num_colors):
    coloring = {}
    for node in graph.get_nodes():
        coloring[node] = random.randint(1, num_colors)
    return coloring

# Main algorithm
def genetic_color(graph, num_colors, population_size=50, generations=100, return_progress=False):

    # Here we store the best fitness in each generation to draw it later
    fitness_progress = []

    # Generate of the first generation
    population = [generate_coloring(graph, num_colors) for _ in range(population_size)]

    for _ in range(generations):
        # Population ranking from best to worst
        population.sort(key=lambda c: fitness(graph, c), reverse=True)

        # Rate the highest fitness
        best_fitness = fitness(graph, population[0])
        fitness_progress.append(best_fitness)

        # If you find a valid coloring, return it immediately.
        if is_valid_coloring(graph, population[0]):
            if return_progress:
                return population[0], fitness_progress
            return population[0]

        # Keep the best 10
        population = population[:10]
        new_population = population.copy()

        while len(new_population) < population_size:
            # Random selection of parents
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = {}

            # Crossover
            for node in graph.get_nodes():
                if random.random() < 0.5:
                    child[node] = parent1[node]
                else:
                    child[node] = parent2[node]

            # Mutation 
            mutation_rate = 0.1
            for node in graph.get_nodes():
                if random.random() < mutation_rate:
                    child[node] = random.randint(1, num_colors)

            new_population.append(child)

        population = new_population

    # After the generations ended, the best coloring is back
    population.sort(key=lambda c: fitness(graph, c), reverse=True)
    if is_valid_coloring(graph, population[0]):
        if return_progress:
            return population[0], fitness_progress
        return population[0]
    else:
        if return_progress:
            return None, fitness_progress
        return None