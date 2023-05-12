class jefe():
    id = str
    nombre = str
    apellido = str
    sueldo = int
    id_empleados = []
    id_vendedores = []

    def __init__(self, id, nombre, apellido, sueldo, id_empleados = [], id_vendedores = []):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.id_empleados = id_empleados
        self.id_vendedores = id_vendedores


# Cargar Jefe

def cargar_jefe():
    jefe = jefe(1, 'Michael', 'scott', 1500000, [2,3,4,5,6], [7,8,9,10,11])
    return jefe