class Viaje:
    def __init__(self, id_viaje, destino, fecha_salida, fecha_regreso, precio, disponibilidad):
        self.id_viaje = id_viaje  # Identificador único del viaje
        self.destino = destino  # Destino del viaje
        self.fecha_salida = fecha_salida  # Fecha de salida
        self.fecha_regreso = fecha_regreso  # Fecha de regreso
        self.precio = precio  # Precio del viaje
        self.disponibilidad = disponibilidad  # Número de plazas disponibles

    def __str__(self):
        return (f"ID: {self.id_viaje}, Destino: {self.destino}, Salida: {self.fecha_salida}, "
                f"Regreso: {self.fecha_regreso}, Precio: ${self.precio:.2f}, Disponibilidad: {self.disponibilidad}")

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.precio = nuevo_precio
            print(f"Precio actualizado a ${self.precio:.2f}")
        else:
            print("El precio debe ser un valor positivo.")

    def actualizar_disponibilidad(self, nueva_disponibilidad):
        if nueva_disponibilidad >= 0:
            self.disponibilidad = nueva_disponibilidad
            print(f"Disponibilidad actualizada a {self.disponibilidad} plazas.")
        else:
            print("La disponibilidad no puede ser un número negativo.")

    def es_disponible(self):
        return self.disponibilidad > 0
