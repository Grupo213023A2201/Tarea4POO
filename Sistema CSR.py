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
class Sistema_gestion_general:
    def __init__(self, nombre):
        self.nombre = nombre
 
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
class reservacion_sala:
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        
    def calcular_hora_reservacion(self):
        # Lógica para calcular la hora de reservación
        return f"{self.fecha} a las {self.hora}"
#clase para la gestios de alquiler de equipos
class alquiler_equipo:
    def __init__(self, cliente, equipo, fecha):
        self.cliente = cliente
        self.equipo = equipo
        self.fecha = fecha
        
    def calcular_costo_alquiler(self):
        # Lógica para calcular el costo del alquiler
        return f"El costo del alquiler de {self.equipo} para {self.cliente} el {self.fecha} es: $100"
#Clase para asesorias especializadas
class asesorias_especializadas:
    def __init__(self, cliente, tema, fecha):
        self.cliente = cliente
        self.tema = tema
        self.fecha = fecha
        
    def calcular_costo_asesoria(self):
        # Lógica para calcular el costo de la asesoría
        return f"El costo de la asesoría sobre {self.tema} para {self.cliente} el {self.fecha} es: $200"
    
