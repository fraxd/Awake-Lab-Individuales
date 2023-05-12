class empleado():
    id = int
    nombre = str
    apellido = str
    sueldo = int
    area = str
    
    def __init__(self, id, nombre, apellido, sueldo, area):
        self.id = id
        self.nombe = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.area  = area
    


# Carga los empleados

def cargar_empleados():
    empleado_1 = empleado(2, 'Angela', 'Martin', '800000', 'Contabilidad')
    empleado_2 = empleado(3, 'Kevin', 'Malone', '800000', 'Contabilidad')
    empleado_3 = empleado(4, 'Darryl', 'Philbin', '1000000', 'Envios')
    empleado_4 = empleado(5, 'Ryan', 'Howard', '400000', 'Practicante')
    empleado_5 = empleado(6, 'Meredith', 'Palmer', '800000', 'Compra | Relaciones')

    return [empleado_1, empleado_2, empleado_3, empleado_4, empleado_5]