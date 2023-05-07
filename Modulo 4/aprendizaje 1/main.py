class cliente:
    def __init__(self, nombre, mail, password, dirrecion, saldo):
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
        

class vendedor:
    def __init__(self, nombre, mail, password, id_supervisor):
        self.nombre = nombre
        self.mail = mail,
        self.password = password
        self.id_supervisor = id_supervisor
        self.comision = 0
    
    def sumarComision(self, monto_Venta):
        self.comision = monto_Venta*0.02 #Osea el 2%
    
    def changePassword(self, newPassword):
        self.password = newPassword
    
    def cambiarSupervisor(self, id_supervisor):
        self.id_supervisor = id_supervisor

class supervisor:
    def __init__(self, nombre, mail, password):
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
