from abc import ABC,abstractmethod

from functools import wraps


def checktype(expected_type):
    def decorator(func):
        
        #__name__ → el nombre de la función original
        #__doc__ → el docstring
        #__module__, __annotations__, etc.
        #Sin wraps, esos atributos se pierden y apuntan al wrapper.

        
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not args:
                raise ValueError("La función no recibió argumentos posicionales")
            if not isinstance(args[0], expected_type):
                raise TypeError(f"El primer argumento debe ser de tipo {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

class Ave(ABC):
    def __init__(self, peso):
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso

    @abstractmethod
    def __str__(self):
        pass


class AveVoladora(Ave, ABC):
    def __init__(self, peso, velocidad):
        super().__init__(peso)
        self.__velocidad = velocidad

    @property
    def velocidad(self):
        return self.__velocidad

    @abstractmethod
    def __str__(self):
        pass


class AveNoVoladora(Ave, ABC):  # Corregido el nombre
    def __init__(self, peso):
        super().__init__(peso)

    @abstractmethod
    def __str__(self):
        pass


class Pinguino(AveNoVoladora):
    def __init__(self, peso):
        super().__init__(peso)

    def __str__(self):
        return f"Pingüino de {self.peso} kg (no volador)"


class Aguila(AveVoladora):
    def __init__(self, peso, velocidad):
        super().__init__(peso, velocidad)
    def __str__(self):
        return f"Águila de {self.peso} kg y velocidad {self.velocidad} km/h"


class Paloma(AveVoladora):
    def __init__(self, peso, velocidad):
        super().__init__(peso, velocidad)
    def __str__(self):
        return f"Peso de {self.peso} kg y velocidad {self.velocidad} km/h"

@checktype(Ave)   
def print_ave(ave: Ave, printer=print):    
    printer(ave)
@checktype(AveVoladora)
def print_ave_voladora(ave: AveVoladora, printer=print):    
    printer(ave)
@checktype(AveNoVoladora)
def print_ave_no_voladora(ave: AveNoVoladora, printer=print):    
    printer(ave)

def main():
    pinguino = Pinguino(5)
    aguila = Aguila(10,100)

    print_ave(pinguino)
    print_ave(aguila)

    print_ave_voladora(aguila)

    print_ave_voladora(pinguino) 

    print_ave_no_voladora(pinguino)

    # print_ave_no_voladora(aguila) TypeError
    
main()

