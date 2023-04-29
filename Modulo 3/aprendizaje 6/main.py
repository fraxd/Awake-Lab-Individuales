import time
usuarios = []

def printUsers(temp):
    print('Listado de usuarios registrados:')
    for usuario in usuarios:
        print(usuario)
        time.sleep(temp)
    print('Listado Finalizado.')


def registerUser(usuario, password,edad):
    usuarios.append({
    'usuario' : usuario,
    'password' : password,
    'edad' : edad
    })
    return True



while True:
    print(' BEST REGISTER')
    usuario = input('Ingresar Usuario: ')
    password = input('Ingresar password: ')
    while True:
        try:
            edad = int(input('Ingrese su edad en numeros: '))
            break
        except:
            print('Eso no es un numero pos.')
    
    if registerUser(usuario,password,edad):
        print('Usuario Registrado Exitosamente')

    print('Analizando datos...')
    
    #Funcion que imprime todos los usuarios
    printUsers(5)

    resp = input('Si desea continuar presione enter, caso contrario escriba SALIR: ')
    if( resp == 'SALIR' or resp == 'salir'):
        print('\n \n \n Adios, gracias por usarnos \n')
        printUsers(0)
        print('\n ------------------------------------------')
        print('\n -----------FRANCO FUENTES SOTO------------')
        print('\n ------------------------------------------')
        break

