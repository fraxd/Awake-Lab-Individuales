class vendedor():
    id = int
    nombre = str
    apellido = str
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


## cargar vendedores
def cargar_vendedores():
    vendedor_1 = vendedor(7, 'Dwight', 'Schrute', '600000')
    vendedor_2 = vendedor(8, 'James', 'Halpert', '600000')
    vendedor_3 = vendedor(9, 'Pam', 'Halpert', '600000')
    vendedor_4 = vendedor(10, 'Andrew', 'Bernard', '600000')
    vendedor_5 = vendedor(11, 'Stanley', 'Hudson', '600000')