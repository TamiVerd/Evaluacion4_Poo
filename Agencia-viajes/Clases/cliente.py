class Cliente:
    def __init__(self, id_cliente, nombre, apellido, email, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} (Email: {self.email}, Teléfono: {self.telefono})"
