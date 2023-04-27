encuestas = []
flagRespuesta = True

print('Bienvenido al Censo AwakeLab 2023')
while flagRespuesta:
    print('¿Eres de America Latina?')
    print('1. Si')
    print('2. No')
    opcion = input('Ingrese la opcion:')

    if opcion == '1':
        encuestas.append('Habitos Alimenticion')
        flagRespuesta = False
    elif opcion == '2':
        flagRespuesta = False
    else:
        print('Opcion Invalida')

edad = input('¿Cual es tu edad?')

if int(edad) >= 18 and int(edad) <= 29:
    encuestas.append('Cuestionario de Empeablididad')
elif int(edad) >=30 and int(edad) <=59 and int(opcion)==1:
    encuestas.append('Cuestionario de experiencia laboral')
elif int(edad) >= 60 and int(opcion)==1:
    encuestas.append('Cuestionario Actividad Recreativas')
flagRespuesta = True
while flagRespuesta:
    print('¿Le gusta los deportes?')
    print('1. Si')
    print('2. No')
    resp = input('Indique su respuesta:')

    if int(resp) == 1 and int(edad) >=60:
        encuestas.append('Encuesta Natacion')
        flagRespuesta = False
    elif int(resp) ==1 and int(edad) <60 and int(opcion)==1:
        encuestas.append('Encuesta Atletismo')
        flagRespuesta = False
    elif int(resp) == 2 :
        encuestas.append('Encuesta Deportes General')
        flagRespuesta = False
    else:
        print('ups, revisa tu respuesta.')

print('Generando Encuesta Personalizada...')
print('Usted debe responder un total de ', len(encuestas), 'encuestas')
for i in encuestas:
    print('-', i)
print('Muy pronto se enviara a su correo la encuesta, Saludos.')