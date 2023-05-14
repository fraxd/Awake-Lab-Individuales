class producto:
    sku = int
    nombre = str
    precio = int

    def __init__(self, sku, nombre, precio):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other):  ## Sobre carga de metodos
        return self.sku == other.sku
    


def cargar_data():
    producto_1 = producto(44623546, 'Resma Carta x 500', 4320)
    producto_2 = producto(44624235, 'Resma Oficio x 500', 4750)
    producto_3 = producto(44614872, 'Resma Carta x 2500',16200)
    producto_4 = producto(44612345, 'Resma Oficio x 2500', 18000)
    producto_5 = producto(44623456, 'Resma A4 x 500', 4520)

    return [producto_1, producto_2, producto_3, producto_4, producto_5]