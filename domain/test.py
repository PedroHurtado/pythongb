from ingredient import Ingredient
from pizza import Pizza

def main():
    ingredient = Ingredient(1,"Tomate",2.0)
    ingredients = set()
    
    ingredients.add(ingredient)
    
    pizza = Pizza(1,"Carbonara","pizza carbonara", ingredients)
    #maliciosa
    #ingredients.add(Ingredient(2,"Queso",3.0))

    #maliciosa
    #pizza.ingredients.add(Ingredient(3,"Pan",1.0))
    
    pizza.add_ingredient(Ingredient(1,"Piña",3.0))

    print(len(pizza.ingredients))
    print("Fin")

main()