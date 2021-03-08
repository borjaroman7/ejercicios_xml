from funciones import leer_xml, menu, num_plazas_modelos, lista_marcas, lista_numero_coches
import sys

fichero = "./proyecto_xml/ejercicios_xml/coches.xml"
coches= leer_xml(fichero)
opcion =0
while opcion !=6:

    if opcion == 1:
        for i in lista_marcas(coches):
            print(i)

    if opcion == 2:
        for coches, num in  zip(lista_marcas(coches) ,lista_numero_coches(coches)):
            print( "Hay", num,"modelos diferentes de", coches)
    if opcion == 3:
        num_plazas = int(input("dime el numero de plazas "))

        for i ,a in num_plazas_modelos(coches):
            print (i,a)
    if opcion == 4:
        pass

    if opcion == 5:
        pass
    opcion = menu(opcion)