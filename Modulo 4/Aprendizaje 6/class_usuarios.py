import pickle

class Usuario:
    def __init__(self, nombre, username, id, password):
        self.nombre = nombre
        self.username = username
        self.id = id
        self.password = password

# Crear instancias de usuarios
def createUsuarios():
    return  [
        Usuario("John Doe", "johndoe", 1, "123456"),
        Usuario("Jane Smith", "janesmith", 2, "abcdef"),
        # Agregar los datos de los otros usuarios
    ]

# Serializar el registro de usuarios en un archivo
def save_usuarios(usuarios):
    with open("usuarios.pickle", "wb") as file:
        pickle.dump(usuarios, file)
    return usuarios

# Deserializar el registro de usuarios desde un archivo
def load_usuarios():
    try:
        with open("usuarios.pickle", "rb") as file:
            usuarios = pickle.load(file)
    except:
        print('No existe el archivo de usuarios, se procede a carga manual.')
        return createUsuarios()
    return usuarios
