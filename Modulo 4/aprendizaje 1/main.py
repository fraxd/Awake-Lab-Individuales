
class usuario:
    def __init__(self, nombre, mail, password):
        self.nombre = nombre
        self.mail = mail
        self.password = password

class cliente(usuario):
    def __init__(self, nombre, mail, password, dirrecion):
        self.nombre = nombre
        self.mail = mail
        self.password = password
        self.dirrecion = dirrecion
        self.pedidos = []
    
    def hacerPedidos():
        #logica interna
        return True

    def cambiarDirrecion(self, dirrecion):
        self.dirrecion = dirrecion
        return True
    
    def anularPedido(self, id_pedido):
        for pedido in self.pedidos:
            if pedido['id_pedido'] == id_pedido:
                pedido.pop()
                return True
        return False

class vendedor(usuario):
    def __init__(self, nombre, mail, password, id_supervisor):
        self.nombre = nombre
        self.mail = mail,
        self.password = password
        self.id_supervisor = id_supervisor
    
    def realizarVenta(self, productos , mail_Cliente):
        #Logica Interna Misteriosa
        return True
    
    def gestionarCambios(self, id_pedido, producto):
        #Logica Interna
        return True
    
    def cambiarSupervisor(self, id_supervisor):
        #logica interna
        return True

class supervisor(usuario):
    def __init__(self, nombre, mail, password):
        self.nombre = nombre
        self.mail = mail,
        self.password = password, 
        self.id_vendedores  = []
    
    def asignar_vendedores(self, id_Vendedor):
        #logica interna
        return True
    
    def rehusar_vendedor(self, id_Vendedor):
        #logica Interna
        return True
    
    def generar_reportes(self):
        #logica interna
        return True
    
