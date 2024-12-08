class Viaje:
    def __init__(self, id_viaje, destino, fecha_salida, fecha_regreso, precio, disponibilidad):
        self.id_viaje = id_viaje  # Identificador único del viaje
        self.destino = destino  # Destino del viaje
        self.fecha_salida = fecha_salida  # Fecha de salida
        self.fecha_regreso = fecha_regreso  # Fecha de regreso
        self.precio = precio  # Precio del viaje
        self.disponibilidad = disponibilidad  # Número de plazas disponibles
