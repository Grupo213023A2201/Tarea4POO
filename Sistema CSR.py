
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

class reservacion:
    def __init__(self, cliente, fecha, hora):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        
    def calcular_hora_reservacion(self):
        # Lógica para calcular la hora de reservación
        return f"{self.fecha} a las {self.hora}"