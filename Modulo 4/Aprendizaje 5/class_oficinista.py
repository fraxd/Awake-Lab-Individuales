from class_empleado import empleado

class oficinista(empleado):
    area = str

    def __init__(self, id, nombre, apellido, email, sueldo_base, area):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.status = True
        self.email = email
        self.sueldo_base = sueldo_base
        self.area = area

    def saludar(self):
        print(f'Hola soy {self.nombre} y mi area es {self.area} ')

    def funcion_oficinista(self):
        print('Esta funcion esta en oficinista')
def cargar_oficinistas():
    oficinista_1 = oficinista(2, 'Angela', 'Martin', 'angela@dunder-mifflin.com', '800000', 'Contabilidad')
    oficinista_2 = oficinista(3, 'Kevin', 'Malone','kevin@dunder-mifflin.com', '800000', 'Contabilidad')
    oficinista_3 = oficinista(4, 'Darryl', 'Philbin','darryl@dunder-mifflin.com', '1000000', 'Envios')
    oficinista_4 = oficinista(5, 'Ryan', 'Howard','ryan@dunder-mifflin.com', '400000', 'Practicante')
    oficinista_5 = oficinista(6, 'Meredith', 'Palmer','meredith@dunder-mifflin.com', '800000', 'Compra | Relaciones')

    return [oficinista_1, oficinista_2, oficinista_3, oficinista_4, oficinista_5]