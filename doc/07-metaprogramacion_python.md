# Metaprogramación en Python

## 🧠 Metaprogramación

La **metaprogramación** permite que un programa trate su propio código como datos, modificándolo en tiempo de ejecución.

### Usos comunes:
- Creación de APIs dinámicas
- Automatización de generación de clases/funciones
- Construcción de ORMs, validadores, decoradores

---

## 🔹 Metaclases

Una **metaclase** es la clase de una clase. Sirve para personalizar la creación de clases.

### Ejemplo:

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creando clase {name}")
        return super().__new__(cls, name, bases, dct)

class MiClase(metaclass=Meta):
    pass
```

**Salida:**
```
Creando clase MiClase
```

✅ `Meta` es una metaclase que intercepta el proceso de creación de `MiClase`.

---

## 🔹 Atributos especiales

Python asigna atributos especiales o mágicos a clases y objetos.

| Atributo         | Propósito |
|------------------|----------|
| `__dict__`       | Diccionario con los atributos del objeto |
| `__class__`      | Referencia a la clase del objeto |
| `__bases__`      | Tupla con las superclases de una clase |
| `__mro__`        | Orden de resolución de métodos |
| `__name__`       | Nombre de la clase |
| `__module__`     | Módulo donde se define la clase |
| `__init__`       | Constructor de instancia |
| `__new__`        | Método que crea la instancia |

### Ejemplo:

```python
class Animal:
    pass

print(Animal.__name__)   # Animal
print(Animal.__module__) # __main__
print(Animal.__bases__)  # (<class 'object'>,)
```

---

## 🔹 Función `type()`

### 1. Consultar el tipo de un objeto

```python
x = 42
print(type(x))  # <class 'int'>
```

### 2. Crear clases dinámicamente

```python
# Sintaxis: type(nombre_clase, tuplas_bases, diccionario_atributos)
Persona = type('Persona', (object,), {
    'nombre': 'Pedro',
    'saludar': lambda self: f'Hola, soy {self.nombre}'
})

p = Persona()
print(p.saludar())  # Hola, soy Pedro
```

✅ Se define una clase al vuelo sin usar `class`.

---

## 🔚 Resumen

| Concepto         | Clave |
|------------------|-------|
| Metaprogramación | Modifica clases/funciones en tiempo de ejecución |
| Metaclases       | Personalizan la creación de clases |
| Atributos mágicos| Información o personalización del comportamiento |
| `type()`         | Consulta tipo de objeto o crea clases dinámicamente |
