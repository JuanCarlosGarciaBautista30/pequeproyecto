print('hola bienbenido') # se le da la bienvenida al usuario para convencerlo de que esta usando la app corrceta
nombre=input('¿Cuál es tu nombre?')

numero_1=int(input('ingresa una fecha: '))
numero_aleatorio=int(input('ingresa otra fecha(la que gustes:)'))

if numero_1 - numero_aleatorio >1:
    print(f'Han pasado {numero_1-numero_aleatorio} años desde {numero_aleatorio}')

elif numero_1 - numero_aleatorio <-1:
    print(f'faltan {numero_aleatorio-numero_1} años para {numero_aleatorio}')

elif numero_1==numero_aleatorio:
    print('estas en la misma fecha')

elif numero_1-numero_aleatorio ==1:
    print(f'ha pasado {numero_1-numero_aleatorio} año desde {numero_aleatorio}')

elif numero_1-numero_aleatorio == -1:
    print(f'falta {numero_aleatorio-numero_1} año para {numero_aleatorio}')

print('gracias por usar nuestra app.')
print('espero regreses pronto')

