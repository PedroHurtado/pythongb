from abc import ABC
class EntityBase(ABC):    
    def __init__(self, id:int):
        self.__id = id

    @property
    def id(self):
        return self.__id
    
    def __eq__(self, other):
        if isinstance(other, EntityBase):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
   
    