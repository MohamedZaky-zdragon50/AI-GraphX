# 🎨 AI GraphX - Graph Coloring Problem Solver

AI GraphX is a smart and interactive **Graph Coloring Problem Solver** built using **Artificial Intelligence algorithms**:\

🧠 Backtracking Search Algorithm and 🧬 Genetic Algorithm.

> **Developed for**:\
> Helwan National University – FCSIT\
> CS212 Artificial Intelligence – Spring Semester 2024-2025

---

## 📌 Project Description

The **Graph Coloring Problem** is a classic optimization challenge where we assign colors to graph vertices such that no two adjacent vertices share the same color.\
This project allows users to:

- Input custom graphs (nodes & edges)
- Choose between two powerful AI algorithms:
  - **Backtracking**
  - **Genetic Algorithm**
- Visualize the coloring process in a user-friendly UI
- View performance metrics like time and fitness evolution

---

## 🧠 Algorithms Used

### 1. Backtracking Search Algorithm

- Systematically explores possible colorings
- Uses recursive depth-first traversal
- Backtracks upon conflicts

### 2. Genetic Algorithm

- Inspired by natural evolution
- Represents solutions as chromosomes
- Applies crossover, mutation & selection
- Tracks fitness (conflict minimization) over generations

---

## 🖼️ Features

- ✅ Add custom number of nodes and edges
- 🎨 Select number of colors
- 🔁 Switch between **Backtracking** or **Genetic Algorithm**
- 🖥️ Beautiful GUI using Tkinter
- 📊 Fitness Plot for Genetic Algorithm
- 🔊 Background music using Pygame
- 🚀 Real-time visualization of graph coloring

---

## 🛠️ Technologies & Libraries

| Library                | Purpose                              |
| ---------------------- | ------------------------------------ |
| `tkinter`              | GUI interface                        |
| `PIL`                  | Image handling (welcome screen)      |
| `pygame`               | Music playback                       |
| `networkx`             | Graph representation & visualization |
| `matplotlib`           | Fitness plotting                     |
| `random`, `time`, `os` | Core Python utilities                |

---

## 🧪 How to Run the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/graph-coloring-ai.git
   cd graph-coloring-ai
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:

   ```bash
   python main.py
   ```

---

## 🧾 Project Structure

```
📁 graph-coloring-ai/
│
├── 📂 assets/                  # Images, sounds (e.g., welcome.png, background.mp3)
├── 📄 main.py                 # Main application interface (UI logic)
├── 📄 graph.py                # Graph class definition
├── 📄 backtracking.py         # Backtracking algorithm implementation
├── 📄 genetic.py              # Genetic algorithm implementation
├── 📄 visualizer.py           # Graph drawing functions
├── 📄 plot_fitness.py         # Fitness plotting utility
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md               # Project documentation
```

---

## 📊 Output Examples

- 🎯 **Backtracking**:
  - Fast and deterministic
  - Suitable for small-to-medium graphs
- 🧬 **Genetic Algorithm**:
  - Heuristic and scalable
  - Shows evolution over generations via a fitness plot

---

## 📬 Contact

**Author**: Mohamed Zaky\
**Email**: [zakym6883@gmail.com](mailto\:zakym6883@gmail.com)\
**GitHub**: [github.com/zakym6883](https://github.com/zakym6883)

---

> "AI GraphX: Visualizing AI in Action, One Color at a Time."

