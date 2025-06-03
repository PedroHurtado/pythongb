class Ingrediente:
    def __init__(self, id, nombre, costo):
        #estado de los atributos es publico
        self.__id = id
        self.__nombre = nombre
        self.__costo = costo
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @property
    def costo(self):
        return self.__costo
    def __str__(self):
        return f"Ingrediente(id={self.__id}, name={self.__nombre}, costo={self.__costo})"

def main():
    ingredient = Ingrediente(1,"Tomate",2.0)       
    ingredient.nombre = "Queso"
    print(ingredient.id, ingredient.nombre, ingredient.costo) #ok
    #ingredient.get_id()
    print("Fin")

main()