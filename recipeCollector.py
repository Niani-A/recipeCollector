'''This program will collect the recipes the user inputs. T
    the user will be given the option to add, list, and read recipes '''

allRecipes = {} #create empty dictionary

print("Type 'start' to begin program")#tell user to start program
#event loop
userInput = input(">").lower()

while userInput != "q" or userInput != "quit":
    if userInput !="q" and userInput != "quit":
        print("Type 'M', 'menu', or 'help' to see menu")
        userInput = input(">").lower()
        if (userInput == "m") or (userInput == "menu") or (userInput == "help"):
            print("N: Add New Recipe \nL: List Existing Recipes \nR: Read Recipes \nQ: Quit")
            
            menu = input(">").upper()
            if menu == "N":
                addRecipe = {}
                recipeName = input("Enter recipe name: ")
                addRecipe["name"] = recipeName
                recipeIngredients = input("Enter ingredients: ")
                addRecipe["ingredients"] = recipeIngredients
                recipeInstructions = input("Enter instructions: ")
                addRecipe["instructions"] = recipeInstructions
            
                #add new recipe if not already added
                if addRecipe in allRecipes.values():
                    print("ERROR THIS RECIPE HAS ALREADY BEEN ADDED")
                elif addRecipe not in allRecipes.values():
                    allRecipes[recipeName] = addRecipe
                    
            #list all recipes
            elif menu == "L":
                if len(allRecipes) > 0:
                    for key, value in allRecipes.items():
                        print(key)
                elif len(allRecipes) == 0:
                    print("No recipes listed")
            #find specifc recipes to read 
            elif menu == "R":
                findRecipe = input("Enter recipe to read: ")
                #print(allRecipes)
                if findRecipe in allRecipes.keys():
                    print((allRecipes[findRecipe]["name"]), "\nIngredients:", 
                       (allRecipes[findRecipe]["ingredients"]), "\nSteps:", 
                       (allRecipes[findRecipe]["instructions"]))
                elif findRecipe not in allRecipes.values():
                    print("RECIPE DOES NOT EXIST")
            elif menu == "Q" or menu == "QUIT":
                break
    elif userInput == "q" or userInput == "quit":
        break