#texto_variado='hola 123 +@.com#|'# este tipo de variables permite letras simbolos espacios dentro de comillas simples o dobles..
#print(type(texto_variado))

# # se utilizan comillas triples (sencillas o dobles para que funcionen los saltos de linea tal cual como se 
# #escrive en la linea de codigo) (\)diagonal invertida quita el salto de linea
# print("""Funcionamiento de la\
#  app (menú)
#     -1:iniciar
#        -2:salir """)

#______________________________________________________________________________________________
# subscripting e indexado

#los identificadores de una cadena se llaman indices y empieza del cero hasta donde termian
# texto='corazon'
# print(texto[4]) # al momento de imprimir en pantallla el [4] sera la letra z 
# print(texto[2])
# print(texto[-3])

# #print(texto[6]) # herror por que el indice indicado en el codigo no existe
# #print(texto[-8])# en esta linea se enmarcara un herror al momento de ejecutar por que no se puede acceder a una pocición que no existe 

# letra=texto[6]
# print(letra)

# #texto [0]='p' herror por que nos e puede modificar una cadena

# letra='p'
# print(letra)

# union_texo=letra+texto[2]# suma de cadenas de texto se les llamn concatenación
# print(union_texo)#al imprimir en pantalla, lo que mostrara es la letra de la variable textoindice[2]+variable letra 

#-------------------------------------------------------------------------------------

#slicing o substringing

# parrafo='practicas'
# print(parrafo[1:4])#en esta linea de codigo se invocan los indices de la variable parrafo 
# print(parrafo[0:-3])
# print(parrafo[0:-5])

# print(parrafo[-2:-4])# desde el indice -2, :dos puntos el salto que se quiere realizar

# print (parrafo[::-1])# en ésta linea de codigo se escriven la variable parrafo'practicas'pero letras alreves
# # y también  el -1 nos indica el numero de indices que se brinca...

#*************************************************************************************************************

# cadenas y formateos

# # escriviendo='hola mundo Sean bienbenidos'
# # print (escriviendo.lower()) # en esta linea de codigo se usa el metodo lower para imprimir la variable pero en minusculas 
# # print (escriviendo.upper()) # caso contrario de la linea anterior, con este métpdp sera todo en mayusculas
# # print (escriviendo.capitalize()) # con este método, capitalize() primer letra mayuscula despues toas minisculas..
# # print (escriviendo.title()) # primer letra de cada palabra en mayyusculas
# # print (escriviendo.swapcase())
# # escriviendo=escriviendo.upper() # en esta linea se cambia el valor de la variable siendo tpdas en mayusculas, se reasigna variable


# # print("{} + {} = {}".format(2,14, 2+14))
# # print("{} + {} = {}".format("hola","bienvenidos","hola bienvenidos"))
# # print("{1}+{0}+{2}={3}".format(2, 3, 5, 2+3+5 ))
# # print("{2}+{3}+{0}+{1}={4}".format(15, 22, 30, 25, 15+22+30+25))
# # print('{:2f}+{:5f}={}'.format(1,4, 1+4))
# # print("{3} + {1} + {0} + {2} + {4} ={5}".format(200, 400, 150,20,500, 200+400+150+20+500))                                                                              v      v          v                                                                                                                                                                                                                      nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnbnbvscccccccc                 }c c abn b

# # print("{} + {} + {} ={}".format(10, 22, 34, 10+22+34))

# # print("{}+{}+{}={}".format(12,23,42, 12+23+42))

# # print("{}+{}+{}={}".format("dia","mes","año","dia mes año "))# en éste ejemplo dia pertenece al primer indice, depues del igual en las llaves
# # #iria( dia mes año) juntos 

# # print("{:d} = {:b} = {:o} = {:x}".format(15, 15, 15, 15))
       

# #***********************************************************************************************************

#     # apartir de esta linea de comentario en adelante seran solo practicas de esta clase de strings utilización y métodos

# print("""bienbenidos a mis practicas de python
# sean bienbenidos \
# todos y todas 
# acontinuación un menú  de opciones
#    1- leer practicas
#    2- salir""")

# print("*************************************************************************")

# parrafo="feliz año"
# print(parrafo[6])# se imprime el indice n°6 de la variable parrafo
# print(parrafo[5])# se imprime el espacp en blanco de la variable parrafo

# print(parrafo[2:])# se imprimen del indice 2 a donde termin ala vaiable parrafo
# print(parrafo[3:-4])
# print("****************************************************************************")

# saludo="hola bienbenido"
# print(saludo.title())
# print(saludo.lower())
# print(saludo.upper())
# print(saludo.capitalize())

# print("*************************************************************************")

# print("{}+{}={}".format(10,25, 10+25))
# print("{1}+{0}={2}".format(10,25, 10+25))
# print("{}+{}={}".format("bienbenido"," saludos","binbenido saludos"))
# print("{}+{}+{}={}".format("hola","saludos","bienvenido", "hola saludos bienvenido"))
# print("{}+{}={}".format("menú","opciones", "menú opciones"))
# print("{:d}={:b}".format(20, 20))
# print("{:2f}+{:4f}={:1f}".format(10,14, 10+14))

print(len('hola'))
















   




