from funciones import *

fichero = "./proyecto_xml/ejercicios_xml/coches.xml"
coches= leer_xml(fichero)

# ejercicio 1
for i in lista_marcas(coches):
    print(i)

# ejercicio 2

for coches, num in  zip(lista_marcas(coches) ,lista_numero_coches(coches)):
    print( "Hay", num,"modelos diferentes de", coches)
# ejercicio 3


# ejercicio 4
# ejercicio 5