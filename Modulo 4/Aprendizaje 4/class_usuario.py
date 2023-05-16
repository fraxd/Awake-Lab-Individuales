class usuario:
    id = int
    nombre = str
    apellido = str
    email = str

    def __init__(self, id, nombre, apellido, email):
        self.id = id
        self.nombre =nombre
        self.apellido = apellido
        self.email = email
    
    def funcion_usuario(self):
        print('Esta funcion esta en usuario')