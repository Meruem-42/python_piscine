lunch_type = ["starter", "lunch", "dessert"]

class Recipe :
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None) :
        if not isinstance(name, str) :
            raise TypeError(f"name must be a string")
        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            raise TypeError(f"cooking_lvl must be a int or is out of range")
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise TypeError(f"cooking_time must be a int or is a negative time")
        if not isinstance(ingredients, list) or not all(isinstance(elem, str) for elem in ingredients) :
            raise TypeError(f"ingredients must be a list and elements in ingredients need to be strings")
        if not isinstance(description, str) and description is not None:
            raise TypeError(f"description must be a string")
        if not isinstance(recipe_type, str) or recipe_type not in lunch_type:
            raise TypeError(f"recipe_type must be a string and need to be in the list of words [starter, lunch, dessert]")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
    
    def __str__(self):
        return f"Recipe:\n \
        Name: {self.name}\n \
        Cooking level: {self.cooking_lvl}\n \
        Cooking time: {self.cooking_time} minutes\n \
        Ingredients: {self.ingredients}\n \
        Description: {self.description}\n \
        Recipe type: {self.recipe_type}\n \
        "

# def main() :
#     tourte = Recipe("Test", 5, 15, ["Ketchup", "Cheese", "Meat"], "lunch")
#     to_print = str(tourte)
#     print(to_print)

# main()