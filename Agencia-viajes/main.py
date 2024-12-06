from baseDatos.base_datos import BaseDatos
from os import system as sys
from Clases.viaje import Viaje
from Clases.cliente import Cliente
from Clases.destino import Destino
from Clases.reserva import Reserva
from Clases.paqueteTuristico import PaqueteTuristico
#--------------------------------------------
#funciones cliente
def agregar_cliente(base_datos):
        nombre = input("Nombre: ").title()
        apellido = input("Apellido: ").title()
        email = input("Email: ").lower()
        telefono = input("Teléfono: ")
        cliente = Cliente(None, nombre, apellido, email, telefono)
        base_datos.agregar_cliente(cliente)
        print("Cliente agregado exitosamente.")

def mostrar_clientes(base_datos):
        base_datos.mostrar_todos_clientes()

def actualizar_cliente(base_datos):
        id_cliente = int(input("ID del cliente: "))
        campo = input("Campo a actualizar (nombre, apellido, email, telefono): ").lower()
        nuevo_valor = input("Nuevo valor: ")
        base_datos.actualizar_cliente(id_cliente, campo, nuevo_valor)

def eliminar_cliente(base_datos):
        id_cliente = int(input("ID del cliente: "))
        base_datos.eliminar_cliente(id_cliente)
#--------------------------------------------
#funcciones viaje
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
    
def agregar_viaje(base_datos):
    destino = input("Destino: ").title()
    fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
    fecha_regreso = input("Fecha de regreso (YYYY-MM-DD): ")
    precio = float(input("Precio: "))
    disponibilidad = int(input("Disponibilidad: "))
    base_datos.agregar_viaje(destino, fecha_salida, fecha_regreso, precio, disponibilidad)
    print("Viaje agregado exitosamente.")

def mostrar_viajes(base_datos):
    base_datos.mostrar_todos_viajes()

def actualizar_viaje(base_datos):
    id_viaje = int(input("ID del viaje: "))
    campo = input("Campo a actualizar (destino, fecha_salida, fecha_regreso, precio, disponibilidad): ").lower()
    nuevo_valor = input("Nuevo valor: ")
    base_datos.actualizar_viaje(id_viaje, campo, nuevo_valor)

def eliminar_viaje(base_datos):
    id_viaje = int(input("ID del viaje: "))
    base_datos.eliminar_viaje(id_viaje)
#--------------------------------------------
#funciones destino

#--------------------------------------------
#funciones paqueteTuristico

#--------------------------------------------
#funciones reserva

#--------------------------------------------

#--------------------------------------------
def menu_principal():
    """
    Muestra el menú principal.
    """
    print("\n--- Menú Principal ---")
    print("1. Gestionar Clientes")
    print("2. Gestionar Viajes")
    print("3. Gestionar Paquetes Turísticos")
    print("4. Gestionar Reservas")
    print("5. Gestionar Destinos")
    print("6. Salir")

def menu_subtitulo(titulo):
    """
    Muestra un subtítulo para los submenús.
    """
    print(f"\n--- {titulo} ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Volver al Menú Principal")

def gestionar_clientes(base_datos):
    while True:
        #sys('cls')  #limpiar la consola, pero que si se vea la tabla???
        menu_subtitulo("Gestión de Clientes")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:  # Agregar cliente
                nombre = input("Nombre: ").title()
                apellido = input("Apellido: ").title()
                email = input("Email: ").lower()
                telefono = input("Teléfono: ")
                cliente = Cliente(None, nombre, apellido, email, telefono)
                base_datos.agregar_cliente(cliente)
                print("Cliente agregado exitosamente.")
            elif opcion == 2:  # Mostrar clientes
                base_datos.mostrar_tabla("clientes")
            elif opcion == 3:  # Actualizar cliente
                id_cliente = int(input("ID del cliente a actualizar: "))
                campo = input("Campo a actualizar (nombre, apellido, email, telefono): ").lower()
                nuevo_valor = input("Nuevo valor: ")
                base_datos.actualizar_cliente(id_cliente, campo, nuevo_valor)
            elif opcion == 4:  # Eliminar cliente
                id_cliente = int(input("ID del cliente a eliminar: "))
                base_datos.eliminar_cliente(id_cliente)
            elif opcion == 5:  # Volver
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

def gestionar_viajes(base_datos):
    while True:
        #sys('cls')  # Limpia la consola
        menu_subtitulo("Gestión de Viajes")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:  # Agregar viaje
                destino = input("Destino: ").title()
                fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
                fecha_regreso = input("Fecha de regreso (YYYY-MM-DD): ")
                precio = float(input("Precio: "))
                disponibilidad = int(input("Disponibilidad: "))
                viaje = Viaje(None, destino, fecha_salida, fecha_regreso, precio, disponibilidad)
                base_datos.agregar_viaje(viaje)
                print("Viaje agregado exitosamente.")
            elif opcion == 2:  # Mostrar viajes
                base_datos.mostrar_todos_viajes()
            elif opcion == 3:  # Actualizar viaje
                id_viaje = int(input("ID del viaje a actualizar: "))
                campo = input("Campo a actualizar (destino, fecha_salida, fecha_regreso, precio, disponibilidad): ").lower()
                nuevo_valor = input("Nuevo valor: ")
                base_datos.actualizar_viaje(id_viaje, campo, nuevo_valor)
            elif opcion == 4:  # Eliminar viaje
                id_viaje = int(input("ID del viaje a eliminar: "))
                base_datos.eliminar_por_id(id_viaje)
            elif opcion == 5:  # Volver
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")
#***
def gestionar_paqueteTuristico(base_datos):
    while True:
        menu_subtitulo("Gestión de Paquetes Turísticos")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                nombre = input("Ingrese el nombre del paquete: ")
                id_destino = int(input("Ingrese el ID del destino asociado: "))
                descripcion = input("Ingrese una descripción: ")
                precio = float(input("Ingrese el precio del paquete: "))
                disponibilidad = int(input("Ingrese la disponibilidad (cantidad de plazas): "))
                base_datos.agregar_paquete(nombre, id_destino, descripcion, precio, disponibilidad)
            
            elif opcion == "2":
                    id_paquete = int(input("Ingrese el ID del paquete a modificar: "))
                    print("Ingrese los nuevos valores (deje en blanco para mantener el actual):")
                    nombre = input("Nuevo nombre: ")
                    id_destino = input("Nuevo ID del destino: ")
                    descripcion = input("Nueva descripción: ")
                    precio = input("Nuevo precio: ")
                    disponibilidad = input("Nueva disponibilidad: ")
                    base_datos.modificar_paquete(id_paquete, nombre, id_destino, descripcion, precio, disponibilidad)
            
            elif opcion == "3":
                    id_paquete = int(input("Ingrese el ID del paquete a eliminar: "))
                    base_datos.eliminar_por_id("paquetes_turisticos", "id_paquete", id_paquete)
                
            elif opcion == "4":
                base_datos.mostrar_tabla("paquetes_turisticos")
            
            elif opcion == "5":
                print("Saliendo del módulo de gestión de paquetes turísticos.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
                print(f"Error: {e}")

                
#def gestionar_reserva(base_datos):
#def gestionar_destino(base_datos):


def main():
    base_datos = BaseDatos()
    base_datos.crear_tablas()
    base_datos.insertar_datos_iniciales()

    while True:
        sys('cls')  # Limpia la consola
        menu_principal()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                gestionar_clientes(base_datos)
            elif opcion == 2:
                gestionar_viajes(base_datos)
            elif opcion == 3:
                print("Gestión de Paquetes Turísticos (en desarrollo)")
            elif opcion == 4:
                print("Gestión de Reservas (en desarrollo)")
            elif opcion == 5:
                print("Gestión de Destinos (en desarrollo)")
            elif opcion == 6:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()