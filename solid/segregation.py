# En mi sistema existen clientes que se pueden 
#   crear,modificar,eliminar y recuperar
# lost usuarios solo se pueden 
#   leer

class Get:
    def get(self):
        pass
class Add:
    def add(self):
        pass
class Update(Get):
    def update(self):
        pass
class Remove(Get):
    def remove(self):
        pass

#mixin
class Repository(Add,Update,Remove):
    pass
    #def add():
    #    pass
    #def remove():
    #    pass
    #def get():
    #    pass
    #def update():
    #    pass

class Customer(Repository):
    pass
class User(Get):
    pass
    #def remove():
    #    pass  #exception
    #def update():
    #    pass  #exception
    #def add():
    #    pass  #exception

user = User()

user.get()

customer = Customer()

customer.add()
customer.update()
customer.remove()
customer.get()