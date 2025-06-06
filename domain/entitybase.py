from abc import ABCMeta

class EntityMeta(ABCMeta):
    def __new__(mcs, name, bases, namespace):
        defaults = {
            'id': property(lambda self: self.__id),
            '__eq__': lambda self, other: isinstance(other, self.__class__) and self.id == other.id,
            '__hash__': lambda self: hash(self.id)
        }

        for key, value in defaults.items():
            namespace.setdefault(key, value)

        return super().__new__(mcs, name, bases, namespace)


class EntityBase(metaclass=EntityMeta):    
    def __init__(self, id:int):
        self.__id = id

    
   
    