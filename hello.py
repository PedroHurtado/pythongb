def fn(a):
    if a==8:
        return "Dato no valido"
    return a

source = [1,2,3,4,5,6,7,8,9,10]

for v in source:
    try:
        print(fn(v))
    except Exception:
        pass