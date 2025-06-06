
import copy

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad
    
    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

# Crear objetos
direccion = Direccion("Calle Mayor 123", "Madrid")
persona1 = Persona("Juan", direccion)

# Copia superficial
persona2 = copy.copy(persona1)
persona2.nombre = "María"
persona2.direccion.calle = "Avenida Libertad 456"

print(f"Persona1: {persona1.nombre}, {persona1.direccion}")
print(f"Persona2: {persona2.nombre}, {persona2.direccion}")
# Ambas comparten la misma dirección

# Copia profunda
persona3 = copy.deepcopy(persona1)
persona3.direccion.calle = "Plaza España 789"

print(f"Persona1 después: {persona1.nombre}, {persona1.direccion}")
print(f"Persona3: {persona3.nombre}, {persona3.direccion}")





    
