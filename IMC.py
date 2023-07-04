print('Bienvenidos') # Damos la bienbenida al usuario.
print('Calcula tu (IMC) indice de masa corporal llenando los tus siguientes datos.\n')

import re
# Usaremos un while True para que este iterando las sentencias hasta que sean falsas.
while True:

  nombre = input('nombre: ') # pedimos el nombre del usuario mediante un input.

    # re.fullmatch nos devuelve un objeto de coincidencia.
    # si el usuario no introduce algo dentro de [A-Za-z ñ ó ú é é ü Ü] en la variable nombre nos imprime la leyenda de abajo, y vuelve a preguntar.
    # {3,25}es el minimo y maximo de caracteres que acepta.Si escrivimos menos o mas{3,25} , también nos manda valor invalido.
  if (not re.fullmatch(r'[A-Za-z ñ ó ú í é á ü Ü ]{2,40}', nombre)):
      
    print('valor invalido. ( Campo vacio, numeros y simbolos estan prohibidos para este campo), intenta otravez.')
    continue
    
  else: # Usamos un else y su break para dejar de iterar.
    break

while True:

  apellido_paterno = input('Apellido Paterno: ') # pedimos el apellido paterno.

   
  if (not re.fullmatch(r'[A-Za-z ñ ó ú í é á ü Ü ]{2,25}',apellido_paterno)):
      
    print('valor invalido. ( Campo vacio, numeros y simbolos estan prohibidos para este campo), intenta otravez.')
    continue
    
  # Usamos un else y su break para dejar de iterar.
  else:
    break

while True:

  apellido_materno = input('Apellido Materno: ') # pedimos el apellido paterno.

   
  if (not re.fullmatch(r'[A-Za-z ñ ó ú í é á ü Ü ]{2,25}',apellido_materno)):
      
    print('valor invalido. ( Campo vacio, numeros y simbolos estan prohibidos para este campo), intenta otravez.')
    continue
    
  else:
    break

while True:
  try: # con el bloque Try intentaremos ejecutar las lineas que queremos ejecutar.
    edad = int(input('Edad: ')) # Pedimos la edad pero tendra que ser de tipo entero. 
       
    if  edad <=0: # la edad no podra ser un valor negativo, es por eso que usamos la condición if
      print('los numeros negativos y (0), no reprecentan una edad, intenta de nuevo, ej(10)')
      continue
    
    else:
      break
    
  # Si es que existe un fallo en el bloque try, nos mandara un herror.
  # Se ejecutara la ecepción de acontinuación y volvera a pedir el dato hasta que while True sea falso 
  except ValueError:
      print('el espacio no deve quedar vacio, tampoco estan permitidas las letras y/o simbolos.')
      continue
  
   
        
# Un while True para pedir el peso 
while True:
  try:
    peso = float(input('peso (kg): ')) # pedimos el peso del usuario con una variable de tipo float, pues el peso no necesariamente es un entero.
        
    if peso < 0: # Un peso siempre sera valor positivo.
      print('los numeros negativos y (0), no reprecentan un peso, intenta de nuevo, ej(50kg)')
      continue
    
    else:
      break

  except ValueError:# Si se ingresa un valor no valido en try se ejecuta la linea de la ecepción y pide datos otra ves.
      print('el espacio no deve quedar vacio, tampoco estan permitidas letras y/o simbolos.')
      continue

   

while True:
  try:
    estatura = float(input('estatura (m): ')) # Pedimos la estatura con una variabñe de tipo float.

    if estatura < 0:
      print('los numeros negativos y (0), no reprecentan una estatura, intenta de nuevo, ej(1.95m)')
      continue
    
    else:
      break
  

  except ValueError:
      print("el espacio no deve quedar vacio, tampoco estan permitidas letras y/o simbolos.")
      continue
  
# imprimimos una serie de lineas para separar nuestros datos de los resultados.
print('___________________________________________________________________________________________\n')
    
# en la siguente linea se escrivira una condicional if para verificar si el usuario es menor o mayor de edad. 
if edad >=18:
  print(nombre + ', eres mayor de edad.\n' )

else:
  print(nombre + ', eres menor de edad.\n')    

imc=round(peso/estatura**2,2) # usamos la palabra reservada (round)para redondear a dos decimales el valor que arrojara esta ecuación

print (nombre + ', Tu indice de masa corporal es: ' + str(imc)+'\n') 

# enseguida sabremos si el IMC del usuario es optimo para su salud.

if imc < 18.5: 
       print(nombre + ', Tienes bajo peso.\n')

elif imc >=18.5 and imc <=24.9: 
   print(nombre + ', Tu peso es optimo para tu salud.\n ')

elif imc >=25 and imc<=29.9:
   print(nombre + ', Tienes sobrepeso.\n')

elif imc > 30: 
   print(nombre + ', Tienes obesidad.\n')