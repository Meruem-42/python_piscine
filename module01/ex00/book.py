from datetime import datetime
from recipe import Recipe

lunch_type = ["starter", "lunch", "dessert"]

class Book :
    def __init__(self, name, last_update, creation_date, recipes_list) :
        if not isinstance(name, str) :
            raise TypeError(f"name need to be of string type")
        if not isinstance(last_update, datetime) :
            raise TypeError(f"last_update needs to be datetime type")
        if not isinstance(creation_date, datetime) :
            raise TypeError(f"creation_date needs to be datetime type")
        if not isinstance(recipes_list, dict) or not set(recipes_list) == set(lunch_type):
            raise TypeError(f"creation_date needs to be datetime type")
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for category, recipes in self.recipes_list.items():
            for recipe_name, recipe_obj in recipes.items():
                if recipe_name == name:
                    print(str(recipe_obj))
                    return recipe_obj
        print("Recipe not found")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type """
        for recipe_names in self.recipes_list[recipe_type] :
            print(recipe_names)

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe) :
            return(print("Wrong type of argument for recipe, needs tobe be Recipe"))
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe