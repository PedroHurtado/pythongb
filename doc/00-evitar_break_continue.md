
# ¿Por qué evitar `break` y `continue` en Python?

El uso de `break` y `continue` en programación, aunque válido y funcional, **no se recomienda en ciertos contextos** porque puede hacer que el flujo del programa sea **menos predecible y más difícil de entender o mantener**, especialmente en estructuras de control complejas.

## ❌ Problemas comunes con `break` y `continue`

1. **Rompen el flujo natural del control**: interrumpen la secuencia lógica de ejecución dentro de un bucle.
2. **Disminuyen la claridad del código**: al forzar salidas o saltos condicionales, aumentan la carga cognitiva para entender qué está ocurriendo y por qué.
3. **Complican la depuración**: puede ser más difícil seguir la lógica del bucle cuando hay múltiples condiciones que interrumpen o reinician el ciclo.
4. **Impiden una programación estructurada limpia**, especialmente en métodos o funciones largas.

## ✅ Alternativa: estructurar el código con condiciones claras


### 🎯 Objetivo:
Encontrar el primer número divisible por 7 en una lista, ignorando los negativos.

---

### 🔴 Con `break` y `continue`:

```python
numeros = [3, -1, -2, 10, 15, 21, 28]

for numero in numeros:
    if numero < 0:
        continue
    if numero % 7 == 0:
        print("Primer divisible por 7:", numero)
        break
```

---

### 🟢 Sin `break` ni `continue`:

```python
numeros = [3, -1, -2, 10, 15, 21, 28]

primer_divisible = None
for numero in numeros:
    if numero >= 0 and numero % 7 == 0:
        primer_divisible = numero
        break  # en este caso se permite si es controlado y explícito

if primer_divisible is not None:
    print("Primer divisible por 7:", primer_divisible)
else:
    print("No se encontró ningún número divisible por 7")
```

#### Alternativa sin `break` usando `for-else`:

```python
for numero in numeros:
    if numero >= 0 and numero % 7 == 0:
        print("Primer divisible por 7:", numero)
        break
else:
    print("No se encontró ningún número divisible por 7")
```

> 💡 Aquí, el `else` del `for` solo se ejecuta si **no se usó `break`**, lo que da una forma elegante de evitar una bandera booleana adicional.

---

## ✅ Conclusión

Aunque `break` y `continue` son útiles y válidos, su abuso puede dificultar la comprensión del código. Siempre que sea posible, **prefiere estructuras condicionales claras y explícitas**. No es que nunca debas usarlos, pero como regla general en código mantenible y limpio, es mejor evitarlos salvo que haya una buena razón para ello.
