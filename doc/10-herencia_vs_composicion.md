# Herencia vs Composición en Python

## Introducción

En la programación orientada a objetos, existen dos enfoques principales para reutilizar código y establecer relaciones entre clases: **herencia** y **composición**. Ambos tienen sus ventajas y desventajas, y elegir el apropiado depende del contexto específico de tu aplicación.

## ¿Qué es la Herencia?

La herencia es un mecanismo que permite crear una nueva clase basada en una clase existente. La nueva clase (clase hija o subclase) hereda atributos y métodos de la clase existente (clase padre o superclase).

### Características de la Herencia
- Establece una relación **"es-un"** (is-a relationship)
- Permite la reutilización de código
- Facilita el polimorfismo
- Puede llevar a jerarquías complejas

### Ejemplo de Herencia

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def dormir(self):
        print(f"{self.nombre} está durmiendo")
    
    def comer(self):
        print(f"{self.nombre} está comiendo")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando: ¡Guau!")
    
    def comer(self):  # Sobrescribiendo método padre
        print(f"{self.nombre} está comiendo croquetas")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    
    def maullar(self):
        print(f"{self.nombre} está maullando: ¡Miau!")

# Uso
mi_perro = Perro("Rex", 3, "Labrador")
mi_gato = Gato("Whiskers", 2, "Negro")

mi_perro.dormir()  # Método heredado
mi_perro.ladrar()  # Método específico
mi_perro.comer()   # Método sobrescrito

mi_gato.dormir()   # Método heredado
mi_gato.maullar()  # Método específico
```

## ¿Qué es la Composición?

La composición es un mecanismo donde una clase contiene referencias a objetos de otras clases como atributos, en lugar de heredar de ellas. Los objetos se combinan para formar objetos más complejos.

### Características de la Composición
- Establece una relación **"tiene-un"** (has-a relationship)
- Mayor flexibilidad en el diseño
- Menor acoplamiento entre clases
- Permite cambios dinámicos en tiempo de ejecución

### Ejemplo de Composición

```python
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def encender(self):
        print(f"Motor {self.tipo} de {self.potencia}HP encendido")
    
    def apagar(self):
        print(f"Motor {self.tipo} apagado")

class Rueda:
    def __init__(self, tamaño, marca):
        self.tamaño = tamaño
        self.marca = marca
    
    def girar(self):
        print(f"Rueda {self.marca} de {self.tamaño}\" girando")

class Coche:
    def __init__(self, marca, modelo, motor, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # Composición: el coche TIENE UN motor
        self.ruedas = ruedas  # Composición: el coche TIENE ruedas
        self.encendido = False
    
    def arrancar(self):
        if not self.encendido:
            self.motor.encender()
            self.encendido = True
            print(f"{self.marca} {self.modelo} arrancado")
        else:
            print("El coche ya está encendido")
    
    def apagar(self):
        if self.encendido:
            self.motor.apagar()
            self.encendido = False
            print(f"{self.marca} {self.modelo} apagado")
        else:
            print("El coche ya está apagado")
    
    def conducir(self):
        if self.encendido:
            for rueda in self.ruedas:
                rueda.girar()
            print(f"Conduciendo el {self.marca} {self.modelo}")
        else:
            print("Primero debes arrancar el coche")

# Uso
motor_v8 = Motor("V8", 400)
ruedas = [Rueda(18, "Michelin") for _ in range(4)]

mi_coche = Coche("Ford", "Mustang", motor_v8, ruedas)

mi_coche.arrancar()
mi_coche.conducir()
mi_coche.apagar()
```

## Comparación Directa

### Mismo Problema, Diferentes Enfoques

Veamos cómo resolver el mismo problema usando herencia y composición:

#### Enfoque con Herencia

```python
class Trabajador:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando")

class Programador(Trabajador):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    
    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}")

class Gerente(Trabajador):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo
    
    def dirigir(self):
        print(f"{self.nombre} está dirigiendo un equipo de {self.equipo} personas")
```

#### Enfoque con Composición

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Salario:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    
    def pagar(self):
        return f"Pagando ${self.cantidad}"

class HabilidadProgramacion:
    def __init__(self, lenguaje):
        self.lenguaje = lenguaje
    
    def programar(self):
        return f"Programando en {self.lenguaje}"

class HabilidadGerencia:
    def __init__(self, tamaño_equipo):
        self.tamaño_equipo = tamaño_equipo
    
    def dirigir(self):
        return f"Dirigiendo equipo de {self.tamaño_equipo} personas"

class Empleado:
    def __init__(self, persona, salario, habilidades=None):
        self.persona = persona
        self.salario = salario
        self.habilidades = habilidades or []
    
    def trabajar(self):
        print(f"{self.persona.nombre} está trabajando")
        for habilidad in self.habilidades:
            if hasattr(habilidad, 'programar'):
                print(habilidad.programar())
            elif hasattr(habilidad, 'dirigir'):
                print(habilidad.dirigir())

# Uso con composición
persona1 = Persona("Ana")
salario1 = Salario(75000)
habilidad_python = HabilidadProgramacion("Python")

programador = Empleado(persona1, salario1, [habilidad_python])
programador.trabajar()
```

## Ventajas y Desventajas

### Herencia

#### Ventajas
- **Reutilización de código**: Evita duplicación
- **Polimorfismo**: Permite tratar objetos de diferentes clases de manera uniforme
- **Jerarquía clara**: Estructura organizacional clara
- **Sobrescritura de métodos**: Permite especializar comportamientos

#### Desventajas
- **Acoplamiento fuerte**: Cambios en la clase padre afectan a las hijas
- **Rigidez**: Difícil modificar la jerarquía una vez establecida
- **Problema del diamante**: Complejidad en herencia múltiple
- **Violación del principio "es-un"**: A veces se usa incorrectamente

### Composición

#### Ventajas
- **Flexibilidad**: Fácil modificar y extender funcionalidad
- **Bajo acoplamiento**: Cambios en una clase no afectan necesariamente a otras
- **Reutilización**: Los componentes pueden reutilizarse en diferentes contextos
- **Principio de responsabilidad única**: Cada clase tiene una responsabilidad específica

#### Desventajas
- **Más código**: Puede requerir más código para delegar funcionalidades
- **Complejidad inicial**: Puede ser más complejo de entender al principio
- **Interfaces**: Necesidad de definir interfaces claras entre componentes

## Cuándo Usar Cada Uno

### Usa Herencia Cuando:
- Existe una relación "es-un" verdadera
- Necesitas polimorfismo
- La jerarquía es estable y no cambiará frecuentemente
- Las clases hijas son especializaciones de la clase padre

### Usa Composición Cuando:
- Existe una relación "tiene-un"
- Necesitas flexibilidad para cambiar comportamientos
- Quieres evitar jerarquías complejas
- Los componentes pueden ser reutilizados en diferentes contextos

## Ejemplo Práctico: Sistema de Notificaciones

### Con Herencia (Problemático)

```python
class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def enviar(self):
        pass

class NotificacionEmail(Notificacion):
    def enviar(self):
        print(f"Enviando email: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self):
        print(f"Enviando SMS: {self.mensaje}")

# ¿Qué pasa si necesitamos NotificacionEmailSMS?
# Tendríamos que crear múltiples clases para cada combinación
```

### Con Composición (Flexible)

```python
class ServicioEmail:
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")

class ServicioSMS:
    def enviar(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class ServicioPush:
    def enviar(self, mensaje):
        print(f"Enviando notificación push: {mensaje}")

class GestorNotificaciones:
    def __init__(self):
        self.servicios = []
    
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
    
    def enviar_notificacion(self, mensaje):
        for servicio in self.servicios:
            servicio.enviar(mensaje)

# Uso flexible
gestor = GestorNotificaciones()
gestor.agregar_servicio(ServicioEmail())
gestor.agregar_servicio(ServicioSMS())
gestor.agregar_servicio(ServicioPush())

gestor.enviar_notificacion("Mensaje importante")
```

## Principios de Diseño Relacionados

### Principio de Composición sobre Herencia
El principio "Favor composition over inheritance" sugiere preferir la composición cuando ambas opciones son viables, debido a la mayor flexibilidad que ofrece.

### Principio SOLID
- **S**ingle Responsibility: Cada clase debe tener una sola razón para cambiar
- **O**pen/Closed: Abierto para extensión, cerrado para modificación
- **L**iskov Substitution: Los objetos de las clases derivadas deben poder reemplazar a los de la clase base
- **I**nterface Segregation: Los clientes no deben depender de interfaces que no usan
- **D**ependency Inversion: Depender de abstracciones, no de concreciones

## Mejores Prácticas

### Para Herencia
1. **Usa herencia solo cuando existe una relación "es-un" verdadera**
2. **Mantén las jerarquías poco profundas** (máximo 3-4 niveles)
3. **Documenta claramente el contrato de la clase base**
4. **Evita cambiar la interfaz pública en clases derivadas**
5. **Considera hacer los métodos virtuales cuando sea apropiado**

### Para Composición
1. **Define interfaces claras entre componentes**
2. **Elige nombres descriptivos para los componentes**
3. **Considera la inyección de dependencias**
4. **Mantén los componentes cohesivos y con bajo acoplamiento**
5. **Documenta las relaciones entre componentes**

## Conclusión

Tanto la herencia como la composición son herramientas valiosas en el desarrollo de software. La clave está en entender cuándo usar cada una:

- **Herencia** es excelente para crear jerarquías claras donde existe una relación "es-un" natural
- **Composición** ofrece mayor flexibilidad y es preferible cuando necesitas cambiar comportamientos dinámicamente

En la práctica moderna, la composición se prefiere debido a su flexibilidad y menor acoplamiento, pero ambos enfoques tienen su lugar en el desarrollo de software bien diseñado.

Recuerda: no hay una respuesta única. La elección depende del contexto específico de tu aplicación, los requisitos de mantenibilidad y la evolución esperada del sistema.