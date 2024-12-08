import sqlite3 as sql
from tabulate import tabulate

class BaseDatos:
    def __init__(self):
        self.conexion = None

    def conexion_bd(self):
        self.conexion = sql.connect("agencia_viajes.db")

    def desconectar(self):
        if self.conexion is not None:
            self.conexion.close()

    def crear_tablas(self):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()

            # Tabla destinos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS destinos (
                    id_destino INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    pais TEXT NOT NULL,
                    descripcion TEXT
                )
            """)

            # Tabla paquetes_turisticos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS paquetes_turisticos (
                    id_paquete INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    id_destino INTEGER NOT NULL,
                    descripcion TEXT,
                    precio REAL NOT NULL,
                    disponibilidad INTEGER NOT NULL,
                    FOREIGN KEY (id_destino) REFERENCES destinos (id_destino)
                )
            """)

            # Tabla viajes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS viajes (
                    id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_paquete INTEGER NOT NULL,
                    fecha_salida TEXT NOT NULL,
                    fecha_regreso TEXT NOT NULL,
                    disponibilidad INTEGER NOT NULL,
                    FOREIGN KEY (id_paquete) REFERENCES paquetes_turisticos (id_paquete)
                )
            """)

            # Tabla clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    telefono TEXT
                )
            """)

            # Tabla reservas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservas (
                    id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    id_viaje INTEGER NOT NULL,
                    cantidad_plazas INTEGER NOT NULL,
                    total_pago REAL NOT NULL,
                    fecha_reserva TEXT NOT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
                    FOREIGN KEY (id_viaje) REFERENCES viajes (id_viaje)
                )
            """)

            print("Tablas creadas exitosamente.")
        except Exception as e:
            print(f"Error al crear las tablas: {e}")
        finally:
            self.desconectar()
    
#-----------------------------------------------------------------------------------

# Función genérica para mostrar cualquier tabla
    def mostrar_tabla(self, nombre_tabla):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = f"SELECT * FROM {nombre_tabla}"
            cursor.execute(sql)
            datos = cursor.fetchall()
            columnas = [description[0] for description in cursor.description]
            print(tabulate(datos, headers=columnas, tablefmt="fancy_grid"))
        except Exception as e:
            print(f"Error al mostrar datos de la tabla '{nombre_tabla}': {e}")
        finally:
            self.desconectar()

    # Función genérica para eliminar un registro por ID
    def eliminar_por_id(self, nombre_tabla, id_columna, id_valor):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = f"DELETE FROM {nombre_tabla} WHERE {id_columna} = ?"
            cursor.execute(sql, (id_valor,))
            self.conexion.commit()
            print(f"Registro eliminado exitosamente de '{nombre_tabla}'.")
        except Exception as e:
            print(f"Error al eliminar registro en la tabla '{nombre_tabla}': {e}")
        finally:
            self.desconectar()

    # Funciones específicas para cada tabla
    def agregar_destino(self, nombre, pais, descripcion):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = "INSERT INTO destinos (nombre, pais, descripcion) VALUES (?, ?, ?)"
            cursor.execute(sql, (nombre, pais, descripcion))
            self.conexion.commit()
            print("Destino agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar destino: {e}")
        finally:
            self.desconectar()

    def agregar_paquete(self, nombre, id_destino, descripcion, precio, disponibilidad):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO paquetes_turisticos (nombre, id_destino, descripcion, precio, disponibilidad) 
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (nombre, id_destino, descripcion, precio, disponibilidad))
            self.conexion.commit()
            print("Paquete turístico agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar paquete turístico: {e}")
        finally:
            self.desconectar()

    def agregar_viaje(self, id_paquete, fecha_salida, fecha_regreso, disponibilidad):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO viajes (id_paquete, fecha_salida, fecha_regreso, disponibilidad) 
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (id_paquete, fecha_salida, fecha_regreso, disponibilidad))
            self.conexion.commit()
            print("Viaje agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar viaje: {e}")
        finally:
            self.desconectar()

    def agregar_cliente(self, nombre, apellido, email, telefono):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = "INSERT INTO clientes (nombre, apellido, email, telefono) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (nombre, apellido, email, telefono))
            self.conexion.commit()
            print("Cliente agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
        finally:
            self.desconectar()

#------------------------------------------------------------------------------------------------------------
    def agregar_reserva(self, id_cliente, id_viaje, cantidad_plazas, total_pago, fecha_reserva):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = """
                INSERT INTO reservas (id_cliente, id_viaje, cantidad_plazas, total_pago, fecha_reserva) 
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (id_cliente, id_viaje, cantidad_plazas, total_pago, fecha_reserva))
            self.conexion.commit()
            print("Reserva agregada exitosamente.")
        except Exception as e:
            print(f"Error al agregar reserva: {e}")
        finally:
            self.desconectar()

    
    def insertar_datos_iniciales(self):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()

            # Insertar datos en la tabla destinos
            destinos = [
                ("París", "Francia", "La ciudad del amor y la torre Eiffel."),
                ("Roma", "Italia", "Ciudad histórica con el Coliseo y el Vaticano."),
                ("Tokio", "Japón", "Capital moderna con tradición y tecnología.")
            ]
            cursor.executemany(
                "INSERT INTO destinos (nombre, pais, descripcion) VALUES (?, ?, ?)", 
                destinos
            )

            # Insertar datos en la tabla paquetes_turisticos
            paquetes = [
                ("Luna de miel en París", 1, "Paquete romántico con visitas guiadas.", 1200.50, 10),
                ("Roma histórica", 2, "Descubre el pasado de Roma.", 950.00, 15),
                ("Aventura en Tokio", 3, "Explora Tokio con un guía local.", 1500.00, 8)
            ]
            cursor.executemany(
                """
                INSERT INTO paquetes_turisticos (nombre, id_destino, descripcion, precio, disponibilidad) 
                VALUES (?, ?, ?, ?, ?)
                """, 
                paquetes
            )

            # Insertar datos en la tabla viajes
            viajes = [
                (1, "2024-12-15", "2024-12-22", 5),
                (2, "2024-12-10", "2024-12-18", 10),
                (3, "2024-12-20", "2024-12-28", 3)
            ]
            cursor.executemany(
                "INSERT INTO viajes (id_paquete, fecha_salida, fecha_regreso, disponibilidad) VALUES (?, ?, ?, ?)",
                viajes
            )

            # Insertar datos en la tabla clientes
            clientes = [
                ("Ana", "Pérez", "ana.perez@example.com", "123456789"),
                ("Luis", "González", "luis.gonzalez@example.com", "987654321"),
                ("María", "Lopez", "maria.lopez@example.com", "567891234")
            ]
            cursor.executemany(
                "INSERT INTO clientes (nombre, apellido, email, telefono) VALUES (?, ?, ?, ?)",
                clientes
            )

            # Insertar datos en la tabla reservas
            reservas = [
                (1, 1, 2, 2401.00, "2024-12-01"),
                (2, 2, 1, 950.00, "2024-12-02"),
                (3, 3, 2, 3000.00, "2024-12-03")
            ]
            cursor.executemany(
                """
                INSERT INTO reservas (id_cliente, id_viaje, cantidad_plazas, total_pago, fecha_reserva) 
                VALUES (?, ?, ?, ?, ?)
                """, 
                reservas
            )


            self.conexion.commit()
            print("Datos iniciales insertados exitosamente.")
        except Exception as e:
            print(f"Error al insertar datos iniciales: {e}")
        finally:
            self.desconectar()
