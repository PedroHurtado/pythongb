
# List Comprehensions en Python

Las list comprehensions permiten crear listas de manera concisa y eficiente.

---

## ✅ 1. Sintaxis básica

```python
[expresion for elemento in iterable]
```

### Ejemplo:

```python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
```

---

## ✅ 2. Con condición (filtro `if`)

```python
[expresion for elemento in iterable if condicion]
```

### Ejemplo:

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

## ✅ 3. Con `if-else` dentro de la expresión

```python
[valor_si_true if condicion else valor_si_false for elemento in iterable]
```

### Ejemplo:

```python
clasificacion = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(clasificacion)  # ['par', 'impar', 'par', 'impar', 'par']
```

---

## ✅ 4. Múltiples `for` (anidados)

```python
[expresion for x in iterable1 for y in iterable2]
```

### Ejemplo:

```python
productos_cartesianos = [(x, y) for x in [1, 2] for y in ['a', 'b']]
print(productos_cartesianos)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

## ✅ 5. Múltiples `for` con condición

```python
[expresion for x in iterable1 for y in iterable2 if condicion]
```

### Ejemplo:

```python
pares_suma = [(x, y) for x in range(3) for y in range(3) if (x + y) % 2 == 0]
print(pares_suma)  # [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
```

---

## ✅ 6. Anidamiento de comprensiones

```python
matriz = [[i * j for j in range(3)] for i in range(3)]
print(matriz)
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

## ✅ 7. Usando funciones en list comprehensions

```python
def cuadrado(n):
    return n * n

valores = [cuadrado(x) for x in range(5)]
print(valores)  # [0, 1, 4, 9, 16]
```

---

## ✅ 8. Consideraciones

Evita usar efectos secundarios (como `print()` o `append()`) dentro de list comprehensions. Si necesitas efectos, usa un bucle `for` tradicional.
