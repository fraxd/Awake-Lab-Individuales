class pedido():
    id = str
    sku_productos = []
    id_vendedor = str
    id_cliente = str

    def __init__(self, sku_productos, id_vendedor, id_cliente):
        self.sku_productos = sku_productos
        self.id_vendedor = id_vendedor
        self.id_cliente = id_cliente