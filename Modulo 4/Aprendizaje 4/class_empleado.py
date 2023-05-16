from class_usuario import usuario

class empleado(usuario):
    sueldo_base = int
    status = True ## si es false esta despedido
    
    def __init__(self, id, nombre, apellido, email, sueldo_base):
        self.id = id
        self.nombe = nombre
        self.apellido = apellido
        self.email = email
        self.status = True
        self.sueldo_base = sueldo_base
    
    def funcion_empleado(self):
        print('Esta es una funcion de clase empleado')


    def getId(self):
        return self.id

    def saludar(self):
        print('Hola soy {nombre}')

    def desactivar(self):
        self.status = False
    
    def activar(self):
        self.status= True
