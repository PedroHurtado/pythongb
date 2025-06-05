# Persistencia de Objetos en Python

## Índice
1. [Introducción a la Persistencia de Objetos](#introducción-a-la-persistencia-de-objetos)
2. [Operaciones de Copia Superficial y Profunda](#operaciones-de-copia-superficial-y-profunda)
3. [Serialización con el Módulo pickle](#serialización-con-el-módulo-pickle)
4. [Persistencia con el Módulo shelve](#persistencia-con-el-módulo-shelve)
5. [Ejemplos Prácticos](#ejemplos-prácticos)
6. [Mejores Prácticas](#mejores-prácticas)

## Introducción a la Persistencia de Objetos

La **persistencia de objetos** es la capacidad de mantener el estado de un objeto más allá del tiempo de ejecución del programa. En Python, esto significa convertir objetos en memoria a un formato que pueda ser almacenado en disco y posteriormente recuperado.

### ¿Por qué es importante?
- Permite guardar el estado de aplicaciones
- Facilita el intercambio de datos entre programas
- Optimiza el rendimiento evitando recalcular datos complejos
- Habilita la creación de cachés persistentes

## Operaciones de Copia Superficial y Profunda

Antes de abordar la persistencia, es crucial entender las diferencias entre tipos de copia de objetos.

### Copia Superficial (Shallow Copy)

Una copia superficial crea un nuevo objeto, pero inserta referencias a los objetos encontrados en el original.

```python
import copy

# Ejemplo con lista anidada
lista_original = [[1, 2, 3], [4, 5, 6]]
copia_superficial = copy.copy(lista_original)

# Modificar la copia afecta al original
copia_superficial[0][0] = 99
print(lista_original)  # [[99, 2, 3], [4, 5, 6]]
```

### Copia Profunda (Deep Copy)

Una copia profunda crea un nuevo objeto y recursivamente copia todos los objetos anidados.

```python
import copy

# Ejemplo con copia profunda
lista_original = [[1, 2, 3], [4, 5, 6]]
copia_profunda = copy.deepcopy(lista_original)

# Modificar la copia NO afecta al original
copia_profunda[0][0] = 99
print(lista_original)  # [[1, 2, 3], [4, 5, 6]]
```

### Ejemplo Práctico con Clases

```python
import copy

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad
    
    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

# Crear objetos
direccion = Direccion("Calle Mayor 123", "Madrid")
persona1 = Persona("Juan", direccion)

# Copia superficial
persona2 = copy.copy(persona1)
persona2.nombre = "María"
persona2.direccion.calle = "Avenida Libertad 456"

print(f"Persona1: {persona1.nombre}, {persona1.direccion}")
print(f"Persona2: {persona2.nombre}, {persona2.direccion}")
# Ambas comparten la misma dirección

# Copia profunda
persona3 = copy.deepcopy(persona1)
persona3.direccion.calle = "Plaza España 789"

print(f"Persona1 después: {persona1.nombre}, {persona1.direccion}")
print(f"Persona3: {persona3.nombre}, {persona3.direccion}")
```

## Serialización con el Módulo pickle

El módulo `pickle` es la herramienta estándar de Python para serializar objetos. Convierte objetos Python en una secuencia de bytes que puede ser almacenada o transmitida.

### Conceptos Básicos

```python
import pickle

# Serializar (pickle)
datos = {'nombre': 'Ana', 'edad': 30, 'hobbies': ['leer', 'nadar']}

# Convertir a bytes
datos_serializados = pickle.dumps(datos)
print(f"Datos serializados: {datos_serializados}")

# Deserializar (unpickle)
datos_recuperados = pickle.loads(datos_serializados)
print(f"Datos recuperados: {datos_recuperados}")
```

### Trabajar con Archivos

```python
import pickle

# Guardar en archivo
datos = {
    'usuarios': ['Juan', 'María', 'Carlos'],
    'configuracion': {'tema': 'oscuro', 'idioma': 'es'},
    'estadisticas': {'visitas': 1500, 'registro': '2024-01-15'}
}

# Escribir archivo pickle
with open('datos.pkl', 'wb') as archivo:
    pickle.dump(datos, archivo)

# Leer archivo pickle
with open('datos.pkl', 'rb') as archivo:
    datos_cargados = pickle.load(archivo)
    print(datos_cargados)
```

### Serializar Objetos Personalizados

```python
import pickle
from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.fecha_creacion = datetime.now()
    
    def __str__(self):
        return f"{self.nombre}: ${self.precio} ({self.categoria})"
    
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)

# Crear y serializar productos
productos = [
    Producto("Laptop", 1200, "Electrónicos"),
    Producto("Mesa", 300, "Muebles"),
    Producto("Libro Python", 45, "Libros")
]

# Guardar productos
with open('productos.pkl', 'wb') as archivo:
    pickle.dump(productos, archivo)

# Cargar productos
with open('productos.pkl', 'rb') as archivo:
    productos_cargados = pickle.load(archivo)
    
for producto in productos_cargados:
    print(producto)
    print(f"Creado: {producto.fecha_creacion}")
```

### Protocolo de Pickle

```python
import pickle

datos = {"ejemplo": "protocolo"}

# Diferentes protocolos (0-5 en Python 3.8+)
for protocolo in range(pickle.HIGHEST_PROTOCOL + 1):
    serializado = pickle.dumps(datos, protocol=protocolo)
    print(f"Protocolo {protocolo}: {len(serializado)} bytes")
```

## Persistencia con el Módulo shelve

El módulo `shelve` proporciona una interfaz similar a un diccionario para la persistencia de objetos, usando pickle internamente.

### Características Principales

- Interfaz tipo diccionario
- Persistencia automática
- Acceso por clave
- Soporte para objetos complejos

### Uso Básico de shelve

```python
import shelve

# Crear/abrir un shelve
with shelve.open('mi_shelve.db') as shelf:
    # Almacenar datos
    shelf['configuracion'] = {
        'tema': 'claro',
        'notificaciones': True,
        'idioma': 'español'
    }
    
    shelf['usuarios'] = ['admin', 'usuario1', 'usuario2']
    
    shelf['estadisticas'] = {
        'total_usuarios': 150,
        'activos_hoy': 42,
        'nuevos_esta_semana': 12
    }

# Leer datos del shelve
with shelve.open('mi_shelve.db') as shelf:
    print("Claves disponibles:", list(shelf.keys()))
    print("Configuración:", shelf['configuracion'])
    print("Total usuarios:", shelf['estadisticas']['total_usuarios'])
```

### Sistema de Gestión de Inventario

```python
import shelve
from datetime import datetime
import uuid

class Articulo:
    def __init__(self, nombre, precio, stock, categoria):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.fecha_creacion = datetime.now()
        self.historial_ventas = []
    
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            venta = {
                'cantidad': cantidad,
                'fecha': datetime.now(),
                'total': cantidad * self.precio
            }
            self.historial_ventas.append(venta)
            return True
        return False
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

class GestorInventario:
    def __init__(self, archivo_db='inventario.db'):
        self.archivo_db = archivo_db
    
    def agregar_articulo(self, articulo):
        with shelve.open(self.archivo_db) as shelf:
            shelf[articulo.id] = articulo
    
    def obtener_articulo(self, id_articulo):
        with shelve.open(self.archivo_db) as shelf:
            return shelf.get(id_articulo)
    
    def listar_articulos(self):
        with shelve.open(self.archivo_db) as shelf:
            return {id_art: art for id_art, art in shelf.items()}
    
    def buscar_por_categoria(self, categoria):
        articulos = self.listar_articulos()
        return {id_art: art for id_art, art in articulos.items() 
                if art.categoria.lower() == categoria.lower()}
    
    def actualizar_stock(self, id_articulo, nuevo_stock):
        with shelve.open(self.archivo_db, writeback=True) as shelf:
            if id_articulo in shelf:
                shelf[id_articulo].stock = nuevo_stock
                return True
        return False
    
    def procesar_venta(self, id_articulo, cantidad):
        with shelve.open(self.archivo_db, writeback=True) as shelf:
            if id_articulo in shelf:
                return shelf[id_articulo].vender(cantidad)
        return False

# Ejemplo de uso
gestor = GestorInventario()

# Agregar artículos
articulos = [
    Articulo("Smartphone", 699, 50, "Electrónicos"),
    Articulo("Silla Ergonómica", 299, 25, "Muebles"),
    Articulo("Cafetera", 129, 15, "Electrodomésticos")
]

for articulo in articulos:
    gestor.agregar_articulo(articulo)

# Listar inventario
print("=== INVENTARIO ACTUAL ===")
inventario = gestor.listar_articulos()
for id_art, articulo in inventario.items():
    print(f"{id_art[:8]}: {articulo}")

# Procesar algunas ventas
print("\n=== PROCESANDO VENTAS ===")
for id_art in list(inventario.keys())[:2]:
    if gestor.procesar_venta(id_art, 2):
        print(f"Venta procesada para artículo {id_art[:8]}")
```

### Opciones Avanzadas de shelve

```python
import shelve

# Shelve con writeback (cambios automáticos)
with shelve.open('datos_avanzados.db', writeback=True) as shelf:
    shelf['lista_modificable'] = [1, 2, 3]
    shelf['diccionario_anidado'] = {'nivel1': {'nivel2': 'valor'}}
    
    # Con writeback=True, estos cambios se guardan automáticamente
    shelf['lista_modificable'].append(4)
    shelf['diccionario_anidado']['nivel1']['nuevo'] = 'añadido'

# Verificar cambios
with shelve.open('datos_avanzados.db') as shelf:
    print("Lista:", shelf['lista_modificable'])
    print("Diccionario:", shelf['diccionario_anidado'])
```

## Ejemplos Prácticos

### Sistema de Cache Inteligente

```python
import shelve
import pickle
from datetime import datetime, timedelta
import hashlib

class CacheInteligente:
    def __init__(self, archivo_cache='cache.db', duracion_horas=24):
        self.archivo_cache = archivo_cache
        self.duracion = timedelta(hours=duracion_horas)
    
    def _generar_clave(self, funcion, args, kwargs):
        # Crear clave única basada en función y parámetros
        contenido = f"{funcion.__name__}_{args}_{sorted(kwargs.items())}"
        return hashlib.md5(contenido.encode()).hexdigest()
    
    def obtener(self, funcion, args=(), kwargs={}):
        clave = self._generar_clave(funcion, args, kwargs)
        
        with shelve.open(self.archivo_cache) as cache:
            if clave in cache:
                entrada = cache[clave]
                if datetime.now() - entrada['timestamp'] < self.duracion:
                    print(f"Cache HIT para {funcion.__name__}")
                    return entrada['resultado']
                else:
                    print(f"Cache EXPIRADO para {funcion.__name__}")
        
        # No está en cache o expiró
        print(f"Cache MISS para {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        self._guardar(clave, resultado)
        return resultado
    
    def _guardar(self, clave, resultado):
        with shelve.open(self.archivo_cache) as cache:
            cache[clave] = {
                'resultado': resultado,
                'timestamp': datetime.now()
            }
    
    def limpiar_expirados(self):
        with shelve.open(self.archivo_cache, writeback=True) as cache:
            claves_expiradas = []
            for clave, entrada in cache.items():
                if datetime.now() - entrada['timestamp'] >= self.duracion:
                    claves_expiradas.append(clave)
            
            for clave in claves_expiradas:
                del cache[clave]
            
            print(f"Eliminadas {len(claves_expiradas)} entradas expiradas")

# Función costosa para cachear
def operacion_costosa(n):
    import time
    time.sleep(2)  # Simular operación lenta
    return sum(i**2 for i in range(n))

# Usar el cache
cache = CacheInteligente(duracion_horas=1)

# Primera llamada - se ejecuta la función
resultado1 = cache.obtener(operacion_costosa, args=(1000,))
print(f"Resultado: {resultado1}")

# Segunda llamada - se obtiene del cache
resultado2 = cache.obtener(operacion_costosa, args=(1000,))
print(f"Resultado: {resultado2}")
```

### Gestor de Configuración Persistente

```python
import shelve
import json
from pathlib import Path

class ConfiguracionApp:
    def __init__(self, archivo_config='config.db'):
        self.archivo_config = archivo_config
        self._cargar_defaults()
    
    def _cargar_defaults(self):
        defaults = {
            'apariencia': {
                'tema': 'claro',
                'fuente': 'Arial',
                'tamaño_fuente': 12
            },
            'funcionalidad': {
                'auto_guardar': True,
                'notificaciones': True,
                'actualizaciones_auto': False
            },
            'avanzado': {
                'debug': False,
                'logs_detallados': False,
                'max_historial': 100
            }
        }
        
        # Solo crear defaults si no existe el archivo
        if not Path(self.archivo_config + '.dat').exists():
            with shelve.open(self.archivo_config) as config:
                for categoria, opciones in defaults.items():
                    config[categoria] = opciones
    
    def obtener(self, categoria, opcion=None):
        with shelve.open(self.archivo_config) as config:
            if categoria not in config:
                return None
            
            categoria_data = config[categoria]
            if opcion is None:
                return categoria_data
            return categoria_data.get(opcion)
    
    def establecer(self, categoria, opcion, valor):
        with shelve.open(self.archivo_config, writeback=True) as config:
            if categoria not in config:
                config[categoria] = {}
            config[categoria][opcion] = valor
    
    def exportar_json(self, archivo_salida):
        with shelve.open(self.archivo_config) as config:
            datos = dict(config)
        
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
    
    def importar_json(self, archivo_entrada):
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        with shelve.open(self.archivo_config, writeback=True) as config:
            config.clear()
            config.update(datos)
    
    def resetear_categoria(self, categoria):
        defaults = {
            'apariencia': {
                'tema': 'claro',
                'fuente': 'Arial',
                'tamaño_fuente': 12
            },
            'funcionalidad': {
                'auto_guardar': True,
                'notificaciones': True,
                'actualizaciones_auto': False
            },
            'avanzado': {
                'debug': False,
                'logs_detallados': False,
                'max_historial': 100
            }
        }
        
        if categoria in defaults:
            with shelve.open(self.archivo_config, writeback=True) as config:
                config[categoria] = defaults[categoria]
    
    def listar_todo(self):
        with shelve.open(self.archivo_config) as config:
            return dict(config)

# Ejemplo de uso
config = ConfiguracionApp()

# Modificar configuraciones
config.establecer('apariencia', 'tema', 'oscuro')
config.establecer('funcionalidad', 'auto_guardar', False)
config.establecer('avanzado', 'debug', True)

# Consultar configuraciones
print("Tema actual:", config.obtener('apariencia', 'tema'))
print("Configuración completa de apariencia:", config.obtener('apariencia'))

# Exportar a JSON
config.exportar_json('configuracion_backup.json')

# Mostrar toda la configuración
print("\n=== CONFIGURACIÓN COMPLETA ===")
for categoria, opciones in config.listar_todo().items():
    print(f"\n{categoria.upper()}:")
    for opcion, valor in opciones.items():
        print(f"  {opcion}: {valor}")
```

## Mejores Prácticas

### Seguridad y Confiabilidad

```python
import pickle
import shelve
from pathlib import Path
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ManejadorSeguro:
    @staticmethod
    def pickle_seguro(obj, archivo):
        """Guardar con manejo de errores"""
        try:
            archivo_temp = f"{archivo}.tmp"
            with open(archivo_temp, 'wb') as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
            
            # Solo reemplazar si se guardó correctamente
            Path(archivo_temp).rename(archivo)
            logger.info(f"Objeto guardado exitosamente en {archivo}")
            return True
            
        except Exception as e:
            logger.error(f"Error al guardar: {e}")
            # Limpiar archivo temporal si existe
            Path(archivo_temp).unlink(missing_ok=True)
            return False
    
    @staticmethod
    def unpickle_seguro(archivo):
        """Cargar con validación"""
        try:
            if not Path(archivo).exists():
                logger.warning(f"Archivo no encontrado: {archivo}")
                return None
            
            with open(archivo, 'rb') as f:
                obj = pickle.load(f)
            
            logger.info(f"Objeto cargado exitosamente desde {archivo}")
            return obj
            
        except Exception as e:
            logger.error(f"Error al cargar: {e}")
            return None
    
    @staticmethod
    def shelve_con_backup(archivo_shelve, operacion_func):
        """Usar shelve con backup automático"""
        archivo_backup = f"{archivo_shelve}_backup"
        
        try:
            # Crear backup si existe el archivo original
            if Path(f"{archivo_shelve}.dat").exists():
                import shutil
                shutil.copy2(f"{archivo_shelve}.dat", f"{archivo_backup}.dat")
            
            # Realizar operación
            with shelve.open(archivo_shelve, writeback=True) as shelf:
                resultado = operacion_func(shelf)
            
            logger.info("Operación shelve completada exitosamente")
            return resultado
            
        except Exception as e:
            logger.error(f"Error en operación shelve: {e}")
            
            # Restaurar backup si existe
            if Path(f"{archivo_backup}.dat").exists():
                import shutil
                shutil.copy2(f"{archivo_backup}.dat", f"{archivo_shelve}.dat")
                logger.info("Backup restaurado")
            
            raise

# Ejemplo de uso seguro
def ejemplo_uso_seguro():
    datos_importantes = {
        'transacciones': [100, 250, 75],
        'saldo_actual': 1425.50,
        'ultima_actualizacion': '2024-06-05'
    }
    
    # Guardar de forma segura
    if ManejadorSeguro.pickle_seguro(datos_importantes, 'datos_criticos.pkl'):
        print("Datos guardados correctamente")
    
    # Cargar de forma segura
    datos_recuperados = ManejadorSeguro.unpickle_seguro('datos_criticos.pkl')
    if datos_recuperados:
        print(f"Datos recuperados: {datos_recuperados}")
    
    # Operación shelve segura
    def operacion_ejemplo(shelf):
        shelf['contador'] = shelf.get('contador', 0) + 1
        shelf['datos'] = datos_importantes
        return shelf['contador']
    
    try:
        contador = ManejadorSeguro.shelve_con_backup('contador.db', operacion_ejemplo)
        print(f"Contador actual: {contador}")
    except Exception as e:
        print(f"Error en operación: {e}")

ejemplo_uso_seguro()
```

### Optimización y Performance

```python
import pickle
import shelve
import time
from functools import wraps

def medir_tiempo(func):
    """Decorador para medir tiempo de ejecución"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} ejecutado en {fin-inicio:.4f} segundos")
        return resultado
    return wrapper

class OptimizadorPersistencia:
    
    @staticmethod
    @medir_tiempo
    def comparar_protocolos_pickle(obj):
        """Comparar diferentes protocolos de pickle"""
        resultados = {}
        
        for protocolo in range(pickle.HIGHEST_PROTOCOL + 1):
            inicio = time.time()
            datos_serializados = pickle.dumps(obj, protocol=protocolo)
            tiempo_serializacion = time.time() - inicio
            
            inicio = time.time()
            pickle.loads(datos_serializados)
            tiempo_deserializacion = time.time() - inicio
            
            resultados[protocolo] = {
                'tamaño': len(datos_serializados),
                'tiempo_serializacion': tiempo_serializacion,
                'tiempo_deserializacion': tiempo_deserializacion
            }
        
        return resultados
    
    @staticmethod
    def shelve_por_lotes(archivo, datos_dict, tamaño_lote=100):
        """Procesar shelve por lotes para mejor performance"""
        claves = list(datos_dict.keys())
        total_lotes = len(claves) // tamaño_lote + (1 if len(claves) % tamaño_lote else 0)
        
        with shelve.open(archivo, writeback=True) as shelf:
            for i in range(0, len(claves), tamaño_lote):
                lote_claves = claves[i:i + tamaño_lote]
                
                for clave in lote_claves:
                    shelf[clave] = datos_dict[clave]
                
                # Sincronizar cada lote
                shelf.sync()
                print(f"Procesado lote {i//tamaño_lote + 1}/{total_lotes}")

# Pruebas de optimización
def pruebas_optimizacion():
    # Crear datos de prueba
    datos_grandes = {
        'lista_numeros': list(range(10000)),
        'diccionario_anidado': {f'clave_{i}': {'valor': i**2, 'datos': [i]*100} 
                               for i in range(1000)},
        'texto_largo': 'Lorem ipsum ' * 10000
    }
    
    print("=== COMPARACIÓN DE PROTOCOLOS PICKLE ===")
    resultados = OptimizadorPersistencia.comparar_protocolos_pickle(datos_grandes)
    
    for protocolo, stats in resultados.items():
        print(f"Protocolo {protocolo}:")
        print(f"  Tamaño: {stats['tamaño']:,} bytes")
        print(f"  Serialización: {stats['tiempo_serializacion']:.6f}s")
        print(f"  Deserialización: {stats['tiempo_deserializacion']:.6f}s")
        print()

pruebas_optimizacion()
```

## Conclusiones

La persistencia de objetos en Python ofrece múltiples opciones según las necesidades específicas:

**Usar `copy` cuando:**
- Necesites duplicar objetos en memoria
- Trabajes con estructuras de datos complejas
- Requieras control sobre el nivel de copia

**Usar `pickle` cuando:**
- Necesites serialización completa de objetos Python
- Trabajes con objetos personalizados complejos
- Requieras máxima compatibilidad con tipos de Python

**Usar `shelve` cuando:**
- Necesites persistencia tipo diccionario
- Trabajes con acceso frecuente por clave
- Requieras una solución simple y eficiente

La elección correcta depende del contexto específico, el volumen de datos, los requisitos de performance y la complejidad de los objetos a persistir.

---

*Guía desarrollada para el aprendizaje de persistencia de objetos en Python - 2024*