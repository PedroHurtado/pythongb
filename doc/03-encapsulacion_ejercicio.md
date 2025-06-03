# Ejercicio de Encapsulación en Python

## 🧠 Enunciado: Clase `Producto`

### Objetivo
Crear una clase que represente un producto en una tienda, con control sobre su precio y stock usando encapsulación.

---

## 📋 Requisitos

1. **Atributos privados**:
   - `__nombre`: nombre del producto.
   - `__precio`: precio unitario (en euros, no puede ser negativo).
   - `__stock`: cantidad disponible (debe ser entero y no negativo).

2. **Métodos públicos**:
   - `mostrar_informacion()`: muestra nombre, precio y stock actual.
   - `agregar_stock(cantidad)`: suma `cantidad` al stock si es positiva.
   - `vender(cantidad)`: descuenta `cantidad` del stock si hay suficiente.
   - Getter y setter para el `precio`, con validación.

---

## 🧪 Ejemplo de uso esperado

```python
p = Producto("Camiseta", 20.0, 50)
p.mostrar_informacion()
# Producto: Camiseta, Precio: 20.0€, Stock: 50 unidades

p.vender(10)
p.mostrar_informacion()
# Producto: Camiseta, Precio: 20.0€, Stock: 40 unidades

p.precio = -5  # Error: precio inválido
p.precio = 25
print(p.precio)  # 25

p.agregar_stock(30)
p.mostrar_informacion()
# Producto: Camiseta, Precio: 25.0€, Stock: 70 unidades
```

---

### 💡 Pista

Puedes usar `@property` y `@precio.setter` para encapsular el atributo `__precio`.
