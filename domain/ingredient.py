from entitybase import EntityBase

class Ingredient(EntityBase):
    def __init__(self, id:int, name:str, cost:float):        
        super().__init__(id)
        self.__name = name
        self.__cost = cost    
    @property
    def name(self):
        return self.__name
    @property
    def cost(self):
        return self.__cost
    def update(self, name:str,cost:float):
        self.__name =name
        self.__cost = cost
    
    @classmethod
    def create(cls,id:int,name:str,cost:float):
        return cls(id,name,cost)
    
    