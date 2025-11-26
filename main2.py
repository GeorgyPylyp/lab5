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


def get_boolean_input(question):
    """Отримати відповідь True/False з обробкою виключень"""
    while True:
        try:
            answer = input(f"{question} (так/ні): ").strip().lower()
            if answer in ['так', 'т', 'yes', 'y', 'true', '1']:
                return True
            elif answer in ['ні', 'н', 'no', 'n', 'false', '0']:
                return False
            else:
                print("❗ Будь ласка, введіть 'так' або 'ні'")
        except KeyboardInterrupt:
            print("\n\nПрограму перервано. До побачення!")
            exit()
        except Exception as e:
            print(f"❗ Сталася помилка: {e}. Спробуйте ще раз.")


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
    
    def interactive_classification(self):
        """Інтерактивна класифікація тварини"""
        print("\n🎯 Давайте класифікуємо тварину!")
        print("Відповідайте на питання 'так' або 'ні'\n")
        
        characteristics = {}
        
        # Питання для класифікації тварин
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
        
        for attr, question in questions:
            characteristics[attr] = get_boolean_input(question)
        
        # Спеціальні атрибути, які потребують додаткових питань
        if characteristics.get('has_stripes') and characteristics.get('has_milk'):
            characteristics['family'] = 'кіт' if get_boolean_input("Чи належить тварина до родини котячих?") else 'інша'
        
        if characteristics.get('has_trunk'):
            characteristics['size'] = 'великий' if get_boolean_input("Чи є тварина великою?") else 'малий'
        
        # Кількість ніг (спеціальна обробка)
        legs_question = "Чи має тварина ноги?"
        if get_boolean_input(legs_question):
            while True:
                try:
                    legs = input("Скільки ніг має тварина? (введіть число): ").strip()
                    characteristics['has_legs'] = int(legs)
                    break
                except ValueError:
                    print("❗ Будь ласка, введіть коректне число ніг")
        else:
            characteristics['has_legs'] = 0
        
        return self.classify_animal(characteristics)


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
    
    def interactive_classification(self):
        """Інтерактивна класифікація рослини"""
        print("\n🌿 Давайте класифікуємо рослину!")
        print("Відповідайте на питання 'так' або 'ні'\n")
        
        characteristics = {}
        
        # Питання для класифікації рослин
        questions = [
            ('has_flowers', 'Чи має рослина квіти?'),
            ('has_thorns', 'Чи має рослина колючки?'),
            ('is_edible', 'Чи їстівна ця рослина?'),
            ('is_poisonous', 'Чи отруйна ця рослина?')
        ]
        
        for attr, question in questions:
            characteristics[attr] = get_boolean_input(question)
        
        # Визначення типу рослини
        print("\n🎯 Який тип рослини?")
        print("1 - Дерево")
        print("2 - Кущ") 
        print("3 - Трава")
        print("4 - Овоч")
        print("5 - Фрукт")
        print("6 - Інше")
        
        while True:
            try:
                type_choice = input("Оберіть номер типу (1-6): ").strip()
                type_map = {
                    '1': 'дерево', '2': 'кущ', '3': 'трава',
                    '4': 'овоч', '5': 'фрукт', '6': 'інше'
                }
                if type_choice in type_map:
                    characteristics['plant_type'] = type_map[type_choice]
                    break
                else:
                    print("❗ Будь ласка, оберіть номер від 1 до 6")
            except KeyboardInterrupt:
                print("\n\nПрограму перервано. До побачення!")
                exit()
            except Exception as e:
                print(f"❗ Сталася помилка: {e}. Спробуйте ще раз.")
        
        # Середовище рослини
        print("\n🎯 Де росте рослина?")
        print("1 - На суші")
        print("2 - У воді")
        print("3 - Інше")
        
        while True:
            try:
                env_choice = input("Оберіть номер середовища (1-3): ").strip()
                env_map = {'1': 'суша', '2': 'вода', '3': 'інше'}
                if env_choice in env_map:
                    characteristics['environment'] = env_map[env_choice]
                    break
                else:
                    print("❗ Будь ласка, оберіть номер від 1 до 3")
            except KeyboardInterrupt:
                print("\n\nПрограму перервано. До побачення!")
                exit()
            except Exception as e:
                print(f"❗ Сталася помилка: {e}. Спробуйте ще раз.")
        
        return self.classify_plant(characteristics)


# Демонстрація роботи системи
def demo_animal_classification():
    print("=== ДЕМОНСТРАЦІЯ КЛАСИФІКАТОРА ТВАРИН ===\n")
    
    classifier = AnimalClassifier()
    
    # Тестові приклади
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
        }
    ]
    
    for animal in test_animals:
        classifications = classifier.classify_animal(animal['characteristics'])
        print(f"Тварина: {animal['name']}")
        print(f"Характеристики: {animal['characteristics']}")
        print(f"Класифікація: {', '.join(classifications) if classifications else 'Не визначено'}")
        print("-" * 50)


# Інтерактивний режим
def interactive_mode():
    print("\n=== ІНТЕРАКТИВНИЙ РЕЖИМ ===")
    print("Оберіть тип класифікації:")
    print("1 - Класифікація тварин")
    print("2 - Класифікація рослин")
    print("3 - Вийти")
    
    while True:
        try:
            choice = input("\nВаш вибір (1/2/3): ").strip()
            
            if choice == "1":
                classifier = AnimalClassifier()
                result = classifier.interactive_classification()
                print(f"\n🎉 Результат класифікації: {', '.join(result) if result else 'Не визначено'}")
                break
                
            elif choice == "2":
                classifier = PlantClassifier()
                result = classifier.interactive_classification()
                print(f"\n🎉 Результат класифікації: {', '.join(result) if result else 'Не визначено'}")
                break
                
            elif choice == "3":
                print("До побачення!")
                exit()
                
            else:
                print("❗ Будь ласка, оберіть 1, 2 або 3")
                
        except KeyboardInterrupt:
            print("\n\nПрограму перервано. До побачення!")
            exit()
        except Exception as e:
            print(f"❗ Сталася помилка: {e}. Спробуйте ще раз.")


if __name__ == "__main__":
    print("🌍 Вітаємо в експертній системі класифікації!")
    
    # Запуск демонстрації
    demo_animal_classification()
    
    # Запуск інтерактивного режиму
    while True:
        interactive_mode()
        
        # Запит на продовження
        while True:
            try:
                continue_choice = input("\n🤔 Бажаєте продовжити? (так/ні): ").strip().lower()
                if continue_choice in ['так', 'т', 'yes', 'y']:
                    break
                elif continue_choice in ['ні', 'н', 'no', 'n']:
                    print("Дякуємо за використання програми! До побачення! 👋")
                    exit()
                else:
                    print("❗ Будь ласка, введіть 'так' або 'ні'")
            except KeyboardInterrupt:
                print("\n\nДякуємо за використання програми! До побачення! 👋")
                exit()