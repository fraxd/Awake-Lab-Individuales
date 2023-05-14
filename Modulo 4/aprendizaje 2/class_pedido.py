class pedido():
    id = str
    sku_productos = []
    subtotal = int
    id_vendedor = str
    id_cliente = str

    def __init__(self, sku_productos, id_vendedor, id_cliente, monto):
        self.sku_productos = sku_productos
        self.id_vendedor = id_vendedor
        self.id_cliente = id_cliente
        self.subtotal = monto

    def agregar_producto(self, producto, cantidad=1): #Sobrecarga ya que parte con un valor por default
        self.sku_productos.append({
            "sku": producto.sku,
            "cant": cantidad
        })
        self += producto.precio
    
    def getSubTotal(self):
        return self.subtotal
    
    def set_id_vendedor(self, id_vendedor):
        self.id_vendedor = id_vendedor
    