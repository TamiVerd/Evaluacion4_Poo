class Destino:
    def __init__(self, id_destino, nombre, pais, descripcion):
        self.id_destino = id_destino
        self.nombre = nombre
        self.pais = pais
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre}, {self.pais} - {self.descripcion}"
