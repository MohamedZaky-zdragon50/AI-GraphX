import matplotlib.pyplot as plt


def show_fitness_plot(fitness_progress):
    plt.plot(fitness_progress, marker="o", linestyle="-", color="blue")
    plt.title("Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Fitness Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
