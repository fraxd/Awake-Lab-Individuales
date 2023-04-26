usuarios ='kevin emilio pepa sofia piraña boris feoman'

list_Usuario = usuarios.split()
print('Hola!, ¿Cual es tu usuario? ')
nombre = input()
#try y except por si el valor que ingresa no aparece en el index.
try:
    indice = usuarios.index(nombre)
    print('Bienvenido', nombre)
except ValueError:
    print('Ups, No te ubicamos.')

print('Hay ', len(list_Usuario), ' registrados en la plataforma')
print('Y se Acabo pos')

