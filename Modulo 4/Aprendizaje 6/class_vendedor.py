from class_empleado import empleado
class vendedor(empleado):
    sueldo_base = int
    comisiones = int
    id_clientes = []
    id_pedidos = []

    def __init__(self, id, nombre, apellido, sueldo_base):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_base = sueldo_base
        self.comisiones = 0 
        self.id_clientes = []
        self.id_pedidos = []

    def add_comision(self, monto): # Añade comision y retorna el total
        self.comisiones += monto
        return self.comisiones
    
    def calcular_sueldo_total(self):
        return self.sueldo_base + self.comisiones
    

## cargar vendedores
def cargar_vendedores():
    vendedor_1 = vendedor(7, 'Dwight', 'Schrute', '600000')
    vendedor_2 = vendedor(8, 'James', 'Halpert', '600000')
    vendedor_3 = vendedor(9, 'Pam', 'Halpert', '600000')
    vendedor_4 = vendedor(10, 'Andrew', 'Bernard', '600000')
    vendedor_5 = vendedor(11, 'Stanley', 'Hudson', '600000')
    return [vendedor_1, vendedor_2, vendedor_3, vendedor_4, vendedor_5]