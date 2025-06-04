def x(a):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(a)
            result = func(*args,**kwargs)
            print(a)
            return result
        return wrapper
    return decorator


@x("Hola decorada")
def decorada(b):   #clousure decorator
    print(b)
@x("Hola r")
def r():
    print("r")

decorada("decorada")  #antes ejecutas el wrapper
r()