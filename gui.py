import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from graph import Graph
from backtracking import solve_coloring
from genetic import genetic_color
from visualizer import draw_colored_graph
from plot_fitness import show_fitness_plot
import time
import pygame
import os  # ✅ مضاف لحل مشكلة الصورة

class GraphColoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI GraphX - Graph Coloring")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e2f")

        self.graph = Graph()
        self.nodes = []

        self.current_step = 0
        self.steps = []

        self.setup_style()
        self.setup_music()
        self.setup_welcome_screen()

    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Custom.TButton",
                             background="#ff6f61",
                             foreground="white",
                             font=("Helvetica Neue", 12, "bold"),
                             padding=10,
                             borderwidth=0)
        self.style.map("Custom.TButton",
                       background=[("active", "#ff3b2e")],
                       foreground=[("active", "white")])

    def setup_music(self):
        try:
            pygame.init()
            pygame.mixer.init()
            audio_path = os.path.join(os.path.dirname(__file__), "background.mp3")
            if not os.path.exists(audio_path):
                raise FileNotFoundError("background.mp3 not found in project directory.")
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(-1)
            print("🎵 Background music started successfully.")
        except Exception as e:
            print("❌ Error loading music:", e)

    def setup_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.welcome_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.welcome_frame, bg="#1e1e2f", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        image_path = os.path.join(os.path.dirname(__file__), "welcome.png")
        self.original_image = Image.open(image_path)

        self.bg_image = ImageTk.PhotoImage(self.original_image)
        self.bg = self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image, tags="bg")

        self.start_button = ttk.Button(
            self.canvas,
            text="Start Now",
            command=self.start_loading,
            style="Custom.TButton"
        )
        self.button_window = self.canvas.create_window(500, 550, window=self.start_button, anchor="center")

        self.canvas.bind("<Configure>", self.resize_background)

    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized = self.original_image.resize((new_width, new_height))
        self.bg_image = ImageTk.PhotoImage(resized)
        self.canvas.itemconfig(self.bg, image=self.bg_image)
        self.canvas.coords(self.button_window, new_width / 2, new_height * 0.8)

    def start_loading(self):
        self.welcome_frame.pack_forget()
        self.loading_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.loading_frame.pack(fill="both", expand=True)

        self.loading_label = tk.Label(
            self.loading_frame,
            text="Loading AI GraphX...",
            font=("Helvetica Neue", 20, "bold"),
            fg="white",
            bg="#1e1e2f"
        )
        self.loading_label.place(relx=0.5, rely=0.4, anchor="center")

        self.progress_bar = ttk.Progressbar(
            self.loading_frame,
            mode='indeterminate',
            length=200
        )
        self.progress_bar.place(relx=0.5, rely=0.5, anchor="center")
        self.progress_bar.start(10)

        self.root.after(3000, self.complete_loading)

    def complete_loading(self):
        self.progress_bar.stop()
        self.loading_frame.pack_forget()
        self.show_main_interface()

    def show_main_interface(self):
        self.main_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.main_frame.pack(fill="both", expand=True)

        title = tk.Label(
            self.main_frame,
            text="AI GraphX - Smart Graph Coloring",
            font=("Helvetica Neue", 24, "bold"),
            fg="#ff6f61",
            bg="#1e1e2f"
        )
        title.pack(pady=20)

        self.steps = []

        step1 = tk.Frame(self.main_frame, bg="#1e1e2f")
        tk.Label(step1, text="Enter Number of Nodes:", font=("Helvetica Neue", 14), fg="white", bg="#1e1e2f").pack(pady=5)
        self.node_entry = ttk.Entry(step1)
        self.node_entry.pack(pady=5)
        ttk.Button(step1, text="Add Nodes", command=self.add_nodes, style="Custom.TButton").pack(pady=5)
        self.node_msg = tk.Label(step1, text="", fg="white", bg="#1e1e2f", font=("Helvetica Neue", 12))
        self.node_msg.pack(pady=5)
        self.steps.append(step1)

        step2 = tk.Frame(self.main_frame, bg="#1e1e2f")
        tk.Label(step2, text="Enter Edges (e.g. 0,1):", font=("Helvetica Neue", 14), fg="white", bg="#1e1e2f").pack(pady=5)
        self.edge_box = tk.Text(step2, height=5, width=40)
        self.edge_box.pack(pady=5)
        ttk.Button(step2, text="Add Edges", command=self.add_edges, style="Custom.TButton").pack(pady=5)
        self.edge_msg = tk.Label(step2, text="", fg="white", bg="#1e1e2f", font=("Helvetica Neue", 12))
        self.edge_msg.pack(pady=5)
        self.steps.append(step2)

        step3 = tk.Frame(self.main_frame, bg="#1e1e2f")
        tk.Label(step3, text="Enter Number of Colors:", font=("Helvetica Neue", 14), fg="white", bg="#1e1e2f").pack(pady=5)
        self.color_entry = ttk.Entry(step3)
        self.color_entry.pack(pady=5)

        self.algorithm = tk.StringVar(value="backtracking")
        ttk.Radiobutton(step3, text="Backtracking", variable=self.algorithm, value="backtracking").pack(pady=2)
        ttk.Radiobutton(step3, text="Genetic", variable=self.algorithm, value="genetic").pack(pady=2)

        ttk.Button(step3, text="Visualize Coloring", command=self.color_graph, style="Custom.TButton").pack(pady=5)
        self.time_label = tk.Label(step3, text="", bg="#1e1e2f", fg="#ffc107", font=("Helvetica Neue", 13, "bold"))
        self.time_label.pack(pady=5)
        self.config_msg = tk.Label(step3, text="", fg="white", bg="#1e1e2f", font=("Helvetica Neue", 12))
        self.config_msg.pack(pady=5)
        ttk.Button(step3, text="Reset Graph", command=self.reset_graph, style="Custom.TButton").pack(pady=10)
        self.steps.append(step3)

        self.show_step(0)

        nav_frame = tk.Frame(self.main_frame, bg="#1e1e2f")
        nav_frame.pack(pady=20)

        self.back_button = ttk.Button(nav_frame, text="<< Back", command=self.prev_step, style="Custom.TButton")
        self.back_button.grid(row=0, column=0, padx=10)

        self.next_button = ttk.Button(nav_frame, text="Next >>", command=self.next_step, style="Custom.TButton")
        self.next_button.grid(row=0, column=1, padx=10)

    def show_step(self, index):
        for i, step in enumerate(self.steps):
            step.pack_forget()
        self.steps[index].pack(pady=20)

        self.back_button.config(state="normal" if index > 0 else "disabled")
        self.next_button.config(state="normal" if index < len(self.steps) - 1 else "disabled")

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_step(self.current_step)

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_step(self.current_step)

    def show_message(self, label, text, color, advance=False):
        label.config(text=text, fg=color)
        self.root.after(2000, lambda: self._hide_message_and_continue(label, advance))

    def _hide_message_and_continue(self, label, advance):
        label.config(text="")
        if advance:
            self.next_step()

    def add_nodes(self):
        try:
            count = int(self.node_entry.get())
            if count <= 0:
                raise ValueError
            self.nodes = [str(i) for i in range(count)]
            self.graph = Graph()
            for node in self.nodes:
                self.graph.add_node(node)
            self.show_message(self.node_msg, "✅ Nodes added successfully!", "#00ff88", advance=True)
        except ValueError:
            self.show_message(self.node_msg, "❌ Enter a valid number of nodes.", "#ff4d4d")

    def add_edges(self):
        lines = self.edge_box.get("1.0", tk.END).strip().split("\n")
        added = False
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 2:
                node1, node2 = parts[0].strip(), parts[1].strip()
                if node1 in self.nodes and node2 in self.nodes:
                    self.graph.add_edge(node1, node2)
                    added = True
        if added:
            self.show_message(self.edge_msg, "✅ Edges added successfully!", "#00ff88", advance=True)
        else:
            self.show_message(self.edge_msg, "❌ Please enter valid edges.", "#ff4d4d")

    def color_graph(self):
        try:
            colors = int(self.color_entry.get())
            if colors <= 0:
                raise ValueError
        except ValueError:
            self.show_message(self.config_msg, "❌ Enter a valid number of colors.", "#ff4d4d")
            return

        method = self.algorithm.get()
        result = {}
        start_time = time.time()

        if method == "backtracking":
            success = solve_coloring(self.graph, self.nodes, colors, result)
            end_time = time.time()
            if not success:
                self.show_message(self.config_msg, "❌ Coloring failed using Backtracking.", "#ff4d4d")
                return
        else:
            result, fitness_progress = genetic_color(self.graph, colors, return_progress=True)
            show_fitness_plot(fitness_progress)
            end_time = time.time()
            if result is None:
                self.show_message(self.config_msg, "❌ Coloring failed using Genetic Algorithm.", "#ff4d4d")
                return

        total_time = end_time - start_time
        draw_colored_graph(self.graph, result)
        self.time_label.config(text=f"Time taken ({method}): {total_time:.3f} seconds")
        self.show_message(self.config_msg, "✅ Coloring completed successfully!", "#00ff88", advance=True)

    def reset_graph(self):
        self.graph = Graph()
        self.nodes = []
        self.node_entry.delete(0, tk.END)
        self.edge_box.delete("1.0", tk.END)
        self.color_entry.delete(0, tk.END)
        self.algorithm.set("backtracking")
        self.time_label.config(text="")
        self.main_frame.pack_forget()
        self.setup_welcome_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphColoringApp(root)
    root.mainloop()
