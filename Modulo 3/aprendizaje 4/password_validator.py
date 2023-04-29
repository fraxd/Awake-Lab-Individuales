requisitos = ['Minimo 8 Caracteres','Usar Mayusculas', 'Usar Minusculas', 'Usar Numeros']

def start():
    print('Instrucciones para una contraseña segura')
    for i in requisitos:
        print('- ', i)
    while True:
        reqPendientes = requisitos.copy()
        password = input('Ingrese contraseña: ')
        
        if validarMayusculas(password):
            reqPendientes.remove('Usar Mayusculas')
        if validarMinusculas(password):
            reqPendientes.remove('Usar Minusculas')
        if validarNumeros(password):
            reqPendientes.remove('Usar Numeros')
        if len(password)>= 8:
            reqPendientes.remove('Minimo 8 Caracteres')
        if len(reqPendientes) == 0:
            print('\n Su contraseña es segura \n')
            break
        else:
            print('Su contraseña aun no cumple todo los requisitos.\n')
            print('Requisitos Pendientes:')
            for i in reqPendientes:
                print('- ',i)

## Funciones que evaluan si hay mayusculas, minusculas o numero en la contraseña
def validarMinusculas(password):
    
    for i in password:
        if i.islower():
            return True
    return False


def validarMayusculas(password):
    for i in password:
        if i.isupper():
            return True
    return False

def validarNumeros(password):
    for i in password:
        if i.isnumeric():
            return True
    return False