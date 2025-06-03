
# Diferencia entre Método de Clase y Método Estático en Python

## Método de Clase (`@classmethod`)

- Primer parámetro: `cls`
- Tiene acceso a la clase
- Se usa para lógica relacionada con la clase como un todo
- Ejemplo común: fábricas o contadores

```python
class Persona:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

    @classmethod
    def crear_con_nombre_mayusculas(cls, nombre):
        return cls(nombre.upper())
```

## Método Estático (`@staticmethod`)

- No tiene parámetros especiales (ni `self` ni `cls`)
- No accede a instancia ni clase
- Se usa para lógica auxiliar o validaciones

```python
class Persona:
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18
```

## Comparativa

| Característica              | Método de Clase       | Método Estático      |
|----------------------------|-----------------------|-----------------------|
| Primer parámetro           | `cls`                 | Ninguno               |
| Accede a atributos de clase| ✅                    | ❌                    |
| Accede a atributos de instancia | ❌              | ❌                    |
| Propósito                  | Lógica de clase       | Funciones auxiliares  |
