# Trabajando con CSV en Python

## El módulo CSV en Python

Python incluye un módulo integrado llamado `csv` que facilita enormemente el trabajo con archivos CSV (Comma Separated Values). Este módulo proporciona funcionalidades para leer y escribir archivos CSV de manera eficiente y flexible.

### Características principales del módulo CSV

El módulo `csv` ofrece varias clases y funciones que permiten manejar diferentes aspectos de los archivos CSV:

- **Lectura de archivos**: Permite leer archivos CSV línea por línea o como diccionarios
- **Escritura de archivos**: Facilita la creación de nuevos archivos CSV o la modificación de existentes
- **Manejo de dialectos**: Soporta diferentes formatos de CSV (delimitadores, comillas, etc.)
- **Gestión de errores**: Proporciona herramientas para manejar datos malformados

### Clases principales

**csv.reader()**: Lee archivos CSV y devuelve cada fila como una lista de strings.

**csv.writer()**: Escribe datos en formato CSV.

**csv.DictReader()**: Lee archivos CSV y devuelve cada fila como un diccionario, usando la primera fila como claves.

**csv.DictWriter()**: Escribe diccionarios en formato CSV.

## Procesamiento de archivos CSV

### Lectura básica de archivos CSV

La forma más simple de leer un archivo CSV es utilizando `csv.reader()`:

```python
import csv

# Lectura básica
with open('archivo.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Cada fila es una lista
```

### Lectura con DictReader

Para trabajar con los datos de manera más intuitiva, `DictReader` es muy útil:

```python
import csv

with open('empleados.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"Nombre: {fila['nombre']}, Edad: {fila['edad']}")
```

### Escritura de archivos CSV

Para crear o escribir en archivos CSV:

```python
import csv

# Datos de ejemplo
datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', 25, 'Madrid'],
    ['Carlos', 30, 'Barcelona'],
    ['María', 28, 'Valencia']
]

# Escribir archivo CSV
with open('nuevo_archivo.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    for fila in datos:
        escritor.writerow(fila)
```

### Escritura con DictWriter

Para escribir usando diccionarios:

```python
import csv

empleados = [
    {'nombre': 'Juan', 'edad': 32, 'departamento': 'IT'},
    {'nombre': 'Laura', 'edad': 27, 'departamento': 'Marketing'},
    {'nombre': 'Pedro', 'edad': 35, 'departamento': 'Ventas'}
]

with open('empleados_dict.csv', 'w', newline='', encoding='utf-8') as archivo:
    campos = ['nombre', 'edad', 'departamento']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()  # Escribe los nombres de las columnas
    for empleado in empleados:
        escritor.writerow(empleado)
```

### Manejo de diferentes dialectos

El módulo CSV permite manejar diferentes formatos:

```python
import csv

# CSV con punto y coma como delimitador
with open('archivo_europeo.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo, delimiter=';')
    for fila in lector:
        print(fila)

# Definir un dialecto personalizado
csv.register_dialect('mi_dialecto', 
                     delimiter='|', 
                     quotechar='"', 
                     quoting=csv.QUOTE_MINIMAL)

with open('archivo_personalizado.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo, dialect='mi_dialecto')
    escritor.writerow(['Campo1', 'Campo2', 'Campo3'])
```

### Procesamiento avanzado de datos

#### Filtrado y transformación de datos

```python
import csv

def procesar_ventas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as salida:
            lector = csv.DictReader(entrada)
            campos_salida = ['producto', 'ventas_totales', 'promedio_mensual']
            escritor = csv.DictWriter(salida, fieldnames=campos_salida)
            
            escritor.writeheader()
            
            for fila in lector:
                # Procesar y transformar datos
                ventas_totales = float(fila['enero']) + float(fila['febrero']) + float(fila['marzo'])
                promedio = ventas_totales / 3
                
                # Escribir solo si las ventas superan cierto umbral
                if ventas_totales > 1000:
                    escritor.writerow({
                        'producto': fila['producto'],
                        'ventas_totales': round(ventas_totales, 2),
                        'promedio_mensual': round(promedio, 2)
                    })
```

#### Agrupación y análisis de datos

```python
import csv
from collections import defaultdict

def analizar_ventas_por_region(archivo_csv):
    ventas_por_region = defaultdict(list)
    
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            region = fila['region']
            venta = float(fila['venta'])
            ventas_por_region[region].append(venta)
    
    # Generar resumen
    resumen = {}
    for region, ventas in ventas_por_region.items():
        resumen[region] = {
            'total': sum(ventas),
            'promedio': sum(ventas) / len(ventas),
            'cantidad': len(ventas)
        }
    
    return resumen
```

### Manejo de errores comunes

```python
import csv

def leer_csv_seguro(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Detectar el dialecto automáticamente
            muestra = archivo.read(1024)
            archivo.seek(0)
            dialecto = csv.Sniffer().sniff(muestra)
            
            lector = csv.reader(archivo, dialecto)
            datos = list(lector)
            return datos
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return None
    except csv.Error as e:
        print(f"Error al procesar CSV: {e}")
        return None
    except UnicodeDecodeError:
        # Intentar con diferente codificación
        try:
            with open(nombre_archivo, 'r', encoding='latin-1') as archivo:
                lector = csv.reader(archivo)
                return list(lector)
        except Exception as e:
            print(f"Error de codificación: {e}")
            return None
```

### Optimización para archivos grandes

Para archivos CSV muy grandes, es importante procesar los datos de manera eficiente:

```python
import csv

def procesar_archivo_grande(archivo_entrada, archivo_salida, funcion_filtro):
    """
    Procesa archivos CSV grandes de manera eficiente
    """
    contador = 0
    
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as salida:
            lector = csv.DictReader(entrada)
            escritor = csv.DictWriter(salida, fieldnames=lector.fieldnames)
            escritor.writeheader()
            
            for fila in lector:
                if funcion_filtro(fila):
                    escritor.writerow(fila)
                    contador += 1
                
                # Mostrar progreso cada 10000 filas
                if contador % 10000 == 0:
                    print(f"Procesadas {contador} filas...")
    
    print(f"Procesamiento completado: {contador} filas escritas")

# Ejemplo de uso
def filtro_ventas_altas(fila):
    return float(fila.get('venta', 0)) > 500

# procesar_archivo_grande('ventas_grandes.csv', 'ventas_filtradas.csv', filtro_ventas_altas)
```

### Integración con pandas (alternativa moderna)

Aunque el módulo `csv` es muy útil, para análisis más complejos, pandas ofrece funcionalidades adicionales:

```python
import pandas as pd

# Lectura con pandas
df = pd.read_csv('archivo.csv', encoding='utf-8')

# Procesamiento básico
df_filtrado = df[df['edad'] > 25]
resumen = df.groupby('departamento')['salario'].agg(['mean', 'sum', 'count'])

# Exportar resultado
resumen.to_csv('resumen_departamentos.csv')
```

## Mejores prácticas

### Codificación de caracteres

Siempre especifica la codificación al abrir archivos CSV, especialmente cuando trabajas con caracteres especiales:

```python
# Recomendado
with open('archivo.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
```

### Uso de context managers

Utiliza siempre `with` para asegurar que los archivos se cierren correctamente:

```python
# Correcto
with open('archivo.csv', 'r') as archivo:
    # procesar archivo
    pass
# El archivo se cierra automáticamente
```

### Validación de datos

Implementa validaciones para asegurar la integridad de los datos:

```python
def validar_fila(fila):
    """Valida que una fila tenga el formato correcto"""
    try:
        # Validar que campos numéricos sean realmente números
        float(fila['precio'])
        int(fila['cantidad'])
        
        # Validar que campos requeridos no estén vacíos
        if not fila['producto'].strip():
            return False
            
        return True
    except (ValueError, KeyError):
        return False
```

### Manejo de memoria

Para archivos muy grandes, procesa los datos línea por línea en lugar de cargar todo en memoria:

```python
def procesar_linea_por_linea(archivo_csv):
    with open(archivo_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Procesar cada fila individualmente
            procesar_fila(fila)
            # No almacenar todas las filas en memoria
```

## Casos de uso prácticos

### 1. Análisis de ventas

```python
import csv
from datetime import datetime

def analizar_ventas_mensuales(archivo_ventas):
    ventas_por_mes = {}
    
    with open(archivo_ventas, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for venta in lector:
            fecha = datetime.strptime(venta['fecha'], '%Y-%m-%d')
            mes_año = fecha.strftime('%Y-%m')
            
            if mes_año not in ventas_por_mes:
                ventas_por_mes[mes_año] = 0
            
            ventas_por_mes[mes_año] += float(venta['importe'])
    
    return ventas_por_mes
```

### 2. Limpieza de datos

```python
import csv
import re

def limpiar_datos_clientes(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as salida:
            lector = csv.DictReader(entrada)
            campos = ['nombre', 'email', 'telefono', 'ciudad']
            escritor = csv.DictWriter(salida, fieldnames=campos)
            escritor.writeheader()
            
            for fila in lector:
                # Limpiar nombre
                nombre = fila['nombre'].strip().title()
                
                # Validar email
                email = fila['email'].strip().lower()
                if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    continue  # Saltar filas con email inválido
                
                # Limpiar teléfono
                telefono = re.sub(r'[^\d+]', '', fila['telefono'])
                
                escritor.writerow({
                    'nombre': nombre,
                    'email': email,
                    'telefono': telefono,
                    'ciudad': fila['ciudad'].strip().title()
                })
```

### 3. Generación de reportes

```python
import csv
from collections import Counter

def generar_reporte_productos(archivo_ventas, archivo_reporte):
    contador_productos = Counter()
    ingresos_productos = {}
    
    # Leer datos de ventas
    with open(archivo_ventas, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        
        for venta in lector:
            producto = venta['producto']
            cantidad = int(venta['cantidad'])
            precio = float(venta['precio_unitario'])
            
            contador_productos[producto] += cantidad
            
            if producto not in ingresos_productos:
                ingresos_productos[producto] = 0
            ingresos_productos[producto] += cantidad * precio
    
    # Generar reporte
    with open(archivo_reporte, 'w', newline='', encoding='utf-8') as archivo:
        campos = ['producto', 'unidades_vendidas', 'ingresos_totales', 'precio_promedio']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        
        for producto in contador_productos:
            unidades = contador_productos[producto]
            ingresos = ingresos_productos[producto]
            precio_promedio = ingresos / unidades
            
            escritor.writerow({
                'producto': producto,
                'unidades_vendidas': unidades,
                'ingresos_totales': round(ingresos, 2),
                'precio_promedio': round(precio_promedio, 2)
            })
```

## Conclusión

El módulo CSV de Python es una herramienta fundamental para el procesamiento de datos tabulares. Su flexibilidad y facilidad de uso lo convierten en la opción ideal para la mayoría de tareas relacionadas con archivos CSV, desde operaciones simples hasta procesamiento complejo de grandes volúmenes de datos.

Las características clave que hacen del módulo CSV una excelente opción incluyen su capacidad para manejar diferentes dialectos, su eficiencia en memoria, y su integración natural con el ecosistema de Python. Ya sea que necesites procesar logs de servidor, analizar datos de ventas, o generar reportes automatizados, el módulo CSV proporciona las herramientas necesarias para realizar estas tareas de manera efectiva y confiable.