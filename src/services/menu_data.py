import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path):
        self.source_path = source_path
        self.dish = set()
        self._load_menu()

    def _load_menu(self):
        with open(self.source_path, newline='') as file:
            csv_reader = csv.DictReader(file)
            dish = {}

            for row in csv_reader:
                name_dish = row['dish']
                name_ingredient = row['ingredient']
                price = float(row['price'])
                recipe_amount = int(row['recipe_amount'])

                if name_dish not in dish:
                    dish_uni = Dish(name_dish, price)
                    dish[name_dish] = dish_uni
                else:
                    dish_uni = dish[name_dish]

                ingredient = Ingredient(name_ingredient)
                dish_uni.add_ingredient_dependency(ingredient, recipe_amount)
        self.dish = set(dish.values())
