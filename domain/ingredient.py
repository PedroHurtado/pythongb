class Ingredient:
    def __init__(self, id:int, name:str, cost:float):        
        self.__id = id
        self.__name = name
        self.__cost = cost
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def cost(self):
        return self.__cost
    def update(self, name:str,cost:float):
        self.__name =name
        self.__cost = cost
    
    def __eq__(self, other):
        if isinstance(other, Ingredient):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)