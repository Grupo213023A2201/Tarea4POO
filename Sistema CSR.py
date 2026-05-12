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
class Servicio(ABC):
    def __init__(self, nombre, precio_base): #Realice correcion en el constructor de la clase Servicio para incluir el precio base
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        pass
class reservacion_sala (Servicio):
    def __init__(self, cliente, fecha, hora, precio_base=50):
        super().__init__("Reservación de Sala", precio_base) # Precio base para reservación de sala
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        
    def calcular_hora_reservacion(self):
        # Lógica para calcular la hora de reservación
      
        return f"{self.fecha} a las {self.hora}"
    
    def calcular_costo(self, tiempo, impuesto=19, descuento=0):
        # Lógica real de calculo (Sobrecarga)
        subtotal = self.precio_base * tiempo
        total = subtotal + (subtotal * impuesto / 100) - (subtotal * descuento /100)
        return total
        
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
    if __name__ == "__main__": #Realice correcion en la indentacion del bloque principal para asegurar su correcta ejecución
        sistema_cliente = Sistema_gestion_cliente("Gestión de Clientes")
        sistema_cliente.agregar_cliente("Empresa XYZ")
        sistema_cliente.agregar_cliente("Empresa ABC")
        print("Clientes registrados:")
        
        sistema_cliente.mostrar_clientes()
        reservacion = reservacion_sala("Empresa XYZ", "2024-07-01", "10:00")
        costo_reservacion = reservacion.calcular_costo(tiempo=2, impuesto=19, descuento=10)
        print(f"Costo de la reservación: ${costo_reservacion:.2f}")
        
        alquiler = alquiler_equipo("Empresa ABC", "Proyector", "2024-07-02")
        costo_alquiler = alquiler.calcular_costo(tiempo=3, impuesto=19, descuento=15)
        print(f"Costo del alquiler: ${costo_alquiler:.2f}")
        
      
        
        print("\nASESORÍA")
        
