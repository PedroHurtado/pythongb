import uuid
class Person:
    def __init__(self):
        print("Creado")
    def __del__(self):
        print("Eliminado")
    def isEquals(self,instance):
        return instance == self
    

def createPerson():
    person = Person()
    print(person.isEquals(person))   #true or false
def main():    
    uuid.uuid4()
    createPerson()        
    print("Fin")    

main()

