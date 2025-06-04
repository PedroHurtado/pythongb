class Persona:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

    @classmethod
    def cantidad_personas(cls):
        return cls.contador
    def __del__(self):
        Persona.contador -=1
    
pedro =Persona("Pedro")
victor =Persona("Victor")
print(Persona.cantidad_personas()) #2
del victor
print(Persona.cantidad_personas()) #1
del pedro
print(Persona.cantidad_personas()) #0