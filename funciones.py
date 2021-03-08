from lxml import etree
import sys

def leer_xml(fichero):
    with open(fichero) as f:
        datos=etree.parse(f)
    return datos


def lista_marcas(coches):
    marcas = coches.xpath('///nombre/text()')
    return marcas

def lista_numero_coches(coches):
    lista = []
    for i in  coches.xpath('///marcas'):
        num_coches= i.xpath('count(./coches)')
        lista.append(int(num_coches))
    return lista

def num_plazas_modelos(coches):
    modelos = coches.xpath('///marcas/coches/modelo/text()')
    plazas = coches.xpath('/////nplazas/text()')

    return zip(modelos,plazas)

def menu(opcion):
    print("")
    print("1- Muestra la lista de las marcas de los coches.")
    print ("2- Muestra el numero de coches que hay por marcas.")
    print("3- Muestra los modelos de coche con el numero de plazas indicados ")
    print("4- Muestra la informacion del modelo.")
    print("5- Muestra los modelos con mayor y menor cilindrada en una fecha determinada.")
    print("6- Salir.")
    opcion = int(input("dime la opcion a elegir "))
    return opcion