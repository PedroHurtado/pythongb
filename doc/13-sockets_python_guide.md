# Sockets en Python - Guía Completa

## Introducción a los Sockets

Los sockets son endpoints de comunicación que permiten la transferencia de datos entre procesos, ya sea en la misma máquina o a través de una red. Python proporciona la biblioteca `socket` para trabajar con conexiones de red de bajo nivel.

## 1. Crear Sockets

### Socket Básico TCP
```python
import socket

# Crear un socket TCP (protocolo confiable)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Crear un socket UDP (protocolo no confiable, más rápido)
servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

### Parámetros principales:
- `AF_INET`: Familia de direcciones IPv4
- `AF_INET6`: Familia de direcciones IPv6
- `SOCK_STREAM`: Socket TCP (confiable, orientado a conexión)
- `SOCK_DGRAM`: Socket UDP (no confiable, sin conexión)

### Ejemplo de Servidor TCP
```python
import socket

def crear_servidor():
    # Crear socket
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Permitir reutilizar la dirección
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Enlazar a una dirección y puerto
    servidor.bind(('localhost', 8080))
    
    # Escuchar conexiones (máximo 5 en cola)
    servidor.listen(5)
    print("Servidor escuchando en puerto 8080...")
    
    return servidor
```

## 2. Conectarse a un Servidor

### Cliente TCP Básico
```python
import socket

def conectar_cliente():
    # Crear socket cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor
        cliente.connect(('localhost', 8080))
        print("Conectado al servidor")
        return cliente
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor")
        return None
```

### Cliente con Timeout
```python
import socket

def cliente_con_timeout():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(10)  # Timeout de 10 segundos
    
    try:
        cliente.connect(('ejemplo.com', 80))
        return cliente
    except socket.timeout:
        print("Timeout al conectar")
        return None
```

## 3. Solicitar Documentos de un Servidor

### Cliente HTTP Básico
```python
import socket

def solicitar_documento(host, puerto, ruta):
    # Crear y conectar socket
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))
    
    # Crear petición HTTP GET
    peticion = f"GET {ruta} HTTP/1.1\r\n"
    peticion += f"Host: {host}\r\n"
    peticion += "Connection: close\r\n"
    peticion += "\r\n"
    
    # Enviar petición
    cliente.send(peticion.encode('utf-8'))
    
    # Recibir respuesta
    respuesta = b""
    while True:
        datos = cliente.recv(4096)
        if not datos:
            break
        respuesta += datos
    
    cliente.close()
    return respuesta.decode('utf-8')

# Ejemplo de uso
try:
    respuesta = solicitar_documento('httpbin.org', 80, '/get')
    print(respuesta)
except Exception as e:
    print(f"Error: {e}")
```

### Descarga de Archivos
```python
import socket
import os

def descargar_archivo(host, puerto, ruta_remota, archivo_local):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect((host, puerto))
        
        # Petición HTTP
        peticion = f"GET {ruta_remota} HTTP/1.1\r\n"
        peticion += f"Host: {host}\r\n"
        peticion += "Connection: close\r\n\r\n"
        
        cliente.send(peticion.encode())
        
        # Recibir respuesta y separar headers del contenido
        respuesta_completa = b""
        while True:
            datos = cliente.recv(4096)
            if not datos:
                break
            respuesta_completa += datos
        
        # Separar headers del contenido
        headers, contenido = respuesta_completa.split(b'\r\n\r\n', 1)
        
        # Guardar archivo
        with open(archivo_local, 'wb') as archivo:
            archivo.write(contenido)
        
        print(f"Archivo descargado: {archivo_local}")
        
    except Exception as e:
        print(f"Error descargando archivo: {e}")
    finally:
        cliente.close()
```

## 4. Cerrar Conexiones

### Cierre Correcto de Sockets
```python
import socket

def cerrar_correctamente(sock):
    try:
        # Cerrar envío de datos
        sock.shutdown(socket.SHUT_WR)
        
        # Recibir datos restantes
        while True:
            datos = sock.recv(1024)
            if not datos:
                break
    except:
        pass
    finally:
        # Cerrar socket completamente
        sock.close()
```

### Context Manager para Sockets
```python
import socket
from contextlib import contextmanager

@contextmanager
def crear_socket_tcp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        yield sock
    finally:
        sock.close()

# Uso del context manager
with crear_socket_tcp() as cliente:
    cliente.connect(('google.com', 80))
    cliente.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
    respuesta = cliente.recv(4096)
    print(respuesta.decode())
```

## 5. Clientes HTTP

### Cliente HTTP Completo
```python
import socket
import urllib.parse

class ClienteHTTP:
    def __init__(self, timeout=10):
        self.timeout = timeout
    
    def get(self, url):
        return self._realizar_peticion('GET', url)
    
    def post(self, url, datos=None):
        return self._realizar_peticion('POST', url, datos)
    
    def _realizar_peticion(self, metodo, url, datos=None):
        # Parsear URL
        parsed = urllib.parse.urlparse(url)
        host = parsed.hostname
        puerto = parsed.port or (443 if parsed.scheme == 'https' else 80)
        ruta = parsed.path or '/'
        
        if parsed.query:
            ruta += '?' + parsed.query
        
        # Crear socket
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(self.timeout)
        
        try:
            cliente.connect((host, puerto))
            
            # Construir petición HTTP
            peticion = f"{metodo} {ruta} HTTP/1.1\r\n"
            peticion += f"Host: {host}\r\n"
            peticion += "User-Agent: ClienteHTTP-Python/1.0\r\n"
            peticion += "Connection: close\r\n"
            
            if datos and metodo == 'POST':
                peticion += f"Content-Length: {len(datos)}\r\n"
                peticion += "Content-Type: application/x-www-form-urlencoded\r\n"
                peticion += f"\r\n{datos}"
            else:
                peticion += "\r\n"
            
            # Enviar petición
            cliente.send(peticion.encode('utf-8'))
            
            # Recibir respuesta
            respuesta = b""
            while True:
                chunk = cliente.recv(4096)
                if not chunk:
                    break
                respuesta += chunk
            
            return self._parsear_respuesta(respuesta)
            
        finally:
            cliente.close()
    
    def _parsear_respuesta(self, respuesta_raw):
        try:
            respuesta_str = respuesta_raw.decode('utf-8')
            headers, contenido = respuesta_str.split('\r\n\r\n', 1)
            
            # Parsear primera línea (status)
            lineas = headers.split('\r\n')
            status_line = lineas[0]
            codigo_status = int(status_line.split()[1])
            
            # Parsear headers
            headers_dict = {}
            for linea in lineas[1:]:
                if ':' in linea:
                    clave, valor = linea.split(':', 1)
                    headers_dict[clave.strip()] = valor.strip()
            
            return {
                'status_code': codigo_status,
                'headers': headers_dict,
                'content': contenido
            }
        except Exception as e:
            return {'error': str(e)}

# Ejemplo de uso
cliente = ClienteHTTP()
respuesta = cliente.get('http://httpbin.org/get')
print(f"Status: {respuesta['status_code']}")
print(f"Content: {respuesta['content'][:200]}...")
```

## 6. La Respuesta del Servidor

### Parsear Respuestas HTTP
```python
def parsear_respuesta_http(respuesta_raw):
    """
    Parsea una respuesta HTTP cruda y extrae componentes importantes
    """
    try:
        # Decodificar bytes a string
        respuesta_str = respuesta_raw.decode('utf-8', errors='ignore')
        
        # Separar headers del contenido
        if '\r\n\r\n' in respuesta_str:
            headers_section, contenido = respuesta_str.split('\r\n\r\n', 1)
        else:
            headers_section = respuesta_str
            contenido = ""
        
        # Parsear línea de status
        lineas = headers_section.split('\r\n')
        status_line = lineas[0]
        partes_status = status_line.split(' ', 2)
        
        version_http = partes_status[0]
        codigo_status = int(partes_status[1])
        mensaje_status = partes_status[2] if len(partes_status) > 2 else ""
        
        # Parsear headers
        headers = {}
        for linea in lineas[1:]:
            if ':' in linea:
                clave, valor = linea.split(':', 1)
                headers[clave.strip().lower()] = valor.strip()
        
        return {
            'version_http': version_http,
            'codigo_status': codigo_status,
            'mensaje_status': mensaje_status,
            'headers': headers,
            'contenido': contenido,
            'longitud_contenido': len(contenido)
        }
        
    except Exception as e:
        return {'error': f"Error parseando respuesta: {e}"}

# Ejemplo de uso
def ejemplo_parseo():
    respuesta_ejemplo = b"""HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 25
Server: nginx/1.18.0

{"message": "Hello World"}"""
    
    resultado = parsear_respuesta_http(respuesta_ejemplo)
    print("Respuesta parseada:")
    for clave, valor in resultado.items():
        print(f"  {clave}: {valor}")
```

### Manejo de Diferentes Códigos de Estado
```python
def manejar_respuesta(respuesta):
    """
    Maneja diferentes códigos de estado HTTP
    """
    codigo = respuesta.get('codigo_status', 0)
    
    if 200 <= codigo < 300:
        print(f"✓ Éxito ({codigo}): {respuesta.get('mensaje_status', '')}")
        return True
    elif 300 <= codigo < 400:
        print(f"→ Redirección ({codigo}): {respuesta.get('mensaje_status', '')}")
        # Obtener URL de redirección
        location = respuesta.get('headers', {}).get('location')
        if location:
            print(f"  Redirigir a: {location}")
        return False
    elif 400 <= codigo < 500:
        print(f"✗ Error del cliente ({codigo}): {respuesta.get('mensaje_status', '')}")
        return False
    elif 500 <= codigo < 600:
        print(f"✗ Error del servidor ({codigo}): {respuesta.get('mensaje_status', '')}")
        return False
    else:
        print(f"? Código desconocido ({codigo})")
        return False
```

## 7. Excepciones

### Tipos Principales de Excepciones
```python
import socket
import errno

def manejar_excepciones_socket():
    """
    Ejemplo completo de manejo de excepciones con sockets
    """
    cliente = None
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.settimeout(5)
        cliente.connect(('ejemplo-inexistente.com', 80))
        
    except socket.gaierror as e:
        print(f"Error de resolución DNS: {e}")
        
    except socket.timeout:
        print("Timeout: La conexión tardó demasiado")
        
    except ConnectionRefusedError:
        print("Conexión rechazada: El servidor no está disponible")
        
    except ConnectionResetError:
        print("Conexión reiniciada por el servidor")
        
    except OSError as e:
        if e.errno == errno.ECONNABORTED:
            print("Conexión abortada")
        elif e.errno == errno.EHOSTUNREACH:
            print("Host inalcanzable")
        elif e.errno == errno.ENETUNREACH:
            print("Red inalcanzable")
        else:
            print(f"Error del sistema operativo: {e}")
            
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    finally:
        if cliente:
            cliente.close()
```

### Decorador para Manejo de Excepciones
```python
import functools
import socket

def manejar_errores_red(func):
    """
    Decorador para manejar errores comunes de red
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except socket.timeout:
            print("⏱️  Timeout: Operación cancelada por tiempo límite")
            return None
        except socket.gaierror as e:
            print(f"🌐 Error DNS: No se pudo resolver la dirección - {e}")
            return None
        except ConnectionError as e:
            print(f"🔌 Error de conexión: {e}")
            return None
        except socket.error as e:
            print(f"🚫 Error de socket: {e}")
            return None
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return None
    return wrapper

@manejar_errores_red
def conectar_con_manejo_errores(host, puerto):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(10)
    cliente.connect((host, puerto))
    return cliente
```

### Reintentos Automáticos
```python
import time
import socket

def conectar_con_reintentos(host, puerto, max_intentos=3, delay=1):
    """
    Intenta conectar con reintentos automáticos
    """
    for intento in range(max_intentos):
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(10)
            cliente.connect((host, puerto))
            print(f"✓ Conectado en intento {intento + 1}")
            return cliente
            
        except (ConnectionError, socket.timeout) as e:
            print(f"✗ Intento {intento + 1} falló: {e}")
            if intento < max_intentos - 1:
                print(f"⏳ Esperando {delay} segundos antes del siguiente intento...")
                time.sleep(delay)
            else:
                print("❌ Todos los intentos fallaron")
                return None
        except Exception as e:
            print(f"❌ Error irrecuperable: {e}")
            return None

# Ejemplo de uso
cliente = conectar_con_reintentos('google.com', 80, max_intentos=3)
if cliente:
    print("Conexión establecida exitosamente")
    cliente.close()
```

## Ejemplo Completo: Servidor y Cliente

### Servidor Echo
```python
import socket
import threading

def manejar_cliente(conexion, direccion):
    """Maneja un cliente individual"""
    print(f"Conexión establecida con {direccion}")
    try:
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break
            mensaje = datos.decode('utf-8')
            print(f"Recibido de {direccion}: {mensaje}")
            # Eco: enviar el mismo mensaje de vuelta
            conexion.send(f"Echo: {mensaje}".encode('utf-8'))
    except Exception as e:
        print(f"Error con cliente {direccion}: {e}")
    finally:
        conexion.close()
        print(f"Conexión cerrada con {direccion}")

def servidor_echo():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        servidor.bind(('localhost', 8080))
        servidor.listen(5)
        print("Servidor Echo iniciado en puerto 8080")
        
        while True:
            conexion, direccion = servidor.accept()
            # Crear hilo para cada cliente
            hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
            hilo.start()
            
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
    finally:
        servidor.close()

# Para ejecutar: servidor_echo()
```

### Cliente Interactivo
```python
import socket

def cliente_interactivo():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect(('localhost', 8080))
        print("Conectado al servidor Echo")
        print("Escribe mensajes (o 'quit' para salir):")
        
        while True:
            mensaje = input("> ")
            if mensaje.lower() == 'quit':
                break
                
            cliente.send(mensaje.encode('utf-8'))
            respuesta = cliente.recv(1024)
            print(f"Servidor: {respuesta.decode('utf-8')}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cliente.close()

# Para ejecutar: cliente_interactivo()
```

## Consejos y Mejores Prácticas

1. **Siempre cerrar sockets**: Usa context managers o try/finally
2. **Manejar excepciones**: Los sockets pueden fallar de muchas maneras
3. **Usar timeouts**: Evita bloqueos indefinidos
4. **Buffering**: Los datos pueden llegar fragmentados
5. **Codificación**: Especifica siempre la codificación (UTF-8)
6. **Reutilización de puertos**: Usa SO_REUSEADDR en servidores
7. **Threading**: Para manejar múltiples conexiones simultáneas

---

Esta guía proporciona una base sólida para trabajar con sockets en Python, desde conceptos básicos hasta implementaciones avanzadas con manejo robusto de errores.