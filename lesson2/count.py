class Budget:
    def __init__(self, name):
        self.name = name
        with open(f"{name}.txt", 'w', encoding='utf-8') as budget_file:
            budget_file.write('0')


class Product:
    is_available = True

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sell(self, file_name):
        if self.is_available:
            self.is_available = False
            with open(f"{file_name}.txt", 'r+', encoding='utf-8') as budget_file:
                current_budget = int(budget_file.read())

            with open(f"{file_name}.txt", 'w+', encoding='utf-8') as budget_file:
                current_budget += self.price
                budget_file.write(str(current_budget))
            print(f"Товар '{self.name}' продан, данные сохранены")
        else:
            print(f"Товара '{self.name}' в наличии нет!")
