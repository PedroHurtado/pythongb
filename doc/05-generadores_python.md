
# Ejemplos de Generadores en Python

Este documento contiene ejemplos de cómo trabajar con generadores en Python, incluyendo expresiones generadoras y técnicas para "extender" generadores.

---

## 1. Generador clásico

```python
def numeros():
    for i in range(5):
        yield i

for n in numeros():
    print(n)
```

---

## 2. Encadenar generadores con `yield from`

```python
def gen1():
    yield from [1, 2, 3]

def gen2():
    yield from [4, 5, 6]

def combinado():
    yield from gen1()
    yield from gen2()

print(list(combinado()))  # [1, 2, 3, 4, 5, 6]
```

---

## 3. Generador con lógica adicional (filtro)

```python
def numeros():
    for i in range(10):
        yield i

def solo_pares(g):
    for n in g:
        if n % 2 == 0:
            yield n

print(list(solo_pares(numeros())))  # [0, 2, 4, 6, 8]
```

---

## 4. Herencia de clases con generadores

```python
class Contador:
    def __init__(self, maximo):
        self.maximo = maximo

    def __iter__(self):
        for i in range(self.maximo):
            yield i

class ContadorPares(Contador):
    def __iter__(self):
        for i in super().__iter__():
            if i % 2 == 0:
                yield i

print(list(ContadorPares(10)))  # [0, 2, 4, 6, 8]
```

---

## 5. Decorador de generador (logging)

```python
def loggear_generador(g):
    for x in g:
        print(f"YIELD: {x}")
        yield x

def datos():
    yield from [10, 20, 30]

for x in loggear_generador(datos()):
    pass
```

---

## 6. Expresión generadora básica

```python
gen = (x**2 for x in range(5))
for num in gen:
    print(num)
```

---

## 7. Extensión de generadores con `itertools.chain`

```python
from itertools import chain

gen1 = (x for x in range(3))
gen2 = (x * 10 for x in range(3))

combinado = chain(gen1, gen2)
print(list(combinado))  # [0, 1, 2, 0, 10, 20]
```

---

## 8. Expresión generadora como argumento

```python
def suma(valores):
    return sum(valores)

resultado = suma(x for x in range(100) if x % 2 == 0)
print(resultado)  # 2450
```

---

## 9. `yield from` con expresión generadora

```python
def wrapper():
    yield from (x * 2 for x in range(5))

print(list(wrapper()))  # [0, 2, 4, 6, 8]
```
