from book import Book
from recipe import Recipe
from datetime import datetime


def main() :
    tourte = Recipe("Tourte", 3, 35, ["Ketchup", "Cheese", "Meat"], "lunch")
    salad = Recipe("Salad", 1, 10, ["vegetables", "Cheese", "tomatoe"], "starter")
    cake = Recipe("Cake", 5, 45, ["Ketchup", "Cheese", "Meat"], "dessert")

    book = Book("Test", datetime.now(), datetime.now(),{"starter": {}, "lunch": {}, "dessert": {}})

    # Ajouter les recettes
    book.add_recipe(tourte)
    book.add_recipe(salad)
    book.add_recipe(cake)

    print("\n--- Vérification du contenu du livre ---")
    print(book.recipes_list)

    print("\n--- Recherche d'une recette ---")
    book.get_recipe_by_name("Tourte")

    print("\n--- Liste des recettes par type ---")
    book.get_recipes_by_types("lunch")
    book.get_recipes_by_types("dessert")
    book.get_recipes_by_types("starter")


if __name__ == "__main__" :
    main()
