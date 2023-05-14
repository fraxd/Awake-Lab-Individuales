import class_producto
import class_cliente
import class_empleado
import class_jefe
import class_pedido
import class_vendedor


#Dunder Mifflin
## Sistema interno para empresa de venta de papel con funcionales basicas de venta y de RRHH
## Cargar Productos

productos = class_producto.cargar_data()
clientes = class_cliente.cargarClientes()
empleados = class_empleado.cargar_empleados()
jefe = class_jefe.cargar_jefe()
vendedor = class_vendedor.cargar_vendedores()


## Aun le falta hartas funciones a este proyecto, en proximas iteracion la idea es ir implementando
