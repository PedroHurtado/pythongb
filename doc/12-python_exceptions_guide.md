# Gestión de Excepciones en Python

## ¿Qué son las Excepciones?

Las excepciones son eventos que ocurren durante la ejecución de un programa que interrumpen el flujo normal de las instrucciones. En Python, cuando ocurre un error, se "lanza" (raise) una excepción que puede ser "capturada" (catch) y manejada adecuadamente.

## Sintaxis Básica: try-except

La estructura básica para manejar excepciones utiliza las palabras clave `try` y `except`:

```python
try:
    # Código que puede generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Manejo específico de la excepción
    print("Error: No se puede dividir por cero")
```

## Captura de Múltiples Excepciones

### Excepciones Específicas Separadas

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
```

### Múltiples Excepciones en una Sola Línea

```python
try:
    # Código que puede fallar
    operacion_riesgosa()
except (ValueError, TypeError, KeyError) as e:
    print(f"Error capturado: {e}")
```

## Bloques else y finally

### Bloque else
Se ejecuta solo si no se produce ninguna excepción:

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Operación exitosa. Resultado: {resultado}")
```

### Bloque finally
Se ejecuta siempre, independientemente de si ocurre una excepción o no:

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
else:
    print("Archivo leído correctamente")
finally:
    # Este bloque siempre se ejecuta
    if 'archivo' in locals():
        archivo.close()
    print("Limpieza completada")
```

## Captura de Información de la Excepción

### Usando la palabra clave as

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Mensaje: {e}")
    print(f"Argumentos: {e.args}")
```

### Captura Genérica

```python
try:
    # Código potencialmente problemático
    operacion_compleja()
except Exception as e:
    print(f"Error inesperado: {e}")
    # Registro del error para debugging
    import traceback
    traceback.print_exc()
```

## Lanzar Excepciones Personalizadas

### Usando raise

```python
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("Edad no realista")
    return True

try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error de validación: {e}")
```

### Re-lanzar Excepciones

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Registrando el error...")
    # Re-lanza la misma excepción
    raise
```

## Creación de Excepciones Personalizadas

### Excepción Básica

```python
class MiExcepcionPersonalizada(Exception):
    pass

def funcion_especial():
    raise MiExcepcionPersonalizada("Algo salió mal en mi función")

try:
    funcion_especial()
except MiExcepcionPersonalizada as e:
    print(f"Error personalizado: {e}")
```

### Excepción con Funcionalidad Adicional

```python
class ErrorValidacion(Exception):
    def __init__(self, mensaje, codigo_error=None):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        self.timestamp = __import__('datetime').datetime.now()

def procesar_datos(datos):
    if not datos:
        raise ErrorValidacion("Datos vacíos", codigo_error=1001)

try:
    procesar_datos([])
except ErrorValidacion as e:
    print(f"Error: {e}")
    print(f"Código: {e.codigo_error}")
    print(f"Timestamp: {e.timestamp}")
```

## Jerarquía de Excepciones Comunes

### Excepciones Built-in Más Frecuentes

- **Exception**: Clase base para la mayoría de excepciones
- **ValueError**: Argumento con tipo correcto pero valor inapropiado
- **TypeError**: Operación en tipo de dato inapropiado
- **KeyError**: Clave no encontrada en diccionario
- **IndexError**: Índice fuera de rango en secuencia
- **FileNotFoundError**: Archivo o directorio no encontrado
- **AttributeError**: Atributo no encontrado en objeto
- **ZeroDivisionError**: División por cero

### Ejemplo Práctico con Múltiples Tipos

```python
def operacion_completa(datos, indice, clave):
    try:
        # Múltiples operaciones que pueden fallar
        elemento = datos[indice]
        valor = elemento[clave]
        resultado = 100 / valor
        return resultado
    
    except IndexError:
        return "Error: Índice fuera de rango"
    except KeyError:
        return "Error: Clave no encontrada"
    except ZeroDivisionError:
        return "Error: División por cero"
    except TypeError:
        return "Error: Tipo de dato incorrecto"
    except Exception as e:
        return f"Error inesperado: {e}"

# Casos de prueba
datos = [{"a": 5}, {"b": 0}, {"c": "texto"}]
print(operacion_completa(datos, 0, "a"))  # Funciona: 20.0
print(operacion_completa(datos, 5, "a"))  # IndexError
print(operacion_completa(datos, 0, "x"))  # KeyError
print(operacion_completa(datos, 1, "b"))  # ZeroDivisionError
```

## Context Managers y Excepciones

### Usando with para Manejo Automático

```python
# Manejo automático de archivos
try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        # El archivo se cierra automáticamente
except FileNotFoundError:
    print("Archivo no encontrado")
except PermissionError:
    print("Sin permisos para leer el archivo")
```

## Mejores Prácticas

### 1. Sea Específico con las Excepciones

```python
# ✅ Bueno - Específico
try:
    valor = int(entrada)
except ValueError:
    print("Entrada no es un número válido")

# ❌ Malo - Demasiado general
try:
    valor = int(entrada)
except:
    print("Algo salió mal")
```

### 2. No Ignore las Excepciones

```python
# ❌ Malo - Silencia errores
try:
    operacion_riesgosa()
except:
    pass

# ✅ Bueno - Al menos registra el error
try:
    operacion_riesgosa()
except Exception as e:
    print(f"Error registrado: {e}")
    # O usar logging
```

### 3. Use finally para Limpieza

```python
recurso = None
try:
    recurso = adquirir_recurso()
    usar_recurso(recurso)
except Exception as e:
    print(f"Error al usar recurso: {e}")
finally:
    if recurso:
        liberar_recurso(recurso)
```

### 4. Documente las Excepciones en sus Funciones

```python
def dividir(a, b):
    """
    Divide dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
    
    Returns:
        float: Resultado de la división
    
    Raises:
        TypeError: Si los argumentos no son números
        ZeroDivisionError: Si b es cero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    
    return a / b
```

## Logging de Excepciones

```python
import logging

# Configurar logging
logging.basicConfig(level=logging.ERROR, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

def operacion_con_logging():
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error de división: {e}", exc_info=True)
        return None
```

## Ejemplo Práctico: Validador de Datos

```python
class ValidadorDatos:
    
    class ErrorValidacion(Exception):
        pass
    
    @staticmethod
    def validar_email(email):
        if "@" not in email:
            raise ValidadorDatos.ErrorValidacion("Email debe contener @")
        return True
    
    @staticmethod
    def validar_edad(edad):
        try:
            edad_int = int(edad)
        except ValueError:
            raise ValidadorDatos.ErrorValidacion("Edad debe ser un número")
        
        if edad_int < 0 or edad_int > 150:
            raise ValidadorDatos.ErrorValidacion("Edad debe estar entre 0 y 150")
        
        return edad_int

def procesar_usuario(datos):
    try:
        # Validaciones
        ValidadorDatos.validar_email(datos.get("email", ""))
        edad = ValidadorDatos.validar_edad(datos.get("edad", ""))
        
        print(f"Usuario válido: {datos['email']}, edad: {edad}")
        return True
        
    except ValidadorDatos.ErrorValidacion as e:
        print(f"Error de validación: {e}")
        return False
    except KeyError as e:
        print(f"Campo requerido faltante: {e}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

# Ejemplos de uso
usuarios = [
    {"email": "user@example.com", "edad": "25"},
    {"email": "invalid-email", "edad": "30"},
    {"email": "user2@example.com", "edad": "abc"},
    {"email": "user3@example.com", "edad": "200"}
]

for usuario in usuarios:
    procesar_usuario(usuario)
```

La gestión adecuada de excepciones es fundamental para crear aplicaciones robustas y mantenibles en Python. Permite que los programas manejen errores de manera elegante y proporcionen experiencias de usuario más fluidas.