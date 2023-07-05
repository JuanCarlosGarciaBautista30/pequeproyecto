# En las lineas siguientes desarrollare algunos ejercicios del curso python del primer modulo

print("""Bienvenidos 
alumnos y alumnas de todas las \
escuelas.....""")

#respuesta_2=0

# while respuesta_2!= "no:":
#     nombre = input('cual es tu nombre?')
#     print('bienbenido a la calculadora basica de tres numeros '+ nombre)

#     valor_1=int(input("introduce primer valor: "))
#     valor_2=int(input("introduce el segundo valor: "))
#     valor_3=int(input("introduce el tercer valor: "))
#     resultado = valor_1+valor_2+valor_3
#     print("el resultado de la suma es: " + str(resultado))#this is a firts way to do this operation
#     print(f"el resultado de la suma es: {resultado}")# and this is another way to do this opertion

#     respuesta=int(input(" Del 1 al 10: que te parecio la app " + str(nombre) + "?"))

#     if respuesta <=6:
#        print("intentaremos mejorar "+ nombre)
#     elif respuesta < 0:
#         print("ingresa un numero valido, calificación minima 1, 10 califocación valida")
#     elif respuesta > 10:
#         print("ingresa un numero valido 1 calificación minima, 10 califocación valida")    
#     else:
#         print("gracias por darnos  una buena calificación " + nombre)   

#     respuesta_2=input("deseas hacer otra operacion?")
 
#______________________________________________________________________________________________________________________
# programa calcula el area de u  circulo

# respuesta=0
# while respuesta!="no":
#     print("""BIENVENIDO
#     es la hora de comenzar """)
#     print("realiza el calculo de tus calificaciones")

#     nombre=input("Nombre del alumno? ")  
#     apellidoPaterno=input("Apellido paterno: ")
#     apellidoMaterno=input("Apellido materno: ")
#     matricul=input("Matricula: ")
#     direccion=input("Direccion: ")
#     edad=int(input("edad: "))

#     print("introduce la calificación de tus materias para poder sacar tu promedio")

#     matematicas=int(input("Matemáticas: "))
#     español=int(input("Español: "))
#     geografia=int(input("Geografia: "))
#     ingles=int(input("Ingles: "))
#     fisica=int(input("Fisica: "))
    
#     # ahora calculamos el promedio de las calificaciones usando la siguiente operación e imprimimos
#     #creamos una variable, la igualamos a la cantidad de materias
#     numeroMaterias=5
#     calFinal= (matematicas + español + geografia + ingles + fisica)/numeroMaterias
   
#     print("calificación final: "+str(calFinal))

#     if calFinal > 7:
#         print("La calificación es aprovatoria")
#         print("felicidades " + nombre)

#     else:
#         print("Reprovado")  
#         print("Animo " + nombre + "no te desanimes")  

#     respuesta=input("deseas hacer otra consulta? ")

#_______________________________________________________________________________________________________________________    

# acontinuación se implementara in programa escolar donde el alumno ingresara los datos personales.
# El alumno tendra la opcion de elegir el grado que esta cursando y dependiendo de la opción que elija 
# el programa desplegara las materias, el alumno devera llenar las calificaciones para que el programa calcule su 
# promedio final, asimismo con una sentecia if  elif else le arrojara si esta aprovado, o si desea hacer examen 
# extraordinario, oral o escrito y pagar 800$ POR DICHO EXAMEN 

print('BIENBENIDO ALUMNO')
print('''Acontinuación llena los datos que se te piden acontinuación
     despues elige tu grado que estas cursando''') 
  
nombre=input("Nombre del alumno? ") 
apellidoPaterno=input("Apellido paterno: ")
apellidoMaterno=input("Apellido materno: ")
matricula=input("Matricula: ")
edad=int(input("edad: "))
gradoEscolar=int(input("Grado: "))

calFinal=0

if gradoEscolar==1:

    print('Primero')
    print('introduce tu calificación en los diferentes apartados')
    español=int(input('Español_1: '))
    matematicas=int(input('Matematicas_1: '))
    geografia=int(input('geografia_1: '))
    cienciasNaturales=int(input('Ciencias Natutrales: '))
    recortes=int(input('Recortes: '))

    calFinal=(español + matematicas + geografia + cienciasNaturales + recortes)/5
     
    print(nombre + ' Calificación final:= ' + str (calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago')           


    
elif gradoEscolar==2:

    print('Segundo')
    print('introduce tu calificación en los diferentes apartados')

    español=int(input('Español Lecturas: '))
    matematicas=int(input('Matemáticas: '))
    c_naturales=int(input('Ciencias Naturales: '))
    dibujo=int(input('Dibujo: '))
    geografia=int(input('Geografia: '))

    calFinal=(español + matematicas + c_naturales + dibujo + geografia )/5

    print(nombre + ' Calificación final: ' + str (calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago') 

    
    

elif gradoEscolar==3:

    print('Tercero')
    print('introduce tu calificación en los diferentes apartados')

    matematicas=int(input('Matemáticas: '))
    español=int(input('Español lecturas: '))
    geografia=int(input('Geografia avanzada_1: '))
    dibujo=int(input('Dibujo y Pintura: '))
    arte=int(input('Arte: '))

    calFinal=(matematicas + español + geografia + dibujo + arte)/5

    print(nombre + 'Calificación final' + str(calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago') 

elif gradoEscolar == 4:
    
    print('Cuarto')
    print('introduce tu calificación en los diferentes apartados')
    
    matematicas=int(input('Matemáticas'))
    español=int(input('Español avanzado_2: '))
    etica=int(input('Etica: '))
    geografia=int(input('Geografia_2: '))
    c_naturales=int(input('Ciencias Naturales_2: '))

    calFinal=(matematicas + español + etica + geografia + c_naturales)/5

    print(nombre + ' Caliicación final: ' + str(calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago') 


  

elif gradoEscolar==5:
    
    print('Quinto')
    print('introduce tu calificación en los diferentes apartados')

    geometria=int(input('Geometria: '))
    español=int(input('Español Lecturas: '))
    arte=int(input('Arte_2: '))
    anatomia=int(input('Anatomia: '))
    E_fisica=int(input('Educación Fisica: '))

    calFinal=(geometria + español + arte + anatomia + E_fisica)/5

    print(nombre + ' Calificación final: ' + str(calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago') 

elif gradoEscolar==6:

    print('Quinto')
    print('introduce tu calificación en los diferentes apartados')

    matematicas=int(input('Matremáticas_4: '))
    lectura=int(input('Lectura y Redacción: '))
    etica=int(input('Etica: '))
    geografia=int(input('Geografia_4: '))
    dibujo=int(input('Dibujo: '))
    taller=int(input('Taller:'))
    comunicación=int(input('Comunicaión: '))

    calFinal=(matematicas + lectura + etica + geografia + dibujo + taller + comunicación)/7

    print(nombre + 'Calificación Final: ' + str(calFinal))

    if calFinal>6 and calFinal < 8:
        print('''Calificación aprovatoria
        cuidado "calificación en peligro" ''')

    elif calFinal>8:
        print('''Calificación aprovatoria
        Felicidades sigue asi''')

    else:
        print('''Reprovado
        alerta hay oportunidad de recuperación''') 

        exRecuperacion=input('Deseas hacer examen extraordinario? \n\t') #salto de linea,\t=tabulacion espacio de 4...

        if exRecuperacion=='si':

            print('el precio del examen es de 800 pesos')
            pago=input('''Deseas pagar en efectivo o con tarjeta?\n\tpreciona
            1:efectivo
            2:targeta''')

            if pago==1:
                print('800 pesos efectivos:')
                print('gracias por su pago')

            elif pago==2:
                print('ingrese su targeta y digite su NIP')
                print('gracias por su pago') 












    
