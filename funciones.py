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