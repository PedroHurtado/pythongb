import copy
from ingredient import Ingredient
from entitybase import EntityBase


class Pizza(EntityBase):

    def __init__(self, id:int,name:str,description:str,ingredients:set[Ingredient]):
        super().__init__(id)
        self.__name = name
        self.__description = description
        self.__ingredients = copy.deepcopy(ingredients)

    def update(self, name:str,description:str):
        self.__name = name
        self.__description = description   
    
    
    @property 
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property    
    def ingredients(self):
        return copy.deepcopy(self.__ingredients)
    
    @property 
    def price(self):

        #price =0
        #for cost,*rest in self.__ingredients:
        #    price+=cost
        #return price * 1.2
        
        return sum(ingredient.cost for ingredient in self.__ingredients) * 1.2
    
    def add_ingredient(self,ingredient:Ingredient):
        self.__ingredients.add(ingredient)

    def remove_ingredient(self,ingredient:Ingredient):
        self.__ingredientes.remove(ingredient)
