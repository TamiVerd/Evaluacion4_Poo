import sqlite3 as sql
from tabulate import tabulate

class BaseDatos:
    def __init__(self):
        self.conexion=None

    def conexion_bd(self):
        self.conexion=sql.connect("agencia_viajes.db")

    def desconectar(self):
        if self.conexion is not None:
            self.conexion.close()
    
    def crear_tabla_viajes(self):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS viajes (
                    id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
                    destino TEXT NOT NULL,
                    fecha_salida TEXT NOT NULL,
                    fecha_regreso TEXT NOT NULL,
                    precio REAL NOT NULL,
                    disponibilidad INTEGER NOT NULL
                )
            """)
            print("Tabla 'viajes' creada exitosamente.")
        except Exception as e:
            print(f"Ha ocurrido un error al crear la tabla 'viajes': {e}")
        finally:
            self.desconectar()
    
    def mostrar_todos_viajes(self):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = "SELECT * FROM viajes"
            cursor.execute(sql)
            viajes = cursor.fetchall()
            columnas = [description[0] for description in cursor.description]
            print(tabulate(viajes, headers=columnas, tablefmt="fancy_grid"))
        except Exception as e:
            print(f"Error al mostrar viajes: {e}")
        finally:
            self.desconectar()

    def eliminar_viaje(self, id_viaje):
        try:
            self.conexion_bd()
            cursor = self.conexion.cursor()
            sql = "DELETE FROM viajes WHERE id_viaje = ?"
            cursor.execute(sql, (id_viaje,))
            self.conexion.commit()
            print("Viaje eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar viaje: {e}")
        finally:
            self.desconectar()
