import password_validator
import encuestas_matico

while True:
    print('1. Elegir Contraseña')
    print('2. Enviar encuestas')
    print('9. Salir')
    opcion = input('Eliga una opcion: ')

    if int(opcion)== 1:
        password_validator.start() 
    elif int(opcion) == 2:
        encuestas_matico.start()
    elif int(opcion) == 9:
        print('Chao, pescado')
        break
    else:
        print('Opcion No valida')