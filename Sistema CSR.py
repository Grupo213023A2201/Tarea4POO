import logging
from abc import ABC, abstractmethod

# configuracion de logs
logging.basicConfig(
    filename='software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# excepciones personalizadas
class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""
    pass


class ValidacionError(SoftwareFJError):
    """Excepción para datos inválidos o faltantes."""
    pass


# Clase abstracta para entidades
class Sistema_gestion_general(ABC):

    def __init__(self, nombre):
        self._nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        pass


# Gestión de clientes
class Sistema_gestion_cliente(Sistema_gestion_general):

    def __init__(self, nombre):

        super().__init__(nombre)

        self.clientes = []

    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

        logging.info(f"Cliente agregado: {cliente}")

    def eliminar_cliente(self, cliente):

        if cliente in self.clientes:

            self.clientes.remove(cliente)

            logging.info(f"Cliente eliminado: {cliente}")

    def mostrar_clientes(self):

        for cliente in self.clientes:
            print(cliente)

    def mostrar_info(self):

        print(f"Sistema: {self._nombre}")

        print(f"Cantidad de clientes: {len(self.clientes)}")


# Clase abstracta para servicios
class Servicio(Sistema_gestion_general):

    def __init__(self, nombre, precio_base):

        super().__init__(nombre)

        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        pass


# Clase para la gestión de reservaciones de salas
class reservacion_sala(Servicio):

    def __init__(self, cliente, fecha, hora, precio_base=50):

        super().__init__("Reservación de Sala", precio_base)

        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def calcular_hora_reservacion(self):

        return f"{self.fecha} a las {self.hora}"

    def calcular_costo(self, tiempo, impuesto=19, descuento=0):

        subtotal = self.precio_base * tiempo

        total = subtotal + (subtotal * impuesto / 100)

        total = total - (subtotal * descuento / 100)

        return total

    def mostrar_info(self):

        print("\nRESERVACIÓN DE SALA")
        print("Cliente:", self.cliente)
        print("Fecha:", self.fecha)
        print("Hora:", self.hora)


# Clase para la gestión de alquiler de equipos
class alquiler_equipo(Servicio):

    def __init__(self, cliente, equipo, fecha, precio_base=100):

        super().__init__(f"Alquiler de {equipo}", precio_base)

        self.cliente = cliente
        self.equipo = equipo
        self.fecha = fecha

    def calcular_costo(self, tiempo, impuesto=19, descuento=0):

        subtotal = self.precio_base * tiempo

        total = subtotal + (subtotal * impuesto / 100)

        total = total - (subtotal * descuento / 100)

        return total

    def mostrar_info(self):

        print("\nALQUILER DE EQUIPO")
        print("Cliente:", self.cliente)
        print("Equipo:", self.equipo)
        print("Fecha:", self.fecha)


# Clase para asesorías especializadas
class asesorias_especializadas(Servicio):

    def __init__(self, cliente, tema, fecha, precio_base=200):

        super().__init__(f"Asesoría: {tema}", precio_base)

        self.cliente = cliente
        self.tema = tema
        self.fecha = fecha

    def calcular_costo(self, tiempo, impuesto=0, descuento=0):

        recargo = 1.20

        total = (self.precio_base * tiempo * recargo) - descuento

        return total

    def mostrar_info(self):

        print("\nASESORÍA ESPECIALIZADA")
        print("Cliente:", self.cliente)
        print("Tema:", self.tema)
        print("Fecha:", self.fecha)


if __name__ == "__main__":

    sistema_cliente = Sistema_gestion_cliente(
        "Gestión de Clientes"
    )

    sistema_cliente.agregar_cliente("Empresa XYZ")

    sistema_cliente.agregar_cliente("Empresa ABC")

    print("Clientes registrados:\n")

    sistema_cliente.mostrar_clientes()

    print()

    sistema_cliente.mostrar_info()

    reservacion = reservacion_sala(
        "Empresa XYZ",
        "2024-07-01",
        "10:00"
    )

    reservacion.mostrar_info()

    costo_reservacion = reservacion.calcular_costo(
        tiempo=2,
        impuesto=19,
        descuento=10
    )

    print(
        f"Costo de la reservación: ${costo_reservacion:.2f}"
    )

    alquiler = alquiler_equipo(
        "Empresa ABC",
        "Proyector",
        "2024-07-02"
    )

    alquiler.mostrar_info()

    costo_alquiler = alquiler.calcular_costo(
        tiempo=3,
        impuesto=19,
        descuento=15
    )

    print(
        f"Costo del alquiler: ${costo_alquiler:.2f}"
    )

    asesoria = asesorias_especializadas(
        "Empresa XYZ",
        "Python",
        "2024-07-03"
    )

    asesoria.mostrar_info()

    costo_asesoria = asesoria.calcular_costo(
        tiempo=2,
        descuento=20
    )

    print(
        f"Costo de la asesoría: ${costo_asesoria:.2f}"
    )
           
