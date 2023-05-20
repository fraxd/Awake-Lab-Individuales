import class_producto
import class_cliente
import class_oficinista
import class_jefe
import class_vendedor
import os  ## Para la funcion de limpiar Pantalla
import time ## Para el controlar Pausas

#Dunder Mifflin
## Sistema interno para empresa de venta de papel con funcionales basicas de venta y de RRHH


productos = class_producto.cargar_data()
clientes = class_cliente.cargarClientes()
oficinistas = class_oficinista.cargar_oficinistas()
jefe = class_jefe.cargar_jefe()
vendedor = class_vendedor.cargar_vendedores()

def limpiar_pantalla():
    if os.name == 'posix':  # Para sistemas tipo Unix (Linux, macOS, etc.)
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')

#Funcion que pide presionar enter para continuar
def pausa():
    input('Presione Enter para continuar.')

# Menu Principal
def menuPrincipal():
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        print('1.- Recursos Humanos Sistems')
        print('2.- Sistema de Ventas')
        print('9.- Salir')
        try:
            op = int(input('\nIngrese la opcion a utilizar: '))
            if op == 1:
                recursosHumanosSystems()
            elif op == 2:
                print('En desarrollo')
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
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        print('1.- Listado Oficinistas')
        print('2.- Modificar Sueldo Oficinistas')
        print('3.- Listado Vendedores')
        print('4.- Modificar Sueldo Vendedores')
        print('9.- Salir')

        try:
            op = int(input('\nIngrese la opcion a utilizar: '))
            if op == 1:
                list_empleados(op)
            elif op == 2:
                print('En desarrollo')
            elif op == 3:
                list_empleados(op)
            elif op == 4:
                print('En desarrollo')
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

def list_empleados(op):
    limpiar_pantalla()
    if op == 1 or op == 2:
        temp = oficinistas
        print('** Oficinistas **')
    else:
        temp = vendedor
        print('** Vendedores **')
    for empleado in temp:
        print(f'Nombre: {empleado.nombre} {empleado.apellido} | Sueldo: {empleado.sueldo_base}')
    if op == 1 or op ==3:
        pausa()

def modificar_Sueldo_oficinistas(op):
    while True:
        limpiar_pantalla()
        print('Sistemas Computacionales Avanzados')
        print(' ****** Dunder Mifflin S.A. ******')
        print('1.- Selecionar via Nombre')
        print('2.- Selecionar Via ID')
        print('9.- Salir')
        try:
            op = int(input('\nIngrese la opcion a utilizar: '))
            if op == 1:
                list_empleados(op)
                nombre = input('Ingrese el nombre: (Solo Nombre, No Apellido)')
                for i in range (len())
            elif op == 2:
                list_empleados(op)
            elif op == 9:
                break
            else:
                raise ValueError('Opcion No valida.')
        except ValueError as e:
            print(f'Error: {e}')
            input('Presione Enter Para continuar: ')

menuPrincipal()




