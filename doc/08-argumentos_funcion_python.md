# Sintaxis de Argumentos de Función Extendida en Python

En Python, la sintaxis de argumentos de función extendida permite mayor flexibilidad al definir funciones.

---

## 1. `*args` y `**kwargs`

```python
def mi_funcion(*args, **kwargs):
    print("Posicionales:", args)
    print("Nombrados:", kwargs)

mi_funcion(1, 2, 3, nombre="Pedro", edad=40)
```

**Salida:**
```
Posicionales: (1, 2, 3)
Nombrados: {'nombre': 'Pedro', 'edad': 40}
```

---

## 2. Argumentos con nombre obligatorios

```python
def saludar(nombre, *, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")

saludar("Pedro", mensaje="Buenos días")  # Correcto
saludar("Pedro", "Buenos días")          # Error
```

---

## 3. Argumentos posicionales obligatorios

```python
def sumar(a, b, /, c):
    print(a + b + c)

sumar(1, 2, c=3)  # Correcto
sumar(a=1, b=2, c=3)  # Error
```

---

## 4. Ejemplo Completo

```python
def ejemplo(a, b, /, c, *, d, **kwargs):
    print(a, b, c, d, kwargs)

ejemplo(1, 2, 3, d=4, extra=5)
```

---

Esta sintaxis es muy útil para definir funciones claras y seguras, especialmente en librerías y APIs.