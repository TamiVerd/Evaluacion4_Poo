class Reserva:
    def __init__(self, id_reserva, id_cliente, id_viaje, cantidad_plazas, total_pago, fecha_reserva):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_viaje = id_viaje
        self.cantidad_plazas = cantidad_plazas
        self.total_pago = total_pago
        self.fecha_reserva = fecha_reserva

    def __str__(self):
        return f"Reserva {self.id_reserva}: Cliente {self.id_cliente}, Viaje {self.id_viaje}, Total: ${self.total_pago}"
