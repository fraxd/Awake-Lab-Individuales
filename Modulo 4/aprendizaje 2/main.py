import class_producto
import class_cliente
import class_empleado
import class_jefe
import class_pedido
import class_vendedor


#Dunder Mifflin

## Cargar Productos

productos = class_producto.cargar_data()
clientes = class_cliente.cargarClientes()
empleados = class_empleado.cargar_empleados()
jefe = class_jefe.cargar_jefe()
vendedor = class_vendedor.cargar_vendedores()


