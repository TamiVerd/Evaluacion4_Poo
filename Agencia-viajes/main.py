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
        nombre_tabla = "clientes"
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:  # Agregar cliente
                nombre = input("Nombre: ").title()
                apellido = input("Apellido: ").title()
                email = input("Email: ").lower()
                telefono = input("Teléfono: ")
                #cliente = Cliente(None, nombre, apellido, email, telefono)
                base_datos.agregar_cliente(nombre, apellido, email, telefono)
                print("Cliente agregado exitosamente.")

            elif opcion == 2:  # Mostrar clientes
                base_datos.mostrar_tabla("clientes")
                
            elif opcion == 3:  # Actualizar cliente
                id_cliente = int(input("ID del cliente a actualizar: "))
                print("Seleccione el campo a actualizar:")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Email")
                print("4. Teléfono")
                opcion_campo = int(input("Ingrese el número correspondiente al campo: "))
                # Mapeo de las opciones a los nombres de los campos
                campos = {1: "nombre", 2: "apellido", 3: "email", 4: "telefono"}
                # Verificar si la opción ingresada es válida
                if opcion_campo in campos:
                    campo = campos[opcion_campo]
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    base_datos.actualizar_cliente(id_cliente, campo, nuevo_valor)
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            elif opcion == 4:  # Eliminar cliente
                id_cliente = int(input("ID del cliente a eliminar: "))
                base_datos.eliminar_por_id("clientes", "id_cliente", id_cliente)

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
                id_paquete = int(input("ID del paquete: "))
                fecha_salida = input("Fecha de salida (YYYY-MM-DD): ")
                fecha_regreso = input("Fecha de regreso (YYYY-MM-DD): ")
                disponibilidad = int(input("Disponibilidad: "))
                base_datos.agregar_viaje(id_paquete, fecha_salida, fecha_regreso, disponibilidad)
            
            elif opcion == 2:  # Mostrar viajes
                base_datos.mostrar_todos_viajes()

            elif opcion == 3:  # Actualizar viaje
                id_viaje = int(input("ID del viaje a actualizar: "))
                print("Seleccione el campo a actualizar:")
                print("1. fecha_salida")
                print("2. fecha_regreso")
                print("3. disponibilidad")
                opcion_campo = int(input("Ingrese el número correspondiente al campo: "))
                campos = {1: "fecha_salida", 2: "fecha_regreso", 3: "disponibilidad"}
                if opcion_campo in campos:
                    campo = campos[opcion_campo]
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    base_datos.actualizar_viaje(id_viaje, campo, nuevo_valor)
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            elif opcion == 4:  # Eliminar viaje
                id_viaje = int(input("ID del viaje a eliminar: "))
                base_datos.eliminar_viaje(id_viaje)
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
            if opcion == 1: # Agregar paqueteTuristico
                nombre = input("Ingrese el nombre del paquete: ")
                id_destino = int(input("Ingrese el ID del destino asociado: "))
                descripcion = input("Ingrese una descripción: ")
                precio = float(input("Ingrese el precio del paquete: "))
                disponibilidad = int(input("Ingrese la disponibilidad (cantidad de plazas): "))
                base_datos.agregar_paquete(nombre, id_destino, descripcion, precio, disponibilidad)
                print("Paquete turístico agregado exitosamente.")

            elif opcion == 2: # Mostrar paqueteTuristico
                base_datos.mostrar_tabla("paquetes_turisticos")
                    
            elif opcion == 3: # Actualizar paqueteTuristico
                id_paquete = int(input("Ingrese el ID del paquete a modificar: "))
                print("Seleccione el campo a actualizar:")
                print("1. Nombre")
                print("2. ID del destino")
                print("3. Descripción")
                print("4. Precio")
                print("5. Disponibilidad")
                opcion_campo = int(input("Ingrese el número correspondiente al campo: "))
                campo = {1: "nombre", 2: "id_destino", 3: "descripcion", 4: "precio", 5: "disponibilidad"}
                if opcion_campo in campo:
                    campo = campo[opcion_campo]
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    base_datos.actualizar_paquete(id_paquete, campo, nuevo_valor)
                    print(f"Campo {campo} del paquete turístico actualizado exitosamente.")
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

                    
            elif opcion == 4: # Eliminar paqueteTuristico
                id_paquete = int(input("Ingrese el ID del paquete a eliminar: "))
                base_datos.eliminar_por_id("paquetes_turisticos", "id_paquete", id_paquete)
                
            
            elif opcion == 5:  # Volver
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")


                
def gestionar_reserva(base_datos):
    while True:
        menu_subtitulo("Gestión de Reservas")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:  # Agregar reserva
                id_cliente = int(input("Ingrese el ID del cliente: "))
                id_viaje = int(input("Ingrese el ID del viaje: "))
                fecha_reserva = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
                cantidad_plazas = int(input("Ingrese la cantidad de personas: "))
                base_datos.agregar_reserva(id_cliente, id_viaje, fecha_reserva, cantidad_plazas)
            
            elif opcion == 2:  # Mostrar reservas
                base_datos.mostrar_tabla("reservas")
            
            elif opcion == 3:  # Actualizar reserva
                id_reserva = int(input("Ingrese el ID de la reserva a modificar: "))
                print("Seleccione el campo a actualizar:")
                print("1. ID del cliente")
                print("2. ID del viaje")
                print("3. Fecha de la reserva")
                print("4. Cantidad de plazas")
                opcion_campo = int(input("Ingrese el número correspondiente al campo: "))
                campos = {1: "id_cliente", 2: "id_viaje", 3: "fecha_reserva", 4: "cantidad_plazas"}
                if opcion_campo in campos:
                    campo = campos[opcion_campo]
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    base_datos.actualizar_reserva(id_reserva, campo, nuevo_valor)
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
                
            elif opcion == 4:  # Eliminar reserva
                id_reserva = int(input("Ingrese el ID de la reserva a eliminar: "))
                base_datos.eliminar_por_id("reservas", "id_reserva", id_reserva)
            
            elif opcion == 5:  # Volver
                print("Saliendo del módulo de gestión de reservas.")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
            print(f"Error: {e}")

def gestionar_destino(base_datos):
    while True:
        #sys('cls')  # Limpia la consola
        menu_subtitulo("Gestión de Destinos")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:  # Agregar destino
                nombre = input("Nombre del destino: ")
                pais = input("País: ")
                descripcion = input("Descripción: ")
                base_datos.agregar_destino(nombre, pais, descripcion)

            elif opcion == 2:  # Mostrar destinos
                base_datos.mostrar_tabla("destinos")

            elif opcion == 3:  # Actualizar destino
                id_destino = int(input("ID del destino a actualizar: "))
                print("Seleccione el campo a actualizar:")
                print("1. Nombre")
                print("2. País")
                print("3. Descripción")
                opcion_campo = int(input("Ingrese el número correspondiente al campo: "))
                campos = {1: "nombre", 2: "pais", 3: "descripcion"}
                if opcion_campo in campos:
                    campo = campos[opcion_campo]
                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
                    base_datos.actualizar_destino(id_destino, campo, nuevo_valor)
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")

            elif opcion == 4:  # Eliminar destino
                id_destino = int(input("ID del destino a eliminar: "))
                base_datos.eliminar_por_id("destinos", "id_destino", id_destino)

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
                gestionar_paqueteTuristico(base_datos)
            elif opcion == 4:
                gestionar_reserva(base_datos)
            elif opcion == 5:
                gestionar_destino(base_datos)
            elif opcion == 6:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()