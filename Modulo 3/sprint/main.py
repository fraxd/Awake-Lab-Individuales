import random
import string
usuarios = [
    {
        'id_usuario': 1,
        'nombre': 'juan araya'
    },
    {
        'id_usuario': 2,
        'nombre': 'kevin mendez'
    },
    {
        'id_usuario': 3,
        'nombre': 'alexis pinto'
    },
    {
        'id_usuario': 4,
        'nombre': 'Maria loo'
    },
    {
        'id_usuario': 5,
        'nombre': 'Catalina palacios'
    },
    {
        'id_usuario': 6,
        'nombre': 'armando mesas'
    },
    {
        'id_usuario': 7,
        'nombre': 'daddy yankee'
    },
    {
        'id_usuario': 8,
        'nombre': 'josefa fuentes'
    },
    {
        'id_usuario': 9,
        'nombre': 'daniel murua'
    },
    {
        'id_usuario': 10,
        'nombre': 'sebastian morales'
    },
]

def generateAccounts():
    for usuario in usuarios:
        username = generateUsername(usuario['nombre'])
        password = generatePassword()
        telefono = requestPhone(usuario['nombre'])
        usuario.update({
            'username': username,
            'password': password,
            'telefono' : telefono
        })
    print('Cuentas Generadas')
    print('----- Desarrollado por -----')
    print('----- Franco Fuentes Soto -----\n')

def generateUsername(nombre):
    #Basicamente crea un usuario con los primeras 3 letras del nombre + 3 priemras letras apellido
    particional = nombre.split()
    part_1 = particional[0]
    part_2= particional[1]
    username = part_1[0] + part_1[1] + part_1[2] + part_2[0] + part_2[1] + part_2[2]
    return username


def generatePassword():
    caracteres = string.ascii_letters + string.digits
    longitud = random.randrange(8,12)
    password = ''.join(random.choice(caracteres) for i in range(longitud))
    return password 


def requestPhone(nombre):
    while True:
        # se evalua que sea un numero.
        print('Creado perfil de', nombre)
        numero = int(input('Ingresar numero de telefono: '))
        # se evalua que sean 8 digitos
        if len(str(numero)) == 8:
            # se retorna un string segun las instrucciones
            return str(numero)
        else:
            print('Recuerda que deben ser 8 digitos.')

def printUsuarios():
    for usuario in usuarios:
        print('-', usuario)

#INICIO
generateAccounts()
printUsuarios() ## Utilizado para revisar que haga todo correctamente