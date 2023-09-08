""" UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertir
Las posibles franquicias son las siguientes:

# Apple,
# Dunkin Donnuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

El programa tendra precargado un menú de opciones en el que debemos programar lo siguiente

1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    genero (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)   
    
2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
3-Género que predomina en la empresa.
4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre 
entre los 18 y 30.
5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
6-Salir
'''

lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
            "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
            32, 22, 29, 27, 19, 49, 27, 22, 29, 27]

lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", 
                "Otro", "Marta", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", 
                "Femenino", "Masculino", "Femenino"]

lista_votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
            "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]    

#PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS


while True:

    print("\n1-Cargar Voto\n2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años\n3-Género que predomina en la empresa.\n4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre.\n5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados\n6-Salir")

    opcion = input("Ingrese una opción 1-6:")
    opcion = int(opcion)
    if opcion == 1:
        print("1")
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        print("5")
    elif opcion == 6:
        print("Adios")
        break
    else:
        print("Opcion incorrecta (1-6)") """
        
encuesta = input('¿Desea comenzar la encuesta? [SI - NO]: ')
encuesta = encuesta.upper()
empresas = "APPLE, DUNKIN, IKEA, TACO"

lista_nombres = []
lista_edades = []
lista_generos = []
lista_votos = []

contador_apple = 0
contador = 0

contador_masculino = 0
contador_femenino = 0
contador_otro = 0

contador_no_apple = 0



while encuesta == "SI":
    # 1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    
    #nombre del encuestado.
    nombre = input('Ingrese su nombre: ')
    nombre.capitalize()
    while nombre == "":
        nombre = input('Error. Ingrese su nombre: ')
        nombre.capitalize()
    
    #edad (no menor a 18)
    edad = int(input('Ingrese su edad: '))
    while edad < 18:
        edad = int(input('Error ingrese una edad mayor de 18 años: '))
    
    #genero (Masculino - Femenino - Otro)
    genero = input('Ingrese su genero [Masculino - Femenino - Otro]: ')
    genero = genero.lower()
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input('ERROR. Ingrese su genero [Masculino - Femenino - Otro]: ')
        genero = genero.lower()
    
    #voto (APPLE, DUNKIN, IKEA, TACO)
    voto = input(f'¿Cual de estas empresas le gustaria en Argentina {empresas}: ')
    voto = voto.upper()
    while voto != "APPLE" and voto != "DUNKIN" and voto != "IKEA" and voto != "TACO" :    
        voto = input(f'ERROR. ¿Cual de estas empresas le gustaria en Argentina {empresas}: ')
        voto = voto.upper()
    
    #AGREGO LOS DATOS A VALIDADOS A LAS RESPECTIVAS LISTAS
    lista_nombres.append(nombre)
    lista_edades.append(edad)
    lista_generos.append(genero)
    lista_votos.append(voto)       
   
    contador += 1
    encuesta = input('¿Desea continuar? [SI-NO]: ')
    encuesta = encuesta.upper()

#2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
for i in range(len(lista_nombres)):    
    if lista_votos[i] == "APPLE" and lista_edades[i] < 35: 
        contador_apple += 1
#3-Género que predomina en la empresa.
    if lista_generos[i] == "masculino":
        contador_masculino += 1
    elif lista_generos[i] == "femenino":
        contador_femenino += 1
    elif lista_generos[i] == "otro":
        contador_otro += 1
#4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre 
# entre los 18 y 30.
    if lista_votos[i] != "APPLE" and (lista_edades[i] > 17 and lista_edades[i] <=30) and lista_generos[i] != "FEMENINO":
        contador_no_apple += 1
        porcentaje_no_apple = (contador * 100) / contador_no_apple


print(f'la cantidad que votaron apple menores de 35 son: {contador_apple}')
if contador_masculino > contador_femenino and contador_masculino > contador_otro:
    print(f'EL GENERO MASCULINO PREDOMINA EN LA EMPRESA')
elif contador_femenino > contador_masculino and contador_femenino > contador_otro:
    print(f'EL GENERO FEMENINO PREDOMINA EN LA EMPRESA')
elif contador_otro > contador_masculino and contador_otro > contador_femenino:
    print(f'EL GENERO OTRO PREDOMINA EN LA EMPRESA')
    


print(f'en la empresa hay {contador_masculino} hombres\nhay {contador_femenino} mujeres \ny {contador_otro} otros')

print(f'las listas son:\n nombres: {lista_nombres}\n edades: {lista_edades}\n genero: {lista_generos}\n voto: {lista_votos}')

print(f'El porcentaje de empleados que no votaron apple es de % {porcentaje_no_apple}')