import tkinter as tk
from tkinter import ttk, messagebox
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GeneticAlgorithm:
    def __init__(self, population_size=50, generations=100, mutation_rate=0.01, crossover_rate=0.7):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def fitness_function(self, x):
        """Функція для оптимізації: f(x) = x² + 3*sin(x)"""
        return x ** 2 + 3 * np.sin(x)

    def create_individual(self):
        """Створення одного індивіда (хромосома)"""
        return random.uniform(-10, 10)

    def create_population(self):
        """Створення початкової популяції"""
        return [self.create_individual() for _ in range(self.population_size)]

    def calculate_fitness(self, population):
        """Розрахунок пристосованості для кожної особини"""
        return [1 / (1 + abs(self.fitness_function(ind))) for ind in population]

    def selection(self, population, fitness):
        """Вибір батьків за допомогою рулетки"""
        total_fitness = sum(fitness)
        probabilities = [f / total_fitness for f in fitness]
        return random.choices(population, weights=probabilities, k=2)

    def crossover(self, parent1, parent2):
        """Одноточковий кросовер"""
        if random.random() < self.crossover_rate:
            alpha = random.random()
            child1 = alpha * parent1 + (1 - alpha) * parent2
            child2 = alpha * parent2 + (1 - alpha) * parent1
            return child1, child2
        return parent1, parent2

    def mutation(self, individual):
        """Мутація з нормальним розподілом"""
        if random.random() < self.mutation_rate:
            return individual + random.gauss(0, 1)
        return individual

    def run(self):
        """Запуск генетичного алгоритму"""
        population = self.create_population()
        best_individuals = []
        avg_fitness_history = []

        for generation in range(self.generations):
            fitness = self.calculate_fitness(population)

            # Збереження статистики
            best_idx = np.argmax(fitness)
            best_individuals.append(population[best_idx])
            avg_fitness_history.append(np.mean(fitness))

            # Створення нової популяції
            new_population = []

            while len(new_population) < self.population_size:
                # Вибір батьків
                parent1, parent2 = self.selection(population, fitness)

                # Кросовер
                child1, child2 = self.crossover(parent1, parent2)

                # Мутація
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)

                new_population.extend([child1, child2])

            population = new_population[:self.population_size]

        # Знаходження найкращого рішення
        final_fitness = self.calculate_fitness(population)
        best_idx = np.argmax(final_fitness)
        best_solution = population[best_idx]
        best_fitness = self.fitness_function(best_solution)

        return best_solution, best_fitness, best_individuals, avg_fitness_history


class GeneticAlgorithmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генетичний алгоритм - Оптимізація функції")
        self.root.geometry("800x600")

        self.ga = GeneticAlgorithm()
        self.setup_ui()

    def setup_ui(self):
        """Налаштування графічного інтерфейсу"""
        # Основний фрейм
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Заголовок
        title_label = ttk.Label(main_frame, text="Генетичний алгоритм для оптимізації функції",
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Фрейм параметрів
        params_frame = ttk.LabelFrame(main_frame, text="Параметри алгоритму", padding="10")
        params_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # Розмір популяції
        ttk.Label(params_frame, text="Розмір популяції:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.population_size = tk.StringVar(value="50")
        population_entry = ttk.Entry(params_frame, textvariable=self.population_size, width=10)
        population_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Кількість поколінь
        ttk.Label(params_frame, text="Кількість поколінь:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.generations = tk.StringVar(value="100")
        generations_entry = ttk.Entry(params_frame, textvariable=self.generations, width=10)
        generations_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Шанс мутації
        ttk.Label(params_frame, text="Шанс мутації:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.mutation_rate = tk.StringVar(value="0.01")
        mutation_entry = ttk.Entry(params_frame, textvariable=self.mutation_rate, width=10)
        mutation_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Шанс кросоверу
        ttk.Label(params_frame, text="Шанс кросоверу:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.crossover_rate = tk.StringVar(value="0.7")
        crossover_entry = ttk.Entry(params_frame, textvariable=self.crossover_rate, width=10)
        crossover_entry.grid(row=3, column=1, sticky=tk.W, pady=5)

        # Кнопки управління
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=20)

        ttk.Button(buttons_frame, text="Запустити алгоритм",
                   command=self.run_algorithm).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Показати графік функції",
                   command=self.show_function_plot).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Інформація",
                   command=self.show_info).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Вихід",
                   command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Фрейм результатів
        results_frame = ttk.LabelFrame(main_frame, text="Результати", padding="10")
        results_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.results_text = tk.Text(results_frame, height=10, width=40, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)

        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Фрейм для графіків
        self.plot_frame = ttk.Frame(main_frame)
        self.plot_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        # Налаштування розтягування
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        params_frame.columnconfigure(1, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)

    def validate_parameters(self):
        """Перевірка коректності введених параметрів"""
        try:
            population_size = int(self.population_size.get())
            generations = int(self.generations.get())
            mutation_rate = float(self.mutation_rate.get())
            crossover_rate = float(self.crossover_rate.get())

            if population_size <= 0 or generations <= 0:
                raise ValueError("Розмір популяції та кількість поколінь повинні бути більше 0")
            if not (0 <= mutation_rate <= 1) or not (0 <= crossover_rate <= 1):
                raise ValueError("Шанси мутації та кросоверу повинні бути в діапазоні [0, 1]")

            return population_size, generations, mutation_rate, crossover_rate

        except ValueError as e:
            messagebox.showerror("Помилка", f"Невірні параметри: {str(e)}")
            return None

    def run_algorithm(self):
        """Запуск генетичного алгоритму"""
        parameters = self.validate_parameters()
        if parameters is None:
            return

        population_size, generations, mutation_rate, crossover_rate = parameters

        # Оновлення параметрів алгоритму
        self.ga = GeneticAlgorithm(population_size, generations, mutation_rate, crossover_rate)

        # Запуск алгоритму
        best_solution, best_fitness, best_individuals, avg_fitness_history = self.ga.run()

        # Виведення результатів
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "=== РЕЗУЛЬТАТИ АЛГОРИТМУ ===\n\n")
        self.results_text.insert(tk.END, f"Знайдений мінімум: x = {best_solution:.4f}\n")
        self.results_text.insert(tk.END, f"Значення функції: f(x) = {best_fitness:.4f}\n")
        self.results_text.insert(tk.END, f"Розмір популяції: {population_size}\n")
        self.results_text.insert(tk.END, f"Кількість поколінь: {generations}\n")
        self.results_text.insert(tk.END, f"Шанс мутації: {mutation_rate}\n")
        self.results_text.insert(tk.END, f"Шанс кросоверу: {crossover_rate}\n")

        # Побудова графіків
        self.plot_results(best_individuals, avg_fitness_history, best_solution)

    def plot_results(self, best_individuals, avg_fitness_history, best_solution):
        """Побудова графіків результатів"""
        # Очищення попередніх графіків
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Створення фігури з двома підграфіками
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        # Графік 1: Збіжність алгоритму
        generations = range(len(best_individuals))
        ax1.plot(generations, [self.ga.fitness_function(x) for x in best_individuals], 'b-', label='Найкраща особина')
        ax1.plot(generations, avg_fitness_history, 'r-', label='Середня пристосованість')
        ax1.set_xlabel('Покоління')
        ax1.set_ylabel('Значення функції')
        ax1.set_title('Збіжність генетичного алгоритму')
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Графік 2: Функція та знайдений мінімум
        x = np.linspace(-10, 10, 400)
        y = self.ga.fitness_function(x)
        ax2.plot(x, y, 'g-', label='f(x) = x² + 3*sin(x)')
        ax2.plot(best_solution, self.ga.fitness_function(best_solution), 'ro',
                 markersize=8, label=f'Мінімум: x={best_solution:.3f}')
        ax2.set_xlabel('x')
        ax2.set_ylabel('f(x)')
        ax2.set_title('Функція та знайдений мінімум')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()

        # Вбудовування графіка в tkinter
        canvas = FigureCanvasTkAgg(fig, self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_function_plot(self):
        """Показати графік функції окремо"""
        x = np.linspace(-10, 10, 400)
        y = self.ga.fitness_function(x)

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.title('Функція для оптимізації: f(x) = x² + 3*sin(x)')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True, alpha=0.3)
        plt.show()

    def show_info(self):
        """Показати інформацію про програму"""
        info_text = """
Генетичний алгоритм для оптимізації функції

Функція: f(x) = x² + 3*sin(x)

Параметри алгоритму:
- Розмір популяції: кількість осіб у популяції
- Кількість поколінь: максимальна кількість ітерацій
- Шанс мутації: ймовірність мутації особини
- Шанс кросоверу: ймовірність схрещування батьків

Алгоритм знаходить мінімум функції на проміжку [-10, 10]
        """
        messagebox.showinfo("Інформація", info_text)


def main():
    root = tk.Tk()
    app = GeneticAlgorithmApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()