
# Clases en Python: Métodos y Propiedades

## 1. Métodos de Instancia

- Usan `self` como primer parámetro.
- Pertenecen a una **instancia** específica de la clase.
- Pueden acceder y modificar atributos de la instancia.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"
```

## 2. Métodos de Clase

- Usan `@classmethod` y reciben `cls` como primer parámetro.
- Acceden a atributos y métodos de **clase**.

```python
class Persona:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

    @classmethod
    def cantidad_personas(cls):
        return cls.contador
```

## 3. Métodos Estáticos

- Usan `@staticmethod`.
- No reciben ni `self` ni `cls`.
- Son funciones auxiliares que tienen lógica relacionada con la clase.

```python
class Matematica:
    @staticmethod
    def suma(a, b):
        return a + b
```

## 4. Propiedades

- Usan `@property` para definir métodos que se acceden como atributos.
- Permiten encapsular acceso y validación.

```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor > 0:
            self._radio = valor
        else:
            raise ValueError("El radio debe ser positivo")
```

## Comparativa rápida

| Tipo de método    | Decorador       | Primer argumento | Accede a instancia | Accede a clase |
|------------------|------------------|------------------|---------------------|----------------|
| Instancia         | (ninguno)        | `self`           | ✅                  | ❌             |
| Clase             | `@classmethod`   | `cls`            | ❌                  | ✅             |
| Estático          | `@staticmethod`  | (ninguno)        | ❌                  | ❌             |
