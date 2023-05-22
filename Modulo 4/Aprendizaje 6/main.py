import class_producto
import class_cliente
import class_oficinista
import class_jefe
import class_vendedor
import os  ## Para la funcion de limpiar Pantalla
import time ## Para el controlar Pausas
from datetime import datetime
import csv
import class_usuarios

#Dunder Mifflin
## Sistema interno para empresa de venta de papel con funcionales basicas de venta y de RRHH


productos = class_producto.cargar_data()
clientes = class_cliente.cargarClientes()
oficinistas = {}
jefe = class_jefe.cargar_jefe()
vendedores = class_vendedor.cargar_vendedores()
#Fecha de pago 
fecha_str = "30/05/2023"
fecha_pagos = datetime.strptime(fecha_str, "%d/%m/%Y")
def limpiar_pantalla():
    if os.name == 'posix':  # Para sistemas tipo Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')

#Funcion que pide presionar enter para continuar
def pausa():
    input('Presione Enter para continuar.')

#Login
def login():
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        global usuarios
        usuarios = class_usuarios.load_usuarios()
        username = input('Ingrese nombre de usuario: ')
        password = input('Ingrese contraseña: ')
        for usuario in usuarios:
            if usuario.username == username:
                if usuario.password == password:
                    menuPrincipal(usuario)
                    break
        print('Usuario o contraseña Invalidos, Favor Revisar.')
        pausa()

# Menu Principal
def menuPrincipal(usuario):
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        print('1.- Recursos Humanos Sistems')
        print('2.- Sistema de Ventas --- NO DISPONIBLE')
        print('3.- Cambiar contraseña Usuario')
        print('9.- Salir')
        try:
            op = int(input('\nIngrese la opcion a utilizar: '))
            if op == 1:
                recursosHumanosSystems()
            elif op == 2:
                print('En desarrollo')
            elif op == 3:
                cambiarPassword(usuario)
            elif op == 9:
                limpiar_pantalla()
                print('Sistemas Computacionales Avanzados')
                print(' ****** Dunder Mifflin S.A. ******')
                print(' Gracias por preferir PencaLabs')
                time.sleep(3)
                break
            else:
                raise ValueError('Opcion No valida.')
        except ValueError as e:
            print(f'Error: {e}')
            input('Presione Enter Para continuar: ')

## Menu de recursos inHumanos
def recursosHumanosSystems():
    global fecha_pagos
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        print('1.- Listado Oficinistas')
        print('2.- Modificar Sueldo Oficinistas')
        print('3.- Listado Vendedores')
        print('4.- Modificar Sueldo Vendedores')
        print('5.- Modificar Fecha de pago.')
        print('6.- Guardar datos usuarios.')
        print('7.- Cargar Datos Oficinistas')
        print('9.- Salir')

        try:
            op = int(input('\nIngrese la opcion a utilizar: '))
            if op == 1:
                list_oficinistas()
                input('Presione Enter para continuar')

            elif op == 2:
                modificar_Sueldo_oficinistas()
                input('Presione Enter para continuar')
            elif op == 3:
                list_Vendedores()
                input('Presione Enter para continuar')
            elif op == 4:
                modificar_Sueldo_vendedor()
                input('Presione Enter para continuar')
            elif op == 5:
                fecha_pagos = modificar_fecha()
                input('Presione Enter para continuar')
            elif op ==6:
                guardar_oficinistas()
                guardar_vendedores()
                print('Datos Guardados Correctamente')
                input('Presione Enter para continuar')
            elif op == 7:
                cargar_oficinitas()
                print('Datos Cargados Correctamente')
                input('Presione Enter para continuar')
            elif op == 9:
                limpiar_pantalla()
                print('Sistemas Computacionales Avanzados')
                print(' ****** Dunder Mifflin S.A. ******')
                print(' Gracias por preferir PencaLabs')
                time.sleep(3)
                break
            else:
                raise ValueError('Opcion No valida.')
        except ValueError as e:
            print(f'Error: {e}')
            input('Presione Enter Para continuar: ')
## Aun le falta hartas funciones a este proyecto, en proximas iteracion la idea es ir implementando

def list_Vendedores():
    limpiar_pantalla()
    i = 0
    for empleado in vendedores:
        i +=1
        print(f'{i}.- Nombre: {empleado.nombre} {empleado.apellido} | Sueldo: {empleado.sueldo_base}')

def list_oficinistas():
    limpiar_pantalla()
    for empleado in oficinistas.values():
        print(f'Nombre: {empleado.nombre} {empleado.apellido} | Sueldo: {empleado.sueldo_base}')


def modificar_Sueldo_oficinistas():
    list_oficinistas()
    while True:
        try:
            op = input('Indique el Nombre del empleado a editar (Solo Primer Nombre): ')
            empleado = oficinistas[op]
            print(f'Editando a {empleado.nombre} con sueldo {empleado.sueldo_base}')
            sueldo = int(input('Ingrese Nuevo sueldo: '))
            empleado.sueldo_base = sueldo
            oficinistas[op] = empleado
            print('Sueldo Actualizado.')
            break
        except KeyError:
            print('No encontramos ese nombre en nuestra base de datos, revisa e intanta denuevo.\n')
        except ValueError:
            print('Error: El monto debe ser ingresado en numeron, sin puntos ni comas.')
        finally:
            print('En esta parte existen 2 potenciales Errores.')
            print(('KeyError: Basicamente es el error si el usuario ingresa un nombre el cual no coincide con ninguno de los Keys (nombres) del diccionario de empleados, por lo cual no existe. \nSolucion: Revisar el listado y copiar textualmente el nombre del empleado a editar.\n'))
            print('ValueError: En el campo de Id o monto ingresaron un string en vez de un numero, por lo que no es aceptado por el sistema.\n Solucion: Ingresar un valor ENTERO.')
def modificar_Sueldo_vendedor():
    list_Vendedores()
    while True:
        try:
            op = int(input('Indique el numero del empleado a editar : '))
            empleado = vendedores[op]
            print(f'Editando a {empleado.nombre} con sueldo {empleado.sueldo_base}')
            sueldo = int(input('Ingrese Nuevo sueldo: '))
            empleado.sueldo_base = sueldo
            vendedores[op]= empleado
            print('Sueldo Actualizado.')
            break
        except IndexError:
            print('No encontramos ese Id en nuestra base de datos, revisa e intanta denuevo.\n')
        except ValueError:
            print('Error: El monto / N° Empleado debe ser ingresado en numeron, sin puntos ni comas.')
        finally:
            print(('IndexError: Basicamente es el error si el usuario ingresa un Id/numero el cual no este dentro de los rangos de la lista por lo que estaria fuera de ella. \nSolucion: Seguir las indicaciones puestas e indicar un numero dentro del rango establecido.\n'))
            print('ValueError: En el campo de Id o monto ingresaron un string en vez de un numero, por lo que no es aceptado por el sistema.\n Solucion: Ingresar un valor ENTERO.')
def modificar_fecha():
    try:
        fecha_str = input("Ingrese una fecha (formato: dd/mm/aaaa): ")
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        print('Fecha Actualizada')
        return fecha
    except TypeError:
        print("Error: El formato de fecha es incorrecto. No se a guardado la nueva fecha.")
        return None
    except Exception:
        print("Error: El formato de fecha es incorrecto. No se a guardado la nueva fecha.")
        return None
    finally:
        print('TypeError: Este error es causado porque el valor ingresado no coincide con el tipo de valor que deberia ser, en este caso se espera un tipo Datetime con el formato dd/mm/yyyy en caso de no cumplirlo existe este error.\nSolucion: Verificar que la fecha ingresada siga claramente el formato de datos antes solicitado.')

def guardar_oficinistas():
    # Obtener los nombres de los atributos
    atributos = oficinistas["Angela"].__dict__.keys()

    # Escribir los objetos en un archivo CSV
    with open("oficinistas.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(atributos)  # Escribir los nombres de los atributos como encabezados

        for objeto in oficinistas.values():
            valores = [getattr(objeto, atributo) for atributo in atributos]
            writer.writerow(valores)
    
def guardar_vendedores():
    with open("vendedores.csv", "w", newline="") as archivo:
        writer = csv.writer(archivo, delimiter=",")

        # Escribir encabezados de columnas
        writer.writerow(["Nombre", "Edad", "Telefono"])

        # Escribir objetos en filas
        for vendedor in vendedores:
            writer.writerow(vendedor) #

def cargar_oficinitas():
    # Leer los datos del archivo CSV
    try:
        with open("oficinistas.csv", mode="r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Leer los encabezados
            for row in reader:  # Leer cada fila de datos
                id = row[0]
                nombre = row[1]
                apellido = row[2]
                status = row[3]
                email = row[4]
                sueldo_base = row[5]
                area = row[6]
                telefono = row[7]
                edad = row[8]
                usuario = class_oficinista.oficinista(id,nombre, apellido, email, sueldo_base, area, telefono, edad)
                oficinistas[nombre] = usuario
    except:
        print('No se encontro archivo csv de oficinistas.')

def cambiarPassword(usuario):
    print(f'Cambiando contraseña para {usuario.nombre}')
    while True:
        password = input('Ingrese nueva contraseña: ')
        confirmPassword = input(' Re ingrese nueva contraseña: ')
        if(confirmPassword == password):
            usuario.password = password
            for i in range(len(usuarios)):
                if usuarios[i].username == usuario.username:
                    usuarios[i] = usuario
            print('Contraseña actualizada. Se procede a realizar guardado en "bd".')
            class_usuarios.save_usuarios(usuarios)
            break
        else:
            print('Las contraseñas no coinciden.')


#Inica el Programa


login()




