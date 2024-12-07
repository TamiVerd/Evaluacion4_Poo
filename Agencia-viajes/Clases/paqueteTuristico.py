class PaqueteTuristico:
    def __init__(self, id_paquete, nombre, id_destino, descripcion, precio, disponibilidad):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.id_destino = id_destino
        self.descripcion = descripcion
        self.precio = precio
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} (Precio: ${self.precio}, Disponibilidad: {self.disponibilidad})"
