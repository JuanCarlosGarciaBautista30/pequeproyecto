

while True:
    try:
        
        año_actual = int(input('\nintroduce el año actual en el que vives: '))
        año_aleatorio = int(input('introduce un año (el que gustes):'))

        if  año_actual - año_aleatorio > 1:
            print(f'Han pasado {año_actual-año_aleatorio} años desde {año_aleatorio}')
            break

        elif  año_actual - año_aleatorio < -1:
            print(f'faltan {año_aleatorio-año_actual} años para el {año_aleatorio}')
            break

        elif año_actual==año_aleatorio:
            print('las dos fechas ingresadas son el mismo año.')
            break
        
        elif año_actual-año_aleatorio == 1:
            print(f'ha pasado 1 año desde el {año_aleatorio}')
            break

        elif  año_actual - año_aleatorio == -1:
            print(f'aun falta un año para el {año_aleatorio}')
            break
        
        else: 
          break
        
    
    except ValueError:
        print('no puedes dejar un campo vacio, ni introcucir letras ni simbolos,intenta de nuevo.')
        continue


    