#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from random import randint


def letra(dni):
    print "%08d%s" % (dni , letraNif(dni))
    
def check(nif):
    dni = int(nif[:-1])
    temp = str(dni) + letraNif( dni )
    if temp == nif:
        print nif + ' correcto'
    else:
        print 'La letra correcta para ' + str(dni) + ' seria: ' + letraNif( dni)
        print "%08d%s" % (dni , letraNif(dni))

def random():
    dni = randint(100000,50000000)
    print "%08d%s" % (dni , letraNif(dni))

    
def letraNif(numeros):
    return "TRWAGMYFPDXBNJZSQVHLCKE"[numeros%23]

def main():
    parser = argparse.ArgumentParser(description='Generador de NIFs aleatorios y comprobador de la letra')    
    parser.add_argument('-c','--check', type=str, dest="nif", help='Comprueba la letra de un NIF', required=False)
    parser.add_argument('-l','--letra', type=int, dest="dni", help='Devuelve la letra de un NIF', required=False)
    parser.add_argument('-r','--random', action="store_true", help='Genera un numero de NIF aleatorio y su letra', required=False)
    args = parser.parse_args()

    if args.random:
        random()
    elif args.dni:
        letra( args.dni )
    else:
        check ( args.nif )


if __name__ == "__main__":
    main()

