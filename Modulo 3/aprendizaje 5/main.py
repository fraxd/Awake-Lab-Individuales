
## Nombre de usuario igual a las 3 primeras letras nombre + 3 primera letras apellido
juaper = {'nombre':'juan', 'apellido' : 'perez', 'edad': '35', 'genero' : 'masculino', 'sueldo': '550000', 'area': 'administracion', 'cargo': 'analista'}
kevsot = {'nombre':'kevin', 'apellido' : 'soto', 'edad': '27', 'genero' : 'masculino', 'sueldo': '600000', 'area': 'seguridad', 'cargo': 'vigilante'}
gilsal = {'nombre':'gillian', 'apellido' : 'salfate', 'edad': '28', 'genero' : 'femenino', 'sueldo': '530000', 'area': 'recepcion', 'cargo': 'recepcionista'}
joscov = {'nombre':'josefa', 'apellido' : 'covarrubias', 'edad': '45', 'genero' : 'femenino', 'sueldo': '620000', 'area': 'administracion', 'cargo': 'analista'}
frafue = {'nombre':'franco', 'apellido' : 'fuentes', 'edad': '25', 'genero' : 'masculino', 'sueldo': '700000', 'area': 'Generencia', 'cargo': 'sub-sub-sub gerente'}
javzun = {'nombre':'javiera', 'apellido' : 'zuñiga', 'edad': '30', 'genero' : 'femenino', 'sueldo': '600000', 'area': 'Sala', 'cargo': 'vendedora'}
eriloo = {'nombre':'erick', 'apellido' : 'loo', 'edad': '47', 'genero' : 'masculino', 'sueldo': '700000', 'area': 'administracion', 'cargo': 'supervisor'}


pencaInc = [juaper, kevsot, gilsal, joscov, frafue, javzun, eriloo]

for trabajador in pencaInc:
    print("Nombre: ", trabajador["nombre"])
    print("apellido: ", trabajador["apellido"])
    print("edad: ", trabajador["edad"])
    print("genero: ", trabajador["genero"])
    print("sueldo: ", trabajador["sueldo"])
    print("area: ", trabajador["area"])
    print("cargo: ", trabajador["cargo"])
    print("\n")

#¿Qué problemas encontró con esta forma de almacenar la información?
    # El problema principal con la forma de almacenar la información es que cada diccionario se refiere a un usuario diferente y no hay una estructura unificada para almacenar la información de todos los usuarios.
input('Aprete enter para continuar')

print('\nNueva version: \n')
pencaInc_v2 = [
    {
        'nombre':'juan', 
        'apellido' : 'perez', 
        'edad': '35', 
        'genero' : 'masculino', 
        'sueldo': '550000', 
        'area': 'administracion', 
        'cargo': 'analista',
        "antiguedad": 3,
        "fecha_incorporacion": "01/01/2020"
    },
    {
        'nombre':'kevin', 
        'apellido' : 'soto', 
        'edad': '27', 
        'genero' : 'masculino', 
        'sueldo': '600000', 
        'area': 'seguridad', 
        'cargo': 'vigilante',
        "antiguedad": 1,
        "fecha_incorporacion": "01/01/2022"
    },
    {
        'nombre':'gillian', 
        'apellido' : 'salfate', 
        'edad': '28', 
        'genero' : 'femenino', 
        'sueldo': '530000', 
        'area': 'recepcion', 
        'cargo': 'recepcionista',
        "antiguedad": 5,
        "fecha_incorporacion": "01/02/2018"
    },
    {
        'nombre':'josefa', 
        'apellido' : 'covarrubias', 
        'edad': '45', 
        'genero' : 'femenino', 
        'sueldo': '620000', 
        'area': 'administracion', 
        'cargo': 'analista',
        "antiguedad": 12,
        "fecha_incorporacion": "01/06/2010"
    },
    {
        'nombre':'franco', 
        'apellido' : 'fuentes', 
        'edad': '25', 
        'genero' : 'masculino', 
        'sueldo': '700000', 
        'area': 'Generencia', 
        'cargo': 'sub-sub-sub gerente',
        "antiguedad": 0,
        "fecha_incorporacion": "01/09/2022"
    },
    {
        'nombre':'javiera', 
        'apellido' : 'zuñiga', 
        'edad': '30', 
        'genero' : 'femenino', 
        'sueldo': '600000', 
        'area': 'Sala', 
        'cargo': 'vendedora',
        "antiguedad": 2,
        "fecha_incorporacion": "01/09/2020"
    },
    {
        'nombre':'erick', 
        'apellido' : 'loo', 
        'edad': '47', 
        'genero' : 'masculino', 
        'sueldo': '700000', 
        'area': 'administracion', 
        'cargo': 'supervisor',
        "antiguedad": 10,
        "fecha_incorporacion": "01/01/2013"
    }
]

for trabajador in pencaInc_v2:
    print(trabajador["fecha_incorporacion"])

print('\n*** Creado por  Franco Fuentes S. ***')