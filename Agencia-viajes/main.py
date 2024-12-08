from baseDatos.base_datos import BaseDatos
from os import system as sys
from Clases.viaje import Viaje
from Clases.cliente import Cliente
from Clases.destino import Destino
from Clases.reserva import Reserva
from Clases.paqueteTuristico import PaqueteTuristico
#--------------------------------------------

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
        sys('cls')  # Limpia la consola
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
        sys('cls')  # Limpia la consola
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
                base_datos.eliminar_viaje(id_viaje)
            elif opcion == 5:  # Volver
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

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