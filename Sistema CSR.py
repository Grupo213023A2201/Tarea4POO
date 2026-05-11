import logging
from abc import ABC, abstractmethod

# configuracion de logs
logging.basicConfig(
    filename='software_fj.log', 
    level=logging.INFO, # realice correcion en el nivel de logging a INFO para registrar eventos importantes
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# excepciones personalizadas
class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ValidacionError(SoftwareFJError):
    """Excepción para datos inválidos o faltantes."""
    pass

#Clase abstracta para entidades
class Sistema_gestion_general(ABC):
    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass
 
class Sistema_gestion_cliente(Sistema_gestion_general):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
    
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
# Clase para la gestión de reservaciones de salas
class reservacion_sala (Servicio):
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        
    def calcular_hora_reservacion(self):
        # Lógica para calcular la hora de reservación
      
        return f"{self.fecha} a las {self.hora}"
        calcular_costo(self, tiempo, impuesto=19, descuento=0).
    #clase para la gestios de alquiler de equipos
class alquiler_equipo(Servicio):
    def __init__(self, cliente, equipo, fecha, precio_base=100):
        super().__init__(f"Alquiler de {equipo}", precio_base)
        self.cliente = cliente
        self.equipo = equipo
        self.fecha = fecha

    def calcular_costo(self, tiempo, impuesto=19, descuento=0):
        # Lógica real de calculo (Sobrecarga)
        subtotal = self.precio_base * tiempo
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento / 100)
        return total

# Clase para asesorias especializadas
class asesorias_especializadas(Servicio):
    def __init__(self, cliente, tema, fecha, precio_base=200):
        super().__init__(f"Asesoría: {tema}", precio_base)
        self.cliente = cliente
        self.tema = tema
        self.fecha = fecha

    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        # Las asesorías suelen tener un recargo del 20% por especialista
        recargo = 1.20
        total = (self.precio_base * tiempo * recargo) - descuento
        return total
