from ingredient import Ingredient
from pizza import Pizza
from entitybase import EntityBase

def main():
    #entity = EntityBase(id)
    #print(entity)
    #ingredient = Ingredient(1,"Tomate",2.0)
    ingredient = Ingredient.create(1,"Tomate",2.0)
    ingredients = set()
    
    ingredients.add(ingredient)
    
    pizza = Pizza(1,"Carbonara","pizza carbonara", ingredients)
    #maliciosa
    #ingredients.add(Ingredient(2,"Queso",3.0))

    #maliciosa
    #pizza.ingredients.add(Ingredient(3,"Pan",1.0))
    
    pizza.add_ingredient(Ingredient(2,"Piña",3.0))

    print(len(pizza.ingredients))
    print(pizza.price)
    print("Fin")

main()