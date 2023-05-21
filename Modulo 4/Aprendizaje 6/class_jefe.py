from class_empleado import empleado

class jefe(empleado):
    id_empleados = []
    id_vendedores = []

    def __init__(self, id, nombre, apellido, sueldo_base, email, id_empleados = [], id_vendedores = []):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_base = sueldo_base
        self.email = email
        self.id_empleados = id_empleados
        self.id_vendedores = id_vendedores

    def despedir(self, empleado):
        self.id_empleados.remove(empleado.getId())
        empleado.desactivar()
        print(f'El empleado {empleado.nombre} a sido despedido.')

    def recontratar(self, empleado):
        self.id_empleados.append(empleado.getId())
        empleado.activar()

    def saludar(self):
        print(f'Hola mi nombre es {self.nombre}, soy el jefe y tengo a mi cargo a {self.id_empleados.len} empleados y a {self.id_Vendedores.len} vendedores')

# Cargar Jefe

def cargar_jefe():
    boss = jefe(1, 'Michael', 'scott', 1500000, [2,3,4,5,6], [7,8,9,10,11])
    return boss