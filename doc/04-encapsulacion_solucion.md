# Solución al Ejercicio de Encapsulación en Python

## ✅ Implementación de la clase `Producto`

```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio if precio >= 0 else 0
        self.__stock = stock if stock >= 0 else 0

    def mostrar_informacion(self):
        print(f"Producto: {self.__nombre}, Precio: {self.__precio}€, Stock: {self.__stock} unidades")

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
        else:
            print("Cantidad inválida para agregar al stock.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Cantidad inválida para vender.")
        elif cantidad > self.__stock:
            print("No hay suficiente stock disponible.")
        else:
            self.__stock -= cantidad

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio no puede ser negativo.")
```

---

## 🧪 Ejemplo de uso

```python
p = Producto("Camiseta", 20.0, 50)

p.mostrar_informacion()
# Producto: Camiseta, Precio: 20.0€, Stock: 50 unidades

p.vender(10)
p.mostrar_informacion()
# Producto: Camiseta, Precio: 20.0€, Stock: 40 unidades

p.precio = -5
# Error: el precio no puede ser negativo.

p.precio = 25
print(p.precio)
# 25

p.agregar_stock(30)
p.mostrar_informacion()
# Producto: Camiseta, Precio: 25.0€, Stock: 70 unidades
```
