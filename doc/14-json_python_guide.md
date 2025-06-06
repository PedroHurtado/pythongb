# Introducción a JSON en Python

## ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero, fácil de leer y escribir. Es independiente del lenguaje y se utiliza ampliamente en aplicaciones web, APIs y configuraciones.

### Características de JSON:
- **Ligero**: Menos verboso que XML
- **Legible**: Sintaxis clara y simple
- **Universal**: Soportado por la mayoría de lenguajes de programación
- **Estructurado**: Organiza datos de forma jerárquica

## Sintaxis básica de JSON

```json
{
  "nombre": "Juan Pérez",
  "edad": 30,
  "activo": true,
  "direccion": {
    "calle": "Calle Principal 123",
    "ciudad": "Madrid",
    "codigoPostal": "28001"
  },
  "hobbies": ["programación", "lectura", "deportes"],
  "telefono": null
}
```

## Trabajar con archivos JSON en Python

### Importar el módulo JSON

```python
import json
```

### Crear archivos JSON

```python
import json

# Datos de ejemplo
datos = {
    "usuarios": [
        {
            "id": 1,
            "nombre": "Ana García",
            "email": "ana@ejemplo.com",
            "activo": True,
            "edad": 28
        },
        {
            "id": 2,
            "nombre": "Carlos López",
            "email": "carlos@ejemplo.com",
            "activo": False,
            "edad": 35
        }
    ],
    "configuracion": {
        "tema": "oscuro",
        "idioma": "es",
        "notificaciones": True,
        "version": "1.0.0"
    }
}

# Escribir datos a un archivo JSON
with open('datos.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)

print("Archivo JSON creado exitosamente")
```

### Leer archivos JSON

```python
import json

# Leer datos desde un archivo JSON
try:
    with open('datos.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
    print("Datos cargados exitosamente:")
    print(f"Número de usuarios: {len(datos['usuarios'])}")
    print(f"Tema actual: {datos['configuracion']['tema']}")
    
    # Mostrar información de usuarios
    for usuario in datos['usuarios']:
        estado = "Activo" if usuario['activo'] else "Inactivo"
        print(f"- {usuario['nombre']} ({usuario['email']}) - {estado}")
        
except FileNotFoundError:
    print("Error: El archivo no existe")
except json.JSONDecodeError:
    print("Error: El archivo no tiene formato JSON válido")
```

## Procesar archivos JSON

### Manipular datos JSON

```python
import json

def procesar_datos_json(archivo_entrada, archivo_salida):
    """
    Procesa un archivo JSON y genera un reporte
    """
    try:
        # Leer datos
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        
        # Procesar datos
        usuarios_activos = [u for u in datos['usuarios'] if u['activo']]
        usuarios_inactivos = [u for u in datos['usuarios'] if not u['activo']]
        
        # Calcular estadísticas
        edad_promedio = sum(u['edad'] for u in datos['usuarios']) / len(datos['usuarios'])
        
        # Crear reporte
        reporte = {
            "fecha_reporte": "2024-06-06",
            "estadisticas": {
                "total_usuarios": len(datos['usuarios']),
                "usuarios_activos": len(usuarios_activos),
                "usuarios_inactivos": len(usuarios_inactivos),
                "edad_promedio": round(edad_promedio, 2)
            },
            "usuarios_activos": usuarios_activos,
            "configuracion_actual": datos['configuracion']
        }
        
        # Guardar reporte
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            json.dump(reporte, archivo, indent=4, ensure_ascii=False)
        
        print(f"Reporte generado: {archivo_salida}")
        return reporte
        
    except Exception as e:
        print(f"Error al procesar archivo: {e}")
        return None

# Usar la función
reporte = procesar_datos_json('datos.json', 'reporte.json')
if reporte:
    print(f"Usuarios activos: {reporte['estadisticas']['usuarios_activos']}")
    print(f"Edad promedio: {reporte['estadisticas']['edad_promedio']} años")
```

### Filtrar y transformar datos

```python
import json

def filtrar_usuarios_por_edad(archivo_json, edad_minima):
    """
    Filtra usuarios por edad mínima
    """
    with open(archivo_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    usuarios_filtrados = [
        usuario for usuario in datos['usuarios'] 
        if usuario['edad'] >= edad_minima
    ]
    
    return usuarios_filtrados

def actualizar_usuario(archivo_json, user_id, nuevos_datos):
    """
    Actualiza información de un usuario específico
    """
    with open(archivo_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    # Buscar y actualizar usuario
    for usuario in datos['usuarios']:
        if usuario['id'] == user_id:
            usuario.update(nuevos_datos)
            break
    
    # Guardar cambios
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    print(f"Usuario {user_id} actualizado")

# Ejemplos de uso
usuarios_mayores_30 = filtrar_usuarios_por_edad('datos.json', 30)
print(f"Usuarios mayores de 30: {len(usuarios_mayores_30)}")

# Actualizar usuario
actualizar_usuario('datos.json', 1, {'edad': 29, 'activo': False})
```

## Trabajando con el módulo JSON

### Métodos principales del módulo json

#### 1. json.dumps() - Convertir a string JSON

```python
import json

datos = {"nombre": "María", "edad": 25, "ciudad": "Barcelona"}

# Convertir diccionario a string JSON
json_string = json.dumps(datos, indent=2, ensure_ascii=False)
print(json_string)

# Opciones útiles
json_compacto = json.dumps(datos, separators=(',', ':'))
print(f"Compacto: {json_compacto}")
```

#### 2. json.loads() - Convertir string JSON a objeto Python

```python
import json

json_string = '{"nombre": "Pedro", "edad": 40, "casado": true}'

# Convertir string JSON a diccionario
datos = json.loads(json_string)
print(f"Nombre: {datos['nombre']}")
print(f"Edad: {datos['edad']}")
print(f"Casado: {datos['casado']}")
```

#### 3. json.dump() - Escribir a archivo

```python
import json

datos = {
    "productos": [
        {"id": 1, "nombre": "Laptop", "precio": 999.99},
        {"id": 2, "nombre": "Mouse", "precio": 25.50}
    ]
}

# Escribir a archivo con formato legible
with open('productos.json', 'w', encoding='utf-8') as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
```

#### 4. json.load() - Leer desde archivo

```python
import json

# Leer desde archivo
with open('productos.json', 'r', encoding='utf-8') as archivo:
    productos = json.load(archivo)

for producto in productos['productos']:
    print(f"{producto['nombre']}: ${producto['precio']}")
```

### Parámetros importantes

```python
import json

datos = {
    "nombre": "José",
    "apellido": "García",
    "edad": 45,
    "salario": 50000.75,
    "activo": True,
    "proyectos": None
}

# Parámetros útiles para json.dumps()
json_formateado = json.dumps(
    datos,
    indent=4,              # Sangría para formato legible
    ensure_ascii=False,    # Permitir caracteres no ASCII
    sort_keys=True,        # Ordenar claves alfabéticamente
    separators=(',', ': ') # Separadores personalizados
)

print(json_formateado)
```

### Manejo de errores

```python
import json

def leer_json_seguro(archivo):
    """
    Lee un archivo JSON con manejo de errores
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe")
        return None
    except json.JSONDecodeError as e:
        print(f"Error de formato JSON: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def escribir_json_seguro(datos, archivo):
    """
    Escribe datos a un archivo JSON con manejo de errores
    """
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Archivo '{archivo}' creado exitosamente")
        return True
    except Exception as e:
        print(f"Error al escribir archivo: {e}")
        return False

# Uso de las funciones
datos = leer_json_seguro('datos.json')
if datos:
    print("Datos cargados correctamente")
    
nuevo_dato = {"test": "valor"}
escribir_json_seguro(nuevo_dato, 'test.json')
```

### Ejemplo práctico: Sistema de gestión de biblioteca

```python
import json
from datetime import datetime

class BibliotecaJSON:
    def __init__(self, archivo='biblioteca.json'):
        self.archivo = archivo
        self.datos = self.cargar_datos()
    
    def cargar_datos(self):
        """Carga datos desde el archivo JSON"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"libros": [], "usuarios": []}
    
    def guardar_datos(self):
        """Guarda datos al archivo JSON"""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)
    
    def agregar_libro(self, titulo, autor, isbn):
        """Agrega un nuevo libro"""
        libro = {
            "id": len(self.datos["libros"]) + 1,
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn,
            "disponible": True,
            "fecha_agregado": datetime.now().isoformat()
        }
        self.datos["libros"].append(libro)
        self.guardar_datos()
        print(f"Libro '{titulo}' agregado exitosamente")
    
    def buscar_libro(self, termino):
        """Busca libros por título o autor"""
        resultados = []
        for libro in self.datos["libros"]:
            if (termino.lower() in libro["titulo"].lower() or 
                termino.lower() in libro["autor"].lower()):
                resultados.append(libro)
        return resultados
    
    def listar_libros(self):
        """Lista todos los libros"""
        if not self.datos["libros"]:
            print("No hay libros en la biblioteca")
            return
        
        print("\n=== CATÁLOGO DE LIBROS ===")
        for libro in self.datos["libros"]:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ID: {libro['id']}")
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"Estado: {estado}")
            print("-" * 30)

# Ejemplo de uso
biblioteca = BibliotecaJSON()

# Agregar libros
biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
biblioteca.agregar_libro("Don Quijote", "Miguel de Cervantes", "978-0060934347")

# Listar libros
biblioteca.listar_libros()

# Buscar libros
resultados = biblioteca.buscar_libro("García")
print(f"\nEncontrados {len(resultados)} libros:")
for libro in resultados:
    print(f"- {libro['titulo']} por {libro['autor']}")
```

## Mejores prácticas

### 1. Validación de datos

```python
import json

def validar_estructura_usuario(datos):
    """Valida que los datos del usuario tengan la estructura correcta"""
    campos_requeridos = ['nombre', 'email', 'edad']
    
    if not isinstance(datos, dict):
        return False, "Los datos deben ser un diccionario"
    
    for campo in campos_requeridos:
        if campo not in datos:
            return False, f"Falta el campo requerido: {campo}"
    
    if not isinstance(datos['edad'], int) or datos['edad'] < 0:
        return False, "La edad debe ser un número entero positivo"
    
    return True, "Válido"

# Ejemplo de uso
usuario = {"nombre": "Ana", "email": "ana@email.com", "edad": 25}
valido, mensaje = validar_estructura_usuario(usuario)
print(f"Validación: {mensaje}")
```

### 2. Backup y recuperación

```python
import json
import shutil
from datetime import datetime

def crear_backup(archivo_original):
    """Crea una copia de seguridad del archivo JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo_backup = f"{archivo_original}.backup_{timestamp}"
    
    try:
        shutil.copy2(archivo_original, archivo_backup)
        print(f"Backup creado: {archivo_backup}")
        return archivo_backup
    except Exception as e:
        print(f"Error al crear backup: {e}")
        return None

def restaurar_desde_backup(archivo_backup, archivo_destino):
    """Restaura desde un archivo de backup"""
    try:
        shutil.copy2(archivo_backup, archivo_destino)
        print(f"Archivo restaurado desde: {archivo_backup}")
        return True
    except Exception as e:
        print(f"Error al restaurar: {e}")
        return False

# Uso
backup_file = crear_backup('datos.json')
# Si algo sale mal...
# restaurar_desde_backup(backup_file, 'datos.json')
```

## Conclusión

JSON es un formato fundamental para el intercambio de datos en aplicaciones modernas. Python proporciona herramientas robustas a través del módulo `json` para trabajar eficientemente con este formato. Las mejores prácticas incluyen:

- Siempre manejar excepciones al leer/escribir archivos
- Validar la estructura de los datos
- Usar encoding UTF-8 para caracteres especiales
- Crear backups antes de modificaciones importantes
- Formatear JSON para legibilidad durante desarrollo

Con estos conocimientos, puedes integrar JSON efectivamente en tus proyectos Python para almacenamiento de configuraciones, intercambio de datos con APIs, y persistencia de información estructurada.