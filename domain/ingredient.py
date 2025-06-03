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
    def costo(self):
        return self.__cost
    def update(self, name:str,cost:float):
        self.__name =name
        self.__cost = cost