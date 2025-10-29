
cookbook = {
    "Sandwich" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"], 
        "meal" : "lunch", 
        "prep_time" : 10
        },
    
    "Cake" : {
        "ingredients" : ["flour", "sugar", "eggs"], 
        "meal" : "dessert", 
        "prep_time" : 60
    },
    
    "Salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"], 
        "meal" : "lunch", 
        "prep_time" : 15
    }

    }

def print_recipe() :
    for key in cookbook :
        print(key)

def print_recipe_details() :
    recipe = input("Input a recipe to get its details: ")
    try :
        for key, value in cookbook[recipe].items() :
            print(recipe, key, ": ", value)        
    except KeyError :
        print("recipe doesn't exist")

def del_recipe() :
    recipe = input("Input a recipe to delete it: ")
    try :
        del cookbook[recipe]
    except KeyError :
        print("recipe doesn't exist")

def add_recipe() :
    recipe = input(">>> Fill the recipe: ")
    cookbook[recipe] = {
        "ingredients": [],
        "meal": "",
        "prep_time": 0
    }

    print (">>> Fill the ingredients: ")
    while True :
        text = input()
        if text == "" :
            break
        cookbook[recipe]["ingredients"].append(text) 

    cookbook[recipe]["meal"] = input(">>> Fill the meal type: ")
    cookbook[recipe]["prep_time"] = input(">>> Fill the preparation time(in minutes): ")    


def main() :
    print("Welcome to the python Cookbook !")
    print("List of available options")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    while True :
        print("\nPlease select an option:")
        choice = input(">> ")

        if choice == "1" :
            add_recipe()  
        elif choice == "2" :
            del_recipe()  
        elif choice == "3" :
            print_recipe_details()  
        elif choice == "4" :
            print_recipe()
        elif choice == "5" :
            return
        else :
            print("Invalid choice")

if __name__ == "__main__" :
    main()