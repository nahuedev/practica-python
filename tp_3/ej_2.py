""" Leer un número entero e imprimir un mensaje indicando si es par o impar. """

from ast import If


number= int(input('Ingrese un numero: '))

if( number % 2 == 0 ):
    print('Su numero es par')
else:
    print('Su numero es impar')
