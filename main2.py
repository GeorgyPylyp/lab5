import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sys
from io import StringIO


class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = {}

    def add_rule(self, condition, conclusion):
        """Додати правило ЯКЩО-ТО"""
        self.rules.append({
            'condition': condition,
            'conclusion': conclusion
        })

    def add_fact(self, attribute, value):
        """Додати факт про об'єкт"""
        self.facts[attribute] = value

    def evaluate(self):
        """Оцінити правила та зробити висновки"""
        conclusions = []

        for rule in self.rules:
            if self._check_condition(rule['condition']):
                conclusions.append(rule['conclusion'])

        return conclusions

    def _check_condition(self, condition):
        """Перевірити умову правила"""
        try:
            return eval(condition, {}, self.facts)
        except:
            return False

    def reset_facts(self):
        """Очистити факти"""
        self.facts = {}


# Приклад 1: Класифікація тварин
class AnimalClassifier:
    def __init__(self):
        self.system = ExpertSystem()
        self._setup_rules()

    def _setup_rules(self):
        # Додаємо правила класифікації тварин
        rules = [
            ("has_feathers == True", "Птах"),
            ("has_milk == True and has_feathers == False", "Ссавець"),
            ("has_scales == True and lives_in_water == True", "Риба"),
            ("has_scales == True and lives_in_water == False", "Рептилія"),
            ("has_legs == 0 and has_scales == False", "Земноводне"),
            ("has_milk == True and can_fly == True", "Кажан (літаючий ссавець)"),
            ("has_feathers == True and can_swim == True", "Водоплавний птах"),
            ("size == 'великий' and has_trunk == True", "Слон"),
            ("has_stripes == True and family == 'кіт'", "Тигр")
        ]

        for condition, conclusion in rules:
            self.system.add_rule(condition, conclusion)

    def classify_animal(self, characteristics):
        """Класифікувати тварину на основі характеристик"""
        self.system.reset_facts()

        # Додаємо факти про тварину
        for attr, value in characteristics.items():
            self.system.add_fact(attr, value)

        # Отримуємо висновки
        return self.system.evaluate()


# Приклад 2: Класифікація рослин
class PlantClassifier:
    def __init__(self):
        self.system = ExpertSystem()
        self._setup_rules()

    def _setup_rules(self):
        rules = [
            ("has_flowers == True and plant_type == 'дерево'", "Квітуче дерево"),
            ("has_flowers == False and plant_type == 'дерево'", "Хвойне дерево"),
            ("environment == 'вода'", "Водяна рослина"),
            ("is_edible == True and plant_type == 'овоч'", "Овочева культура"),
            ("is_edible == True and plant_type == 'фрукт'", "Фруктове дерево"),
            ("has_thorns == True", "Колюча рослина"),
            ("is_poisonous == True", "Отруйна рослина")
        ]

        for condition, conclusion in rules:
            self.system.add_rule(condition, conclusion)

    def classify_plant(self, characteristics):
        self.system.reset_facts()

        for attr, value in characteristics.items():
            self.system.add_fact(attr, value)

        return self.system.evaluate()


class ExpertSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌍 Експертна система класифікації")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.animal_classifier = AnimalClassifier()
        self.plant_classifier = PlantClassifier()

        self.setup_ui()

    def setup_ui(self):
        # Головний фрейм
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = ttk.Label(main_frame,
                                text="Експертна система класифікації",
                                font=('Arial', 16, 'bold'),
                                foreground='#2c3e50')
        title_label.pack(pady=20)

        # Фрейм для кнопок
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=30)

        # Кнопки меню
        buttons = [
            ("🐾 Класифікація тварин", self.open_animal_classification),
            ("🌿 Класифікація рослин", self.open_plant_classification),
            ("📊 Демонстрація", self.show_demo),
            ("ℹ️ Довідка", self.show_help),
            ("🚪 Вийти", self.root.quit)
        ]

        for text, command in buttons:
            btn = ttk.Button(button_frame,
                             text=text,
                             command=command,
                             width=25)
            btn.pack(pady=10)

        # Текстове поле для виводу
        self.output_text = scrolledtext.ScrolledText(main_frame,
                                                     height=15,
                                                     width=80,
                                                     font=('Consolas', 10))
        self.output_text.pack(pady=20, fill=tk.BOTH, expand=True)

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def print_output(self, text):
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)

    def open_animal_classification(self):
        self.clear_output()
        self.print_output("🐾 КЛАСИФІКАТОР ТВАРИН\n")
        self.print_output("Заповніть характеристики тварини:\n")

        animal_window = tk.Toplevel(self.root)
        animal_window.title("Класифікація тварин")
        animal_window.geometry("500x700")

        # Змінні для зберігання відповідей
        self.animal_vars = {}

        # Питання для тварин
        questions = [
            ('has_feathers', 'Чи має тварина пірья?'),
            ('has_milk', 'Чи годує тварина молоком своїх дітей?'),
            ('has_scales', 'Чи має тварина луску?'),
            ('lives_in_water', 'Чи живе тварина у воді?'),
            ('can_fly', 'Чи вміє тварина літати?'),
            ('can_swim', 'Чи вміє тварина добре плавати?'),
            ('has_stripes', 'Чи має тварина смуги?'),
            ('has_trunk', 'Чи має тварина хобот?')
        ]

        for i, (attr, question) in enumerate(questions):
            frame = ttk.Frame(animal_window)
            frame.pack(fill=tk.X, padx=20, pady=5)

            label = ttk.Label(frame, text=question, width=40)
            label.pack(side=tk.LEFT)

            var = tk.BooleanVar()
            self.animal_vars[attr] = var

            yes_btn = ttk.Radiobutton(frame, text="Так", variable=var, value=True)
            no_btn = ttk.Radiobutton(frame, text="Ні", variable=var, value=False)

            yes_btn.pack(side=tk.LEFT, padx=5)
            no_btn.pack(side=tk.LEFT, padx=5)

        # Додаткові поля
        extra_frame = ttk.Frame(animal_window)
        extra_frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(extra_frame, text="Кількість ніг:").pack(side=tk.LEFT)
        self.legs_var = tk.StringVar(value="0")
        legs_entry = ttk.Entry(extra_frame, textvariable=self.legs_var, width=10)
        legs_entry.pack(side=tk.LEFT, padx=5)

        # Кнопка класифікації
        classify_btn = ttk.Button(animal_window,
                                  text="Класифікувати",
                                  command=lambda: self.classify_animal_gui(animal_window))
        classify_btn.pack(pady=20)

    def classify_animal_gui(self, window):
        try:
            characteristics = {}

            # Збираємо відповіді з перемикачів
            for attr, var in self.animal_vars.items():
                characteristics[attr] = var.get()

            # Додаємо кількість ніг
            characteristics['has_legs'] = int(self.legs_var.get())

            # Додаткові характеристики
            if characteristics.get('has_stripes') and characteristics.get('has_milk'):
                characteristics['family'] = 'кіт'
            if characteristics.get('has_trunk'):
                characteristics['size'] = 'великий'

            # Класифікація
            result = self.animal_classifier.classify_animal(characteristics)

            # Вивід результату
            self.clear_output()
            self.print_output("🐾 РЕЗУЛЬТАТ КЛАСИФІКАЦІЇ ТВАРИНИ\n")
            self.print_output("Введені характеристики:")
            for attr, value in characteristics.items():
                self.print_output(f"  {attr}: {value}")

            self.print_output("\n🔍 Результат класифікації:")
            if result:
                for classification in result:
                    self.print_output(f"  ✅ {classification}")
            else:
                self.print_output("  ❌ Класифікація не визначена")

            window.destroy()

        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректне число ніг")
        except Exception as e:
            messagebox.showerror("Помилка", f"Сталася помилка: {e}")

    def open_plant_classification(self):
        self.clear_output()
        self.print_output("🌿 КЛАСИФІКАТОР РОСЛИН\n")

        plant_window = tk.Toplevel(self.root)
        plant_window.title("Класифікація рослин")
        plant_window.geometry("500x600")

        # Змінні для зберігання відповідей
        self.plant_vars = {}

        # Питання для рослин
        questions = [
            ('has_flowers', 'Чи має рослина квіти?'),
            ('has_thorns', 'Чи має рослина колючки?'),
            ('is_edible', 'Чи їстівна ця рослина?'),
            ('is_poisonous', 'Чи отруйна ця рослина?')
        ]

        for i, (attr, question) in enumerate(questions):
            frame = ttk.Frame(plant_window)
            frame.pack(fill=tk.X, padx=20, pady=5)

            label = ttk.Label(frame, text=question, width=40)
            label.pack(side=tk.LEFT)

            var = tk.BooleanVar()
            self.plant_vars[attr] = var

            yes_btn = ttk.Radiobutton(frame, text="Так", variable=var, value=True)
            no_btn = ttk.Radiobutton(frame, text="Ні", variable=var, value=False)

            yes_btn.pack(side=tk.LEFT, padx=5)
            no_btn.pack(side=tk.LEFT, padx=5)

        # Тип рослини
        type_frame = ttk.Frame(plant_window)
        type_frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(type_frame, text="Тип рослини:").pack(anchor=tk.W)
        self.plant_type_var = tk.StringVar(value="дерево")

        types = [("Дерево", "дерево"), ("Кущ", "кущ"), ("Трава", "трава"),
                 ("Овоч", "овоч"), ("Фрукт", "фрукт"), ("Інше", "інше")]

        for text, value in types:
            ttk.Radiobutton(type_frame, text=text, variable=self.plant_type_var,
                            value=value).pack(anchor=tk.W)

        # Середовище
        env_frame = ttk.Frame(plant_window)
        env_frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(env_frame, text="Середовище:").pack(anchor=tk.W)
        self.environment_var = tk.StringVar(value="суша")

        environments = [("На суші", "суша"), ("У воді", "вода"), ("Інше", "інше")]

        for text, value in environments:
            ttk.Radiobutton(env_frame, text=text, variable=self.environment_var,
                            value=value).pack(anchor=tk.W)

        # Кнопка класифікації
        classify_btn = ttk.Button(plant_window,
                                  text="Класифікувати",
                                  command=lambda: self.classify_plant_gui(plant_window))
        classify_btn.pack(pady=20)

    def classify_plant_gui(self, window):
        try:
            characteristics = {}

            # Збираємо відповіді з перемикачів
            for attr, var in self.plant_vars.items():
                characteristics[attr] = var.get()

            # Додаємо тип та середовище
            characteristics['plant_type'] = self.plant_type_var.get()
            characteristics['environment'] = self.environment_var.get()

            # Класифікація
            result = self.plant_classifier.classify_plant(characteristics)

            # Вивід результату
            self.clear_output()
            self.print_output("🌿 РЕЗУЛЬТАТ КЛАСИФІКАЦІЇ РОСЛИНИ\n")
            self.print_output("Введені характеристики:")
            for attr, value in characteristics.items():
                self.print_output(f"  {attr}: {value}")

            self.print_output("\n🔍 Результат класифікації:")
            if result:
                for classification in result:
                    self.print_output(f"  ✅ {classification}")
            else:
                self.print_output("  ❌ Класифікація не визначена")

            window.destroy()

        except Exception as e:
            messagebox.showerror("Помилка", f"Сталася помилка: {e}")

    def show_demo(self):
        self.clear_output()
        self.print_output("📊 ДЕМОНСТРАЦІЯ РОБОТИ СИСТЕМИ\n")

        # Демонстрація для тварин
        self.print_output("\n🐾 ПРИКЛАДИ КЛАСИФІКАЦІЇ ТВАРИН:")

        test_animals = [
            {
                'name': 'Орел',
                'characteristics': {
                    'has_feathers': True,
                    'has_milk': False,
                    'can_fly': True,
                    'has_legs': 2
                }
            },
            {
                'name': 'Кит',
                'characteristics': {
                    'has_feathers': False,
                    'has_milk': True,
                    'lives_in_water': True,
                    'has_scales': False
                }
            },
            {
                'name': 'Змія',
                'characteristics': {
                    'has_scales': True,
                    'lives_in_water': False,
                    'has_legs': 0,
                    'has_milk': False
                }
            }
        ]

        for animal in test_animals:
            classifications = self.animal_classifier.classify_animal(animal['characteristics'])
            self.print_output(f"\nТварина: {animal['name']}")
            self.print_output(f"Характеристики: {animal['characteristics']}")
            self.print_output(f"Класифікація: {', '.join(classifications) if classifications else 'Не визначено'}")

    def show_help(self):
        self.clear_output()
        self.print_output("ℹ️ ДОВІДКА ПО СИСТЕМІ\n")
        self.print_output("Ця експертна система використовує правила типу 'ЯКЩО-ТО'")
        self.print_output("для класифікації об'єктів на основі їх характеристик.\n")

        self.print_output("ДОСТУПНІ МОДУЛІ:")
        self.print_output("🐾 Класифікація тварин - визначення типу тварини")
        self.print_output("🌿 Класифікація рослин - визначення типу рослини")
        self.print_output("📊 Демонстрація - приклади роботи системи\n")

        self.print_output("ІНСТРУКЦІЯ:")
        self.print_output("1. Оберіть тип класифікації з головного меню")
        self.print_output("2. Заповніть характеристики об'єкта")
        self.print_output("3. Натисніть 'Класифікувати' для отримання результату")
        self.print_output("4. Результат з'явиться у текстовому полі\n")

        self.print_output("ПРАВИЛА СИСТЕМИ:")
        self.print_output("- Система аналізує введені факти")
        self.print_output("- Застосовує відповідні правила")
        self.print_output("- Повертає всі підходящі категорії")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ExpertSystemGUI()
    app.run()
