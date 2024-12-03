from baseDatos.base_datos import BaseDatos
from Viajes.viajes import Viaje
from os import system as sys

OPCIONES = ("Agregar viaje", "Mostrar viajes", "Actualizar precio de viaje", "Actualizar disponibilidad", "Salir")

def menu():
    print("| Agencia de Viajes |".center(50))
    print("-" * 50)
    for indice, opcion in enumerate(OPCIONES, start=1):
        print(f"{indice}. {opcion}")
    print("-" * 50)

def agregar_viaje():
    id_viaje = input("Ingrese el ID del viaje: ")
    destino = input("Ingrese el destino del viaje: ").title()
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
    fecha_regreso = input("Ingrese la fecha de regreso (YYYY-MM-DD): ")
    precio = float(input("Ingrese el precio del viaje: "))
    disponibilidad = int(input("Ingrese la cantidad de plazas disponibles: "))
    return Viaje(id_viaje, destino, fecha_salida, fecha_regreso, precio, disponibilidad)

# Lista para almacenar viajes
viajes = []

while True:
    menu()
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:  # Agregar viaje
            nuevo_viaje = agregar_viaje()
            viajes.append(nuevo_viaje)
            print("¡Viaje agregado exitosamente!")
        elif opcion == 2:  # Mostrar viajes
            if viajes:
                print("Viajes disponibles:")
                for viaje in viajes:
                    print(viaje)
            else:
                print("No hay viajes disponibles.")
        elif opcion == 3:  # Actualizar precio
            id_viaje = input("Ingrese el ID del viaje a actualizar: ")
            for viaje in viajes:
                if viaje.id_viaje == id_viaje:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    viaje.actualizar_precio(nuevo_precio)
                    break
            else:
                print("Viaje no encontrado.")
        elif opcion == 4:  # Actualizar disponibilidad
            id_viaje = input("Ingrese el ID del viaje a actualizar: ")
            for viaje in viajes:
                if viaje.id_viaje == id_viaje:
                    nueva_disponibilidad = int(input("Ingrese la nueva disponibilidad: "))
                    viaje.actualizar_disponibilidad(nueva_disponibilidad)
                    break
            else:
                print("Viaje no encontrado.")
        elif opcion == 5:  # Salir
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Por favor, seleccione una opción válida.")
    except Exception as e:
        print(f"Error: {e}")
