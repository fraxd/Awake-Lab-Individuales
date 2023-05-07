class cliente:
    def __init__(self, nombre, mail, password, dirrecion, saldo = '0'):
        self.nombre = nombre
        self.mail = mail
        self.password = password
        self.dirrecion = dirrecion
        self.saldo = saldo
    
    def cambiarDirrecion(self, dirrecion):
        self.dirrecion = dirrecion
        print('Dirrecion Cambiada Correctamente')

    def sumarSaldo(self, saldo):
        self.saldo += saldo
        print('Saldo Actualizado')
    
    def ocuparSaldo(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print('Saldo Descontado')
            return True
        else:
            print('Saldo Insuficiente')
            return False
    
    def __eq__(self, other): ## Basicamente es para que al momento de compararlos si son iguales se vea netamente el correo
        return self.mail == other.mail

class vendedor:
    def __init__(self, id_vendedor, nombre, mail, password, id_supervisor):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.mail = mail,
        self.password = password
        self.id_supervisor = id_supervisor
        self.comision = 0
        self.cant_Ventas = 0
    
    def sumarComision(self, monto_Venta):
        self.comision = monto_Venta*0.02 #Osea el 2%7
        self.cant_Ventas += 1
    
    def changePassword(self, newPassword):
        self.password = newPassword
    
    def cambiarSupervisor(self, id_supervisor):
        self.id_supervisor = id_supervisor

    def calcularSueldoBruto(self):
        return 440000 + self.comision + self.cant_Ventas*250

class supervisor:
    def __init__(self, id_supervisor, nombre, mail, password):
        self.id_supervisor = id_supervisor
        self.nombre = nombre
        self.mail = mail,
        self.password = password, 
        self.id_vendedores  = []
    
    def asignar_vendedores(self, id_Vendedor):
        self.id_vendedores.append(id_Vendedor)
    
    def rehusar_vendedor(self, id_Vendedor):
        self.id_vendedores.remove(id_Vendedor)
        print('Vendedor Removido')
    
    def print_id_vendedores(self):
        for id_vendedores in self.id_vendedores:
            print(id_vendedores)        
    
    def reasignar_vendedor(self, other, id_vendedor): #El self Cede y el other absorve
        self.rehusar_vendedor(id_vendedor)
        other.asignar_vendedores(id_vendedor)


class producto:
    def __init__(self, nombre, precio, stock, provedor=''):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.provedor = provedor
        
    def agregarStock(self, nuevoStock): # se agrega stock y se retorna el nuevo stock
        self.stock += nuevoStock
        return self.stock
    
    def generarVenta(self, stock_Solicitado):
        if self.stock >= stock_Solicitado:
            print('Pedido Confirmado')
            self.stock -= stock_Solicitado
            return True
        else:  
            print('Stock Insuficiente - Pedido Cancelado')
            return False
    
    def cambiarNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print('Nombre de producto Actualizado.')

    def cambiarProvedor(self, nuevo_provedor):
        self.provedor = nuevo_provedor
        print('Provedor Actualizado.')

    def __eq__(self, other):
        return self.nombre == other.nombre and self.precio == other.precio


cliente_a = cliente('juan perez', 'juanito@hot.cl', '123456', 'Por ahi #133')
cliente_b = cliente('juan peres', 'juanito@hot.cl', '123456789', 'Por ahi #133')

if cliente_a == cliente_b:
    print('Son iguales ya que tienen el mismo correo')
else: 
    print('Son distintos')

vendedor_a = vendedor(1,'Michael Scott', 'michael@dundermifflin.com', '987654321', 1)

vendedor_a.sumarComision(90000)
print('Sueldo Bruto del vendedor a:', vendedor_a.calcularSueldoBruto())

supervisor_a = supervisor(1,'Dr Simi' , 'simi@simi.cl', 'lomismoperomasbarato')
supervisor_b = supervisor(1,'Dr ugarte' , 'ugarte@simi.cl', 'laveselasmanos')
supervisor_a.asignar_vendedores(1)

supervisor_a.reasignar_vendedor(supervisor_b, 1)
