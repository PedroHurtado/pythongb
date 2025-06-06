import time
from functools import wraps

def info_funcion(func):
    """
    Decorador que muestra información detallada sobre la ejecución de una función:
    - Nombre de la función
    - Argumentos posicionales
    - Argumentos por nombre (keyword arguments)
    - Tiempo de ejecución
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Registrar tiempo de inicio
        
        
        # Mostrar información de la función
        print(f"\n--- Ejecutando función: {func.__name__} ---")
        print(f"Argumentos posicionales: {args}")
        print(f"Argumentos por nombre: {kwargs}")
        
        # Ejecutar la función original
        start = time.time()
        resultado = func(*args, **kwargs)       
        end = time.time()
        tiempo_ejecucion = end - start
        
        # Mostrar tiempo de ejecución
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
        print(f"--- Fin de ejecución de {func.__name__} ---\n")
        
        return resultado
    
    return wrapper


# Ejemplos de uso del decorador
@info_funcion
def suma(a, b):
    """Función simple que suma dos números"""
    time.sleep(0.1)  # Simular procesamiento
    return a + b

@info_funcion
def saludar(nombre, apellido="", formal=False):
    """Función que saluda con diferentes opciones"""
    time.sleep(0.05)  # Simular procesamiento
    if formal:
        saludo = f"Estimado/a {nombre} {apellido}".strip()
    else:
        saludo = f"Hola {nombre}!"
    print(f"Saludo: {saludo}")
    return saludo

@info_funcion
def operacion_compleja(*numeros, operacion="suma"):
    """Función que realiza operaciones con múltiples números"""
    time.sleep(0.2)  # Simular procesamiento complejo
    
    if operacion == "suma":
        resultado = sum(numeros)
    elif operacion == "multiplicacion":
        resultado = 1
        for num in numeros:
            resultado *= num
    else:
        resultado = 0
    
    return resultado


# Ejemplos de ejecución
if __name__ == "__main__":
    print("=== EJEMPLOS DE USO DEL DECORADOR ===")
    
    # Ejemplo 1: Función con argumentos posicionales
    resultado1 = suma(5, 3)
    print(f"Resultado suma: {resultado1}")
    
    # Ejemplo 2: Función con argumentos posicionales y por nombre
    resultado2 = saludar("Ana", apellido="García", formal=True)
    
    # Ejemplo 3: Función con *args y **kwargs
    resultado3 = operacion_compleja(2, 4, 6, 8, operacion="multiplicacion")
    print(f"Resultado multiplicación: {resultado3}")
    
    # Ejemplo 4: Solo argumentos por nombre
    resultado4 = operacion_compleja(operacion="suma")
    print(f"Resultado sin números: {resultado4}")
