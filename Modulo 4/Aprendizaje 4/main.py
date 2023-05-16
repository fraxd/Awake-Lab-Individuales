import class_producto
import class_cliente
import class_oficinista
import class_jefe
import class_vendedor


#Dunder Mifflin
## Sistema interno para empresa de venta de papel con funcionales basicas de venta y de RRHH


productos = class_producto.cargar_data()
clientes = class_cliente.cargarClientes()
oficinistas = class_oficinista.cargar_oficinistas()
jefe = class_jefe.cargar_jefe()
vendedor = class_vendedor.cargar_vendedores()
for oficinista in oficinistas:
    #Basicamente oficinita hereda Empleado y Empleado Hereda Usuario
    oficinista.saludar()
    oficinista.funcion_usuario()
    oficinista.funcion_empleado()
    oficinista.funcion_oficinista()
    print('-------------')

## Aun le falta hartas funciones a este proyecto, en proximas iteracion la idea es ir implementando
